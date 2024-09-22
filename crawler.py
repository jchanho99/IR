import requests
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser

url = "https://www.openstack.org"
robot_url = urljoin(url, '/robots.txt')

robot_parser = RobotFileParser()
robot_parser.set_url(robot_url)
robot_parser.read()

print(robot_parser.can_fetch("wjscksgh", url))
#r = requests.get(url)
# https://www.youtube.com/watch?v=sS4ooVBFiQE