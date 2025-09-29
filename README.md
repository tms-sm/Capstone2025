# 🦷 Proyecto DentaPlus

Sistema de gestión dental desarrollado en **Django** con **MySQL** como base de datos.  
Incluye página de inicio, panel de administración y estructura para gestión de pacientes, doctores y citas.  

---

## 📌 Requisitos previos
Antes de ejecutar este proyecto asegúrate de tener instalado:
- **Python 3.12+**
- **MySQL 8+**
- **Pip** (ya viene con Python)
- **Virtualenv** (opcional, pero recomendado)

---

## ⚙️ Instalación paso a paso

### 1. Clonar o copiar el proyecto
Guarda este proyecto en una carpeta de tu máquina, por ejemplo:
```
C:\Users\TuUsuario\dentaplus
```

### 2. Crear entorno virtual (venv)
En la raíz del proyecto (donde está `manage.py`) ejecuta:

#### En **Windows (PowerShell)**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

#### En **Windows (CMD)**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

#### En **Linux / Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```

👉 Si el entorno está activado verás algo como `(venv)` al inicio de la terminal.

---

### 3. Instalar dependencias
Ejecuta:
```bash
pip install -r requirements.txt
```

---

### 4. Configurar la base de datos
En el archivo `dentaplus/settings.py`, ajusta según tu instalación de MySQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dentaplus_db',
        'USER': 'root',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

### 5. Crear base de datos en MySQL
En consola de MySQL:
```sql
CREATE DATABASE dentaplus_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

---

### 6. Migrar las tablas
En la terminal (con venv activo):
```bash
python manage.py migrate
```

---

### 7. Crear superusuario
```bash
python manage.py createsuperuser
```
👉 Ingresa usuario, correo y contraseña.

---

### 8. Ejecutar el servidor
```bash
python manage.py runserver
```

---

## 🚀 Uso del proyecto
- Página de inicio: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
- Panel de administración: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  

---

## 💾 Exportar e importar la base de datos (opcional)
Si ya tienes datos cargados y quieres moverlos a otra máquina:

### Exportar:
```bash
mysqldump -u root -p dentaplus_db > dentaplus_db.sql
```

### Importar:
```bash
mysql -u root -p dentaplus_db < dentaplus_db.sql
```

---

✅ Con estos pasos podrás llevar y ejecutar tu proyecto Django en cualquier computadora sin problemas.
