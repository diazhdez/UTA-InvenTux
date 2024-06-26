from flask import Blueprint, render_template, redirect, url_for, flash, request

from functions.functions import enviar_correo_contacto

import database.database as dbase

db = dbase.dbConnection()

main_routes = Blueprint('main', __name__)


# Ruta principal
@main_routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            correos = db['correos']
            # Guardar el correo en MongoDB
            correos.insert_one({'email': email})
            return redirect(url_for('main.index'))
        else:
            return redirect(url_for('main.index'))
    else:
        return render_template('index.html')


@main_routes.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        message = request.form['message']
        
        # Enviar correo de contacto utilizando la función
        exito = enviar_correo_contacto(name, subject, message)
        
        if exito:
            flash('¡Mensaje enviado correctamente!', 'success')
        else:
            flash('Hubo un problema al enviar el mensaje. Por favor, inténtalo de nuevo más tarde.', 'error')
        
        return redirect(url_for('main.contact'))  # Redireccionar a la página de contacto
    else:
        return render_template('contact.html')
