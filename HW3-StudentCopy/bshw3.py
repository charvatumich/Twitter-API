"""
PROJECT 3; CHALLENGE A:
BY: Hunter Charvat

CHALLENGE SPECIFICATIONS:
---------------------------------------------------------------------
Use https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions
    as a template.

STEPS
Create a similar HTML file but
1) Replace every occurrence of the word “student” with “AMAZING
student.”
2) Replace the main picture with a picture of yourself.
3) Replace any local images with the image I provided in media.  (You
must keep the image in a separate folder than your html code.

Deliverables:
1) Make sure the new page is uploaded to your GitHub account.
---------------------------------------------------------------------

CITATIONS:
---------------------------------------------------------------------
(1):
        -
        -
---------------------------------------------------------------------

"""

from bs4 import BeautifulSoup
import urllib.request
import requests
import re

base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")
clean = soup.prettify()
rep1 = clean.replace('student', 'AMAZING student')


