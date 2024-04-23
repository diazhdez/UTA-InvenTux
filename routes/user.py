from flask import Blueprint, render_template, url_for, redirect, session, request

from functions.functions import get_user

import plotly.graph_objs as go

from plotly.offline import plot

from bson import ObjectId

import database.database as dbase

db = dbase.dbConnection()

user_routes = Blueprint('user', __name__)


# Ruta para inicio de usuarios
@user_routes.route('/user/')
def user():
    if 'email' in session:
        email = session['email']
        # Función para obtener datos del usuario desde MongoDB
        user = get_user(email)
        if user:
            return render_template('user.html', user=user)
    else:
        return redirect(url_for('session.login'))


# Ruta para mostrar encuesta
@user_routes.route('/test/')
def test():
    if 'email' in session:
        email = session['email']
        # Función para obtener datos del usuario desde MongoDB
        user = get_user(email)
        if user:
            return render_template('test.html', user=user)
    else:
        return redirect(url_for('session.login'))


# Ruta para contestar encuesta en Español
@user_routes.route('/test/es/')
def testEs():
    if 'email' in session:
        email = session['email']
        # Función para obtener datos del usuario desde MongoDB
        user = get_user(email)
        if user:
            return render_template('testEs.html', user=user)
    else:
        return redirect(url_for('session.login'))


# Ruta para contestar encuesta en Nahuatl
@user_routes.route('/test/na/')
def testNa():
    if 'email' in session:
        email = session['email']
        # Función para obtener datos del usuario desde MongoDB
        user = get_user(email)
        if user:
            return render_template('testNa.html', user=user)
    else:
        return redirect(url_for('session.login'))


# Ruta para contestar encuesta en Mixteco
@user_routes.route('/test/mix/')
def testMix():
    if 'email' in session:
        email = session['email']
        # Función para obtener datos del usuario desde MongoDB
        user = get_user(email)
        if user:
            return render_template('testMix.html', user=user)
    else:
        return redirect(url_for('session.login'))


# Ruta para contestar encuesta en Tlapaneco
@user_routes.route('/test/tla/')
def testTla():
    if 'email' in session:
        email = session['email']
        # Función para obtener datos del usuario desde MongoDB
        user = get_user(email)
        if user:
            return render_template('testTla.html', user=user)
    else:
        return redirect(url_for('session.login'))


# Ruta para contestar encuesta en Portugues
@user_routes.route('/test/por/')
def testPor():
    if 'email' in session:
        email = session['email']
        # Función para obtener datos del usuario desde MongoDB
        user = get_user(email)
        if user:
            return render_template('testPor.html', user=user)
    else:
        return redirect(url_for('session.login'))


# Ruta para contestar encuesta en español
@user_routes.route('/test/fra/')
def testFra():
    if 'email' in session:
        email = session['email']
        # Función para obtener datos del usuario desde MongoDB
        user = get_user(email)
        if user:
            return render_template('testFra.html', user=user)
    else:
        return redirect(url_for('session.login'))
    

# Ruta para mandar las respuestas
@user_routes.route('/guardar/', methods=['POST', 'GET'])
def guardar():
    if 'email' in session:
        email = session['email']
        # Función para obtener datos del usuario desde MongoDB
        user = get_user(email)
        if user:
            if request.method == 'POST':
                respuestas = db['respuestas']
                # Obtener los datos del formulario
                user_id = request.form.get('user_id')
                pregunta1 = request.form.get('pregunta1')
                pregunta2 = request.form.get('pregunta2')
                pregunta3 = request.form.get('pregunta3')
                pregunta4 = request.form.get('pregunta4')
                pregunta5 = request.form.get('pregunta5')
                pregunta6 = request.form.get('pregunta6')
                pregunta7 = request.form.get('pregunta7')
                pregunta8 = request.form.get('pregunta8')
                pregunta9 = request.form.get('pregunta9')
                pregunta10 = request.form.get('pregunta10')
                pregunta11 = request.form.get('pregunta11')
                pregunta12 = request.form.get('pregunta12')
                pregunta13 = request.form.get('pregunta13')
                pregunta14 = request.form.get('pregunta14')
                pregunta15 = request.form.get('pregunta15')
                pregunta16 = request.form.get('pregunta16')
                pregunta17 = request.form.get('pregunta17')
                pregunta18 = request.form.get('pregunta18')
                pregunta19 = request.form.get('pregunta19')
                pregunta20 = request.form.get('pregunta20')
                pregunta21 = request.form.get('pregunta21')
                pregunta22 = request.form.get('pregunta22')
                pregunta23 = request.form.get('pregunta23')
                pregunta24 = request.form.get('pregunta24')

                # Guardar las respuestas en la base de datos MongoDB
                respuestas.insert_one({
                    'user_id': user_id,
                    'pregunta_1': pregunta1,
                    'pregunta_2': pregunta2,
                    'pregunta_3': pregunta3,
                    'pregunta_4': pregunta4,
                    'pregunta_5': pregunta5,
                    'pregunta_6': pregunta6,
                    'pregunta_7': pregunta7,
                    'pregunta_8': pregunta8,
                    'pregunta_9': pregunta9,
                    'pregunta_10': pregunta10,
                    'pregunta_11': pregunta11,
                    'pregunta_12': pregunta12,
                    'pregunta_13': pregunta13,
                    'pregunta_14': pregunta14,
                    'pregunta_15': pregunta15,
                    'pregunta_16': pregunta16,
                    'pregunta_17': pregunta17,
                    'pregunta_18': pregunta18,
                    'pregunta_19': pregunta19,
                    'pregunta_20': pregunta20,
                    'pregunta_21': pregunta21,
                    'pregunta_22': pregunta22,
                    'pregunta_23': pregunta23,
                    'pregunta_24': pregunta24
                })

                return redirect(url_for('user.test'))
        else:
            return redirect(url_for('session.login'))
        
    return redirect(url_for('user.test'))



# Ruta para mostrar resultados
@user_routes.route('/results/')
def results():
    if 'email' in session:
        email = session['email']
        # Función para obtener datos del usuario desde MongoDB
        user = get_user(email)
        if user:
            # Obtener el ID del usuario actual
            user_id = user['_id']
            
            # Obtener todas las respuestas del usuario actual desde la base de datos
            respuestas_usuario = db.respuestas.find({'user_id': str(user_id)})

            # Inicializar el contador de carreras
            carreras_count = {'TICS': 0, 'Gastronomía': 0, 'Mantenimiento Industrial': 0, 'Desarrollo de Negocios': 0}

            # Iterar sobre todas las respuestas del usuario
            for respuesta in respuestas_usuario:
                # Iterar sobre las preguntas en cada respuesta
                for pregunta, carrera in respuesta.items():
                    # Verificar si la respuesta corresponde a una carrera
                    if pregunta.startswith('pregunta_') and carrera in carreras_count:
                        # Incrementar el contador de la carrera correspondiente
                        carreras_count[carrera] += 1

            # Crear el gráfico de barras con Plotly
            data = [go.Bar(x=list(carreras_count.keys()), y=list(carreras_count.values()))]

            # Configurar el diseño del gráfico
            layout = go.Layout(xaxis=dict(title='Carreras'),
                               yaxis=dict(title='Número de respuestas'))

            # Crear la figura
            fig = go.Figure(data=data, layout=layout)

            # Convertir la figura a HTML
            graph_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

            return render_template('results.html', graph=graph_html)
    else:
        return redirect(url_for('session.login'))
