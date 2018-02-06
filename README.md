<img src="project/static/images/logos/Fifty50.png" width="150" height="150">

Fifty50 Mentoring Platform
==========================

*Student-run organisation promoting gender equity in STEMM.*

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


Want to help us work on the website! Yes, please!

Some basic web dev or django knowledge is strongly recommended. It only take a little while to learn the basics, but without them this project is going to seem a little bit intense to get set up.

If you're starting from scratch with Python/Django look through a tutorial first, we'd recommend on of these:

* Django Girls Tutorial (https://tutorial.djangogirls.org)
* The official "Writing your first Django app" Tutorial (https://docs.djangoproject.com)
* Tango With Django (https://tangowithdjango.com)
* The Django Book (https://djangobook.com/)

There are heaps of other resources out there.

You will need a familiarity with using CLI/shell and some an understanding of python virtual environments will make this less confusing.

Quickstart Here!
----------------

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)


If you're familiar with the basics get going here:

    git clone https://github.com/Fifty50STEMM/mentorship.fifty50.org.au.git

    # enter your freshly minted project
    cd mentorship.fifty50.org.au

    # Windows start:
    pip install virtualenvwrapper-win

    # Linux/OSX start:
    pip install virtualenvwrapper

    mkvirtualenv Fifty50

    # use the virtual environement
    workon Fifty50

    # one-off install all the project dependencies
    pip install -r requirements/local.txt

    # one-off instantiate db and superuser
    ./manage.py migrate
    ./manage.py createsuperuser
    # ... Follow prompts to create user

    # run!
    ./manage.py runserver

Go check out the website at:

http://localhost:8000/ or http://127.0.0.1:8000/

Awesome! Now you've got it working to the fun stuff.

Your superuser login will work at: http://localhost:8000/admin/

Looking at `config/urls.py` is one way of getting an idea of what apps are active.

This project is for managing the Mentor/Mentee program that Fifty50 runs, so an interesting use case is to create some new users as "Mentors" and "Mentees" and then match them up as an admin. We're intentionally being vague with these instruction as by trying to do this you will discover how tough it is to make good UI and how this is a student/volunteer project and that we have a long way to go :) ... We'd love your help though!

Specific issues we're aware of are tracked using the public github bug tracker:
https://github.com/Fifty50STEMM/mentorship.fifty50.org.au/issues

<3




Credit
------

Migrated from previous version of the project created as a year long student-lead project as part of the ANU Techlauncher program run through the College of Engineering and Computer Science (CECS):
https://github.com/Nikita1710/ANUFifty50-Online-Mentoring-Platform


Contact <3
----------


If you are having issues running the site, please log an issue with Github Issues OR
 contact:
  * Nikita (u5830260@anu.edu.au)
  * Tyrus (u5800279@anu.edu.au)
  * Elena (fifty50@elena.net.au)

We also have a slack channel, join up :)

https://fifty50mentoring.slack.com/


