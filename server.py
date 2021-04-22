from flask import Flask

app = Flask(__name__) # creates an instance

@app.route('/')
def hell0_word():
  return 'Why hello there'