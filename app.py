from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello Daljeet !"


if __name__ == "__main__":
  # print("I'm inside the if now")
  app.run(host='0.0.0.0', debug= True)