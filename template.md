# Especificación de Requisitos del Software
## Para JuegosMax

Versión 0.1  
Preparado por <Ignacio Mella>  
<organización>  
15/06/2024 

Tabla de Contenidos
=================
* [Historial de Revisiones](#historial-de-revisiones)
* 1 [Introducción](#1-introducción)
  * 1.1 [Propósito del Documento](#11-propósito-del-documento)
  * 1.2 [Alcance del Producto](#12-alcance-del-producto)
  * 1.3 [Definiciones, Acrónimos y Abreviaturas](#13-definiciones-acrónimos-y-abreviaturas)
  * 1.4 [Referencias](#14-referencias)
  * 1.5 [Resumen del Documento](#15-resumen-del-documento)
* 2 [Descripción del Producto](#2-descripción-del-producto)
  * 2.1 [Perspectiva del Producto](#21-perspectiva-del-producto)
  * 2.2 [Funciones del Producto](#22-funciones-del-producto)
  * 2.3 [Restricciones del Producto](#23-restricciones-del-producto)
  * 2.4 [Características del Usuario](#24-características-del-usuario)
  * 2.5 [Suposiciones y Dependencias](#25-suposiciones-y-dependencias)
  * 2.6 [Asignación de Requisitos](#26-asignación-de-requisitos)
* 3 [Requisitos](#3-requisitos)
  * 3.1 [Interfaces Externas](#31-interfaces-externas)
    * 3.1.1 [Interfaces de Usuario](#311-interfaces-de-usuario)
    * 3.1.2 [Interfaces de Hardware](#312-interfaces-de-hardware)
    * 3.1.3 [Interfaces de Software](#313-interfaces-de-software)
  * 3.2 [Funcionales](#32-funcionales)
  * 3.3 [Calidad del Servicio](#33-calidad-del-servicio)
    * 3.3.1 [Rendimiento](#331-rendimiento)
    * 3.3.2 [Seguridad](#332-seguridad)
    * 3.3.3 [Fiabilidad](#333-fiabilidad)
    * 3.3.4 [Disponibilidad](#334-disponibilidad)
  * 3.4 [Cumplimiento](#34-cumplimiento)
  * 3.5 [Diseño e Implementación](#35-diseño-e-implementación)
    * 3.5.1 [Instalación](#351-instalación)
    * 3.5.2 [Distribución](#352-distribución)
    * 3.5.3 [Mantenibilidad](#353-mantenibilidad)
    * 3.5.4 [Reusabilidad](#354-reusabilidad)
    * 3.5.5 [Portabilidad](#355-portabilidad)
    * 3.5.6 [Costo](#356-costo)
    * 3.5.7 [Fecha Límite](#357-fecha-límite)
    * 3.5.8 [Prueba de Concepto](#358-prueba-de-concepto)
* 4 [Verificación](#4-verificación)
* 5 [Apéndices](#5-apéndices)

## Historial de Revisiones
| Nombre | Fecha   | Razón de los Cambios  | Versión   |
| ------ | ------- | --------------------- | --------- |
|        |         |                       |           |
|        |         |                       |           |
|        |         |                       |           |

## 1. Introducción


### 1.1 Propósito del Documento
El propósito de este documento es definir los requisitos para el desarrollo de una página web de ventas de videojuegos, utilizando Django como backend y una base de datos Oracle. El sistema permitirá a los usuarios buscar, comprar y revisar videojuegos.

### 1.2 Alcance del Producto
Este documento cubre todas las funcionalidades necesarias para la gestión de productos (videojuegos), usuarios, carritos de compra y revisiones de productos.
### 1.3 Definiciones, Acrónimos y Abreviaturas
* SGB: Sistema de Gestión de Base de Datos.
* DBA: Administrador de Base de Datos.
* ERP: Planificación de Recursos Empresariales.
* API: Interfaz de Programación de Aplicaciones.
* Oracle: Sistema de gestión de bases de datos relacional
### 1.4 Referencias
* Documentación de Django.
* Documentación de Oracle Database.
* Guía de diseño de la interfaz de usuario.
### 1.5 Resumen del Documento
Este documento describe los requisitos para el desarrollo de una página web de ventas de videojuegos. Se describen las interfaces externas, los requisitos funcionales y de calidad del servicio, y los requisitos de diseño e implementación.
## 2. Descripción del Producto

### 2.1 Perspectiva del Producto
La página web de ventas de videojuegos es una aplicación web que se integra con una base de datos Oracle y utiliza Django para el backend. El sistema será accesible a través de navegadores web.
### 2.2 Funciones del Producto
* Gestión de productos (videojuegos).
* Gestión de usuarios y autenticación.
* Carrito de compras.
* Procesamiento de pedidos y pagos.
* Revisiones y valoraciones de productos.
* Búsqueda de productos por plataforma.
* Modificar, agregar y eliminar productos del catálogo (solo administrador).
### 2.3 Restricciones del Producto
* Administradores del sistema.
* Usuarios registrados (clientes).
* Visitantes no registrados.

### 2.4 Características del Usuario
* El sistema debe ser accesible solo mediante autenticación para ciertas funciones.
* Debe cumplir con las normativas de protección de datos y privacidad.
### 2.5 Suposiciones y Dependencias
* Todos los usuarios tienen acceso a Internet.
* Los navegadores soportan HTML5 y CSS3.
### 2.6 Asignación de Requisitos
| Función                      | Elemento de Software          | Versión Inicial | Versión Futura |
|------------------------------|-------------------------------| --------------- | -------------- |
| Gestión de Usuarios          | Backend Django                | Sí              | No             |
| Catálogo de Productos        | Base de Datos Oracle          | Sí              | No             |
| Modificacion Catalogo        | Base de Datos Oracle          | Sí              | No             |
| Carrito de Compras           | Backend Django                | Sí              | No             |
| Procesamiento de Pagos       | Integración                   | Sí              | No             |
| Búsqueda                     | Backend Django                | Sí              | No             |
| Sistema de Recomendaciones   | Motor de Recomendación        | No              | Sí             |
| Análisis y Reportes          | Módulo de Reportes            | No              | Sí             |
| Seguridad y Autenticación    | Backend Django                | Sí              | No             |
| Disponibilidad y Rendimiento | Infraestructura de Servidores | Sí              | No             |
| Mantenibilidad               | Documentación y Modularidad   | Sí              | No             |
| Portabilidad                 | Configuración del Sistema     | Sí              | No             |
## 3. Requisitos

### 3.1 Interfaces Externas

#### 3.1.1 Interfaces de Usuario
La página web de ventas de videojuegos tiene las siguientes interfaces de usuario:

* Página de inicio: Muestra una lista de productos destacados y ofertas especiales.
* Página de búsqueda: Permite a los usuarios buscar productos por plataforma.
* Página de detalles del producto: Muestra información detallada sobre un producto específico, incluyendo imágenes, descripción y precio.
* Página de carrito de compras: Muestra los productos agregados al carrito de compras y permite a los usuarios proceder al pago.
* Página de pago: Permite a los usuarios ingresar información de pago y completar la transacción.
* Página de registro: Permite a los usuarios registrarse creando una cuenta con su nombre, dirección de correo electrónico y contraseña.
* Página de inicio de sesión: Permite a los usuarios iniciar sesión con su dirección de correo electrónico y contraseña.

#### 3.1.2 Interfaces de Hardware
La pagina web de ventas de videojuegos no tiene interfaces de hardware, ya que es una aplicación web que se ejecuta en un servidor y se accede a través de un navegador web.

#### 3.1.3 Interfaces de Software
**Base de Datos Oracle**

* Nombre y Versión: Oracle Database 19c
* Ítems de Datos o Mensajes: Consultas y actualizaciones de datos de productos, usuarios registrados, transacciones de ventas, información de inventario.
* Propósito: Almacenamiento persistente de datos relacionados con productos, usuarios y transacciones.
* Servicios Necesarios: Acceso a través de conexiones JDBC/ODBC para consultas y actualizaciones desde el backend Django.
* Naturaleza de las Comunicaciones: Comunicación de datos estructurados utilizando SQL estándar.
* Restricción de Implementación: Utilización de transacciones para garantizar la integridad de los datos y el uso eficiente del espacio en disco.

**Herramientas y Bibliotecas de Desarrollo**

* Nombre y Versión: Django 3.2, Python 3.9, ORM de Django para Oracle
* Ítems de Datos o Mensajes: Lógica de negocio y acceso a datos, operaciones CRUD sobre la base de datos Oracle.
* Propósito: Implementación de la lógica de la aplicación web, interacción con la base de datos Oracle para gestionar productos, usuarios y transacciones.
* Servicios Necesarios: Framework Django para el desarrollo web, y bibliotecas específicas para la conexión y manipulación de datos en la base de datos Oracle.
* Naturaleza de las Comunicaciones: Llamadas de función y métodos para realizar operaciones de base de datos utilizando ORM de Django.
* Restricción de Implementación: Uso eficiente de recursos de servidor y optimización de consultas SQL para mejorar el rendimiento.* 
### 3.2 Funcionales
>Registro de Usuarios
* El sistema debe permitir a los usuarios registrarse creando una cuenta con su nombre, dirección de correo electrónico y contraseña.
Debe enviar un correo electrónico de confirmación al usuario después del registro exitoso.

>Visualización de Productos
* Los usuarios deben poder buscar productos por plataforma.
Debe mostrar una lista paginada de resultados de búsqueda con imágenes, títulos y precios de productos.

>Gestión de Carrito de Compras
* Los usuarios deben poder agregar y eliminar productos de su carrito de compras.
Debe mostrar el subtotal actualizado y permitir a los usuarios proceder al pago.

>Agregar productos
* Los administradores del sistema deben poder agregar nuevos productos al catálogo.

### 3.3 Calidad del Servicio
> 
#### 3.3.1 Rendimiento
* Tiempo de carga de la página: Todas las páginas del sitio web deben cargar en menos de 3 segundos en condiciones normales de carga.
* Capacidad de manejo de usuarios simultáneos: El sistema debe poder manejar al menos 1000 usuarios concurrentes sin degradación significativa del rendimiento.
* Respuesta a consultas de base de datos: Las consultas de base de datos deben completarse en menos de 100 milisegundos en promedio.
* Escalabilidad: El sistema debe ser escalable para manejar un aumento en el tráfico y la carga de trabajo sin cambios significativos en la arquitectura o el rendimiento.
#### 3.3.2 Seguridad
* Autenticación de usuarios: Todos los usuarios deben autenticarse antes de acceder a funcionalidades protegidas del sistema.
* Encriptación de datos sensibles: Los datos de pago y otros datos personales sensibles deben estar encriptados tanto en reposo como en tránsito.
#### 3.3.3 Fiabilidad
* Tasa de fallos: El sistema no debe experimentar más de un fallo crítico por mes.
* Recuperación de errores: Debe haber mecanismos de recuperación automatizados para restaurar el sistema en caso de fallos.
#### 3.3.4 Disponibilidad
* Tiempo de actividad del sistema: El sistema debe estar disponible al menos el 99.9% del tiempo de servicio planificado.
* Procedimientos de recuperación ante desastres: Debe haber un plan documentado y probado para la recuperación del sistema en caso de interrupciones graves.
### 3.4 Cumplimiento
* Cumplimiento con PCI-DSS: El sistema debe cumplir con los estándares de seguridad de datos de la industria de tarjetas de pago (PCI-DSS) para asegurar que toda la información de pago se maneje de manera segura.
### 3.5 Diseño e Implementación

#### 3.5.1 Instalación
Se proporcionará un documento de instalación detallado que describa los pasos necesarios para instalar y configurar el sistema en un entorno de producción. Se incluirán instrucciones para la configuración de la base de datos Oracle, la instalación de Django y la configuración del servidor web.
#### 3.5.2 Distribución
Se debe permitir la replicacion de la base de datos y el sistema en múltiples servidores para garantizar la disponibilidad y la redundancia. Se proporcionará un plan de distribución detallado que describa cómo se puede implementar el sistema en un entorno de producción distribuido.
#### 3.5.3 Mantenibilidad
El código debe estar bien documentado y estructurado de manera modular, siguiendo las mejores prácticas de desarrollo de Django. Las actualizaciones del sistema, como nuevos lanzamientos de juegos o cambios en el diseño del sitio web, deben poder realizarse sin afectar la disponibilidad del servicio.
#### 3.5.4 Reusabilidad
Los módulos de autenticación y autorización de usuarios, así como los componentes de carrito de compras y procesamiento de pagos, deben ser implementados como bibliotecas reutilizables.
#### 3.5.5 Portabilidad
El código fuente debe ser compatible con diferentes sistemas operativos y configuraciones de base de datos. Esto incluye la capacidad de migrar el entorno de desarrollo de un servidor local a un servicio de alojamiento en la nube sin modificaciones significativas.

#### 3.5.6 Costo
El costo estimado del desarrollo inicial del sistema es de $25.000.000, incluyendo licencias de software, infraestructura de hardware, y salarios del personal técnico. Los costos de mantenimiento anual, que incluyen actualizaciones de software, soporte técnico y gestión de la base de datos Oracle, se estiman en $7.000.000.
#### 3.5.7 Fecha Límite
La primera versión funcional del sistema ya esta completada. Esto incluye funcionalidades básicas como registro de usuarios, catálogo de videojuegos, insercion de juegos, carrito de compras y procesamiento de pagos. Las actualizaciones mayores, como la implementación de recomendaciones personalizadas y la vista de andministrador para modificar y agregar imagenes de videojuegos, deben planificarse y entregarse.
#### 3.5.8 Prueba de Concepto

## 4. Verificación
> 
## 5. Apéndices
