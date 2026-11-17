# EcoAlerta

Plataforma web de gestión de residuos (Django + MySQL + Bootstrap + Leaflet).

## Ejecutar (Windows, PowerShell)

1. Inicia **MySQL** desde el panel de XAMPP.
2. Crea la base de datos (phpMyAdmin o consola):
   `CREATE DATABASE ecoalerta CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;`
3. En la carpeta del proyecto:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py crear_usuarios_demo
python manage.py runserver
```

Abrir http://127.0.0.1:8000/

Si XAMPP tiene contraseña para root: `$env:DB_PASSWORD="tuclave"` antes de `migrate`.

## Usuarios de prueba (contraseña `Eco12345!`)
- admin@ecoalerta.test
- recolector.aseo@ecoalerta.test / recolector.equipo@ecoalerta.test / recolector.maquinaria@ecoalerta.test
- ciudadano@ecoalerta.test

## Pruebas
```powershell
python manage.py test apps
```
Las pruebas crean su propia base `test_ecoalerta` en MySQL (root debe poder crear bases).
