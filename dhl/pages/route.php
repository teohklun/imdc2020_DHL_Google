<?php 
  require '../vendor/autoload.php';
  use Google\Cloud\Core\ServiceBuilder;



  if($_POST){
    $mode = $_POST["mode"];
    if($mode === "singe-date") {
      $fileName = $_POST["fileName"];
      
      $gcloud = new ServiceBuilder([
        'keyFilePath' => '../../../gjson.json',
        'projectId' => 'supple-folder-256709'
      ]);

      $storage = $gcloud->storage();
      
      $mode = "";
      $session = "a";
      $date = "a";
      $routeID = "a";
      // $fileName = "";

      $bucket = $storage->bucket('real-bucket-dhl');
      $json = Null;
      if(!$bucket){
        #show no bucket not exist
      } else {
        $object = $bucket->object($fileName);
        if(!$object) {
          print_r("object not exist");
          #show file no exist
        } else {
          $json = $object->downloadAsString();
        }
      }
    } else {
      print_r("some parameter missing");
      die;
    }

  }else{
    print_r(($_POST));
    print_r("Webpage not support entered with non-post method.");
    die;
  }


  // $blob = $bucket.get_blob("testing1.json ");

  // $file = $storage->objects->get($bucket, $object, ['alt' => 'media']);


  // $a = $bucket->file_get_contents("https://storage.googleapis.com/" . "testing1.json");

  // $json_data_bytes = $blob.download_as_string();
  // print_r($json);

?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset=utf-8 />
  <title>DHL VRP Solution Solver</title>
    <meta name="viewport" content="initial-scale=1.0 maximum-scale=1.0">

    <link rel="stylesheet" href="../assets/css/route/OpenSans.css" />
    <link rel="stylesheet" href="../node_modules/leaflet/dist/leaflet.css">
    <link rel="stylesheet" href="../node_modules/leaflet-control-geocoder/dist/Control.Geocoder.css">
    <!-- <link rel="stylesheet" href="../assets/css/route/leaflet.css"> -->
    <!-- <link rel="stylesheet" href="../assets/css/route/Control.Geocoder.css"> -->
    <link rel="stylesheet" href="../assets/css/route/vroom.css" />
  </head>
  <body>

<?php print_r($_GET); ?>
    <div id="map"></div>
    <!-- <script src="src/map.js"></script> -->
    <script src="bundle.js"></script>
  <script type="text/javascript">
    loadJsonWithData2(<?= json_encode($json) ?>);
  </script>
  </body>
</html>
