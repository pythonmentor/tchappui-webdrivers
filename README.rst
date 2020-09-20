==================
install-webdrivers
==================

Easy-to-use script to install the latest versions of chromedriver 
and geckodriver on Travis-CI.

Installation
------------
You can install this commamd directly from PyPI using the following
command::
    
    $ pip install txhappui-webdrivers

User guide
----------

After having put tchappui-webdrivers in your requirements.txt file,
simply install the last stable versions of chromedriver and 
geckdriver using the install-webdrivers command. Here is a sample
.travis.yml file::

    dist: bionic
    language: python

    python:
      - '3.8'

    addons:
      # ajouter uniquement les navigateurs utilisés
      chrome: stable
      firefox: latest

    branches:
      only:
        - staging
    
    install:
      - pip install -r requirements.txt
      - pip install tchappui-webdrivers

    before_script:
      - install-webdrivers

    env:
      global:
        # we suppose the settings for Travis are in a dedicated file
        - DJANGO_SETTINGS_MODULE="config.settings.travis"

    services:
      - postgresql

    script:
      - python manage.py test -v2
