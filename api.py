from inspect import indentsize
import json
import os
import sys
import secrets
from flask import Flask, request, jsonify, session
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from supabase import create_client

from chatbot import get_response, predict_class

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)
app.config['JWT_SECRET_KEY'] = secrets.token_urlsafe(32)
jwt = JWTManager(app)
intents = json.loads(open('intents.json', encoding='utf-8').read())
# Configuración de las credenciales de Supabase
SUPABASE_URL = "https://nrnbqoxuhupcxlboisyg.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5ybmJxb3h1aHVwY3hsYm9pc3lnIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NzM4MzI5MCwiZXhwIjoyMDEyOTU5MjkwfQ.YkFTxwAKzNs6gukWMOA9ug6sboUJgEVU_SWJQmtzawU" 
supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)

@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    try:
        response = supabase.table("usuarios").select("*").execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/usuarios', methods=['POST'])
def registrar_usuario():
    try:
        data = request.get_json()
        nombre = data.get('nombre')
        email = data.get('email')
        contraseña = data.get('contraseña')

        response = supabase.auth.sign_up({"email": email, "password": contraseña})
        nuevo_usuario = {
            "nombre": nombre,
            "email": email,
            "contraseña": contraseña,
            "es_administrador": False,
        }
        supabase.table("usuarios").upsert([nuevo_usuario]).execute()

        return jsonify({"mensaje": "Usuario registrado con éxito"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/historial_chat', methods=['GET'])
@jwt_required()
def consultar_historial():
    try:
        response = supabase.table("historial_chat").select("*").execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    try:
        data = request.get_json()
        email = data.get('email')
        contraseña = data.get('password')

        # Autenticar al usuario
        supabase.auth.sign_in_with_password({"email": email, "password": contraseña})

        # Crear un token JWT
        access_token = create_access_token(identity=email)

        # Almacenar el token en la variable de sesión (opcional)
        session['access_token'] = access_token

        return jsonify({"mensaje": "Usuario autenticado con éxito", "access_token": access_token})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/api/chat', methods=['POST'])
@jwt_required()
def chat():
    data = request.get_json()
    message = data.get('message', '')
    
    ints = predict_class(message)
    res = get_response(ints, intents)
    
    try:
        mensaje = message
        respuesta_chatbot = res

        # Obtener el usuario_id utilizando el email de la sesión
        email = get_jwt_identity()
        lista = supabase.table("usuarios").select("*").match({'email': email}).execute()
        usuario_id = lista.data[0]['id']

        # Insertar en la tabla historial_chat
        supabase.table("historial_chat").upsert([
            {
                "usuario_id": usuario_id,
                "mensaje": mensaje,
                "respuesta_chatbot": respuesta_chatbot
            }
        ]).execute()

        return jsonify({"response": res, "mensaje": "Historial de chat guardado con éxito"})
    except Exception as e:
        return jsonify({"response": res, "error": str(e)})

@app.route('/api/cerrar_sesion', methods=['GET'])
@jwt_required()
def cerrar_sesion():
    try:
        response = supabase.auth.sign_out()
        return jsonify({"mensaje": "Usuario desconectado"})
    except Exception as e:
        return jsonify({"error": str(e)})
if __name__ == "__main__":
    app.run(debug=True)