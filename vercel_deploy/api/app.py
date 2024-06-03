from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            number = int(request.form["number"])
            result = [number + i for i in range(1, 5)]
        except ValueError:
            result = None
    return render_template("home.html", result=result)


@app.route('/personalizada')
def home_perso():
    usu = 'Gabriel Guimarães'
    return render_template('home_personalizada.html', usuario=usu)

