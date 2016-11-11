# PROJECT 3; CHALLENGE A:
# BY: Hunter Charvat
#
# CHALLENGE SPECIFICATIONS:
# ---------------------------------------------------------------------
# Use https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions
#     as a template.
#
# STEPS
# Create a similar HTML file but
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.
#
# Deliverables:
# 1) Make sure the new page is uploaded to your GitHub account.
# ---------------------------------------------------------------------
#
# CITATIONS:
# ---------------------------------------------------------------------
# (1): Stackoverflow users Mark Ransom
#         - How to create a file from Python
#         - http://stackoverflow.com/questions/16346914/python-3-2-unicodeencodeerror-charmap-codec-cant-encode-character-u2013-i
# (2): Stackoverflow user Martin v. Lowis
#         - How to make a raw string
#         - http://stackoverflow.com/questions/1347791/unicode-error-unicodeescape-codec-cant-decode-bytes-cannot-open-text-file
# ---------------------------------------------------------------------
#

from bs4 import BeautifulSoup
import urllib.request
import requests
import os

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")
for x in soup.find_all('img'):
    if 'testbed' not in x['src']:
        x['src'] = os.path.abspath(r'media\logo.png')

clean = soup.prettify()
rep1 = clean.replace('student', 'AMAZING student')
rep2 = rep1.replace("https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg", "hunter.jpg")

html_file = open('new.html', 'w', encoding='utf-8')
html_file.write(rep2)