Downplay
========

If you're going on a Christmas holiday somewhere with a bad or expensive internet connection, use this script to download Youtube playlists before you go.

I cobbled this together on a whim. Less than 30 lines of code, it has a CLI interface using Click (awesome Python package, by the way) and uses pytube for the downloading.

Installation
============

`git clone https://github.com/jbeyers/downplay.git`

`cd downplay`

`virtualenv ve --python=python3.6`

`. ve/bin/activate`

`pip install -r requirements.txt`

`python downplay.py`

Usage
=====

If you installed it using the above instructions, activate the virtualenv:

`. ve/bin/activate`

Then run:

`python downplay.py`

The program will ask for the url of the playlist, and for the name of a target folder to download it to. The target folder name should be just a word, no slashes etc.

It will create a 'downloads' folder in the current folder, and add another folder inside it, named after the target name you gave.

You can also use the --playlist option to specify the playlist url, and the --target option to specify the name of the target folder on the commandline.

Type `python downplay.py --help` for a listing of the options.
