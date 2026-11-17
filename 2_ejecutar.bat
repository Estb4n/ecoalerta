@echo off
REM Uso diario: solo arranca el servidor.
cd /d "%~dp0"
call venv\Scripts\activate.bat
python manage.py runserver
pause
