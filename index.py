from flask  import Flask, render_template, abort
from conexion_bd import  consulta_transporte
from flask_bootstrap import Bootstrap
app  = Flask(__name__)
Bootstrap(app)
rows = consulta_transporte()


@app.route("/")
def traking():
    return render_template("index.html", rows=rows)

