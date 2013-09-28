to-be-musician
==============

`to-be-musician` is a project made in 48 hours for [Django Dash][1]. It's purpose is to automate some common tasks
for music students, like keeping musics, search for audio, lyrics, tabs, etc.

It's alive! [Check it out][2].

How it works
------------

When you are studying a song, you have a workflow to follow. It begins with you looking for the song in some resource
(MP3, Grooveshark, Rdio), looking for some score or tablature, and listening to the music over and over again, until you have
mastered the song.

With this web application we want to automate all this process, and let you discover and study songs with more agility and
facility. At the end, when you are rocking the song, you could share this and let others know how you turned yourself
into a hero.


Installing & Running
--------------------

You can install `to-be-musician` cloning it from GitHub:

        $ git clone git@github.com:romulojales/to-be-musician.git to_be_musician

Use pip to install all project's dependencies:

        $ cd to_be_musician/
        $ pip install -r requirements-dev.txt

Oh yeah! The `requirements.txt` file is only for our buddy **Heroku**.

Now you can run all tests:

        $ cd to_be_a_musician/
        $ python manage.py test

And run the Django built-in server:

        $ python manage.py runserver

Soon, we'll create a `Makefile`. That is a promise.


Facebook authentication x development environ
---------------------------------------------

We are using `python-social-auth` to handle our Facebook integration.

To use `to-be-a-musician` in your development environment, you must to add the following to your `/etc/hosts/`:

    127.0.0.1   local.to-be-a-musician.herokuapp.com

Also, you need to create two environment variables: `FACEBOOK_KEY` and `FACEBOOK_SECRET`.

Finally, you can access the application using `http://local.to-be-a-musician.herokuapp.com:8000/` and do login with your Facebook account.

  [1]: http://djangodash.com/
    "Django Dash 2013"
  [2]: http://to-be-a-musician.herokuapp.com/
    "Check the development evolution"
