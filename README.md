# Remote-Logs-Downloader
A Simple Way To Download Logs From Remote Server
No need to share the logs manually.

1. Extract the code at your desktop.

2. Go to mysite -> config.json provide projectname,pass and root path where the logs folder is stored.

3. run the command from mysite directory
    python manage.py runserver

How does it works ?
=========================
It creates a django web server which can be hosted on any server with django installed.
User just need to login and select the file from the list which is displayed and the file will be downloaded to the machine.
