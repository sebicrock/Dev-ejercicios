# Event Management App Frontend

Este es el frontend de la aplicación de gestión de eventos, construido con React. La aplicación se conecta a dos microservicios: uno para la autenticación de usuarios y otro para la gestión de eventos.

## Estructura del Proyecto

- **public/index.html**: Página HTML principal que carga la aplicación React.
- **src/App.js**: Componente principal que maneja la estructura y navegación de la aplicación.
- **src/components/EventList.js**: Componente que muestra la lista de eventos obtenidos del microservicio de eventos.
- **src/services/authService.js**: Funciones para interactuar con el microservicio de autenticación.
- **src/services/eventService.js**: Funciones para interactuar con el microservicio de eventos.
- **src/index.js**: Punto de entrada de la aplicación React.

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   ```
2. Navega al directorio del frontend:
   ```
   cd event-management-app/frontend
   ```
3. Instala las dependencias:
   ```
   npm install
   ```

## Ejecución

Para ejecutar la aplicación en modo de desarrollo, utiliza el siguiente comando:
```
npm start
```

La aplicación se abrirá en `http://localhost:3000`.

## Construcción

Para construir la imagen Docker del frontend, utiliza el siguiente comando:
```
docker build -t event-management-frontend .
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.