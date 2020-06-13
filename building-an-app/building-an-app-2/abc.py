import requests
import pandas
import datetime
import json
from apscheduler.schedulers.blocking import BlockingScheduler

def some_job():
    token = "cd82096acc02f28c6a9fc93b88dca73f0029efa0"
    url = "http://api.waqi.info/feed/kualalumpur/?token=" + token
    headers = {
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }


    response = requests.get(url, headers=headers)
    print(response.content)
    now = datetime.datetime.now()
    dt_string = now.strftime("%d-m-%Y-%H-%M-%S")


    # with open(dt_string + '.json', 'wb') as f:
    #     json.dump(response.content, f)

    text_file = open(dt_string + '.json', "wb")
    n = text_file.write(response.content )
    text_file.close()
# pandas.read_json(response.content).to_excel(dt_string + ".xlsx")
scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', hours=1)
try:
    some_job()
    sched.start()
except (KeyboardInterrupt):
    logger.debug('Got SIGTERM! Terminating...')