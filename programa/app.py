from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import leave_room, join_room, send, SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "hola"
socketio = SocketIO(app)

salas = {}

def generate_unique_code(length):
    while True:
        cod = ""
        for _ in range(length):
            cod += random.choice(ascii_uppercase)    

        if cod not in salas:
            break

    return cod


@app.route("/", methods=["POST", "GET"])
def home():
    session.clear()
    if request.method =="POST":
        nombre =request.form.get("nombre")
        cod = request.form.get("cod")
        unir = request.form.get("unir", False)
        crear = request.form.get("crear", False)

        if not nombre:
            return render_template ("home.html", error="Por favor, ingresa un nombre.", cod=cod, nombre=nombre)
        
        if unir != False and not cod:
            return render_template ("home.html", error="Por favor, ingresa un código de sala.", cod=cod, nombre=nombre)

        sala=cod 
        if crear != False:
            sala = generate_unique_code(4)
            salas[sala]={"miembros": 0, "mensajes": []}
        elif cod not in salas:
            return render_template ("home.html", error="La sala no existe, intenta de nuevo.", cod=cod, nombre=nombre)
        
        session["sala"] = sala
        session["nombre"] = nombre
        return redirect(url_for("sala"))

    return render_template("home.html")

@app.route("/sala")
def sala():
    sala= session.get("sala")
    if sala is None or session.get("nombre") is None or sala not in salas:
        return redirect(url_for("home"))
    
    return render_template ("sala.html", cod=sala, mensajes=salas[sala]["mensajes"])

@socketio.on("mensaje")
def mensaje(data):
    sala = session.get("sala")
    if sala not in salas:
        return
    
    content = {"nombre": session.get ("nombre"), "mensaje": data["data"]}

    send(content, to=sala)
    salas[sala]["mensajes"].append(content)
    print(f"{session.get("nombre")} said: {data["data"]}")

@socketio.on("connect")
def connect(auth):
    sala = session.get("sala")
    nombre = session.get("nombre")
    if not sala or not nombre:
        return
    if sala not in salas:
        leave_room(sala)
        return
    
    join_room(sala)
    send({"nombre": nombre, "mensaje": "ha entrado a la sala"}, to=sala)
    socketio.emit("usuario_conectado", {"nombre": nombre}, to=sala)
    salas[sala]["miembros"] += 1
    print(f"{nombre} se unió a la sala {sala}")

@socketio.on("disconnect")
def disconnect():
    sala = session.get("sala")
    nombre = session.get("nombre")
    leave_room(sala)

    if sala in salas:
        salas[sala]["miembros"] -= 1
        if salas[sala]["miembros"] <= 0:
            del salas[sala]
    send({"nombre": nombre, "mensaje": "ha salido de la sala"}, to=sala)
    socketio.emit("usuario_desconectado", {"nombre": nombre}, to=sala)
    print(f"{nombre} salió de la sala {sala}")


if __name__ == "__main__":
    socketio.run(app, debug=True)

