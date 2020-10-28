# packages.py

#COMMON
import requests
from itertools import islice
#3RD PARTY
from bs4 import BeautifulSoup
#CUSTOM
from .errors import ResponseNot200, NoScheduleFound
