Pasos para ejecutar el proyecto completo (Backend y Frontend) en Visual Studio Code
________________________________________
Paso 1: Instalación de herramientas necesarias
1.	Instalar Visual Studio Code:
o	Descarga e instala Visual Studio Code desde aquí.
2.	Instalar Python (para el backend):
o	Si no tienes Python instalado, descárgalo desde aquí.
3.	Instalar Node.js (para el frontend):
o	Si no tienes Node.js instalado, descárgalo desde aquí.
4.	Instalar Docker (opcional, para contenedores):
o	Si deseas usar Docker para ejecutar los contenedores de desarrollo, descarga e instala Docker desde aquí.
________________________________________
Paso 2: Configuración del Proyecto Backend (Flask)
1. Crear carpeta para el Backend
1.	Crea una carpeta llamada employee-crud en tu computadora.
2.	Dentro de employee-crud, crea una subcarpeta llamada backend.
2. Configurar el entorno virtual en Python
1.	Abre Visual Studio Code.
2.	Abre la terminal integrada de VS Code (usa el atajo Ctrl + ` o ve a Terminal > New Terminal).
3.	En la terminal, navega a la carpeta backend:
bash
Copy code
cd employee-crud/backend
4.	Crea un entorno virtual para el proyecto:
bash
Copy code
python -m venv venv
5.	Activa el entorno virtual:
o	En Windows:
bash
Copy code
.\venv\Scripts\activate
o	En Mac/Linux:
bash
Copy code
source venv/bin/activate
6.	Verás que el entorno virtual está activado cuando aparezca (venv) al principio de la línea de comandos.
3. Instalar dependencias de Flask
1.	Crea un archivo llamado requirements.txt en la carpeta backend y agrega el siguiente contenido:
makefile
Copy code
Flask==2.3.2
Flask-SQLAlchemy==2.5.1
2.	Instala las dependencias ejecutando:
bash
Copy code
pip install -r requirements.txt
4. Crear el archivo app.py para el Backend
1.	En la carpeta backend, crea un archivo llamado app.py y copia el código de Flask que te proporcioné anteriormente.
2.	Este código contiene los endpoints de la API para manejar los datos de los empleados.
5. Ejecutar el Backend
1.	Para ejecutar el servidor Flask, usa el siguiente comando en la terminal de VS Code:
bash
Copy code
python app.py
2.	Esto iniciará el servidor de desarrollo de Flask en http://localhost:5000.
________________________________________
Paso 3: Configuración del Proyecto Frontend (React)
1. Crear carpeta para el Frontend
1.	En la raíz de tu proyecto employee-crud, crea una subcarpeta llamada frontend.
2. Crear la aplicación React
1.	Abre la terminal de VS Code y navega a la carpeta frontend:
bash
Copy code
cd ../frontend
2.	Inicializa un nuevo proyecto de React utilizando Create React App:
bash
Copy code
npx create-react-app .
Esto instalará todo lo necesario para el proyecto de React.
3. Instalar Axios (para las solicitudes HTTP)
1.	En la terminal, dentro de la carpeta frontend, instala Axios:
bash
Copy code
npm install axios
4. Reemplazar los archivos React
1.	Dentro de la carpeta frontend/src, reemplaza los siguientes archivos con el código proporcionado:
o	App.js (componente principal): Copia el contenido de App.js desde el código proporcionado.
o	EmployeeTable.js (componente para la tabla de empleados): Copia el contenido de EmployeeTable.js desde el código proporcionado.
5. Ejecutar el Frontend
1.	Para iniciar la aplicación de React, ejecuta el siguiente comando en la terminal:
bash
Copy code
npm start
2.	Esto iniciará el servidor de desarrollo en http://localhost:3000.
________________________________________
Paso 4: Ejecutar el Proyecto en Docker (Opcional)
Si deseas usar Docker para ejecutar ambos servicios (Backend y Frontend) en contenedores, sigue estos pasos.
1. Crear los Dockerfiles
1.	En la carpeta backend, crea un archivo llamado Dockerfile y agrega el siguiente contenido:
Dockerfile para Backend (Flask):
dockerfile
Copy code
# Dockerfile para Flask
FROM python:3.9

# Establecer directorio de trabajo
WORKDIR /app

# Copiar el código de la aplicación
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
2.	En la carpeta frontend, crea un archivo llamado Dockerfile y agrega el siguiente contenido:
Dockerfile para Frontend (React):
dockerfile
Copy code
# Dockerfile para React
FROM node:16

# Establecer directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY . /app

# Instalar dependencias
RUN npm install

# Construir el proyecto
RUN npm run build

# Exponer el puerto
EXPOSE 3000

# Ejecutar la aplicación
CMD ["npm", "start"]
2. Crear el archivo docker-compose.yml
1.	En la raíz del proyecto employee-crud, crea un archivo llamado docker-compose.yml y agrega el siguiente contenido:
docker-compose.yml:
yaml
Copy code
version: '3'
services:
  backend:
    build:
      context: ./backend
    ports:
      - "5000:5000"
    networks:
      - app-network
  frontend:
    build:
      context: ./frontend
    ports:
      - "3000:3000"
    networks:
      - app-network

networks:
  app-network:
    driver: bridge
3. Ejecutar los contenedores con Docker Compose
1.	En la terminal, desde la raíz de tu proyecto, ejecuta el siguiente comando para construir y correr ambos contenedores:
bash
Copy code
docker-compose up --build
2.	Esto construirá los contenedores para el backend (Flask) y el frontend (React) y los ejecutará. La aplicación será accesible en:
o	Frontend: http://localhost:3000
o	Backend: http://localhost:5000
________________________________________
Paso 5: Probar la Aplicación
1.	Backend:
o	Puedes usar Postman o cualquier herramienta similar para hacer pruebas de la API.
o	Realiza las solicitudes a http://localhost:5000/employees, GET, POST, PUT y DELETE para probar las funcionalidades.
2.	Frontend:
o	Accede a http://localhost:3000 en tu navegador para ver la interfaz de usuario.
o	La lista de empleados debería mostrarse y permitirte agregar, editar y eliminar empleados.
________________________________________
Paso 6: Mantenimiento y Despliegue
1.	Puedes continuar desarrollando, depurando y mejorando la aplicación.
2.	Si deseas desplegar la aplicación en la nube o en un servidor, puedes crear imágenes Docker y subirlas a Docker Hub o usar plataformas como Heroku o AWS.

