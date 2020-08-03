AUTH_PORT = 5001
USER_PORT = 5002

USER_SERVICE = {
    "port": USER_PORT
}

AUTH_SERVICE = {
    "port": AUTH_PORT
}

SERVICE = {
    'user': USER_SERVICE,
    'auth': AUTH_SERVICE
}
