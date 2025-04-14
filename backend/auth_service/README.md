# Auth Service

Este microservicio se encarga de la autenticación de usuarios en la aplicación de gestión de eventos. Proporciona rutas para el registro y la autenticación, así como la generación de tokens JWT para el acceso seguro a otros servicios.

## Estructura del Proyecto

- `app.py`: Contiene la lógica del microservicio, incluyendo las rutas y la validación de usuarios.
- `requirements.txt`: Lista las dependencias necesarias para el funcionamiento del microservicio.
- `Dockerfile`: Instrucciones para construir la imagen Docker del microservicio.

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd event-management-app/backend/auth_service
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Ejecución

Para ejecutar el microservicio, utiliza el siguiente comando:
```
python app.py
```

## Docker

Para construir y ejecutar el microservicio en un contenedor Docker, utiliza los siguientes comandos:

1. Construir la imagen:
   ```
   docker build -t auth_service .
   ```

2. Ejecutar el contenedor:
   ```
   docker run -p 5000:5000 auth_service
   ```

## Uso

- **Registro de usuario**: Realiza una solicitud POST a `/register` con los datos del usuario.
- **Autenticación**: Realiza una solicitud POST a `/login` con las credenciales del usuario para obtener un token JWT.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cambios.