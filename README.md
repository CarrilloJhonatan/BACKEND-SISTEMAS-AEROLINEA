# BACKEND-SISTEMAS-AEROLINEA
A continuación, explicaré las funciones de cada ruta en la Api:

Obtener Usuarios (/api/usuarios, método GET):

Descripción: Esta ruta obtiene la lista de todos los usuarios almacenados en la base de datos.
Uso:
Método HTTP: GET
Endpoint: /api/usuarios
Retorno:
JSON con la lista de usuarios o un mensaje de error si ocurre algún problema.
Registrar Usuario (/api/usuarios, método POST):

Descripción: Registra un nuevo usuario en la base de datos y en el servicio de autenticación.
Uso:
Método HTTP: POST
Endpoint: /api/usuarios
Datos requeridos en el cuerpo de la solicitud (JSON): nombre, email, contraseña
Retorno:
JSON con un mensaje de éxito si el usuario se registra correctamente o un mensaje de error si ocurre algún problema.
Consultar Historial de Chat (/api/historial_chat, método GET):

Descripción: Consulta el historial de chat, requiriendo autenticación mediante un token JWT.
Uso:
Método HTTP: GET
Endpoint: /api/historial_chat
Encabezado de autenticación: Authorization: Bearer <TOKEN_JWT>
Retorno:
JSON con el historial de chat o un mensaje de error si la autenticación falla o hay algún problema.
Iniciar Sesión (/api/iniciar_sesion, método POST):

Descripción: Autentica a un usuario con su correo electrónico y contraseña y proporciona un token de acceso JWT.
Uso:
Método HTTP: POST
Endpoint: /api/iniciar_sesion
Datos requeridos en el cuerpo de la solicitud (JSON): email, contraseña
Retorno:
JSON con un mensaje de éxito y un token de acceso si la autenticación es exitosa o un mensaje de error si ocurre algún problema.
Procesar Chat (/api/chat, método POST):

Descripción: Procesa solicitudes del chatbot, requiriendo autenticación mediante un token JWT, y guarda la conversación en el historial.
Uso:
Método HTTP: POST
Endpoint: /api/chat
Encabezado de autenticación: Authorization: Bearer <TOKEN_JWT>
Datos requeridos en el cuerpo de la solicitud (JSON): message
Retorno:
JSON con la respuesta del chatbot y un mensaje de éxito si la operación es exitosa, o un mensaje de error si ocurre algún problema.
Cerrar Sesión (/api/cerrar_sesion, método GET):

Descripción: Cierra la sesión del usuario, requiriendo autenticación mediante un token JWT.
Uso:
Método HTTP: GET
Endpoint: /api/cerrar_sesion
Encabezado de autenticación: Authorization: Bearer <TOKEN_JWT>
Retorno:
JSON con un mensaje de éxito si la sesión se cierra correctamente o un mensaje de error si ocurre algún problema.
