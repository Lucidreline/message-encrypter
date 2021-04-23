from flask import Flask
import encryption

app = Flask(__name__)  # creates an instance


@app.route('/encrypt/<string:decryptedMsg>')
def encrypt(decryptedMsg):
    return encryption.encrypt(decryptedMsg, True)


@app.route('/decrypt/<string:encryptedMsg>')
def decrypt(encryptedMsg):
    return encryption.encrypt(encryptedMsg, False)
