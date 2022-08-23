# Nombre: Jhostyn Javier Gavilanez Suarez
# Fecha: 21/07/2022

"""
Importa la libreria de flask, redner templates, entre otras para hacer el llamado y otras funcionalidades.

"""

from flask import Flask, render_template, redirect, request, url_for

# ---------------------------------------------------------------------------
# Se inicializa y se llama a la carpeta de templates para ejecutar la pagina prinicipal. 
app = Flask(__name__, template_folder='templates')

# ---------------------------------------------------------------------------
# En este caso primero lo hare en forma de lista, para luego crear el script y guardarlo en la bases de datos. 
RegistrosCliente = []  # arreglo de la lista
# ---------------------------------------------------------------------------
# Password para tener acceso a dicha aplicacion mediante el uso del secret key
app.secret_key = 'jhostyn2022'

# ---------------------------------------------------------------------------
"""
Este es el primer paso para ver las listas de las tareas que luego seran almacenadas en la bases de datos 
de MongoDB. 
"""
@app.route('/')
# llamar a index.html en la ruta principal e inggresamos el registro cliente. 
def panelPrincipalC():
    return render_template('/index.html', RegistrosCliente=RegistrosCliente)

# ---------------------------------------------------------------------------

"""
Como segundo paso tenemos el controlador de ennvio de datos a nuestro registro mediante un formulario dado.
para luego establecer la conexion con mongo. 
"""
@app.route('/enviarRegistroClientes', methods=['POST'])
# metodo de guardar los datos
def enviarRegistroClientes():  # Aqui realiza el envio de datos para ser guardados en la lista.
    if request.method == 'POST':
        # el mensaje de añadir un registro de un nuevo dato se muestra por codigo javascript en el html
        Registro_Cedula = request.form['Registro_Cedula']
        Registro_Nombre = request.form['Registro_Nombre']
        Registro_Apellido = request.form['Registro_Apellido']
        Registro_Direccion = request.form['Registro_Direccion']
        Registro_Telefono = request.form['Registro_Telefono']
       

        # El mensaje esta por codigo javascript dentro del HTML
        if Registro_Cedula == '' or Registro_Nombre == '' or Registro_Apellido == '' or Registro_Direccion == '' or Registro_Telefono == '':
            return redirect(url_for('panelPrincipalC'))
        else:
            RegistrosCliente.append(
                {'Registro_Cedula': Registro_Cedula,
                 'Registro_Nombre': Registro_Nombre,
                 'Registro_Apellido': Registro_Apellido,
                 'Registro_Direccion': Registro_Direccion,
                 'Registro_Telefono': Registro_Telefono})

            return redirect(url_for('panelPrincipalC'))


# ---------------------------------------------------------------------------
# Controlador de la ruta para borrar todos los datos encontrados del registro 
# Controlador de borrar registros del cliente
@app.route('/borrarRegistroClientes', methods=['POST'])
def borrarRegistroClientes():              # La funcion de envio de mensaje borrado se hace mediante codigo Javascript
    RegistrosCliente.clear()
    return redirect(url_for('panelPrincipalC'))


# ---------------------------------------------------------------------------
# Controlador de registrar los datos al aplicativo Zona Azul 


# ejecutar del main principal para nuestra pagina 
if __name__ == '__main__':

    app.run(debug=True)