# Event Management App - Event Service

Este microservicio es responsable de la gestión de eventos en la aplicación de gestión de eventos. Proporciona las siguientes funcionalidades:

## Funcionalidades

- **Crear Evento**: Permite a los usuarios crear nuevos eventos.
- **Obtener Evento**: Permite a los usuarios obtener detalles de un evento específico.
- **Listar Eventos**: Permite a los usuarios listar todos los eventos disponibles.

## Requisitos

Este microservicio requiere las siguientes dependencias:

- Flask
- SQLAlchemy

## Instrucciones de Uso

1. **Instalación de Dependencias**: Asegúrate de tener todas las dependencias instaladas. Puedes hacerlo ejecutando el siguiente comando en el directorio del microservicio:

   ```
   pip install -r requirements.txt
   ```

2. **Ejecutar el Servidor**: Para iniciar el microservicio, ejecuta el siguiente comando:

   ```
   python app.py
   ```

3. **Pruebas de API**: Puedes probar las rutas de la API utilizando herramientas como Postman o cURL.

## Docker

Para ejecutar este microservicio en un contenedor Docker, puedes construir la imagen utilizando el siguiente comando:

```
docker build -t event_service .
```

Luego, puedes ejecutar el contenedor con:

```
docker run -p 5000:5000 event_service
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o un pull request en el repositorio.