from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    expression = ""
    if request.method == "POST":
        if 'expression' in request.form:
            expression = request.form['expression']
            try:
                result = eval(expression)
            except Exception as e:
                result = "Error"
            return render_template("index.html", expression=expression, result=result)
    return render_template("index.html", expression=expression)

if __name__ == "__main__":
    app.run(debug=True)
