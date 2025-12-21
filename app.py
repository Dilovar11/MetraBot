from flask import Flask, render_template

app = Flask(__name__, template_folder='webapp')

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # В продакшене нужно HTTPS
    app.run(host="0.0.0.0", port=8000, debug=True)
