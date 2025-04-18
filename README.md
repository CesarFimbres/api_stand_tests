# Pruebas para el parámetro `firstName` al crear un usuario

Este archivo documenta las pruebas automatizadas realizadas en el archivo `create_user_tests.py` para validar el comportamiento del parámetro `firstName` en la API de creación de usuarios.

## Requisitos previos

- **Paquetes necesarios**: Asegúrate de tener instalados los paquetes `pytest` y `requests`. Puedes instalarlos ejecutando:

  ```bash
  pip install pytest requests
- **Ejecución de las pruebas**:  Para ejecutar todas las pruebas, utiliza el siguiente comando en la terminal

  ```bash
  pytest

## Descripción de las pruebas

### Pruebas positivas

Estas pruebas verifican que la API permite crear usuarios con valores válidos para el parámetro firstName.

- **Prueba 1**: El parámetro firstName contiene 2 caracteres.
   1. **Función**: test\_create\_user\_2\_letter\_in\_first\_name\_get\_success\_response
   1. **Resultado esperado**: Código de estado 201 y el usuario se crea correctamente.
- **Prueba 2**: El parámetro firstName contiene 15 caracteres.
   1. **Función**: test\_create\_user\_15\_letter\_in\_first\_name\_get\_success\_response
   1. **Resultado esperado**: Código de estado 201 y el usuario se crea correctamente.

### Pruebas negativas

Estas pruebas verifican que la API rechaza valores inválidos para el parámetro firstName.

- **Prueba 3**: El parámetro firstName contiene 1 carácter.
   1. **Función**: test\_create\_user\_1\_letter\_in\_first\_name\_get\_error\_response
   1. **Resultado esperado**: Código de estado 400 con un mensaje de error.
- **Prueba 4**: El parámetro firstName contiene 16 caracteres.
   1. **Función**: test\_create\_user\_16\_letter\_in\_first\_name\_get\_error\_response
   1. **Resultado esperado**: Código de estado 400 con un mensaje de error.
- **Prueba 5**: El parámetro firstName contiene caracteres latinos.
   1. **Función**: test\_create\_user\_english\_letter\_in\_first\_name\_get\_success\_response
   1. **Resultado esperado**: Código de estado 201 y el usuario se crea correctamente.
- **Prueba 6**: El parámetro firstName contiene caracteres especiales.
   1. **Función**: test\_create\_user\_has\_special\_symbol\_in\_first\_name\_get\_error\_response
   2. **Resultado esperado**: Código de estado 400 con un mensaje de error.
- **Prueba 7**: El parámetro firstName contiene un string de dígitos.
   1. **Función**: test\_create\_user\_has\_number\_in\_first\_name\_get\_error\_response
   2. **Resultado esperado**: Código de estado 400 con un mensaje de error.
- **Prueba 8**: Falta el parámetro firstName en la solicitud.
   1. **Función**: test\_create\_user\_no\_first\_name\_get\_error\_response
   2. **Resultado esperado**: Código de estado 400 con un mensaje de error.
- **Prueba 9**: El parámetro firstName contiene un string vacío.
   1. **Función**: test\_create\_user\_empty\_first\_name\_get\_error\_response
   2. **Resultado esperado**: Código de estado 400 con un mensaje de error.
- **Prueba 10**: El parámetro firstName tiene un tipo de dato incorrecto (número).
   1. **Función**: test\_create\_user\_number\_type\_first\_name\_get\_error\_response
   2. **Resultado esperado**: Código de estado 400 con un mensaje de error.

## Estructura del código

- **Funciones auxiliares**:
  - get\_user\_body(first\_name): Genera el cuerpo de la solicitud con el valor especificado para firstName.
  - positive\_assert(first\_name): Valida casos positivos donde el usuario se crea correctamente.
  - negative\_assert\_symbol(first\_name): Valida casos negativos relacionados con caracteres inválidos.
  - negative\_assert\_no\_firstname(user\_body): Valida casos negativos donde falta el parámetro firstName.
- **Pruebas unitarias**: Cada prueba está implementada como una función independiente que utiliza las funciones auxiliares para realizar las validaciones.

## Notas adicionales

- Asegúrate de que la API esté en funcionamiento antes de ejecutar las pruebas.
- Si necesitas modificar los datos de prueba, actualiza el archivo data.py o las funciones auxiliares según sea necesario.
