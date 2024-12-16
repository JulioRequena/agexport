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
