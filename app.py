from flask import Flask, render_template

app = Flask(__name__)

# Página de inicio
@app.route('/')
def inicio():
    return render_template('inicio.html')

# Página nosotros
@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

# Página contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# Página galería de fotos
@app.route('/censgaleria')
def censgaleria():
    return render_template('censgaleria.html')

#Boton wsp
def canal_wsp(request):
    return render(request, "canal_wsp.html")

#Pàgina de cursos
@app.route("/ofertas_educativas")
def cursos():
    return render_template("cursos.html")


if __name__ == '__main__':
    app.run(debug=True)
