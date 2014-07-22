emailer
=======

A html emailer for those who cant send them.
*****************
What you will need to do to set it up:
*****************

creating a python env
============

1. So first things first youll need to download python 2.7 just google it for a link.

2. Next youll need to install pip there are several ways of doing this for instance on ubuntu:

$ sudo apt-get install python-pip python-dev build-essential              ($ means in the terminal)

Again depending on your system you may need to google this. It should be easy. To check its installed run $ pip list Then we will need to make a virtual env so you dont hurt your computer if its ubuntu but this is good for all other running systems as well.

3. Now run 

$ pip install virtualenv (wait to finish)
$ virtualenv myfirstenv
$ cd (or $ cd home/ for windows)
$ ls

DO YOU SEE  myfirstenv ?  then 

$ cd myfirstenv
$ ls

if a file called bin in present cd bin
if lib cd /lib then cd /bin
now

$ ls

is "activate" there?

$ source activate

4. Now using pip youll want to install a package called beautifulsoup run $ pip install BeautifulSoup4



OK so now you have all of these installed I believe this is all you need. If it complains it can find something when you run it look up the name and have a go at pip installing it.

Right so dowload this whole zipped folder to your computer. Add your email adress and password to email_settings.py and who you want to send it too in settings.py Move your html template to the folder.

Then go to your terminal cd /path/to/your/folder and run python -d reporter.py -t YOURTEMPLATENAME.html
