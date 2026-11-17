@echo off
REM PRIMERA VEZ: crea el entorno, REINICIA la base ecoalerta (borra sus datos), migra y arranca.
cd /d "%~dp0"
echo === 1/5 Entorno virtual ===
if not exist venv\Scripts\activate.bat python -m venv venv
call venv\Scripts\activate.bat
echo === 2/5 Instalando dependencias ===
pip install -r requirements.txt
if errorlevel 1 goto error
echo === 3/5 Base de datos (MySQL de XAMPP debe estar iniciado) ===
python crear_bd.py --reiniciar
if errorlevel 1 goto error
echo === 4/5 Migraciones y usuarios de prueba ===
python manage.py migrate
if errorlevel 1 goto error
python manage.py crear_usuarios_demo
if errorlevel 1 goto error
echo === 5/5 Servidor: abre http://127.0.0.1:8000/ ===
python manage.py runserver
goto fin
:error
echo.
echo *** Algo fallo. Copia el mensaje de arriba y enviamelo. ***
:fin
pause
