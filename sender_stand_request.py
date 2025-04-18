'''Este script realiza una petición a un API de ejemplo y 
maneja posibles errores que puedan surgir durante la conexión.'''

import configuration
import data
import requests


def get_docs():
    '''Realiza una petición GET a la URL especificada en la configuración.'''
    # Se establece un timeout de 10 segundos para la petición
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH,
                        timeout=10)


response = get_docs()
print('Petición GET a la URL de documentación get_docs:')
print(response.status_code)


def get_logs():
    '''Realiza una petición GET a la URL de logs especificada en la configuración.'''
    # Se establece un timeout de 10 segundos para la petición
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        timeout=10)


response = get_logs()
print('Petición GET a la URL de documentación get_logs:')
print(response.status_code)
print(response.headers)


def get_users_table():
    '''Realiza una petición GET a la URL de la tabla de usuarios especificada en la configuración'''
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH,
                        timeout=10)  # Se establece un timeout de 10 segundos para la petición


response = get_users_table()
print('Petición GET a la URL de documentación get_users_table:')
print(response.status_code)


def post_new_user(body):
    '''Realiza una petición POST a la URL especificada en la configuración.'''
    # Se establece un timeout de 10 segundos para la petición
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, # establece URL
                        json=body,  # inserta el cuerpo de solicitud
                        headers=data.headers,  # inserta los encabezados
                        timeout=10)  # se establece un timeout de 10 segundos para la petición


response = post_new_user(data.user_body)
print('Petición POST a la URL de documentación post_new_user:')
print(response.status_code)
print(response.json())


def post_products_kits(products_ids):
    '''Realiza una petición POST a la URL de productos kits especificada en la configuración.'''
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                        json=products_ids,  # Datos enviados en solicitud.
                        headers=data.headers,
                        timeout=10)  # Encabezados de solicitud.


response = post_products_kits(data.product_ids)
print('Petición POST a la URL de documentación post_products_kits:')
print(response.status_code)
# print(response.json())


# try:
#     respuesta = requests.get(
#         'https://cnt-27f4feee-dc48-4e18-a21c-5a5587c235ec.containerhub.tripleten-services.com',
#         timeout=10)
#     # Lanza una excepción para códigos de error HTTP (4xx o 5xx)
#     respuesta.raise_for_status()

#     datos = respuesta.json()
#     print("Respuesta JSON:", datos)

# except requests.exceptions.RequestException as e:
#     print(f"Ocurrió un error al hacer la petición: {e}")
