from flask import Flask, jsonify,request
from flask_migrate import Migrate
from models import db, User
from flask_cors import CORS

app = Flask(__name__)
app.url_map.slashes = False
app.config['DEBUG'] = True 
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db.init_app(app)
Migrate(app, db) #recibe primero la logica app y luego los models
CORS(app)        # evitar problemas de cors al hacer querys

@app.route("/")
def main():
    return "hola desde flask"

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users), 200

@app.route('/api/create', methods=['POST'])
def create_user():
    
    name = request.json.get("name", None)
    if name == None or name == "":
        return jsonify({"msg":"debe ingresar un nombre"}), 400
    
    lastname = request.json.get("lastname", None)
    if lastname == None or lastname == "":
        return jsonify({"msg":"debe ingresar un apellido"}),400
    
    email = request.json.get("email", None)
    if email == None or email == "":
        return jsonify({"msg":"debe ingresar un email"}),400
    
    password = request.json.get("password", None)
    if password == None or password == "":
        return jsonify({"msg":"debe ingresar un password"}), 400
    
    # Se instancia una nueva clase User
    user = User()
    # Se asigna a las propiedades los valores del json cliente
    user.name = name
    user.lastname = lastname
    user.email = email
    user.password = password
    # se importa la funcion de la clase User, que agrega y guarda lo seteado
    user.save()
    
    return jsonify({"msg":"user creado"}), 201

if __name__ == '__main__':
    app.run()















