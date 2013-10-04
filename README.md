to-be-musician
==============
[![Build Status](https://travis-ci.org/romulojales/to-be-musician.png?branch=master)](https://travis-ci.org/romulojales/to-be-musician) [![Coverage Status](https://coveralls.io/repos/romulojales/to-be-musician/badge.png?branch=master)](https://coveralls.io/r/romulojales/to-be-musician?branch=master)


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

Use `make setup` to install all project's dependencies and run migrations:

        $ cd to_be_musician/
        $ make setup

Now you can run all tests:

        $ make test

And run the Django built-in server:

        $ make run

The project uses `Sass` and `Compass`, so, if you want to do some styles, it's necessary to run the watcher:

        $ make compass


Facebook authentication x development environment
-------------------------------------------------

We are using `python-social-auth` to handle our Facebook integration.

To use `to-be-a-musician` in your development environment, you must to add the following to your `/etc/hosts/`:

    127.0.0.1   local.to-be-a-musician.herokuapp.com

Also, you need to create two environment variables: `FACEBOOK_KEY` and `FACEBOOK_SECRET`.

Finally, you can access the application using `http://local.to-be-a-musician.herokuapp.com:8000/` and do login with your Facebook account.

  [1]: http://djangodash.com/
    "Django Dash 2013"
  [2]: http://to-be-a-musician.herokuapp.com/
    "Check the development evolution"
