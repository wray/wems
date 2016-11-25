import time

from setuptools import find_packages

from distutils.core import setup

patch_level = int(time.time())

ver = "0.2." + str(patch_level)[1:]

setup(
  name = 'slackbot_wems',
  packages = find_packages(),
  version = ver,
  description = 'Python Code for Tech Em Studios WEMS Class',
  author = 'Techem Studios',
  author_email = 'wray@techemstudios.com',
  url = 'https://github.com/wray/wems',
  download_url = 'https://github.com/wray/wems/tarball/'+ver,
  keywords = ['slackbot', 'RPi', 'AWS'],
  classifiers = [],
)
