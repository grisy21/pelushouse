import multiprocessing
import time
import sqlite3
import smtplib

# Clase para consultar el estado de los caninos
class ConsultarCaninos(multiprocessing.Process):
    def run(self):
        conn = sqlite3.connect('adopciones.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM caninos')
        caninos = cursor.fetchall()
        conn.close()

        print("Caninos disponibles para adopción:")
        for canino in caninos:
            print(f"ID: {canino[0]} - Nombre: {canino[1]} - Estado: {canino[2]} - Estatus Médico: {canino[3]}")
        time.sleep(2)  # Simulación de una consulta lenta

# Clase para simular el registro de adopción
class RegistrarAdopcion(multiprocessing.Process):
    def run(self):
        conn = sqlite3.connect('adopciones.db')
        cursor = conn.cursor()

        # Simulación de actualización de estado del canino
        cursor.execute('UPDATE caninos SET estado = "Adoptado" WHERE id = 1')
        conn.commit()
        conn.close()

        print("Adopción registrada exitosamente.")
        time.sleep(1)

# Clase para actualizar el inventario (ej. alimentos)
class ActualizarInventario(multiprocessing.Process):
    def run(self):
        conn = sqlite3.connect('adopciones.db')
        cursor = conn.cursor()

        # Simulación de actualización de inventario
        cursor.execute('UPDATE inventario SET cantidad = cantidad - 1 WHERE item = "Alimento"')
        conn.commit()
        conn.close()

        print("Inventario actualizado (Alimentos).")
        time.sleep(1)

# Clase para actualizar el historial médico del canino
class ActualizarHistorialMedico(multiprocessing.Process):
    def run(self):
        conn = sqlite3.connect('adopciones.db')
        cursor = conn.cursor()

        # Simulación de actualización de historial médico
        cursor.execute('UPDATE caninos SET historial_medico = "Vacunas al día" WHERE id = 1')
        conn.commit()
        conn.close()

        print("Historial médico actualizado.")
        time.sleep(1)

# Clase para enviar un correo de confirmación de adopción
class EnviarConfirmacionCorreo(multiprocessing.Process):
    def run(self):
        time.sleep(1)  # Simulación de tiempo de envío
        print("Correo de confirmación de adopción enviado.")

if __name__ == '__main__':
    # Crear procesos
    consulta = ConsultarCaninos()
    registro = RegistrarAdopcion()
    inventario = ActualizarInventario()
    historial = ActualizarHistorialMedico()
    correo = EnviarConfirmacionCorreo()

    # Iniciar procesos
    consulta.start()
    registro.start()
    inventario.start()
    historial.start()
    correo.start()

    # Esperar a que todos los procesos terminen
    consulta.join()
    registro.join()
    inventario.join()
    historial.join()
    correo.join()

    print("Todos los procesos han terminado.")
