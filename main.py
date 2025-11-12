from flask import Flask, render_template, request

app = Flask(__name__)


# Página principal con los 2 botones
@app.route('/')
def inicio():
    return render_template('inicio.html')


# Ejercicio 1 - Formulario de notas
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')


# Ejercicio 1 - Procesar resultados
@app.route('/procesar_ejercicio1', methods=['POST'])
def procesar_ejercicio1():
    # Obtener datos del formulario
    nota1 = int(request.form['nota1'])
    nota2 = int(request.form['nota2'])
    nota3 = int(request.form['nota3'])
    asistencia = int(request.form['asistencia'])

    # Calcular promedio
    promedio = (nota1 + nota2 + nota3) / 3

    # Verificar aprobación
    if promedio >= 40 and asistencia >= 75:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"

    return render_template('ejercicio1.html',
                           promedio=round(promedio, 1),
                           estado=estado,
                           mostrar_resultado=True)


# Ejercicio 2 - Formulario de nombres
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')


# Ejercicio 2 - Procesar resultados
@app.route('/procesar_ejercicio2', methods=['POST'])
def procesar_ejercicio2():
    # Obtener nombres
    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    nombre3 = request.form['nombre3']

    # Encontrar el nombre más largo
    nombres = [nombre1, nombre2, nombre3]
    nombre_mas_largo = max(nombres, key=len)
    longitud = len(nombre_mas_largo)

    return render_template('ejercicio2.html',
                           nombre=nombre_mas_largo,
                           longitud=longitud,
                           mostrar_resultado=True)


if __name__ == '__main__':
    app.run(debug=True)

