import sqlite3

# Crear la base de datos 'adopciones.db'
conn = sqlite3.connect('adopciones.db')
cursor = conn.cursor()

# Crear la tabla 'caninos'
cursor.execute('''
CREATE TABLE IF NOT EXISTS caninos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    estado TEXT NOT NULL,
    historial_medico TEXT
)
''')

# Crear la tabla 'inventario'
cursor.execute('''
CREATE TABLE IF NOT EXISTS inventario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT NOT NULL,
    cantidad INTEGER NOT NULL
)
''')

# Insertar algunos datos de ejemplo
cursor.execute('INSERT INTO caninos (nombre, estado, historial_medico) VALUES ("Max", "Disponible", "Pendiente de vacunas")')
cursor.execute('INSERT INTO caninos (nombre, estado, historial_medico) VALUES ("Bella", "Disponible", "Vacunas al día")')
cursor.execute('INSERT INTO inventario (item, cantidad) VALUES ("Alimento", 20)')

# Guardar los cambios
conn.commit()
conn.close()

print("Base de datos creada exitosamente con caninos e inventario.")
