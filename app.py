from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello, world!"

@app.route("/add/<x>/<y>")
def result_route(x, y):
    return str(int(x)+int(y))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)