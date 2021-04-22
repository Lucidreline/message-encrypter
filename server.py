from flask import Flask
import encryption

app = Flask(__name__)  # creates an instance


@app.route('/encrypt/<string:decryptedMsg>')
def encrypt(decryptedMsg):
    return encryption.encrypt(decryptedMsg)


@app.route('/welcome/<string:encryptedMsg>')
def welcome(name):
    return 'Welcome, %s!' % name
