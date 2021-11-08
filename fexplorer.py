#!/usr/bin/env python3

from flask import (Flask, redirect, render_template,
                   send_from_directory, url_for)
from os import path
from urllib.parse import unquote
import os

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('root'))


# Display root('/') directory
@app.route('/explore/')
def root():
    dirpath = '/'
    dirlist, filelist = [], []
    files = sorted(os.listdir(dirpath), key=lambda x: x.lower())
    for f in files:
        if path.isdir(f'/{dirpath}/'+f):
            dirlist.append(f)
        else:
            filelist.append(f)
    return render_template('root.html', dirs=dirlist, files=filelist,
                           title='/')


# Display folders and files at the path.
@app.route('/explore/<path:dirpath>')
def explorer(dirpath):
    if dirpath[-1] == '/':
        return redirect(url_for('explorer', dirpath=dirpath[:-1]))
    dirpath = '/' + unquote(dirpath)
    dirlist, filelist = [], []
    temp = dirpath.split('/')
    temp.pop()
    previous_directory = '/' + '/'.join(temp)
    try:
        files = sorted(os.listdir(dirpath), key=lambda name: name.lower())
    except PermissionError:
        return render_template('message.html',
                               message='Oops!! It seems you do not have \
                                        permission to access this path.')
    except NotADirectoryError:
        text = ''
        try:
            with open(dirpath, 'r') as data:
                try:
                    text = data.readline()
                except UnicodeError:
                    pass
        except PermissionError:
            return render_template('message.html',
                                   message='Oops!! It seems you do not have \
                                            permission to access this path.')
        if text:
            return redirect(url_for('read', filepath=dirpath))
        return redirect(url_for('download', filepath=dirpath))
    for f in files:
        if path.isdir(f'/{dirpath}/'+f):
            dirlist.append(f)
        else:
            filelist.append(f)
    return render_template('index.html', dirs=dirlist, files=filelist,
                           curr=dirpath[1:], prev=previous_directory, 
                           title=dirpath+'/')


# Endpoint to download file at the specified path
@app.route('/download/<path:filepath>')
def download(filepath):
    filename = unquote(filepath)
    return send_from_directory('/', filename)


# Read file at the path and display it
# WARNING: Will blow up if the file at the specified path is not a text file or
# unreadable (contains non unicode charactars).
@app.route('/read/<path:filepath>')
def read(filepath):
    filename = '/' + unquote(filepath)
    filename = open(filename)
    text = ''.join(filename.readlines())
    filename.close()
    return render_template('reader.html', text=text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
