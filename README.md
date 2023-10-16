# BACKEND-SISTEMAS-AEROLINEA
A continuación, explicaré las funciones de cada ruta en la Api:

# Rutas relacionadas con Usuarios
Obtener todos los usuarios
Ruta: /api/usuarios
Método HTTP: GET
Descripción: Retorna todos los usuarios registrados.
Autenticación: No se requiere.
Obtener un usuario por ID
Ruta: /api/usuarios/<int:usuario_id>
Método HTTP: GET
Descripción: Retorna la información de un usuario específico.
Parámetros de Ruta: usuario_id es el identificador único del usuario.
Autenticación: No se requiere.
Registrar un nuevo usuario
Ruta: /api/usuarios
Método HTTP: POST
Descripción: Registra un nuevo usuario en el sistema.
Datos de la Solicitud: Nombre, email, y contraseña del nuevo usuario.
Autenticación: No se requiere.
Actualizar un usuario por ID
Ruta: /api/usuarios/<int:usuario_id>
Método HTTP: PUT
Descripción: Actualiza la información de un usuario específico.
Parámetros de Ruta: usuario_id es el identificador único del usuario.
Datos de la Solicitud: Los campos a actualizar (nombre, email, contraseña).
Autenticación: Se requiere un token JWT.
Eliminar un usuario por ID
Ruta: /api/usuarios/<int:usuario_id>
Método HTTP: DELETE
Descripción: Elimina un usuario específico del sistema.
Parámetros de Ruta: usuario_id es el identificador único del usuario.
Autenticación: Se requiere un token JWT.
Iniciar Sesión
Ruta: /api/iniciar_sesion
Método HTTP: POST
Descripción: Autentica al usuario y proporciona un token JWT.
Datos de la Solicitud: Email y contraseña del usuario.
Autenticación: No se requiere.
Cerrar Sesión
Ruta: /api/cerrar_sesion
Método HTTP: GET
Descripción: Cierra la sesión actual del usuario.
Autenticación: Se requiere un token JWT.
# Rutas relacionadas con Historial de Chat
Obtener historial de chat
Ruta: /api/historial_chat
Método HTTP: GET
Descripción: Retorna el historial completo de chat.
Autenticación: Se requiere un token JWT.
Obtener historial de chat por ID de Usuario
Ruta: /api/historial_chat/<int:usuario_id>
Método HTTP: GET
Descripción: Retorna el historial de chat de un usuario específico.
Parámetros de Ruta: usuario_id es el identificador único del usuario.
Autenticación: Se requiere un token JWT.
# Rutas relacionadas con Contactos
Obtener todos los contactos
Ruta: /api/contactos
Método HTTP: GET
Descripción: Retorna todos los contactos registrados.
Autenticación: No se requiere.
Obtener contacto por ID de Usuario
Ruta: /api/contactos/<int:usuario_id>
Método HTTP: GET
Descripción: Retorna los contactos de un usuario específico.
Parámetros de Ruta: usuario_id es el identificador único del usuario.
Autenticación: No se requiere.
Insertar nuevo contacto
Ruta: /api/contactos
Método HTTP: POST
Descripción: Registra un nuevo contacto.
Datos de la Solicitud: Mensaje del contacto.
Autenticación: Se requiere un token JWT.
