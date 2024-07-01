# Crear Base de Datos en Oracle
## Instalar el programa Oracle Database Express Edition
>* https://www.oracle.com/cl/database/technologies/xe-downloads.html
>* Al instalarlo se solicitara una contraseña para el usuario system, recuerda la contraseña que ingresaste, ya que esta contraseña se utilizara para crear la base de datos en sqldeveloper.
>* Al finalizar reinicia el equipo.
>* Abre el programa SQL Developer y crea una nueva conexión con los siguientes datos:
>* Nombre de la conexión: System
>* Nombre de usuario: sys
>* Contraseña: la contraseña que ingresaste al instalar Oracle Database Express Edition
>* Rol: SYSDBA
>* Hostname: localhost
>* Puerto: 1521
>* SID: xe

### Ahora crea una conexión con la cuenta de system, luego ejecuta los siguientes comandos:
>* create user c##juegosMax identified by juegosMax;
>* grant connect, resource to c##juegosMax;
>* alter user c##juegosMax default tablespace users quota unlimited on users;


## Ahora ejecutar el proyecto para que se creen las tablas

## Para poblar las tablas ya creadas estan los scripts en la carpeta /Poblacion de Base de Datos
