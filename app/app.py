from flask import Flask, render_template, request
app = Flask("app")
@app.route("/")
def say_hello():
    return render_template("app.html")

@app.route("/<name>")
def hello_someone(name):

    return render_template("app.html", name=name.title())

@app.route("/feedback", methods = ["POST"])
def get_feedback():
    data = request.values
    return render_template("feedback.html", form_data = data)

app.run(debug=True)
