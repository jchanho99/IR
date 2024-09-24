import requests
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser

url = "https://www.openstack.org"
robot_url = urljoin(url, '/robots.txt')
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
          AppleWebKit/537.36 (KHTML, like Gecko) \
          Chrome/129.0.0.0 Safari/537.36",
          "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}

robot_parser = RobotFileParser()
robot_parser.set_url(robot_url)

robot_request = requests.get(url)

if robot_request.status_code == 200:
    robot_parser.parse(robot_request.text.splitlines())

    if robot_parser.can_fetch("IR2024JeonbukUniv", url):
        print("ALLOWED")
    else:
        print("DISALLOWED")
else:
    print(robot_request.status_code)
# https://www.youtube.com/watch?v=sS4ooVBFiQE