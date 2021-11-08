# fexplorer
A minimal in-browser file explorer for Unix-like systems, written in python.

# About

This program starts a local server which can be visited from the browser to access the files on which the server is running. This program can run on servers, home computer or a RaspberryPi and grants access their files anywhere in the Internet.

It features an in-built text viewer and by default will open any file that can be opened as text. ALso it can open any other content(pdfs, videos, audios) as long as the browser can open it. Most modern browsers often come with a video player, music player and a pdf reader, so no external dependencies are required. Files can also be downloaded from the web UI directrly or streamed using your favourite player. .

# Pre-requisites

* Python (3.6+)
* A computer to run this program on

# Installation

* Clone the repo:
* (Optional) Create virtual environment.
* Install requirements.
* Run the program.
    ```bash
    git clone https://github.com/neelkamal0310/fexplorer.git
    cd fexplorer
    
    python3 -m venv env
    source env/bin/activate
    
    python3 -m pip install -r requirements.txt
    
    python3 app.py
    ```
    
# Notes

* By default, the program listens on loopback address 0.0.0.0 and port 5000 (can be changed), and will not work if there are any other programs using port 5000.
* Only files and directories accessible by the user running the program will be accessible.

# Work in progress

* An authentication system so that files are not exposed openly to everyone in the local network (or internet).
* Text Editor
