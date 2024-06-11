=================
django-model_ml
=================

getting the code
============

git clone https://github.com/fotsingriemann/test_model.git

Installation
============

You need install the pre-requirements for run this Hello World example.

Update repositories of available packages to install, with
the following command:

::

  $ sudo apt update

Install necessary minimum dependencies, with the following command:

::

  $ sudo apt install python3-dev python3-pip python3-virtualenv sqlitebrowser

For run this example need to install Django framework, mpu, openlocationcode and statsmodels execute the follow command:

::

    $ sudo pip install -r requirements.txt

And later followed by:

Run application
===============

After which you can run::

    $ python3 manage.py runserver

Then, you can open the URL http://127.0.0.1:8000/ in your web browser and you can 
see the hello world example like this:


Deploy it in the server
===============
    build the image
      $ sudo docker build -t test_de_mon_model .
    Deploy the container
      $ sudo docker run --name model_ml -p 8000:8000 test_de_mon_model


Redeploy if the modification on files
===============

    rebuild the image
      $ sudo docker build -t test_de_mon_model .
    Deploy the container
      $ sudo docker run --name model_ml -p 8000:8000 test_de_mon_model