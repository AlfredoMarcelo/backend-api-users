### Ver versiones

- `python --version`, muestra la version instalada en window

- `pip3 --version`, muestra la version de pip

- `pipenv --version`, muestra la version de pipenv

#### Instalacion pipenv

- En modo administrador, `pip install pipenv`, se hace una sola vez, quedará instalado de manera global en el sistema

- En mac se utiliza `sudo pip3 install pipenv`, pedira contraseña


#### Instalacion entorno virtual

- para instalar el entorno `pipenv --python=3.10`

- Para activar el entorno dentro del proyecto `pipenv shell`

- Para salir del entorno virtual, se utiliza `exit`

### Instalacion de frameworsks

- Se utiliza `pipenv install nombreFramework`
- En caso de usa una librería no instalada el error sera 'No module named 'nombreLibreria'' 
- Las librerias instaladas se podrán ver en el archivo Pipfile.



### Correr el proyecto

- se utiliza `python nombreArchivoPrincipal.py`
- por defecto arranca un servidor o entorno de desarrollo
- para terminar o salir del modo servidor, se utiliza `CTRL + c`
- es importante activar el modo debug en el documento para ver errores `(debug=True)`


#### Funciones del framework flask

- `render_tempalte("nombreArchivo.html")`, sirve para retornar un html desde la carpeta templates

- `request()`, para identificar el metodo de la solicitud que esta recibiendo el endpoint ej: request.method='POST', por defecto las rutas responden a solicitudes GET. Además permite saber si se esta recibiendo datos desde la query.

- `jsonify()`, permite devolver una respuesta en formato json. Retorna dos argumentos,la primera puede ser un string, datos, etc y la segunda es la respuesta a la solicitud, 200,300,400,500. 
Ej: ` return jsonify({"msg":"El nombre es requerido."}),400`
Ej2; `return jsonify(data)`

- request.get_json(), obtiene el json que viene desde el cliente. Para acceder a una de sus propiedades o para guardarlas dentro de una variable, se utiliza el nombre de la variable y destrcturing de objeto ej:
`data = request.get_json()
 nombrePropiedad = data['key']
`

- request.json.get(), recibe dos argumentos, el primero es el nombre del atributo o propiedad y el segundo es el valor por defecto que le queremos asignar a la propiedad en caso de que venga sin valor. Ej:
`label = request.json.get("nombrePropiedad", valorPorDefecto)`

#### Funciones del framework flask-sqlalchemy

- Permite hacer la conexion entre los modelos y la logica de la api
- 

#### Funciones del framework flask-migrate

- permite la migracion de los modelos creados a la aplicacion. Tiene tres comando para realizar esto:
1. flask db init, crea los contenedores para la base de datos

#### Funciones del framework flask-cors

- Esto evita errores de cors al llamar a la api desde una promesa fetch


### Observaciones


- Para generar rutas se utiliza `@app.route("path", method=GET, POST, PUT, DELETE)`

- Para usar dos metodos http dentro de una sola ruta, se  utiliza como segundo parametro entre corchetes, methods=['GET','POST', 'PUT', 'DELETE']



