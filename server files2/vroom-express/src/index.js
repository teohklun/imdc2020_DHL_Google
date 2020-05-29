const bodyParser = require('body-parser');
const express = require('express');
const fs = require('fs');
const helmet = require('helmet');
const morgan = require('morgan');
const uuid = require('uuid');
const config = require('./config');

// App and loaded modules.
const app = express();

const HTTP_OK_CODE = 200;
const HTTP_ERROR_CODE = 400;
const HTTP_TOOLARGE_CODE = 413;
const HTTP_INTERNALERROR_CODE = 500;

// Enable cross-origin ressource sharing.
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header(
    'Access-Control-Allow-Headers',
    'Origin, X-Requested-With, Content-Type, Accept'
  );
  res.setHeader('Content-Type', 'application/json');
  next();
});

const args = config.cliArgs;
app.use(bodyParser.json({limit: args.limit}));
app.use(bodyParser.urlencoded({extended: true, limit: args.limit}));

const accessLogStream = fs.createWriteStream(args.logdir + '/access.log', {
  flags: 'a'
});

app.use(morgan('combined', {stream: accessLogStream}));

app.use(helmet());

app.use((err, req, res, next) => {
  if (
    err instanceof SyntaxError &&
    err.status === HTTP_ERROR_CODE &&
    'body' in err
  ) {
    const message =
      'Invalid JSON object in request, please add jobs and vehicles to the object body';
    console.log(now() + ': ' + JSON.stringify(message));
    res.status(HTTP_ERROR_CODE);
    res.send({
      code: config.vroomErrorCodes.input,
      error: message
    });
  }
});

// Simple date generator for console output.
const now = function() {
  const date = new Date();
  return date.toUTCString();
};

const logToFile = function(input) {
  const timestamp = Math.floor(Date.now() / 1000); //eslint-disable-line
  const fileName = args.logdir + '/' + timestamp + '_' + uuid.v1() + '.json';
  fs.writeFileSync(fileName, input, (err, data) => {
    if (err) {
      console.log(now() + err);
    }
  });

  return fileName;
};

const fileExists = function(filePath) {
  try {
    return fs.statSync(filePath).isFile();
  } catch (err) {
    return false;
  }
};

// Callback for size and some input validity checks.
const sizeCheckCallback = function(maxJobNumber, maxVehicleNumber) {
  return function(req, res, next) {
    const correctInput = 'jobs' in req.body && 'vehicles' in req.body;
    if (!correctInput) {
      const message =
        'Invalid JSON object in request, please add jobs and vehicles to the object body';
      console.error(now() + ': ' + JSON.stringify(message));
      res.status(HTTP_ERROR_CODE);
      res.send({
        code: config.vroomErrorCodes.input,
        error: message
      });
      return;
    }

    if (req.body.jobs.length > maxJobNumber) {
      const jobs = req.body.jobs.length;
      const message = [
        'Too many jobs (',
        jobs,
        ') in query, maximum is set to',
        maxJobNumber
      ].join(' ');
      console.error(now() + ': ' + JSON.stringify(message));
      res.status(HTTP_TOOLARGE_CODE);
      res.send({
        code: config.vroomErrorCodes.tooLarge,
        error: message
      });
      return;
    }
    if (req.body.vehicles.length > maxVehicleNumber) {
      const vehicles = req.body.vehicles.length;
      const message = [
        'Too many vehicles (',
        vehicles,
        ') in query, maximum is set to',
        maxVehicleNumber
      ].join(' ');
      console.error(now() + ': ' + JSON.stringify(message));
      res.status(HTTP_TOOLARGE_CODE);
      res.send({
        code: config.vroomErrorCodes.tooLarge,
        error: message
      });
      return;
    }
    next();
  };
};

// Cli wrapper and associated callback.
const spawn = require('child_process').spawn;

const vroomCommand = args.path + 'vroom';
const options = [];
options.push('-r', args.router);
options.push('-t', args.nb_threads);
if (args.router != 'libosrm') {
  const routingServers = config.routingServers;
  for (const profileName in routingServers) {
    const profile = routingServers[profileName];
    if ('host' in profile && 'port' in profile) {
      options.push('-a', profileName + ':' + profile.host);
      options.push('-p', profileName + ':' + profile.port);
    } else {
      console.error(
        "Incomplete configuration: profile '" +
          profileName +
          "' requires 'host' and 'port'."
      );
    }
  }
}
//if (args.geometry) {
 // options.push('-g');
//}

options.push('-g');

const execCallback = function(req, res) {
  const reqOptions = options.slice();
  if (
    !args.geometry &&
    args.override &&
    'options' in req.body &&
    'g' in req.body.options &&
    req.body.options.g
  ) {
    reqOptions.push('-g');
  }

  const fileName = logToFile(JSON.stringify(req.body));
  reqOptions.push('-i ' + fileName);

  console.log("after push -i");

  const vroom = spawn(vroomCommand, reqOptions, {shell: true});
  console.log("after vroom spawn");

  // Handle errors.
  vroom.on('error', err => {
    const message = ['Unknown internal error', err].join(': ');
    console.error(now() + ': ' + JSON.stringify(message));
    res.status(HTTP_INTERNALERROR_CODE);
    res.send({
      code: config.vroomErrorCodes.internal,
      error: message
    });
  });

  vroom.stderr.on('data', data => {
    console.error(now() + ': ' + data.toString());
  });

  // Handle solution. The temporary solution variable is required as
  // we also want to adjust the status that is only retrieved with
  // 'exit', after data is written in stdout.
  let solution = '';

  vroom.stdout.on('data', data => {
    console.log("Writing solution . . .");
    solution += data.toString();
    console.log(solution.length);
  });

  vroom.on('close', (code, signal) => {
    console.log("vroom closing . . .");

    switch (code) {
      case config.vroomErrorCodes.ok:
        res.status(HTTP_OK_CODE);
        break;
      case config.vroomErrorCodes.internal:
        // Internal error.
        res.status(HTTP_INTERNALERROR_CODE);
        break;
      case config.vroomErrorCodes.input:
        // Input error.
        res.status(HTTP_ERROR_CODE);
        break;
      case config.vroomErrorCodes.routing:
        // Routing error.
        res.status(HTTP_INTERNALERROR_CODE);
        break;
      case 127: //eslint-disable-line
        // vroom not found on command line
        res.status(HTTP_INTERNALERROR_CODE);
        break;
    }
    console.log("before send solution.");
    res.send(solution);
    console.log("after send solution.");

    if (fileExists(fileName)) {
      fs.unlinkSync(fileName);
    }
    console.log("near after send solution.");
  });
};

app.post('/', [
  sizeCheckCallback(args.maxjobs, args.maxvehicles),
  execCallback
]);

const server = app.listen(args.port, () => {
  console.log('vroom-express listening on port ' + args.port + '!');
});

server.setTimeout(args.timeout);
