from bottle import route, run, template, static_file
import os
import server_reloader
import subprocess


@route('/')
def index():
    return "Got it."


@route('/hello/<name>')
def helloWorld(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/static/<path:path>')
def static_files(path):
    return static_file(path, root='public')


@route('/getDirectory')
def getDirectory():
    print("Getting directory...")

    data = subprocess.Popen("ls -l", shell=True,
                            stdout=subprocess.PIPE).stdout.read()

    data = str(data, "utf-8")

    fields = data.split('\n')

    return bytes("<br>".join(fields), "utf-8")


myPort = os.getenv('PORT', 3000)
myIP = os.getenv('IP', 'localhost')

run(host=myIP, port=myPort)
