# fexplorer
A minimal in-browser file explorer for Unix-like systems, written in python.

# About

This program starts a local server which can be visited from the browser to
access the files on which the server is running. This program can run on
servers, home computer or a RaspberryPi and grants access their files anywhere
in the Internet.

It features an in-built text viewer and by default will open any file that can
be opened as text. ALso it can open any other content(pdfs, videos, audios) as
long as the browser can open it. Most modern browsers often come with a video
player, music player and a pdf reader, so no external dependencies are
required. Files can also be downloaded from the web UI directrly or streamed
using your favourite player. .

# Pre-requisites

* python3 (3.6+)
* gunicorn (installed via package manager)

# Installation

* Clone the repo:
    ```bash
    git clone https://github.com/neelkamal0310/fexplorer.git
    cd fexplorer
    ```
* Install requirements.
    ```bash
    python3 -m pip install -r requirements.txt
    ```
* Run `install.sh` after making it executable.
    ```
    chmod +x install.sh
    ./install.sh
    ```

* This creates and copies files to a relevant location and starts a systemd
  service. To autostart this after you login, run
  ```bash
  systemctl enable --user fexplorer.service
  ```

* Note: The systemd service will terminate when the user logs out. This is more
  relevant on a server or Raspberry Pi where you have to SSH to log in. After
  you log out or exit the SSH session, the service will be terminated. To
  prevent this either start the service inside a `tmux` session or run the
  following command:
  ``` bash
  loginctl enable-linger $(whoami)
  ```
  More info on what this command does [here](https://wiki.archlinux.org/title/Systemd/User#Automatic_start-up_of_systemd_user_instances)
    
# Notes

* By default, the program listens on loopback address 0.0.0.0 and port 5000 (can be changed), and will not work if there are any other programs using port 5000.
* Only files and directories accessible by the user running the program will be accessible.

# Work in progress

* Authentication
