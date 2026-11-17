"""Crea (o reinicia) la base de datos de EcoAlerta en el MySQL/MariaDB de XAMPP.

Uso:
    python crear_bd.py              -> crea la base si no existe
    python crear_bd.py --reiniciar  -> BORRA la base y la crea vacía
"""
import os
import sys

import MySQLdb

nombre = os.environ.get("DB_NAME", "ecoalerta")

try:
    conexion = MySQLdb.connect(
        host=os.environ.get("DB_HOST", "127.0.0.1"),
        port=int(os.environ.get("DB_PORT", "3306")),
        user=os.environ.get("DB_USER", "root"),
        passwd=os.environ.get("DB_PASSWORD", ""),
        charset="utf8mb4",
    )
except MySQLdb.OperationalError as error:
    print("\nNo se pudo conectar a MySQL:", error)
    print("Abre XAMPP y pulsa Start en MySQL. Si root tiene contraseña: set DB_PASSWORD=tuclave")
    sys.exit(1)

cursor = conexion.cursor()
if "--reiniciar" in sys.argv:
    cursor.execute(f"DROP DATABASE IF EXISTS `{nombre}`")
    print(f"Base '{nombre}' borrada.")
cursor.execute(
    f"CREATE DATABASE IF NOT EXISTS `{nombre}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
)
print(f"Base '{nombre}' lista.")
conexion.close()
