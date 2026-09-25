# Documentación de Variables de Entorno

Este proyecto requiere configurar variables de entorno para funcionar correctamente.  
**Importante:** No se incluyen contraseñas reales ni credenciales privadas en este archivo.  
En su lugar se muestran **placeholders** que deben ser reemplazados por valores reales al momento de desplegar la aplicación.

---

## Variables requeridas

### 1. `DATABASE_URL`
Cadena de conexión a la base de datos PostgreSQL en RDS.

- **Formato:**
postgresql://<USUARIO>:<PASSWORD>@<ENDPOINT_RDS>:5432/<DB_NAME>
- **Ejemplo con placeholders:**
postgresql://postgres:<PASSWORD>@<ENDPOINT_RDS>:5432/<DB_NAME>
- **Descripción de cada parte:**
- `<USUARIO>` → Usuario de la base (ejemplo: `postgres`)
- `<PASSWORD>` → Contraseña del usuario (no se expone aquí)
- `<ENDPOINT_RDS>` → Endpoint de la instancia RDS (ejemplo: `database-1.cxuswsim2rg7.us-east-2.rds.amazonaws.com`)
- `<DB_NAME>` → Nombre de la base de datos creada (ejemplo: `mibasedatos`)

---

### 2. `SECRET_KEY`
Llave secreta utilizada para firmar tokens (JWT, sesiones, etc.).

- **Ejemplo con placeholder:**
SECRET_KEY=<YOUR_SECRET_KEY>
- **Nota:** Debe ser una cadena aleatoria segura. No se expone aquí.

---

### 3. `DEBUG`
Activa o desactiva el modo debug de la aplicación.

- **Valores posibles:**
- `True` → Desarrollo
- `False` → Producción

---

## Archivo `.env.example`

Se incluye un archivo de ejemplo (`.env.example`) con los placeholders para que otros desarrolladores sepan qué variables configurar:

```env
# Variables de entorno requeridas para la API

DATABASE_URL=postgresql://postgres:<PASSWORD>@<ENDPOINT_RDS>:5432/<DB_NAME>
SECRET_KEY=<YOUR_SECRET_KEY>
DEBUG=True
## Instrucciones de uso

1. Copiar el archivo `.env.example` y renombrarlo a `.env`.
2. Sustituir los placeholders (`<PASSWORD>`, `<ENDPOINT_RDS>`, `<DB_NAME>`, `<YOUR_SECRET_KEY>`) por los valores reales.
3. Guardar el archivo `.env` en la raíz del proyecto.
4. La aplicación leerá automáticamente estas variables al iniciar.

---
