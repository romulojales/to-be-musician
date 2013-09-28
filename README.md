to-be-musician
==============

Django application for to be a musician.


Installing & Running
--------------------

You can install `to-be-musician` cloning it from GitHub:

        $ git clone git@github.com:romulojales/to-be-musician.git to_be_musician

Use pip to install all project's dependencies:

        $ pip install -r requirements-dev.txt

Oh yeah! The `requirements.txt` file is only for our buddy **Heroku**.

Now you can run all tests:

        $ cd to_be_a_musician
        $ python manage.py test

And run the Django built-in server:

        $ python manage.py runserver

Soon, we'll create a `Makefile`. That is a promise.


Facebook authentication
-----------------------

We are using `python-social-auth` to handle our Facebook integration.

To use `to-be-a-musician` in your development environment, you must to add the following to your `/etc/hosts/`:

    127.0.0.1   local.to-be-a-musician.com

Also, you need to create two environment variables: `FACEBOOK_KEY` and `FACEBOOK_SECRET`.

Finally, you can access the application using `http://local.to-be-a-musician.com:8000` and do login with your Facebook account.
