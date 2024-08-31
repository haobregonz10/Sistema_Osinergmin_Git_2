from sqlite3 import Error
from .connection import create_connection
from xlsxwriter.workbook import Workbook
from datetime import datetime

def insert_book(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM central_generacion WHERE COD_CENTRAL = ?"
    insert_sql = """
        INSERT INTO central_generacion (COD_EMP,COD_CENTRAL,NOMBRE,TIPO_CENTRAL,COD_AREA,TIPO_SISTEMA,AREA_OPERATIVA,REGION_GEOGRAFICA,ZONA,ALTITUD,CAUDAL_DISENO,COEF_PRODUCCION,CONSUMO_PROPIO,DIRECCION,TELEFONO,ESTADO,FECHA_ALTA,DATUM_UTM,ZONA_UTM) 
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """
    update_sql = """
        UPDATE central_generacion SET 
        NOMBRE = ?, 
        TIPO_CENTRAL = ?, 
        COD_AREA = ?, 
        TIPO_SISTEMA = ?, 
        AREA_OPERATIVA = ?, 
        REGION_GEOGRAFICA = ?, 
        ZONA = ?, 
        ALTITUD = ?, 
        CAUDAL_DISENO = ?, 
        COEF_PRODUCCION = ?, 
        CONSUMO_PROPIO = ?, 
        DIRECCION = ?, 
        TELEFONO = ?, 
        ESTADO = ?, 
        FECHA_ALTA = ?, 
        DATUM_UTM = ?, 
        ZONA_UTM = ?
        WHERE COD_CENTRAL = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1],))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL, actualiza los datos
            cur.execute(update_sql, data[2:] + (data[1],))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_book_central_generacion_coordenadas(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Central_Generacion_Vertice_Perimetro_Coordenadas_Geograficas WHERE COD_CENTRAL = ?"
    insert_sql = """ 
        INSERT INTO Central_Generacion_Vertice_Perimetro_Coordenadas_Geograficas (COD_EMP,COD_CENTRAL,SECUENCIA,X,Y,Z) 
        VALUES(?,?,?,?,?,?)
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1],))
        cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de coordenadas agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de coordenadas:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_central_generacion_vertice_plano(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Central_Generacion_Vertice_Perimetro_Plano_Planta WHERE COD_CENTRAL = ?"
    insert_sql = """ 
        INSERT INTO Central_Generacion_Vertice_Perimetro_Plano_Planta (COD_EMP,COD_CENTRAL,SECUENCIA,X,Y,Z) 
        VALUES(?,?,?,?,?,?)
    """
    update_sql = """
        UPDATE Central_Generacion_Vertice_Perimetro_Plano_Planta SET 
        SECUENCIA = ?, 
        X = ?, 
        Y = ?, 
        Z = ?
        WHERE COD_CENTRAL = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1],))

        cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de vértice plano agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de vértice plano:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_book_central_generador(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Generador_Central_Generacion WHERE COD_CENTRAL = ? AND COD_GENERADOR = ?"
    insert_sql = """ 
        INSERT INTO Generador_Central_Generacion (COD_EMP,COD_CENTRAL,COD_GENERADOR,POT_NOM,TENSION_NOM,TIPO_TURBINA,ESTADO,FECHA_ALTA) 
        VALUES(?,?,?,?,?,?,?,?)
    """
    update_sql = """
        UPDATE Generador_Central_Generacion SET 
        POT_NOM = ?, 
        TENSION_NOM = ?, 
        TIPO_TURBINA = ?, 
        ESTADO = ?, 
        FECHA_ALTA = ?
        WHERE COD_CENTRAL = ? AND COD_GENERADOR = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_GENERADOR, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de generador agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de generador:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_celda_central_generacion(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Celda_Central_Generacion 
                    WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_CELDA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Celda_Central_Generacion 
                            SET TIPO_CELDA = ?, TIPO_INSTALACION = ?, TENSION_NOM = ?, ESTADO = ?, FECHA_ALTA = ?
                            WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_CELDA = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[6], data[7], data[0], data[1], data[2]))
            conn.commit()
            print("Registro de celda central de generación actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Celda_Central_Generacion (COD_EMP, COD_CENTRAL, COD_CELDA, TIPO_CELDA, TIPO_INSTALACION, TENSION_NOM, ESTADO, FECHA_ALTA) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de celda central de generación agregado!")
        
        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de celda central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_barra_central_generacion(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Barra_Central_Generacion WHERE COD_CENTRAL = ? AND COD_BARRA = ?"
    insert_sql = """ 
        INSERT INTO Barra_Central_Generacion (COD_EMP,COD_CENTRAL,COD_BARRA,TIPO_ARREGLO,TIPO_INSTALACION,TENSION,BARRA_REFERENCIA,ESTADO,FECHA_ALTA) 
        VALUES(?,?,?,?,?,?,?,?,?)
    """
    update_sql = """
        UPDATE Barra_Central_Generacion SET 
        TIPO_ARREGLO = ?, 
        TIPO_INSTALACION = ?, 
        TENSION = ?, 
        BARRA_REFERENCIA = ?, 
        ESTADO = ?, 
        FECHA_ALTA = ?
        WHERE COD_CENTRAL = ? AND COD_BARRA = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_BARRA, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de barra central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de barra central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_portico_central_generacion(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Portico_Central_Generacion WHERE COD_CENTRAL = ? AND COD_PORTICO = ?"
    insert_sql = """ 
        INSERT INTO Portico_Central_Generacion (COD_EMP,COD_CENTRAL,COD_PORTICO,TIPO,ALTURA,ESTADO,FECHA_ALTA) 
        VALUES(?,?,?,?,?,?,?)
    """
    update_sql = """
        UPDATE Portico_Central_Generacion SET 
        TIPO = ?, 
        ALTURA = ?, 
        ESTADO = ?, 
        FECHA_ALTA = ?
        WHERE COD_CENTRAL = ? AND COD_PORTICO = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_PORTICO, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de portico central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de portico central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()




def insert_book_interruptor_central_generacion(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Interruptor_Central_Generacion 
                    WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_INTERRUPTOR = ? AND COD_CELDA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2], data[3]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Interruptor_Central_Generacion 
                            SET TIPO_INSTALACION = ?, TENSION_NOM = ?, MARCA = ?, ANIO_FA = ?, ESTADO = ?, FECHA_ALTA = ?
                            WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_INTERRUPTOR = ? AND COD_CELDA = ?"""
            cur.execute(sql_update, (data[4], data[5], data[6], data[7], data[8], data[9], data[0], data[1], data[2], data[3]))
            conn.commit()
            print("Registro de interruptor central de generación actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Interruptor_Central_Generacion (
                                COD_EMP, COD_CENTRAL, COD_INTERRUPTOR, COD_CELDA, TIPO_INSTALACION, TENSION_NOM, MARCA, ANIO_FA, ESTADO, FECHA_ALTA
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de interruptor central de generación agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de interruptor central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_seccionador_central_generacion(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Seccionador_Central_Generacion 
                    WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_SECCIONADOR = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Seccionador_Central_Generacion 
                            SET COD_CELDA = ?, TIPO_SECCIONADOR = ?, TIPO_INSTALACION = ?, 
                                TENSION_NOM = ?, MARCA = ?, ANIO_FA = ?, ESTADO = ?, FECHA_ALTA = ?
                            WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_SECCIONADOR = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], 
                                      data[0], data[1], data[2]))
            conn.commit()
            print("Registro de seccionador central de generación actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Seccionador_Central_Generacion (
                                COD_EMP, COD_CENTRAL, COD_SECCIONADOR, COD_CELDA, TIPO_SECCIONADOR, 
                                TIPO_INSTALACION, TENSION_NOM, MARCA, ANIO_FA, ESTADO, FECHA_ALTA
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de seccionador central de generación agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de seccionador central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_transformador_central_generacion(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Transformador_Central_Generacion WHERE COD_CENTRAL = ? AND COD_TRANSF = ?"
    insert_sql = """ 
        INSERT INTO Transformador_Central_Generacion (
            COD_EMP, COD_CENTRAL, COD_TRANSF, TIPO_TRANSF, 
            TIPO_INSTALACION, CONEXION, NUM_SERIE, TENSION_PRI, 
            TENSION_SEC, TENSION_TER, POT_PRI, POT_SEC, POT_TER, 
            MARCA, ANIO_FA, DISPONIBILIDAD, VCC_PS, VCC_ST, 
            VCC_PT, VCC_SBASE, PERCU_P, PERCU_S, PERCU_T, PERH_P, 
            PERH_S, PERH_T, ESTADO, FECHA_ALTA
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Transformador_Central_Generacion SET 
        TIPO_TRANSF = ?, 
        TIPO_INSTALACION = ?, 
        CONEXION = ?, 
        NUM_SERIE = ?, 
        TENSION_PRI = ?, 
        TENSION_SEC = ?, 
        TENSION_TER = ?, 
        POT_PRI = ?, 
        POT_SEC = ?, 
        POT_TER = ?, 
        MARCA = ?, 
        ANIO_FA = ?, 
        DISPONIBILIDAD = ?, 
        VCC_PS = ?, 
        VCC_ST = ?, 
        VCC_PT = ?, 
        VCC_SBASE = ?, 
        PERCU_P = ?, 
        PERCU_S = ?, 
        PERCU_T = ?, 
        PERH_P = ?, 
        PERH_S = ?, 
        PERH_T = ?, 
        ESTADO = ?, 
        FECHA_ALTA = ?
        WHERE COD_CENTRAL = ? AND COD_TRANSF = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_TRANSF, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de transformador central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de transformador central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_pararrayo_central_generacion(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Pararrayo_Central_Generacion WHERE COD_CENTRAL = ? AND COD_PARARRAYO = ?"
    insert_sql = """ 
        INSERT INTO Pararrayo_Central_Generacion (COD_EMP,COD_CENTRAL,COD_PARARRAYO,TENSION_NOM,MARCA,ANIO_FA,ESTADO,FECHA_ALTA) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Pararrayo_Central_Generacion SET 
        TENSION_NOM = ?, 
        MARCA = ?, 
        ANIO_FA = ?, 
        ESTADO = ?, 
        FECHA_ALTA = ?
        WHERE COD_CENTRAL = ? AND COD_PARARRAYO = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_PARARRAYO, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de pararrayo central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de pararrayo central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()




def insert_book_transformador_medicion_central_generacion(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Transformador_Medicion_Central_Generacion WHERE COD_CENTRAL = ? AND COD_TRANSF = ?"
    insert_sql = """ 
        INSERT INTO Transformador_Medicion_Central_Generacion (
            COD_EMP, COD_CENTRAL, COD_TRANSF, TIPO_TRANSF, TIPO_INSTALACION, TENSION_NOM, MARCA, ANIO_FA, ESTADO, FECHA_ALTA
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Transformador_Medicion_Central_Generacion SET 
        TIPO_TRANSF = ?, 
        TIPO_INSTALACION = ?, 
        TENSION_NOM = ?, 
        MARCA = ?, 
        ANIO_FA = ?, 
        ESTADO = ?, 
        FECHA_ALTA = ?
        WHERE COD_CENTRAL = ? AND COD_TRANSF = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_TRANSF, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de transformador de medición central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de transformador de medición central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_conductor_central_generacion(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Conductor_Central_Generacion WHERE COD_CENTRAL = ? AND COD_CONDUCTOR = ?"
    insert_sql = """ 
        INSERT INTO Conductor_Central_Generacion (
            COD_EMP, COD_CENTRAL, COD_CONDUCTOR, TENSION_NOM, ESTADO, FECHA_ALTA
        ) 
        VALUES (?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Conductor_Central_Generacion SET 
        TENSION_NOM = ?, 
        ESTADO = ?, 
        FECHA_ALTA = ?
        WHERE COD_CENTRAL = ? AND COD_CONDUCTOR = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_CONDUCTOR, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de conductor central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de conductor central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_subestacion(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Subestacion 
                    WHERE COD_EMP = ? AND COD_SE = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Subestacion 
                            SET NOMBRE = ?, COD_CALIFICACION = ?, TIPO_SISTEMA = ?, COD_AREA = ?, AREA_OPERATIVA = ?, REGION_GEOGRAFICA = ?,
                                ZONA = ?, ALTITUD = ?, TECNOLOGIA_SE = ?, FUNCION = ?, ATENDIDA = ?, DIRECCION = ?, TELEFONO = ?,
                                COD_MODULO_SERV_AUX = ?, COD_MODULO_OBRA_CIVIL = ?, COD_MODULO_EDIF_CONTROL = ?, COD_MODULO_TIERRA_PROF = ?,
                                COD_MODULO_IEE = ?, ESTADO = ?, FECHA_ALTA = ?, DATUM_UTM = ?, ZONA_UTM = ?
                            WHERE COD_EMP = ? AND COD_SE = ?"""
            cur.execute(sql_update, (*data[2:], *data[:2]))
            conn.commit()
            print("Registro de Subestación actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Subestacion (
                                COD_EMP, COD_SE, NOMBRE, COD_CALIFICACION, TIPO_SISTEMA, COD_AREA, AREA_OPERATIVA, REGION_GEOGRAFICA,
                                ZONA, ALTITUD, TECNOLOGIA_SE, FUNCION, ATENDIDA, DIRECCION, TELEFONO, COD_MODULO_SERV_AUX, 
                                COD_MODULO_OBRA_CIVIL, COD_MODULO_EDIF_CONTROL, COD_MODULO_TIERRA_PROF, COD_MODULO_IEE,
                                ESTADO, FECHA_ALTA, DATUM_UTM, ZONA_UTM
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Subestación agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Subestación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_linea_transmision(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Linea_Transmision 
                    WHERE COD_EMP = ? AND COD_LINEA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Linea_Transmision 
                            SET NOMBRE = ?, TIPO_SISTEMA = ?, TENSION_NOM = ?, NODO_SALIDA = ?, NODO_LLEGADA = ?, CELDA_SALIDA = ?, CELDA_LLEGADA = ?
                            WHERE COD_EMP = ? AND COD_LINEA = ?"""
            cur.execute(sql_update, (*data[2:], *data[:2]))
            conn.commit()
            print("Registro de Línea de Transmisión actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Linea_Transmision (
                                COD_EMP, COD_LINEA, NOMBRE, TIPO_SISTEMA, TENSION_NOM, NODO_SALIDA, NODO_LLEGADA, CELDA_SALIDA, CELDA_LLEGADA
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Línea de Transmisión agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Línea de Transmisión:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_book_tramo_linea_transmision(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Tramo_Linea_Transmision 
                    WHERE COD_EMP = ? AND COD_LINEA = ? AND COD_TRAMO = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Tramo_Linea_Transmision 
                            SET COD_CALIFICACION = ?, TIPO_CIRCUITO = ?, COD_AREA = ?, AREA_OPERATIVA = ?, REGION_GEOGRAFICA = ?, ZONA = ?, ALTITUD = ?,
                                TIPO_RED = ?, LONGITUD = ?, DISPOSICION_FASES = ?, NUM_COND_X_FASE = ?, TIPO_CONDUCTOR = ?, SECCION_CONDUCTOR = ?, 
                                POTENCIA_NOM = ?, CORRIENTE_NOM = ?, TENSION_NOM = ?, TENSION_OPERACION = ?, TENSION_AISLAMIENTO = ?, R1_TRAMO = ?, 
                                X1_TRAMO = ?, B1_TRAMO = ?, G1_TRAMO = ?, NUM_CABLE_GUARDA = ?, MAT_CABLE_GUARDA = ?, SECCION_CABLE_GUARDA = ?, 
                                COD_MODULO = ?, ESTADO = ?, FECHA_ALTA = ?, DATUM_UTM = ?, ZONA_UTM = ?
                            WHERE COD_EMP = ? AND COD_LINEA = ? AND COD_TRAMO = ?"""
            cur.execute(sql_update, (*data[3:], data[0], data[1], data[2]))
            conn.commit()
            print("Registro del Tramo de Línea de Transmisión actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Tramo_Linea_Transmision (
                                COD_EMP, COD_LINEA, COD_TRAMO, COD_CALIFICACION, TIPO_CIRCUITO, COD_AREA, AREA_OPERATIVA, REGION_GEOGRAFICA, ZONA, ALTITUD,
                                TIPO_RED, LONGITUD, DISPOSICION_FASES, NUM_COND_X_FASE, TIPO_CONDUCTOR, SECCION_CONDUCTOR, POTENCIA_NOM, CORRIENTE_NOM, 
                                TENSION_NOM, TENSION_OPERACION, TENSION_AISLAMIENTO, R1_TRAMO, X1_TRAMO, B1_TRAMO, G1_TRAMO, NUM_CABLE_GUARDA, MAT_CABLE_GUARDA,
                                SECCION_CABLE_GUARDA, COD_MODULO, ESTADO, FECHA_ALTA, DATUM_UTM, ZONA_UTM
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Tramo de Línea de Transmisión agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro del Tramo de Línea de Transmisión:", e)
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_tramo_linea_transmision_ubicacion_geografica(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Tramo_Linea_Vertice_Ubicacion_Geografica 
                    WHERE COD_EMP = ? AND COD_LINEA = ? AND COD_TRAMO = ? AND SECUENCIA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2], data[3]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Tramo_Linea_Vertice_Ubicacion_Geografica 
                            SET  X = ?, Y = ?, Z = ?
                            WHERE COD_EMP = ? AND COD_LINEA = ? AND COD_TRAMO = ? AND SECUENCIA = ?"""
            cur.execute(sql_update, (*data[4:], *data[:4]))
            conn.commit()
            print("Registro de Ubicación Geográfica del Tramo de Línea de Transmisión actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Tramo_Linea_Vertice_Ubicacion_Geografica (
                                COD_EMP, COD_LINEA, COD_TRAMO, SECUENCIA, X, Y, Z
                            ) VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Ubicación Geográfica del Tramo de Línea de Transmisión agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Ubicación Geográfica del Tramo de Línea de Transmisión:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_transmision_linea_estructura(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Estructura 
                    WHERE COD_EMP = ? AND COD_LINEA = ? AND COD_ESTRUCTURA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Estructura 
                            SET COD_CALIFICACION = ?, TIPO = ?, FUNCION = ?, ALTURA = ?, NUM_CIRCUITOS = ?, FORMACION_FASE = ?, 
                                NUM_CABLE_GUARDA = ?, LOCALIDAD = ?, ESTADO = ?, FECHA_ALTA = ?
                            WHERE COD_EMP = ? AND COD_LINEA = ? AND COD_ESTRUCTURA = ?"""
            cur.execute(sql_update, (*data[3:], *data[:3]))
            conn.commit()
            print("Registro de Estructura de Transmisión actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Estructura (
                                COD_EMP, COD_LINEA, COD_ESTRUCTURA, COD_CALIFICACION, TIPO, FUNCION, ALTURA, NUM_CIRCUITOS, 
                                FORMACION_FASE, NUM_CABLE_GUARDA, LOCALIDAD, ESTADO, FECHA_ALTA
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Estructura de Transmisión agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Estructura de Transmisión:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_transmision_linea_estructura_ubicacion_geografica(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Estructura_Ubicacion_Geografica 
                    WHERE COD_EMP = ? AND COD_LINEA = ? AND COD_ESTRUCTURA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Estructura_Ubicacion_Geografica 
                            SET DATUM = ?, ZONA = ?, X = ?, Y = ?, Z = ?, ANG = ?
                            WHERE COD_EMP = ? AND COD_LINEA = ? AND COD_ESTRUCTURA = ?"""
            cur.execute(sql_update, (*data[3:], *data[:3]))
            conn.commit()
            print("Registro de Ubicación Geográfica de Estructura de Transmisión actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Estructura_Ubicacion_Geografica (
                                COD_EMP, COD_LINEA, COD_ESTRUCTURA, DATUM, ZONA, X, Y, Z, ANG
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Ubicación Geográfica de Estructura de Transmisión agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Ubicación Geográfica de Estructura de Transmisión:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()




def insert_book_transmision_linea_estructura_ubicacion_subestacion(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Estructura_Ubicacion_Plano_Planta_Subestacion 
                    WHERE COD_EMP = ? AND COD_LINEA = ? AND COD_ESTRUCTURA = ? AND COD_SE = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2], data[3]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Estructura_Ubicacion_Plano_Planta_Subestacion 
                            SET X = ?, Y = ?, Z = ?, ANG = ?
                            WHERE COD_EMP = ? AND COD_LINEA = ? AND COD_ESTRUCTURA = ? AND COD_SE = ?"""
            cur.execute(sql_update, (*data[4:], *data[:4]))
            conn.commit()
            print("Registro de Ubicación en Plano/Planta de Estructura de Transmisión en Subestación actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Estructura_Ubicacion_Plano_Planta_Subestacion (
                                COD_EMP, COD_LINEA, COD_ESTRUCTURA, COD_SE, X, Y, Z, ANG
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Ubicación en Plano/Planta de Estructura de Transmisión en Subestación agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Ubicación en Plano/Planta de Estructura de Transmisión en Subestación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_transmision_linea_estructura_ubicacion_central(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Estructura_Ubicacion_Plano_Planta_Central_Generacion 
                    WHERE COD_EMP = ? AND COD_LINEA = ? AND COD_ESTRUCTURA = ? AND COD_CENTRAL = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2], data[3]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Estructura_Ubicacion_Plano_Planta_Central_Generacion 
                            SET X = ?, Y = ?, Z = ?, ANG = ?
                            WHERE COD_EMP = ? AND COD_LINEA = ? AND COD_ESTRUCTURA = ? AND COD_CENTRAL = ?"""
            cur.execute(sql_update, (*data[4:], *data[:4]))
            conn.commit()
            print("Registro de Ubicación en Plano/Planta de Estructura de Transmisión en Central de Generación actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Estructura_Ubicacion_Plano_Planta_Central_Generacion (
                                COD_EMP, COD_LINEA, COD_ESTRUCTURA, COD_CENTRAL, X, Y, Z, ANG
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Ubicación en Plano/Planta de Estructura de Transmisión en Central de Generación agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Ubicación en Plano/Planta de Estructura de Transmisión en Central de Generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_subestacion_coordenadas_geograficas(data):
    conn = create_connection()
    sql = """INSERT INTO Subestacion_Vertice_Perimetro_Coordenadas_Geograficas (
                COD_EMP, COD_SE, SECUENCIA, X, Y, Z
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar nuevo registro:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_book_subestacion_plano_planta(data):
    conn = create_connection()
    sql = """INSERT INTO Subestacion_Vertice_Perimetro_Plano_Planta (
                COD_EMP, COD_SE, SECUENCIA, X, Y, Z
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar nuevo registro:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_book_barra(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Barra WHERE COD_SE = ? AND COD_BARRA = ?"
    insert_sql = """ 
        INSERT INTO Barra (
            COD_EMP, COD_SE, COD_BARRA, COD_CALIFICACION, TIPO_BARRA, 
            TIPO_ARREGLO, TIPO_INSTALACION, TENSION_NOM, BARRA_REFERENCIA, 
            ESTADO, FECHA_ALTA
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Barra SET 
            COD_CALIFICACION = ?, 
            TIPO_BARRA = ?, 
            TIPO_ARREGLO = ?, 
            TIPO_INSTALACION = ?, 
            TENSION_NOM = ?, 
            BARRA_REFERENCIA = ?, 
            ESTADO = ?, 
            FECHA_ALTA = ?
        WHERE COD_SE = ? AND COD_BARRA = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_SE y COD_BARRA, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de barra agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de barra:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_barra_ubicacion_esquema(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Barra_Ubicacion_Esquema WHERE COD_EMP = ? AND COD_SE = ? AND COD_BARRA = ? AND SECUENCIA = ?"
    insert_sql = """ 
        INSERT INTO Barra_Ubicacion_Esquema (
            COD_EMP, COD_SE, COD_BARRA, SECUENCIA, X, Y
        ) 
        VALUES (?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Barra_Ubicacion_Esquema SET 
            SECUENCIA = ?, 
            X = ?, 
            Y = ?
        WHERE COD_SE = ? AND COD_BARRA = ? AND SECUENCIA = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[0],data[1], data[2],data[3]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_SE y COD_BARRA, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2], data[3]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en esquema de barra agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en esquema de barra:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_barra_plano_planta(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Barra_Ubicacion_Plano_Planta WHERE COD_EMP = ? AND COD_SE = ? AND COD_BARRA = ? AND SECUENCIA = ?"
    insert_sql = """ 
        INSERT INTO Barra_Ubicacion_Plano_Planta (
            COD_EMP, COD_SE, COD_BARRA, COD_SEGMENTO, COD_FASE, SECUENCIA, X, Y, Z
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Barra_Ubicacion_Plano_Planta SET 
            COD_SEGMENTO = ?, 
            COD_FASE = ?, 
            SECUENCIA = ?, 
            X = ?, 
            Y = ?, 
            Z = ?
        WHERE COD_SE = ? AND COD_BARRA = ? AND SECUENCIA = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[0],data[1], data[2],data[5]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_SE y COD_BARRA, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2], data[5]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en plano planta de barra agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en plano planta de barra:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_transformador_potencia(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Transformador_Potencia WHERE COD_SE = ? AND COD_TRANSF = ?"
    insert_sql = """ 
        INSERT INTO Transformador_Potencia (
            COD_EMP, COD_SE, COD_TRANSF, COD_CALIFICACION, NUM_SERIE, TIPO_TRANSF, TIPO_INSTALACION, CONEXION, TENSION_PRI, TENSION_SEC, TENSION_TER,
            POT_PRI, POT_SEC, POT_TER, MARCA, ANIO_FA, DISPONIBILIDAD, REGULA_TEN_N_TAPS, REGULA_TEN_V_TAP, REGULA_TEN_TIPO, REGULA_TEN_POS, VCC_PS,
            VCC_ST, VCC_PT, VCC_SBASE, PERCU_P, PERCU_S, PERCU_T, PERH_P, PERH_S, PERH_T, COD_MODULO, ESTADO, FECHA_ALTA
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    update_sql = """
        UPDATE Transformador_Potencia SET 
            COD_CALIFICACION = ?, NUM_SERIE = ?, TIPO_TRANSF = ?, TIPO_INSTALACION = ?, CONEXION = ?, TENSION_PRI = ?, 
            TENSION_SEC = ?, TENSION_TER = ?, POT_PRI = ?, POT_SEC = ?, POT_TER = ?, MARCA = ?, ANIO_FA = ?, DISPONIBILIDAD = ?, 
            REGULA_TEN_N_TAPS = ?, REGULA_TEN_V_TAP = ?, REGULA_TEN_TIPO = ?, REGULA_TEN_POS = ?, VCC_PS = ?, VCC_ST = ?, 
            VCC_PT = ?, VCC_SBASE = ?, PERCU_P = ?, PERCU_S = ?, PERCU_T = ?, PERH_P = ?, PERH_S = ?, PERH_T = ?, 
            COD_MODULO = ?, ESTADO = ?, FECHA_ALTA = ?
        WHERE COD_SE = ? AND COD_TRANSF = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_SE y COD_TRANSF, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de transformador de potencia agregado o actualizado correctamente!")
        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de transformador de potencia:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_transformador_potencia_ubicacion_esquema(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Transformador_Potencia_Ubicacion_Esquema WHERE COD_SE = ? AND COD_TRANSF = ?"
    insert_sql = """ 
        INSERT INTO Transformador_Potencia_Ubicacion_Esquema (
            COD_EMP, COD_SE, COD_TRANSF, X, Y, ANG
        ) 
        VALUES (?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Transformador_Potencia_Ubicacion_Esquema SET 
            X = ?, 
            Y = ?, 
            ANG = ?
        WHERE COD_SE = ? AND COD_TRANSF = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_SE y COD_TRANSF, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en esquema de transformador de potencia agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en esquema de transformador de potencia:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_transformador_potencia_ubicacion_plano(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Transformador_Potencia_Ubicacion_Plano_Planta WHERE COD_SE = ? AND COD_TRANSF = ?"
    insert_sql = """ 
        INSERT INTO Transformador_Potencia_Ubicacion_Plano_Planta (
            COD_EMP, COD_SE, COD_TRANSF, X, Y, Z, ANG
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Transformador_Potencia_Ubicacion_Plano_Planta SET 
            X = ?, 
            Y = ?, 
            Z = ?, 
            ANG = ?
        WHERE COD_SE = ? AND COD_TRANSF = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_SE y COD_TRANSF, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en plano planta de transformador de potencia agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en plano planta de transformador de potencia:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_transmision_interruptor(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Interruptor_Potencia 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_INTERRUPTOR = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Interruptor_Potencia 
                            SET COD_CELDA = ?, COD_CALIFICACION = ?, TIPO_INSTALACION = ?, TENSION_NOM = ?, MARCA = ?, ANIO_FA = ?, ESTADO = ?, FECHA_ALTA = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_INTERRUPTOR = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[0], data[1], data[2]))
            conn.commit()
            print("Registro de Interruptor Potencia actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Interruptor_Potencia (
                                COD_EMP, COD_SE, COD_INTERRUPTOR, COD_CELDA, COD_CALIFICACION, TIPO_INSTALACION, TENSION_NOM, MARCA, ANIO_FA, ESTADO, FECHA_ALTA
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Interruptor Potencia agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Interruptor Potencia:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()




def insert_book_transmision_interruptor_ubicacion_plano(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Interruptor_Potencia_Ubicacion_Plano_Planta 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_INTERRUPTOR = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Interruptor_Potencia_Ubicacion_Plano_Planta 
                            SET X = ?, Y = ?, Z = ?, ANG = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_INTERRUPTOR = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[6], data[0], data[1], data[2]))
            conn.commit()
            print("Registro de ubicación de Interruptor Potencia actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Interruptor_Potencia_Ubicacion_Plano_Planta (
                                COD_EMP, COD_SE, COD_INTERRUPTOR, X, Y, Z, ANG
                            ) VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de ubicación de Interruptor Potencia agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación de Interruptor Potencia:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_transmision_interruptor_ubicacion_esquema(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Interruptor_Potencia_Ubicacion_Esquema 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_INTERRUPTOR = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Interruptor_Potencia_Ubicacion_Esquema 
                            SET X = ?, Y = ?, ANG = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_INTERRUPTOR = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[0], data[1], data[2]))
            conn.commit()
            print("Registro de ubicación de Interruptor Potencia actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Interruptor_Potencia_Ubicacion_Esquema (
                                COD_EMP, COD_SE, COD_INTERRUPTOR, X, Y, ANG
                            ) VALUES (?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de ubicación de Interruptor Potencia agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación de Interruptor Potencia:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_transmision_seccionador(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Seccionador 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_SECCIONADOR = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Seccionador 
                            SET COD_CELDA = ?, COD_CALIFICACION = ?, TIPO_SECCIONADOR = ?, TIPO_INSTALACION = ?, TENSION_NOM = ?, MARCA = ?, ANIO_FA = ?, ESTADO = ?, FECHA_ALTA = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_SECCIONADOR = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[0], data[1], data[2]))
            conn.commit()
            print("Registro de Seccionador actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Seccionador (
                                COD_EMP, COD_SE, COD_SECCIONADOR, COD_CELDA, COD_CALIFICACION, TIPO_SECCIONADOR, TIPO_INSTALACION, TENSION_NOM, MARCA, ANIO_FA, ESTADO, FECHA_ALTA
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Seccionador agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Seccionador:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_transmision_seccionador_ubicacion_plano(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Seccionador_Ubicacion_Plano_Planta 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_SECCIONADOR = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Seccionador_Ubicacion_Plano_Planta 
                            SET X = ?, Y = ?, Z = ?, ANG = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_SECCIONADOR = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[6], data[0], data[1], data[2]))
            conn.commit()
            print("Registro de Seccionador Ubicación Plano Planta actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Seccionador_Ubicacion_Plano_Planta (
                                COD_EMP, COD_SE, COD_SECCIONADOR, X, Y, Z, ANG
                            ) VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Seccionador Ubicación Plano Planta agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Seccionador Ubicación Plano Planta:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_transmision_seccionador_ubicacion_esquema(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Seccionador_Ubicacion_Esquema 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_SECCIONADOR = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Seccionador_Ubicacion_Esquema 
                            SET X = ?, Y = ?, ANG = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_SECCIONADOR = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[0], data[1], data[2]))
            conn.commit()
            print("Registro de Seccionador Ubicación Esquema actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Seccionador_Ubicacion_Esquema (
                                COD_EMP, COD_SE, COD_SECCIONADOR, X, Y, ANG
                            ) VALUES (?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Seccionador Ubicación Esquema agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Seccionador Ubicación Esquema:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_interruptor_central_generacion_ubicacion_esquema(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Interruptor_Central_Generacion_Ubicacion_Esquema 
                    WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_INTERRUPTOR = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Interruptor_Central_Generacion_Ubicacion_Esquema 
                            SET X = ?, Y = ?, ANG = ?
                            WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_INTERRUPTOR = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[0], data[1], data[2]))
            conn.commit()
            print("Registro de ubicación de esquema de interruptor central de generación actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Interruptor_Central_Generacion_Ubicacion_Esquema (
                                COD_EMP, COD_CENTRAL, COD_INTERRUPTOR, X, Y, ANG
                            ) VALUES (?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de ubicación de esquema de interruptor central de generación agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación de esquema de interruptor central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_interruptor_central_generacion_ubicacion_planta(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Interruptor_Central_Generacion_Ubicacion_Plano_Planta 
                    WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_INTERRUPTOR = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Interruptor_Central_Generacion_Ubicacion_Plano_Planta 
                            SET X = ?, Y = ?, Z = ?, ANG = ?
                            WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_INTERRUPTOR = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[6], data[0], data[1], data[2]))
            conn.commit()
            print("Registro de ubicación de plano planta de interruptor central de generación actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Interruptor_Central_Generacion_Ubicacion_Plano_Planta (
                                COD_EMP, COD_CENTRAL, COD_INTERRUPTOR, X, Y, Z, ANG
                            ) VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de ubicación de plano planta de interruptor central de generación agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación de plano planta de interruptor central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_transmision_pararrayo(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Pararrayo WHERE COD_SE = ? AND COD_PARARRAYO = ?"
    insert_sql = """ 
        INSERT INTO Pararrayo (
            COD_EMP, COD_SE, COD_PARARRAYO, COD_CALIFICACION, TENSION_NOM, MARCA, ANIO_FA, ESTADO, FECHA_ALTA
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Pararrayo SET 
            COD_CALIFICACION = ?, 
            TENSION_NOM = ?, 
            MARCA = ?, 
            ANIO_FA = ?, 
            ESTADO = ?, 
            FECHA_ALTA = ?
        WHERE COD_SE = ? AND COD_PARARRAYO = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_SE y COD_PARARRAYO, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de pararrayo de transmisión agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de pararrayo de transmisión:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_book_transmision_pararrayo_ubicacion_esquema(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Pararrayo_Ubicacion_Esquema WHERE COD_SE = ? AND COD_PARARRAYO = ?"
    insert_sql = """ 
        INSERT INTO Pararrayo_Ubicacion_Esquema (
            COD_EMP, COD_SE, COD_PARARRAYO, X, Y, ANG
        ) 
        VALUES (?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Pararrayo_Ubicacion_Esquema SET 
            X = ?, 
            Y = ?, 
            ANG = ?
        WHERE COD_SE = ? AND COD_PARARRAYO = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_SE y COD_PARARRAYO, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en esquema de pararrayo de transmisión agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en esquema de pararrayo de transmisión:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_transmision_pararrayo_ubicacion_plano(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Pararrayo_Ubicacion_Plano_Planta WHERE COD_SE = ? AND COD_PARARRAYO = ?"
    insert_sql = """ 
        INSERT INTO Pararrayo_Ubicacion_Plano_Planta (
            COD_EMP, COD_SE, COD_PARARRAYO, X, Y, Z, ANG
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Pararrayo_Ubicacion_Plano_Planta SET 
            X = ?, 
            Y = ?, 
            Z = ?, 
            ANG = ?
        WHERE COD_SE = ? AND COD_PARARRAYO = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_SE y COD_PARARRAYO, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en plano planta de pararrayo de transmisión agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en plano planta de pararrayo de transmisión:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_transformador_medicion(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Transformador_Medicion WHERE COD_SE = ? AND COD_TRANSF = ?"
    insert_sql = """ 
        INSERT INTO Transformador_Medicion (
            COD_EMP, COD_SE, COD_TRANSF, COD_CALIFICACION, TIPO_TRANSF, TIPO_INSTALACION, TENSION_NOM, MARCA, ANIO_FA, ESTADO, FECHA_ALTA
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Transformador_Medicion SET 
            COD_CALIFICACION = ?, 
            TIPO_TRANSF = ?, 
            TIPO_INSTALACION = ?, 
            TENSION_NOM = ?, 
            MARCA = ?, 
            ANIO_FA = ?, 
            ESTADO = ?, 
            FECHA_ALTA = ?
        WHERE COD_SE = ? AND COD_TRANSF = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_SE y COD_TRANSF, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de transformador de medición agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de transformador de medición:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_transformador_medicion_ubicacion_esquema(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Transformador_Medicion_Ubicacion_Esquema WHERE COD_SE = ? AND COD_TRANSF = ?"
    insert_sql = """ 
        INSERT INTO Transformador_Medicion_Ubicacion_Esquema (
            COD_EMP, COD_SE, COD_TRANSF, X, Y, ANG
        ) 
        VALUES (?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Transformador_Medicion_Ubicacion_Esquema SET 
            X = ?, 
            Y = ?, 
            ANG = ?
        WHERE COD_SE = ? AND COD_TRANSF = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_SE y COD_TRANSF, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación esquemática de transformador de medición agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación esquemática de transformador de medición:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_transformador_medicion_ubicacion_plano(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Transformador_Medicion_Ubicacion_Plano_Planta WHERE COD_SE = ? AND COD_TRANSF = ?"
    insert_sql = """ 
        INSERT INTO Transformador_Medicion_Ubicacion_Plano_Planta (
            COD_EMP, COD_SE, COD_TRANSF, X, Y, Z, ANG
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Transformador_Medicion_Ubicacion_Plano_Planta SET 
            X = ?, 
            Y = ?, 
            Z = ?, 
            ANG = ?
        WHERE COD_SE = ? AND COD_TRANSF = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_SE y COD_TRANSF, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en plano de transformador de medición agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en plano de transformador de medición:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_bobina(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Bobina_Bloqueo WHERE COD_EMP = ? AND COD_SE = ? AND COD_BOBINA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # If the record already exists, update it
            sql_update = """UPDATE Bobina_Bloqueo SET COD_CALIFICACION = ?, TENSION_NOM = ?, MARCA = ?, ANIO_FA = ?, ESTADO = ?, FECHA_ALTA = ? 
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_BOBINA = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[6], data[7], data[8], data[0], data[1], data[2]))
            conn.commit()
            print("Registro actualizado!")
        else:
            # If the record does not exist, insert it
            sql_insert = """INSERT INTO Bobina_Bloqueo (
                                COD_EMP, COD_SE, COD_BOBINA, COD_CALIFICACION, TENSION_NOM, MARCA, ANIO_FA, ESTADO, FECHA_ALTA
                            )
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro agregado!")
        
        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar registro de bobina:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_book_compensador(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Compensador_Reactivo 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_COMP = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Compensador_Reactivo 
                            SET COD_CALIFICACION = ?, TIPO_COMP = ?, TIPO_INSTALACION = ?, TENSION_NOM = ?, MARCA = ?, ANIO_FA = ?, MODELO = ?, 
                                NUM_SERIE = ?, POT_NOM_CAP = ?, POT_NOM_IND = ?, COD_MODULO = ?, ESTADO = ?, FECHA_ALTA = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_COMP = ?"""
            cur.execute(sql_update, (*data[3:], *data[:3]))
            conn.commit()
            print("Registro de Compensador Reactivo actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Compensador_Reactivo (
                                COD_EMP, COD_SE, COD_COMP, COD_CALIFICACION, TIPO_COMP, TIPO_INSTALACION,
                                TENSION_NOM, MARCA, ANIO_FA, MODELO, NUM_SERIE, POT_NOM_CAP,
                                POT_NOM_IND, COD_MODULO, ESTADO, FECHA_ALTA
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Compensador Reactivo agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Compensador Reactivo:", e)
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_compensador_ubicacion_esquema(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Compensador_Reactivo_Ubicacion_Esquema 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_COMP = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Compensador_Reactivo_Ubicacion_Esquema 
                            SET X = ?, Y = ?, ANG = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_COMP = ?"""
            cur.execute(sql_update, (*data[3:], *data[:3]))
            conn.commit()
            print("Registro de Ubicación de Compensador Reactivo en Esquema actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Compensador_Reactivo_Ubicacion_Esquema (
                                COD_EMP, COD_SE, COD_COMP, X, Y, ANG
                            ) VALUES (?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Ubicación de Compensador Reactivo en Esquema agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Ubicación de Compensador Reactivo en Esquema:", e)
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_compensador_ubicacion_plano(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Compensador_Reactivo_Ubicacion_Plano_Planta 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_COMP = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Compensador_Reactivo_Ubicacion_Plano_Planta 
                            SET X = ?, Y = ?, Z = ?, ANG = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_COMP = ?"""
            cur.execute(sql_update, (*data[3:], *data[:3]))
            conn.commit()
            print("Registro de Ubicación de Compensador Reactivo en Plano Planta actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Compensador_Reactivo_Ubicacion_Plano_Planta (
                                COD_EMP, COD_SE, COD_COMP, X, Y, Z, ANG
                            ) VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Ubicación de Compensador Reactivo en Plano Planta agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Ubicación de Compensador Reactivo en Plano Planta:", e)
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_bobina_ubicacion_esquema(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Bobina_Bloqueo_Ubicacion_Esquema WHERE COD_EMP = ? AND COD_SE = ? AND COD_BOBINA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # If the record already exists, update it
            sql_update = """UPDATE Bobina_Bloqueo_Ubicacion_Esquema SET X = ?, Y = ?, ANG = ? 
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_BOBINA = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[0], data[1], data[2]))
            conn.commit()
            print("Registro de ubicación esquemática actualizado!")
        else:
            # If the record does not exist, insert it
            sql_insert = """INSERT INTO Bobina_Bloqueo_Ubicacion_Esquema (
                                COD_EMP, COD_SE, COD_BOBINA, X, Y, ANG
                            )
                            VALUES (?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de ubicación esquemática agregado!")
        
        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar registro de ubicación esquemática de bobina:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_bobina_ubicacion_plano(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Bobina_Bloqueo_Ubicacion_Plano_Planta 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_BOBINA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # If the record already exists, update it
            sql_update = """UPDATE Bobina_Bloqueo_Ubicacion_Plano_Planta 
                            SET X = ?, Y = ?, Z = ?, ANG = ? 
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_BOBINA = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[6], data[0], data[1], data[2]))
            conn.commit()
            print("Registro de ubicación en plano planta de bobina actualizado!")
        else:
            # If the record does not exist, insert it
            sql_insert = """INSERT INTO Bobina_Bloqueo_Ubicacion_Plano_Planta (
                                COD_EMP, COD_SE, COD_BOBINA, X, Y, Z, ANG
                            )
                            VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de ubicación en plano planta de bobina agregado!")
        
        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar registro de ubicación en plano planta de bobina:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_conductor(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Conductor 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_CONDUCTOR = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[3]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Conductor 
                            SET COD_CALIFICACION = ?, TENSION_NOM = ?, ESTADO = ?, FECHA_ALTA = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_CONDUCTOR = ?"""
            cur.execute(sql_update, (data[2], data[4], data[5], data[6], data[0], data[1], data[3]))
            conn.commit()
            print("Registro de conductor actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Conductor (
                                COD_EMP, COD_SE, COD_CALIFICACION, COD_CONDUCTOR, TENSION_NOM, ESTADO, FECHA_ALTA
                            )
                            VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de conductor agregado!")
        
        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar registro de conductor:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_conductor_ubicacion_esquema(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Conductor_Ubicacion_Esquema 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_CONDUCTOR = ? AND  SECUENCIA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2], data[3]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Conductor_Ubicacion_Esquema 
                            SET  X = ?, Y = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_CONDUCTOR = ? AND SECUENCIA = ?"""
            cur.execute(sql_update, (data[4], data[5], data[0], data[1], data[2] , data[3]))
            conn.commit()
            print("Registro de ubicación de conductor en esquema actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Conductor_Ubicacion_Esquema (
                                COD_EMP, COD_SE, COD_CONDUCTOR, SECUENCIA, X, Y
                            )
                            VALUES (?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de ubicación de conductor en esquema agregado!")
        
        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar registro de ubicación de conductor en esquema:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_conductor_ubicacion_plano(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Conductor_Ubicacion_Plano_Planta 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_CONDUCTOR = ? AND SECUENCIA = ? """

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2], data[4]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Conductor_Ubicacion_Plano_Planta 
                            SET COD_FASE = ? , X = ?, Y = ?, Z = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_CONDUCTOR = ? AND SECUENCIA = ?"""
            cur.execute(sql_update, ( data[3], data[5], data[6], data[7], data[0], data[1], data[2], data[4]))
            conn.commit()
            print("Registro de ubicación de conductor en plano planta actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Conductor_Ubicacion_Plano_Planta (
                                COD_EMP, COD_SE, COD_CONDUCTOR, COD_FASE, SECUENCIA, X, Y, Z
                            )
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de ubicación de conductor en plano planta agregado!")
        
        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar registro de ubicación de conductor en plano planta:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_central_generador_ubicacion_esquema(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Generador_Central_Generacion_Ubicacion_Esquema WHERE COD_CENTRAL = ? AND COD_GENERADOR = ?"
    insert_sql = """ 
        INSERT INTO Generador_Central_Generacion_Ubicacion_Esquema (COD_EMP, COD_CENTRAL, COD_GENERADOR, X, Y, ANG) 
        VALUES (?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Generador_Central_Generacion_Ubicacion_Esquema SET 
        X = ?, 
        Y = ?, 
        ANG = ?
        WHERE COD_CENTRAL = ? AND COD_GENERADOR = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_GENERADOR, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en esquema agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en esquema:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_central_generador_planta(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Generador_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ? AND COD_GENERADOR = ?"
    insert_sql = """ 
        INSERT INTO Generador_Central_Generacion_Ubicacion_Plano_Planta (COD_EMP, COD_CENTRAL, COD_GENERADOR, X, Y, Z, ANG) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Generador_Central_Generacion_Ubicacion_Plano_Planta SET 
        X = ?, 
        Y = ?, 
        Z = ?, 
        ANG = ?
        WHERE COD_CENTRAL = ? AND COD_GENERADOR = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_GENERADOR, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en planta agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en planta:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_celda_central_generacion_ubicacion_esquema(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Celda_Central_Generacion_Ubicacion_Esquema 
                    WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_CELDA = ? AND SECUENCIA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2], data[3]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Celda_Central_Generacion_Ubicacion_Esquema 
                            SET SECUENCIA = ?, X = ?, Y = ? 
                            WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_CELDA = ? AND SECUENCIA = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[0], data[1], data[2], data[3]))
            conn.commit()
            print("Registro de ubicación de celda central de generación actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Celda_Central_Generacion_Ubicacion_Esquema (
                                COD_EMP, COD_CENTRAL, COD_CELDA, SECUENCIA, X, Y
                            ) VALUES (?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de ubicación de celda central de generación agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación de celda central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_celda_central_generacion_planta(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Celda_Central_Generacion_Ubicacion_Plano_Planta 
                    WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_CELDA = ? AND SECUENCIA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2],data[3]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Celda_Central_Generacion_Ubicacion_Plano_Planta 
                            SET X = ?, Y = ?, Z = ?
                            WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_CELDA = ? AND SECUENCIA = ?"""
            cur.execute(sql_update, ( data[4], data[5], data[6], data[0], data[1], data[2],data[3]))
            conn.commit()
            print("Registro de ubicación de celda central de generación en planta actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Celda_Central_Generacion_Ubicacion_Plano_Planta (
                                COD_EMP, COD_CENTRAL, COD_CELDA, SECUENCIA, X, Y, Z
                            ) VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de ubicación de celda central de generación en planta agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación de celda central de generación en planta:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_barra_central_generacion_ubicacion_esquema(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Barra_Central_Generacion_Ubicacion_Esquema WHERE  COD_EMP = ? AND COD_CENTRAL = ? AND COD_BARRA = ? AND SECUENCIA = ?"
    insert_sql = """ 
        INSERT INTO Barra_Central_Generacion_Ubicacion_Esquema (COD_EMP, COD_CENTRAL, COD_BARRA, SECUENCIA, X, Y) 
        VALUES (?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Barra_Central_Generacion_Ubicacion_Esquema SET 
        X = ?, 
        Y = ?
        WHERE COD_CENTRAL = ? AND COD_BARRA = ? AND SECUENCIA = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[0],data[1], data[2], data[3]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_BARRA, actualiza los datos
            cur.execute(update_sql, data[4:] + (data[1], data[2], data[3]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en esquema de barra central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en esquema de barra central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_barra_central_generacion_planta(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Barra_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_BARRA = ? AND SECUENCIA = ?"
    insert_sql = """ 
        INSERT INTO Barra_Central_Generacion_Ubicacion_Plano_Planta (COD_EMP, COD_CENTRAL, COD_BARRA, COD_SEGMENTO, COD_FASE, SECUENCIA, X, Y, Z) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Barra_Central_Generacion_Ubicacion_Plano_Planta SET 
        COD_SEGMENTO = ?, 
        COD_FASE = ?,
        SECUENCIA = ?, 
        X = ?, 
        Y = ?, 
        Z = ?
        WHERE COD_CENTRAL = ? AND COD_BARRA = ? AND SECUENCIA = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[0],data[1], data[2],data[5]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_BARRA, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2],data[5]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en planta de barra central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en planta de barra central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_transformador_central_generacion_ubicacion_esquema(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Transformador_Central_Generacion_Ubicacion_Esquema WHERE COD_CENTRAL = ? AND COD_TRANSF = ?"
    insert_sql = """ 
        INSERT INTO Transformador_Central_Generacion_Ubicacion_Esquema (
            COD_EMP, COD_CENTRAL, COD_TRANSF, X, Y, ANG
        ) 
        VALUES (?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Transformador_Central_Generacion_Ubicacion_Esquema SET 
        X = ?, 
        Y = ?, 
        ANG = ?
        WHERE COD_CENTRAL = ? AND COD_TRANSF = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_TRANSF, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en esquema de transformador central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en esquema de transformador central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_transformador_central_generacion_planta(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Transformador_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ? AND COD_TRANSF = ?"
    insert_sql = """ 
        INSERT INTO Transformador_Central_Generacion_Ubicacion_Plano_Planta (
            COD_EMP, COD_CENTRAL, COD_TRANSF, X, Y, Z, ANG
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Transformador_Central_Generacion_Ubicacion_Plano_Planta SET 
        X = ?, 
        Y = ?, 
        Z = ?, 
        ANG = ?
        WHERE COD_CENTRAL = ? AND COD_TRANSF = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_TRANSF, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en planta de transformador central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en planta de transformador central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_pararrayo_central_generacion_ubicacion_esquema(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Pararrayo_Central_Generacion_Ubicacion_Esquema WHERE COD_CENTRAL = ? AND COD_PARARRAYO = ?"
    insert_sql = """ 
        INSERT INTO Pararrayo_Central_Generacion_Ubicacion_Esquema (
            COD_EMP, COD_CENTRAL, COD_PARARRAYO, X, Y, ANG
        ) 
        VALUES (?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Pararrayo_Central_Generacion_Ubicacion_Esquema SET 
        X = ?, 
        Y = ?, 
        ANG = ?
        WHERE COD_CENTRAL = ? AND COD_PARARRAYO = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_PARARRAYO, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en esquema de pararrayo central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en esquema de pararrayo central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_pararrayo_central_generacion_planta(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Pararrayo_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ? AND COD_PARARRAYO = ?"
    insert_sql = """ 
        INSERT INTO Pararrayo_Central_Generacion_Ubicacion_Plano_Planta (
            COD_EMP, COD_CENTRAL, COD_PARARRAYO, X, Y, Z, ANG
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Pararrayo_Central_Generacion_Ubicacion_Plano_Planta SET 
        X = ?, 
        Y = ?, 
        Z = ?, 
        ANG = ?
        WHERE COD_CENTRAL = ? AND COD_PARARRAYO = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_PARARRAYO, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en planta de pararrayo central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en planta de pararrayo central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_book_transformador_medicion_central_generacion_ubicacion_esquema(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Transformador_Medicion_Central_Ubicacion_Esquema WHERE COD_CENTRAL = ? AND COD_TRANSF = ?"
    insert_sql = """ 
        INSERT INTO Transformador_Medicion_Central_Ubicacion_Esquema (
            COD_EMP, COD_CENTRAL, COD_TRANSF, X, Y, ANG
        ) 
        VALUES (?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Transformador_Medicion_Central_Ubicacion_Esquema SET 
        X = ?, 
        Y = ?, 
        ANG = ?
        WHERE COD_CENTRAL = ? AND COD_TRANSF = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_TRANSF, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en esquema de transformador de medición central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en esquema de transformador de medición central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_transformador_medicion_central_generacion_planta(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Transformador_Medicion_Central_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ? AND COD_TRANSF = ?"
    insert_sql = """ 
        INSERT INTO Transformador_Medicion_Central_Ubicacion_Plano_Planta (
            COD_EMP, COD_CENTRAL, COD_TRANSF, X, Y, Z, ANG
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Transformador_Medicion_Central_Ubicacion_Plano_Planta SET 
        X = ?, 
        Y = ?, 
        Z = ?, 
        ANG = ?
        WHERE COD_CENTRAL = ? AND COD_TRANSF = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_TRANSF, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en planta de transformador de medición central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en planta de transformador de medición central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_book_conductor_central_generacion_ubicacion_esquema(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Conductor_Central_Generacion_Ubicacion_Esquema WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_CONDUCTOR = ? AND SECUENCIA = ?"
    insert_sql = """ 
        INSERT INTO Conductor_Central_Generacion_Ubicacion_Esquema (
            COD_EMP, COD_CENTRAL, COD_CONDUCTOR, SECUENCIA, X, Y
        ) 
        VALUES (?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Conductor_Central_Generacion_Ubicacion_Esquema SET 
        SECUENCIA = ?, 
        X = ?, 
        Y = ?
        WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_CONDUCTOR = ? AND SECUENCIA = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[0],data[1], data[2],data[3]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_CONDUCTOR, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[0],data[1], data[2],data[3]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en esquema de conductor central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en esquema de conductor central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_conductor_central_generacion_planta(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Conductor_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_CONDUCTOR = ? AND SECUENCIA = ?"
    insert_sql = """ 
        INSERT INTO Conductor_Central_Generacion_Ubicacion_Plano_Planta (
            COD_EMP, COD_CENTRAL, COD_CONDUCTOR, COD_FASE, SECUENCIA, X, Y, Z
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Conductor_Central_Generacion_Ubicacion_Plano_Planta SET 
        COD_FASE = ?, 
        SECUENCIA = ?, 
        X = ?, 
        Y = ?, 
        Z = ?
        WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_CONDUCTOR = ? AND SECUENCIA = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[0],data[1], data[2],data[4]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_CONDUCTOR, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[0],data[1], data[2],data[4]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de ubicación en plano planta de conductor central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en plano planta de conductor central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_portico_central_generacion_estructura(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Portico_Central_Generacion_Estructura 
                    WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_PORTICO = ? AND COD_ESTRUCTURA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2], data[3]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Portico_Central_Generacion_Estructura 
                            SET ALTURA = ?, X = ?, Y = ?, Z = ?
                            WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_PORTICO = ? AND COD_ESTRUCTURA = ?"""
            cur.execute(sql_update, (*data[4:], *data[:4]))
            conn.commit()
            print("Registro de Pórtico Central Generación Estructura actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Portico_Central_Generacion_Estructura (
                                COD_EMP, COD_CENTRAL, COD_PORTICO, COD_ESTRUCTURA, ALTURA, X, Y, Z
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Pórtico Central Generación Estructura agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Pórtico Central Generación Estructura:", e)
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_portico_central_generacion_travesanio(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Portico_Central_Generacion_Travesano WHERE COD_CENTRAL = ? AND COD_PORTICO = ?"
    insert_sql = """ 
        INSERT INTO Portico_Central_Generacion_Travesano (
            COD_EMP, COD_CENTRAL, COD_PORTICO, ALTURA, COD_ESTRUCTURA_1, COD_ESTRUCTURA_2
        ) 
        VALUES (?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Portico_Central_Generacion_Travesano SET 
        ALTURA = ?, 
        COD_ESTRUCTURA_1 = ?, 
        COD_ESTRUCTURA_2 = ?
        WHERE COD_CENTRAL = ? AND COD_PORTICO = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_CENTRAL y COD_PORTICO, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de travesaño de portico central de generación agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de travesaño de portico central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_portico(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Portico WHERE COD_SE = ? AND COD_PORTICO = ?"
    insert_sql = """ 
        INSERT INTO Portico (
            COD_EMP, COD_SE, COD_PORTICO, COD_CALIFICACION, TIPO, ALTURA, ESTADO, FECHA_ALTA
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Portico SET 
            COD_CALIFICACION = ?, 
            TIPO = ?, 
            ALTURA = ?, 
            ESTADO = ?, 
            FECHA_ALTA = ?
        WHERE COD_SE = ? AND COD_PORTICO = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_SE y COD_PORTICO, actualiza los datos
            cur.execute(update_sql, data[3:] + (data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de pórtico agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de pórtico:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_portico_travesanio(data):
    conn = create_connection()
    select_sql = "SELECT COUNT(*) FROM Portico_Travesanio WHERE COD_SE = ? AND COD_PORTICO = ?"
    insert_sql = """ 
        INSERT INTO Portico_Travesanio (
            COD_EMP, COD_SE, COD_PORTICO, ALTURA, COD_ESTRUCTURA_1, COD_ESTRUCTURA_2
        ) 
        VALUES (?, ?, ?, ?, ?, ?)
    """
    update_sql = """
        UPDATE Portico_Travesanio SET 
            ALTURA = ?, 
            COD_ESTRUCTURA_1 = ?, 
            COD_ESTRUCTURA_2 = ?
        WHERE COD_SE = ? AND COD_PORTICO = ?
    """

    try:
        cur = conn.cursor()
        cur.execute(select_sql, (data[1], data[2]))
        count = cur.fetchone()[0]
        if count > 0:
            # Si ya existe un registro con el mismo COD_SE y COD_PORTICO, actualiza los datos
            cur.execute(update_sql, (data[3], data[4], data[5], data[1], data[2]))
        else:
            # Si no existe, inserta un nuevo registro
            cur.execute(insert_sql, data)
        conn.commit()
        print("Registro de pórtico travesaño agregado o actualizado correctamente!")
        return True
    except Error as e:
        print("Error al insertar o actualizar el registro de pórtico travesaño:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_portico_estructura(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Portico_Estructura 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_PORTICO = ? AND COD_ESTRUCTURA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2], data[3]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Portico_Estructura 
                            SET ALTURA = ?, X = ?, Y = ?, Z = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_PORTICO = ? AND COD_ESTRUCTURA = ?"""
            cur.execute(sql_update, (*data[4:], *data[:4]))
            conn.commit()
            print("Registro de Pórtico Estructura actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Portico_Estructura (
                                COD_EMP, COD_SE, COD_PORTICO, COD_ESTRUCTURA, ALTURA, X, Y, Z
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Pórtico Estructura agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Pórtico Estructura:", e)
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_celda(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Celda 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_CELDA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Celda 
                            SET COD_CALIFICACION = ?, TIPO_CELDA = ?, TIPO_INSTALACION = ?, TENSION_NOM = ?, COD_MODULO = ?, ESTADO = ?, FECHA_ALTA = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_CELDA = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[0], data[1], data[2]))
            conn.commit()
            print("Registro de celda actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Celda (
                                COD_EMP, COD_SE, COD_CELDA, COD_CALIFICACION, TIPO_CELDA, TIPO_INSTALACION, TENSION_NOM, COD_MODULO, ESTADO, FECHA_ALTA
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de celda agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de celda:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_book_celda_ubicacion_esquema(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Celda_Ubicacion_Esquema 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_CELDA = ? AND SECUENCIA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2], data[3]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Celda_Ubicacion_Esquema 
                            SET SECUENCIA = ?, X = ?, Y = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_CELDA = ? AND AND SECUENCIA = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[0], data[1], data[2], data[3]))
            conn.commit()
            print("Registro de Celda_Ubicacion_Esquema actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Celda_Ubicacion_Esquema (
                                COD_EMP, COD_SE, COD_CELDA, SECUENCIA, X, Y
                            ) VALUES (?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Celda_Ubicacion_Esquema agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Celda_Ubicacion_Esquema:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_celda_plano_planta(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Celda_Ubicacion_Plano_Planta 
                    WHERE COD_EMP = ? AND COD_SE = ? AND COD_CELDA = ? AND SECUENCIA = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2], data[3]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Celda_Ubicacion_Plano_Planta 
                            SET SECUENCIA = ?, X = ?, Y = ?, Z = ?
                            WHERE COD_EMP = ? AND COD_SE = ? AND COD_CELDA = ? AND SECUENCIA = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[6], data[0], data[1], data[2], data[3]))
            conn.commit()
            print("Registro de Celda_Ubicacion_Plano_Planta actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Celda_Ubicacion_Plano_Planta (
                                COD_EMP, COD_SE, COD_CELDA, SECUENCIA, X, Y, Z
                            ) VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de Celda_Ubicacion_Plano_Planta agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de Celda_Ubicacion_Plano_Planta:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_seccionador_central_generacion_ubicacion_esquema(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Seccionador_Central_Generacion_Ubicacion_Esquema 
                    WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_SECCIONADOR = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Seccionador_Central_Generacion_Ubicacion_Esquema 
                            SET X = ?, Y = ?, ANG = ?
                            WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_SECCIONADOR = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[0], data[1], data[2]))
            conn.commit()
            print("Registro de ubicación esquemática de seccionador central de generación actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Seccionador_Central_Generacion_Ubicacion_Esquema (
                                COD_EMP, COD_CENTRAL, COD_SECCIONADOR, X, Y, ANG
                            ) VALUES (?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de ubicación esquemática de seccionador central de generación agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación esquemática de seccionador central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_seccionador_central_generacion_ubicacion_planta(data):
    conn = create_connection()
    sql_select = """SELECT * FROM Seccionador_Central_Generacion_Ubicacion_Plano_Planta 
                    WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_SECCIONADOR = ?"""

    try:
        cur = conn.cursor()
        cur.execute(sql_select, (data[0], data[1], data[2]))
        existing_row = cur.fetchone()

        if existing_row:
            # Si el registro ya existe, actualizarlo
            sql_update = """UPDATE Seccionador_Central_Generacion_Ubicacion_Plano_Planta 
                            SET X = ?, Y = ?, Z = ?, ANG = ?
                            WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_SECCIONADOR = ?"""
            cur.execute(sql_update, (data[3], data[4], data[5], data[6], data[0], data[1], data[2]))
            conn.commit()
            print("Registro de ubicación en plano planta de seccionador central de generación actualizado!")
        else:
            # Si el registro no existe, insertarlo
            sql_insert = """INSERT INTO Seccionador_Central_Generacion_Ubicacion_Plano_Planta (
                                COD_EMP, COD_CENTRAL, COD_SECCIONADOR, X, Y, Z, ANG
                            ) VALUES (?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(sql_insert, data)
            conn.commit()
            print("Nuevo Registro de ubicación en plano planta de seccionador central de generación agregado!")

        return True, cur.lastrowid
    except Error as e:
        print("Error al insertar o actualizar el registro de ubicación en plano planta de seccionador central de generación:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def insert_book_prueba(data):
    conn = create_connection()
    sql = """INSERT INTO Celda_Ubicacion_Plano_Planta (
                    COD_EMP, COD_SE, COD_CELDA, SECUENCIA, X, Y, Z
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
def update_book(_id, data):
    conn = create_connection()

    sql = f""" UPDATE books SET  
                            fecha = ?,
                            dni = ?,
                            visitante = ?,
                            entidadempresa = ?,
                            motivovisita = ?,
                            aquienvisita = ?,
                            autoriza = ?,
                            areavisitada = ?,
                            piso = ?,
                            horaingreso = ?,
                            horasalida = ?,
                            observaciones=?,
                            estado = ?
            WHERE book_id = {_id}
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Libro Actualizado")
        return True
    except Error as e:
        print("Error updating book: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book(_id):
    conn = create_connection()
    sql = f"DELETE FROM books WHERE book_id = {_id}"


    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_books(_user):
    conn = create_connection()
    sql = "SELECT COD_CENTRAL,NOMBRE,TIPO_CENTRAL,COD_AREA,TIPO_SISTEMA,AREA_OPERATIVA,REGION_GEOGRAFICA,ZONA,ALTITUD,CAUDAL_DISENO,COEF_PRODUCCION,CONSUMO_PROPIO,DIRECCION,TELEFONO,ESTADO,FECHA_ALTA,DATUM_UTM,ZONA_UTM FROM central_generacion WHERE COD_EMP='"+_user+"' "
    #
    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_books_subestacion(_user):
    conn = create_connection()
    sql = "SELECT COD_SE, NOMBRE, COD_CALIFICACION, TIPO_SISTEMA, COD_AREA, AREA_OPERATIVA, REGION_GEOGRAFICA, ZONA, ALTITUD, TECNOLOGIA_SE, FUNCION, ATENDIDA, DIRECCION, TELEFONO, COD_MODULO_SERV_AUX, COD_MODULO_OBRA_CIVIL, COD_MODULO_EDIF_CONTROL, COD_MODULO_TIERRA_PROF, COD_MODULO_IEE, ESTADO, FECHA_ALTA, DATUM_UTM, ZONA_UTM FROM Subestacion WHERE COD_EMP='"+_user+"'"
#
    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_books_linea(_user):
    conn = create_connection()
    sql = "SELECT COD_LINEA, NOMBRE, TIPO_SISTEMA, TENSION_NOM, NODO_SALIDA, NODO_LLEGADA, CELDA_SALIDA, CELDA_LLEGADA FROM Linea_Transmision WHERE COD_EMP='"+_user+"'"

    #
    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_books_admin():
    conn = create_connection()
    sql = "SELECT COD_EMP,COD_CENTRAL,NOMBRE,TIPO_CENTRAL,COD_AREA,TIPO_SISTEMA,AREA_OPERATIVA,REGION_GEOGRAFICA,ZONA,ALTITUD,CAUDAL_DISENO,COEF_PRODUCCION,CONSUMO_PROPIO,DIRECCION,TELEFONO,ESTADO,FECHA_ALTA,DATUM_UTM,ZONA_UTM FROM central_generacion "
    #
    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_books_subestacion_admin():
    conn = create_connection()
    sql = "SELECT COD_EMP,COD_SE, NOMBRE, COD_CALIFICACION, TIPO_SISTEMA, COD_AREA, AREA_OPERATIVA, REGION_GEOGRAFICA, ZONA, ALTITUD, TECNOLOGIA_SE, FUNCION, ATENDIDA, DIRECCION, TELEFONO, COD_MODULO_SERV_AUX, COD_MODULO_OBRA_CIVIL, COD_MODULO_EDIF_CONTROL, COD_MODULO_TIERRA_PROF, COD_MODULO_IEE, ESTADO, FECHA_ALTA, DATUM_UTM, ZONA_UTM FROM Subestacion"
#
    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_books_linea_admin():
    conn = create_connection()
    sql = "SELECT COD_EMP,COD_LINEA, NOMBRE, TIPO_SISTEMA, TENSION_NOM, NODO_SALIDA, NODO_LLEGADA, CELDA_SALIDA, CELDA_LLEGADA FROM Linea_Transmision"

    #
    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_cod_generadores(_id):
    conn = create_connection()
    sql = "SELECT COD_GENERADOR FROM Generador_Central_Generacion WHERE COD_CENTRAL = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_cod_interruptores(_codCentral,_codCelda):
    conn = create_connection()
    sql = "SELECT COD_INTERRUPTOR,TIPO_INSTALACION,TENSION_NOM ,MARCA,ANIO_FA FROM Interruptor_Central_Generacion WHERE COD_CENTRAL = ? AND COD_CELDA= ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_codCentral,_codCelda,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_cod_interruptores_sub(_codCentral,_codCelda):
    conn = create_connection()
    sql = "SELECT COD_INTERRUPTOR,COD_CALIFICACION,TIPO_INSTALACION,TENSION_NOM ,MARCA,ANIO_FA FROM Interruptor_Potencia WHERE COD_SE = ? AND COD_CELDA= ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_codCentral,_codCelda,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_cod_seccionadores(_codCentral,_codCelda):
    conn = create_connection()
    sql = "SELECT COD_SECCIONADOR,TIPO_SECCIONADOR,TIPO_INSTALACION,TENSION_NOM,MARCA FROM Seccionador_Central_Generacion WHERE COD_CENTRAL = ? AND COD_CELDA= ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_codCentral,_codCelda,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_cod_seccionadores_sub(_codCentral,_codCelda):
    conn = create_connection()
    sql = "SELECT COD_SECCIONADOR,COD_CALIFICACION,TIPO_SECCIONADOR,TIPO_INSTALACION,TENSION_NOM,MARCA FROM Seccionador WHERE COD_SE = ? AND COD_CELDA= ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_codCentral,_codCelda,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_cod_celdas(_id):
    conn = create_connection()
    sql = "SELECT COD_CELDA FROM Celda_Central_Generacion where COD_CENTRAL = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        celdas = cur.fetchall()
        return celdas
    except Error as e:
        print("Error selecting celdas: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_cod_barras(_id):
    conn = create_connection()
    sql = "SELECT COD_BARRA FROM Barra_Central_Generacion where COD_CENTRAL = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        barras = cur.fetchall()
        return barras
    except Error as e:
        print("Error selecting barras: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_cod_porticos(_id):
    conn = create_connection()
    sql = "SELECT COD_PORTICO FROM Portico_Central_Generacion where COD_CENTRAL = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        barras = cur.fetchall()
        return barras
    except Error as e:
        print("Error selecting barras: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_cod_interruptor(_id):
    conn = create_connection()
    sql = "SELECT COD_INTERRUPTOR FROM Interruptor_Central_Generacion where COD_CENTRAL = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        interruptores = cur.fetchall()
        return interruptores
    except Error as e:
        print("Error selecting interruptores: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_cod_transformador(_id):
    conn = create_connection()
    sql = "SELECT COD_TRANSF FROM Transformador_Central_Generacion WHERE COD_CENTRAL = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        transformadores = cur.fetchall()
        return transformadores
    except Error as e:
        print("Error selecting transformadores: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_cod_seccionador(_id):
    conn = create_connection()
    sql = "SELECT COD_SECCIONADOR FROM Seccionador_Central_Generacion WHERE COD_CENTRAL = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        seccionadores = cur.fetchall()
        return seccionadores
    except Error as e:
        print("Error selecting seccionadores: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_cod_medicion(_id):
    conn = create_connection()
    sql = "SELECT COD_TRANSF FROM Transformador_Medicion_Central_Generacion WHERE COD_CENTRAL = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        mediciones = cur.fetchall()
        return mediciones
    except Error as e:
        print("Error selecting mediciones: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_cod_pararrayo(_id):
    conn = create_connection()
    sql = "SELECT COD_PARARRAYO FROM Pararrayo_Central_Generacion WHERE COD_CENTRAL = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        pararrayos = cur.fetchall()
        return pararrayos
    except Error as e:
        print("Error selecting pararrayos: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_cod_conductor(_id):
    conn = create_connection()
    sql = "SELECT COD_CONDUCTOR FROM Conductor_Central_Generacion WHERE COD_CENTRAL = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        conductores = cur.fetchall()
        return conductores
    except Error as e:
        print("Error selecting conductores: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()





def select_cod_barras_sub(_id):
    conn = create_connection()
    sql = "SELECT COD_BARRA FROM Barra WHERE COD_SE = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_cod_porticos_sub(_id):
    conn = create_connection()
    sql = "SELECT COD_PORTICO FROM Portico WHERE COD_SE = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_cod_celdas_sub(_id):
    conn = create_connection()
    sql = "SELECT COD_CELDA FROM Celda WHERE COD_SE = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_cod_transp_sub(_id):
    conn = create_connection()
    sql = "SELECT COD_TRANSF FROM Transformador_Potencia WHERE COD_SE = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_cod_pararrayos_sub(_id):
    conn = create_connection()
    sql = "SELECT COD_PARARRAYO FROM Pararrayo WHERE COD_SE = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_cod_transm_sub(_id):
    conn = create_connection()
    sql = "SELECT COD_TRANSF FROM Transformador_Medicion WHERE COD_SE = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_cod_bobinas_sub(_id):
    conn = create_connection()
    sql = "SELECT COD_BOBINA FROM Bobina_Bloqueo WHERE COD_SE = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_cod_conductor_sub(_id):
    conn = create_connection()
    sql = "SELECT COD_CONDUCTOR FROM Conductor WHERE COD_SE = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_cod_compensador_sub(_id):
    conn = create_connection()
    sql = "SELECT COD_COMP FROM Compensador_Reactivo WHERE COD_SE = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_cod_tramo_linea(_id):
    conn = create_connection()
    sql = "SELECT COD_TRAMO FROM Tramo_Linea_Transmision WHERE COD_LINEA = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_cod_estructura(_id):
    conn = create_connection()
    sql = "SELECT COD_ESTRUCTURA FROM Estructura WHERE COD_LINEA = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_cod_estructura_portico(cod_central,cod_portico):
    conn = create_connection()
    sql = "SELECT COD_ESTRUCTURA, ALTURA, X,Y,Z FROM Portico_Central_Generacion_Estructura WHERE COD_CENTRAL = ? AND COD_PORTICO= ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_central,cod_portico,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_ubicacion_tramo_linea(cod_linea,cod_tramo):
    conn = create_connection()
    sql = "SELECT SECUENCIA, X,Y,Z FROM Tramo_Linea_Vertice_Ubicacion_Geografica WHERE COD_LINEA = ? AND COD_TRAMO= ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_linea,cod_tramo,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_geografica_central(cod_linea):
    conn = create_connection()
    sql = "SELECT SECUENCIA, X,Y,Z FROM Central_Generacion_Vertice_Perimetro_Coordenadas_Geograficas WHERE COD_CENTRAL = ? "
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_linea,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_central_perimetro(cod_linea):
    conn = create_connection()
    sql = "SELECT SECUENCIA, X,Y,Z FROM Central_Generacion_Vertice_Perimetro_Plano_Planta WHERE COD_CENTRAL = ? "
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_linea,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_coordenadas_subestacion(cod_linea):
    conn = create_connection()
    sql = "SELECT SECUENCIA, X,Y,Z FROM Subestacion_Vertice_Perimetro_Coordenadas_Geograficas WHERE COD_SE = ? "
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_linea,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_plano_subestacion(cod_linea):
    conn = create_connection()
    sql = "SELECT SECUENCIA, X,Y,Z FROM Subestacion_Vertice_Perimetro_Plano_Planta WHERE COD_SE = ? "
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_linea,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_plano_barra_central(cod_central, cod_barra):
    conn = create_connection()
    sql = "SELECT COD_SEGMENTO,COD_FASE,SECUENCIA, X,Y,Z FROM Barra_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ? AND COD_BARRA = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_central,cod_barra,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_esquema_barra_central(cod_central, cod_barra):
    conn = create_connection()
    sql = "SELECT SECUENCIA, X,Y FROM Barra_Central_Generacion_Ubicacion_Esquema WHERE COD_CENTRAL = ? AND COD_BARRA = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_central,cod_barra,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_plano_barra_subestacion(cod_central, cod_barra):
    conn = create_connection()
    sql = "SELECT COD_SEGMENTO,COD_FASE,SECUENCIA, X,Y,Z FROM Barra_Ubicacion_Plano_Planta WHERE COD_SE = ? AND COD_BARRA = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_central,cod_barra,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_esquema_barra_subestacion(cod_central, cod_barra):
    conn = create_connection()
    sql = "SELECT SECUENCIA, X,Y FROM Barra_Ubicacion_Esquema WHERE COD_SE = ? AND COD_BARRA = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_central,cod_barra,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_plano_conductor_central(cod_central, cod_barra):
    conn = create_connection()
    sql = "SELECT COD_FASE,SECUENCIA, X,Y,Z FROM Conductor_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ? AND COD_CONDUCTOR = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_central,cod_barra,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_esquema_conductor_central(cod_central, cod_barra):
    conn = create_connection()
    sql = "SELECT SECUENCIA, X,Y FROM Conductor_Central_Generacion_Ubicacion_Esquema WHERE COD_CENTRAL = ? AND COD_CONDUCTOR = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_central,cod_barra,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_plano_conductor_subestacion(cod_central, cod_barra):
    conn = create_connection()
    sql = "SELECT COD_FASE,SECUENCIA, X,Y,Z FROM Conductor_Ubicacion_Plano_Planta WHERE COD_SE = ? AND COD_CONDUCTOR = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_central,cod_barra,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_esquema_conductor_subestacion(cod_central, cod_barra):
    conn = create_connection()
    sql = "SELECT SECUENCIA, X,Y FROM Conductor_Ubicacion_Esquema WHERE COD_SE = ? AND COD_CONDUCTOR = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_central,cod_barra,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_esquema_celda_central(cod_central, cod_barra):
    conn = create_connection()
    sql = "SELECT SECUENCIA, X,Y FROM Celda_Central_Generacion_Ubicacion_Esquema WHERE COD_CENTRAL = ? AND COD_CELDA = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_central,cod_barra,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_esquema_celda_subestacion(cod_central, cod_barra):
    conn = create_connection()
    sql = "SELECT SECUENCIA, X,Y FROM Celda_Ubicacion_Esquema WHERE COD_SE = ? AND COD_CELDA = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_central,cod_barra,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_plano_celda_central(cod_central, cod_barra):
    conn = create_connection()
    sql = "SELECT SECUENCIA, X,Y,Z FROM Celda_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ? AND COD_CELDA = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_central,cod_barra,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_plano_celda_subestacion(cod_central, cod_barra):
    conn = create_connection()
    sql = "SELECT SECUENCIA, X,Y,Z FROM Celda_Ubicacion_Plano_Planta WHERE COD_SE = ? AND COD_CELDA = ?"
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_central,cod_barra,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
# Define las funciones select_cod_interruptor, select_cod_transformador, select_cod_seccionador, 
# select_cod_medicion, select_cod_pararrayo, select_cod_conductor siguiendo el mismo patrón.
def select_cod_estructura_portico_sub(cod_se, cod_portico):
    conn = create_connection()
    sql = """
    SELECT COD_ESTRUCTURA, ALTURA, X, Y, Z 
    FROM Portico_Estructura 
    WHERE COD_SE = ? AND COD_PORTICO = ?
    """
    try:
        cur = conn.cursor()
        cur.execute(sql, (cod_se, cod_portico,))
        rows = cur.fetchall()
        return rows
    except Error as e:
        print("Error selecting data: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_all_EntidadTabla():
    conn = create_connection()
    sql = "SELECT nombreentidad FROM EntidadTabla ORDER BY nombreentidad ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_book_by_id(_id):
    conn = create_connection()
    sql = f"SELECT * FROM books WHERE book_id = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        book = cur.fetchone()
        return book
    except Error as e:
        print("Error selecting book by id: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def generar_data_excel_hoy(fechastr):
    
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    print("date and time =", dt_string)
    dt_string=dt_string.replace(':','_')
    dt_string=dt_string.replace('/','-')
    workbook = Workbook('REPORTES/REPORTE VISITAS '+dt_string+'.xlsx')
    worksheet = workbook.add_worksheet()

    header_data = ['Fecha','Doc. Identidad','APELLIDOS Y NOMBRES','Entidad o Empresa','Motivo de la visita','Persona que Visita','Autorizado por:','Área de la persona visitada','Piso','Hora   de ingreso','Hora de salida','Observaciones']

    header_format = workbook.add_format({'bold': True,
                                        'border': 1,
                                        'font_color':'white',
                                        'font_name': 'Cambria',
                                        'font_size':10,
                                        'bg_color': '#4F81BD',
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})

    for col_num, data in enumerate(header_data):
        worksheet.write(0, col_num, data, header_format)
       

    formatogeneral=workbook.add_format({'font_name': 'Cambria',
                                        'border': 1,
                                        'font_size':10,
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})
    conn = create_connection()
    c=conn.cursor()
    #c.execute(f"select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books WHERE fecha= '{fecha_hoy}'")
    mysel=c.execute(f"select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books WHERE fecha= '{fechastr}'")
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i+1, j, value,formatogeneral)
    
    worksheet.set_column(0, 0, 12.43)
    worksheet.set_column(1,1, 11.57)
    worksheet.set_column(2,2 , 37.14)
    worksheet.set_column(3,3 , 25.43)
    worksheet.set_column(4,4 , 21.43)
    worksheet.set_column(5,5 , 22.86)
    worksheet.set_column(6,6 , 20.71)
    worksheet.set_column(7,7 , 22.29)
    worksheet.set_column(8,8 , 7)
    worksheet.set_column(9,9 , 7)
    worksheet.set_column(10,10 , 6)
    worksheet.set_column(11,11 , 36.29)
    worksheet.set_zoom(80)
    workbook.close()


def generar_data_excel_fechas(fechainicio, fechafinal):
    
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    dt_string=dt_string.replace(':','_')
    dt_string=dt_string.replace('/','-')
    workbook = Workbook('REPORTES/REPORTE FILTRADO VISITAS '+dt_string+'.xlsx')

    #TRANSFORMANDO EL FORMATO DE FECHAS

    worksheet = workbook.add_worksheet()

    header_data = ['Fecha','Doc. Identidad','APELLIDOS Y NOMBRES','Entidad o Empresa','Motivo de la visita','Persona que Visita','Autorizado por:','Área de la persona visitada','Piso','Hora   de ingreso','Hora de salida','Observaciones']

    header_format = workbook.add_format({'bold': True,
                                        'border': 1,
                                        'font_color':'white',
                                        'font_name': 'Cambria',
                                        'font_size':10,
                                        'bg_color': '#4F81BD',
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})

    for col_num, data in enumerate(header_data):
        worksheet.write(0, col_num, data, header_format)
       

    formatogeneral=workbook.add_format({'font_name': 'Cambria',
                                        'border': 1,
                                        'font_size':10,
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})
    conn = create_connection()
    c=conn.cursor()
    #c.execute(f"select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books WHERE fecha= '{fecha_hoy}'")1/01/2021       2021-01-01' and '2021-12-12
    #2021-01-01' and '2021-12-12
    CadenaFechaInicial= fechainicio.split('/')
    CadenaFechaFinal= fechafinal.split('/')
    NuevaFechaFinal=CadenaFechaFinal[2]+"-"+CadenaFechaFinal[1]+"-"+CadenaFechaFinal[0]
    NuevaFechaInicial=CadenaFechaInicial[2]+"-"+CadenaFechaInicial[1]+"-"+CadenaFechaInicial[0]
    myData=(NuevaFechaInicial,NuevaFechaFinal)
    q="select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books WHERE (substr(fecha, 7, 4) || '-' || substr(fecha, 4, 2) || '-' || substr(fecha, 1, 2)) between ? and ?"
    mysel=c.execute(q,myData)
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i+1, j, value,formatogeneral)
    
    worksheet.set_column(0, 0, 12.43)
    worksheet.set_column(1,1, 11.57)
    worksheet.set_column(2,2 , 37.14)
    worksheet.set_column(3,3 , 25.43)
    worksheet.set_column(4,4 , 21.43)
    worksheet.set_column(5,5 , 22.86)
    worksheet.set_column(6,6 , 20.71)
    worksheet.set_column(7,7 , 22.29)
    worksheet.set_column(8,8 , 7)
    worksheet.set_column(9,9 , 7)
    worksheet.set_column(10,10 , 6)
    worksheet.set_column(11,11 , 36.29)
    worksheet.set_zoom(80)
    workbook.close()

def select_book_by_all(parameterDni,parameterPiso,parameterVisitante,parameterFecha,parameterMotivo,parameterEstado):
    conn = create_connection()
    sql = f"SELECT * FROM books WHERE dni LIKE '%{parameterDni}%' AND piso LIKE '%{parameterPiso}%' AND visitante LIKE '%{parameterVisitante}%' AND fecha LIKE '%{parameterFecha}%' AND motivovisita LIKE '%{parameterMotivo}%' AND estado LIKE '%{parameterEstado}%' "

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error Selecting book by category: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def ExisteDni(_dni):
    conn = create_connection()
    sql = f"SELECT dni FROM visitantes WHERE dni='{_dni}'"

    try:


        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True    
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarDni(_dni):
    conn = create_connection()
    sql = f"SELECT nombre FROM visitantes WHERE dni='{_dni}'"

    try:
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        if len(dniencontrado)==0:
            dniencontrado.append('0');
        print("ESTE ES EL DNI ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def EncontrarAutorizaArea(_nombreautoriza):
    conn = create_connection()
    sql = f"SELECT area FROM personalfeban WHERE nombrepersonal='{_nombreautoriza}'"

    try:
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        areaencontrada = cur.execute(sql).fetchall()
        if len(areaencontrada)==0:
            areaencontrada.append('0');
        print("ESTE ES EL areaencontrada: "+str(areaencontrada[0]))
        return areaencontrada[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()







def ExisteNombreVisitante(_nombre):
    conn = create_connection()
    sql = f"SELECT nombre FROM visitantes WHERE nombre='{_nombre}'"

    try:


        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True    
    except Error as e:
        print("Error Selecting book by NombreVisitante: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarNombreVisitante(_nombre):
    conn = create_connection()
    sql = f"SELECT dni FROM visitantes WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL NombreVisitante ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoDNI(dni,nombre):
    conn = create_connection()
    sql = """ INSERT INTO visitantes (DNI,nombre) 
                                                                
                VALUES(?, ?)
    """

    try:
        data=(dni,nombre)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Visitantes agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

#//////////////////////////////////////////////////////////////////
def ExisteMotivo(_nombremotivo):
    conn = create_connection()
    sql = f"SELECT nombremotivo FROM motivoTabla WHERE nombremotivo='{_nombremotivo}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoMotivo(_nombremotivo):
    conn = create_connection()
    sql = """ INSERT INTO motivoTabla (nombremotivo) 
                                                                
                VALUES(?)
    """

    try:
        data=(_nombremotivo,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Motivo agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
##*////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
def ExisteVisita(_aquienVisita):
    conn = create_connection()
    sql = f"SELECT nombrepersonal FROM personalfeban WHERE nombrepersonal='{_aquienVisita}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoVisita(_aquienVisita):
    conn = create_connection()
    sql = """ INSERT INTO personalfeban (nombrepersonal) 
                                                                
                VALUES(?)
    """

    try:
        data=(_aquienVisita,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro AquienVisita agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
##*////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
def ExisteAutoriza(_autoriza):
    conn = create_connection()
    sql = f"SELECT nombrepersonal FROM personalfeban WHERE nombrepersonal='{_autoriza}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_NuevoAutoriza(_autoriza,_areavisitada):
    conn = create_connection()
    sql = """ INSERT INTO personalfeban (nombrepersonal,area) 
                                                                
                VALUES(?,?)
    """

    try:
        data=(_autoriza,_areavisitada)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Autoriza agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
##*////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
def ExisteEntidad(_entidad):
    conn = create_connection()
    sql = f"SELECT nombreentidad FROM EntidadTabla WHERE nombreentidad='{_entidad}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoEntidad(_nombreentidad):
    conn = create_connection()
    sql = """ INSERT INTO EntidadTabla (nombreentidad) 
                                                                
                VALUES(?)
    """

    try:
        data=(_nombreentidad,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Entidad agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
##*////////////////////////////////////////////////////////////////

def UpdateVisitante(_dni, nombrevisitanteNuevo):
    conn = create_connection()

    sql = f""" UPDATE visitantes SET  
                            nombre = ?           
            WHERE DNI = '{_dni}'
    """
    data=(nombrevisitanteNuevo,)
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("VisitantesTable Actualizado")
        return True
    except Error as e:
        print("Error updating VisitantesTable: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def UpdateAutoriza(_nombreautoriza, area):
    conn = create_connection()

    sql = f""" UPDATE personalfeban SET  
                            area = ?           
            WHERE nombrepersonal = '{_nombreautoriza}'
    """
    data=(area,)
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("VisitantesTable Actualizado")
        return True
    except Error as e:
        print("Error updating VisitantesTable: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def BuscarUsuario(_nombreusuario):
    conn = create_connection()
    sql = f"SELECT password FROM UsuariosTabla WHERE usuario='{_nombreusuario}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        cur.execute(sql)
        usuarios = cur.execute(sql).fetchall()
        if len(usuarios)==0:
            return ""
        else:
            return usuarios[0]
    except Error as e:
        print("EL USUARIO NO EXISTE!: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def actualizar_estados_usuarios(_nombreusuario):
    conn = create_connection()
    sql_reset = """UPDATE UsuariosTabla SET estado = ''"""
    sql_set_access = """UPDATE UsuariosTabla SET estado = 'acceso' WHERE usuario = ?"""

    try:
        cur = conn.cursor()
        # Resetear todos los estados a cadenas vacías
        cur.execute(sql_reset)
        # Establecer el estado de acceso para el usuario especificado
        cur.execute(sql_set_access, (_nombreusuario,))
        conn.commit()
        print("Estados actualizados exitosamente.")
    except Error as e:
        print("Error al actualizar estados: ", str(e))
    finally:
        if conn:
            conn.close()

def buscar_usuario_acceso():
    conn = create_connection()
    sql = """SELECT usuario FROM UsuariosTabla WHERE estado = 'acceso'"""

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        cur.execute(sql)
        usuarios = cur.fetchall()
        if len(usuarios) == 0:
            return None
        else:
            return usuarios[0]
    except Error as e:
        print("Error al buscar usuario de acceso: ", str(e))
    finally:
        if conn:
            conn.close()

def SelectUsuarios(_usuarioactual):
    conn = create_connection()
    sql = f"SELECT usuario, password FROM UsuariosTabla WHERE usuario != ?"

    try:
        cur = conn.cursor()
        cur.execute(sql, (_usuarioactual,))
        usuarios = cur.fetchall()
        return usuarios
    except Error as e:
        print("Error al seleccionar usuarios: " + str(e))
        return []
    finally:
        if conn:
            cur.close()
            conn.close()


#################################### LOCADORES ###############################################

def insert_book_locadores(data):
    conn = create_connection()
    sql = """ INSERT INTO books_locadores (fecha, dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada, piso,horaingreso,horasalida,observaciones,estado) 
                                                                
                VALUES(?, ?, ?, ?, ?,?,?,?,?,?,?,?,?)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def update_book_locadores(_id, data):
    conn = create_connection()

    sql = f""" UPDATE books_locadores SET  
                            fecha = ?,
                            dni = ?,
                            visitante = ?,
                            entidadempresa = ?,
                            motivovisita = ?,
                            aquienvisita = ?,
                            autoriza = ?,
                            areavisitada = ?,
                            piso = ?,
                            horaingreso = ?,
                            horasalida = ?,
                            observaciones=?,
                            estado = ?
            WHERE book_id = {_id}
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Libro Actualizado")
        return True
    except Error as e:
        print("Error updating book: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book_locadores(_id):
    conn = create_connection()
    sql = f"DELETE FROM books_locadores WHERE book_id = {_id}"


    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_books_locadores():
    conn = create_connection()
    sql = "SELECT * FROM   books_locadores  ORDER  BY Substr(fecha, 7, 4) DESC, Substr(fecha, 4, 2) DESC, Substr(fecha, 0, 3) DESC , horaingreso DESC LIMIT 500"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        print("LOS LIBROS SON::: ",books)
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_personalFeban_locadores():
    conn = create_connection()
    sql = "SELECT nombrepersonal FROM personalfeban_locadores ORDER BY nombrepersonal ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_all_areaTabla_locadores():
    conn = create_connection()
    sql = "SELECT nombrearea FROM AreaTabla_locadores ORDER BY nombrearea ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_EntidadTabla_locadores():
    conn = create_connection()
    sql = "SELECT nombreentidad FROM EntidadTabla_locadores ORDER BY nombreentidad ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_motivoTabla_locadores():
    conn = create_connection()
    sql = "SELECT nombremotivo FROM motivoTabla_locadores ORDER BY nombremotivo ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_visitantesNombres_locadores():
    conn = create_connection()
    sql = "SELECT nombre FROM visitantes_locadores ORDER BY nombre ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_visitantesDNI_locadores():
    conn = create_connection()
    sql = "SELECT DNI FROM visitantes_locadores ORDER BY DNI ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_id_locadores(_id):
    conn = create_connection()
    sql = f"SELECT * FROM books_locadores WHERE book_id = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        book = cur.fetchone()
        return book
    except Error as e:
        print("Error selecting book by id: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_title_locadores(dni):
    conn = create_connection()
    sql = f"SELECT * FROM books_locadores WHERE dni LIKE '%{dni}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting book by title: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_category_locadores(category):
    conn = create_connection()
    sql = f"SELECT * FROM books_locadores WHERE category LIKE '%{category}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error Selecting book by category: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def generar_data_excel_hoy_locadores(fechastr):
    
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    print("date and time =", dt_string)
    dt_string=dt_string.replace(':','_')
    dt_string=dt_string.replace('/','-')
    workbook = Workbook('REPORTES/REPORTE LOCADORES '+dt_string+'.xlsx')
    worksheet = workbook.add_worksheet()

    header_data = ['Fecha','Doc. Identidad','APELLIDOS Y NOMBRES','Entidad o Empresa','Motivo de la visita','Persona que Visita','Autorizado por:','Área de la persona visitada','Piso','Hora   de ingreso','Hora de salida','Observaciones']

    header_format = workbook.add_format({'bold': True,
                                        'border': 1,
                                        'font_color':'white',
                                        'font_name': 'Cambria',
                                        'font_size':10,
                                        'bg_color': '#4F81BD',
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})

    for col_num, data in enumerate(header_data):
        worksheet.write(0, col_num, data, header_format)
       

    formatogeneral=workbook.add_format({'font_name': 'Cambria',
                                        'border': 1,
                                        'font_size':10,
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})
    conn = create_connection()
    c=conn.cursor()
    #c.execute(f"select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books WHERE fecha= '{fecha_hoy}'")
    mysel=c.execute(f"select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books_locadores WHERE fecha= '{fechastr}'")
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i+1, j, value,formatogeneral)
    
    worksheet.set_column(0, 0, 12.43)
    worksheet.set_column(1,1, 11.57)
    worksheet.set_column(2,2 , 37.14)
    worksheet.set_column(3,3 , 25.43)
    worksheet.set_column(4,4 , 21.43)
    worksheet.set_column(5,5 , 22.86)
    worksheet.set_column(6,6 , 20.71)
    worksheet.set_column(7,7 , 22.29)
    worksheet.set_column(8,8 , 7)
    worksheet.set_column(9,9 , 7)
    worksheet.set_column(10,10 , 6)
    worksheet.set_column(11,11 , 36.29)
    worksheet.set_zoom(80)
    workbook.close()


def generar_data_excel_fechas_locadores(fechainicio, fechafinal):
    
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    dt_string=dt_string.replace(':','_')
    dt_string=dt_string.replace('/','-')
    workbook = Workbook('REPORTES/REPORTE FILTRADO LOCADORES '+dt_string+'.xlsx')

    #TRANSFORMANDO EL FORMATO DE FECHAS

    worksheet = workbook.add_worksheet()

    header_data = ['Fecha','Doc. Identidad','APELLIDOS Y NOMBRES','Entidad o Empresa','Motivo de la visita','Persona que Visita','Autorizado por:','Área de la persona visitada','Piso','Hora   de ingreso','Hora de salida','Observaciones']

    header_format = workbook.add_format({'bold': True,
                                        'border': 1,
                                        'font_color':'white',
                                        'font_name': 'Cambria',
                                        'font_size':10,
                                        'bg_color': '#4F81BD',
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})

    for col_num, data in enumerate(header_data):
        worksheet.write(0, col_num, data, header_format)
       

    formatogeneral=workbook.add_format({'font_name': 'Cambria',
                                        'border': 1,
                                        'font_size':10,
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})
    conn = create_connection()
    c=conn.cursor()
    #c.execute(f"select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books WHERE fecha= '{fecha_hoy}'")1/01/2021       2021-01-01' and '2021-12-12
    #2021-01-01' and '2021-12-12
    CadenaFechaInicial= fechainicio.split('/')
    CadenaFechaFinal= fechafinal.split('/')
    NuevaFechaFinal=CadenaFechaFinal[2]+"-"+CadenaFechaFinal[1]+"-"+CadenaFechaFinal[0]
    NuevaFechaInicial=CadenaFechaInicial[2]+"-"+CadenaFechaInicial[1]+"-"+CadenaFechaInicial[0]
    myData=(NuevaFechaInicial,NuevaFechaFinal)
    q="select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books_locadores WHERE (substr(fecha, 7, 4) || '-' || substr(fecha, 4, 2) || '-' || substr(fecha, 1, 2)) between ? and ?"
    mysel=c.execute(q,myData)
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i+1, j, value,formatogeneral)
    
    worksheet.set_column(0, 0, 12.43)
    worksheet.set_column(1,1, 11.57)
    worksheet.set_column(2,2 , 37.14)
    worksheet.set_column(3,3 , 25.43)
    worksheet.set_column(4,4 , 21.43)
    worksheet.set_column(5,5 , 22.86)
    worksheet.set_column(6,6 , 20.71)
    worksheet.set_column(7,7 , 22.29)
    worksheet.set_column(8,8 , 7)
    worksheet.set_column(9,9 , 7)
    worksheet.set_column(10,10 , 6)
    worksheet.set_column(11,11 , 36.29)
    worksheet.set_zoom(80)
    workbook.close()

def select_book_by_all_locadores(parameterDni,parameterPiso,parameterVisitante,parameterFecha,parameterMotivo,parameterEstado):
    conn = create_connection()
    sql = f"SELECT * FROM books_locadores WHERE dni LIKE '%{parameterDni}%' AND piso LIKE '%{parameterPiso}%' AND visitante LIKE '%{parameterVisitante}%' AND fecha LIKE '%{parameterFecha}%' AND motivovisita LIKE '%{parameterMotivo}%' AND estado LIKE '%{parameterEstado}%' "

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error Selecting book by category: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def ExisteDni_locadores(_dni):
    conn = create_connection()
    sql = f"SELECT dni FROM visitantes_locadores WHERE dni='{_dni}'"

    try:


        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True    
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarDni_locadores(_dni):
    conn = create_connection()
    sql = f"SELECT nombre FROM visitantes_locadores WHERE dni='{_dni}'"

    try:
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        if len(dniencontrado)==0:
            dniencontrado.append('0');
        print("ESTE ES EL DNI ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def EncontrarAutorizaArea_locadores(_nombreautoriza):
    conn = create_connection()
    sql = f"SELECT area FROM personalfeban_locadores WHERE nombrepersonal='{_nombreautoriza}'"

    try:
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        areaencontrada = cur.execute(sql).fetchall()
        if len(areaencontrada)==0:
            areaencontrada.append('0');
        print("ESTE ES EL areaencontrada: "+str(areaencontrada[0]))
        return areaencontrada[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarPisoSeleccionado(_pisoseleccionado):
    conn = create_connection()
    sql = f"SELECT nombrearea FROM areatabla_locadores WHERE codigo='{_pisoseleccionado}'"

    try:
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        areaencontrada = cur.execute(sql).fetchall()
        if len(areaencontrada)==0:
            areaencontrada.append('0');
        print("ESTE ES EL areaencontrada del piso: "+str(areaencontrada[0]))
        return areaencontrada[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def EncontrarAreaSeleccionada(_areaseleccionado):
    conn = create_connection()
    sql = f"SELECT codigo FROM areatabla_locadores WHERE nombrearea='{_areaseleccionado}'"

    try:
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        areaencontrada = cur.execute(sql).fetchall()
        if len(areaencontrada)==0:
            areaencontrada.append('0');
        print("ESTE ES EL areaencontrada del piso: "+str(areaencontrada[0]))
        return areaencontrada[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()




def ExisteNombreVisitante_locadores(_nombre):
    conn = create_connection()
    sql = f"SELECT nombre FROM visitantes_locadores WHERE nombre='{_nombre}'"

    try:


        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True    
    except Error as e:
        print("Error Selecting book by NombreVisitante: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarNombreVisitante_locadores(_nombre):
    conn = create_connection()
    sql = f"SELECT dni FROM visitantes_locadores WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL NombreVisitante ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
def EncontrarEntidadVisitante_locadores(_nombre):
    conn = create_connection()
    sql = f"SELECT entidad FROM visitantes_locadores WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL entidad ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarMotivoVisitante_locadores(_nombre):
    conn = create_connection()
    sql = f"SELECT motivo FROM visitantes_locadores WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL motivo ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarVisitaVisitante_locadores(_nombre):
    conn = create_connection()
    sql = f"SELECT visita FROM visitantes_locadores WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL visita ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarAutorizaVisitante_locadores(_nombre):
    conn = create_connection()
    sql = f"SELECT autoriza FROM visitantes_locadores WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL autoriza ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarAreaVisitante_locadores(_nombre):
    conn = create_connection()
    sql = f"SELECT area FROM visitantes_locadores WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL area ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarPisoVisitante_locadores(_nombre):
    conn = create_connection()
    sql = f"SELECT piso FROM visitantes_locadores WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL area ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoDNI_locadores(_dni,_visitante,_entidadempresa,_motivovisita,_aquienvisita,_autoriza,_areavisitada,_piso):
   
    conn = create_connection()
    sql = """ INSERT INTO visitantes_locadores (DNI,nombre,entidad,motivo,visita,autoriza,area,piso) 
                                                                
                VALUES(?, ?, ?, ?, ?, ?, ?, ?)
    """

    try:
        data=(_dni,_visitante,_entidadempresa,_motivovisita,_aquienvisita,_autoriza,_areavisitada,_piso,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Visitantes agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def update_NuevoDNI_locadores(dni,nombre):
    conn = create_connection()



    sql = """ UPDATE visitantes_locadores SET (DNI,nombre,entidad,motivo,visita,autoriza,area,piso) 
                                                                
                VALUES(?, ?, ?, ?, ?, ?, ?, ?)
    """

    try:
        data=(dni,nombre)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Visitantes agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def update_NuevoDNI_locadoresV2(_dni,_visitante,_entidadempresa,_motivovisita,_aquienvisita,_autoriza,_areavisitada,_piso):
    conn = create_connection()

    sql = f""" UPDATE visitantes_locadores SET  
                            nombre = ? , entidad = ? , motivo = ? , visita = ? , autoriza = ? , area = ? , piso = ?         
            WHERE DNI = '{_dni}'
    """
    data=(_visitante,_entidadempresa,_motivovisita,_aquienvisita,_autoriza,_areavisitada,_piso,)
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("VisitantesTable Actualizado 444")
        return True
    except Error as e:
        print("Error updating VisitantesTable: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def update_NuevoDNI_personal(dni,nombre):
    conn = create_connection()



    sql = """ UPDATE visitantes_personal SET (DNI,nombre,entidad,motivo,visita,autoriza,area,piso) 
                                                                
                VALUES(?, ?, ?, ?, ?, ?, ?, ?)
    """

    try:
        data=(dni,nombre)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Visitantes agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def update_NuevoDNI_personalV2(_dni,_visitante,_entidadempresa,_motivovisita,_aquienvisita,_autoriza,_areavisitada,_piso):
    conn = create_connection()

    sql = f""" UPDATE visitantes_personal SET  
                            nombre = ? , entidad = ? , motivo = ? , visita = ? , autoriza = ? , area = ? , piso = ?         
            WHERE DNI = '{_dni}'
    """
    data=(_visitante,_entidadempresa,_motivovisita,_aquienvisita,_autoriza,_areavisitada,_piso,)
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("_personalTable Actualizado 444")
        return True
    except Error as e:
        print("Error updating VisitantesTable: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def update_NuevoDNI_mantenimientoV2(_dni,_visitante,_entidadempresa,_motivovisita,_aquienvisita,_autoriza,_areavisitada,_piso):
    conn = create_connection()

    sql = f""" UPDATE visitantes_mantenimiento SET  
                            nombre = ? , entidad = ? , motivo = ? , visita = ? , autoriza = ? , area = ? , piso = ?         
            WHERE DNI = '{_dni}'
    """
    data=(_visitante,_entidadempresa,_motivovisita,_aquienvisita,_autoriza,_areavisitada,_piso,)
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("VisitantesTable Actualizado 444")
        return True
    except Error as e:
        print("Error updating VisitantesTable: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

#//////////////////////////////////////////////////////////////////
def ExisteMotivo_locadores(_nombremotivo):
    conn = create_connection()
    sql = f"SELECT nombremotivo FROM motivoTabla_locadores WHERE nombremotivo='{_nombremotivo}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoMotivo_locadores(_nombremotivo):
    conn = create_connection()
    sql = """ INSERT INTO motivoTabla_locadores (nombremotivo) 
                                                                
                VALUES(?)
    """

    try:
        data=(_nombremotivo,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Motivo agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
##*////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
def ExisteVisita_locadores(_aquienVisita):
    conn = create_connection()
    sql = f"SELECT nombrepersonal FROM personalfeban_locadores WHERE nombrepersonal='{_aquienVisita}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoVisita_locadores(_aquienVisita):
    conn = create_connection()
    sql = """ INSERT INTO personalfeban_locadores (nombrepersonal) 
                                                                
                VALUES(?)
    """

    try:
        data=(_aquienVisita,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro AquienVisita agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
##*////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
def ExisteAutoriza_locadores(_autoriza):
    conn = create_connection()
    sql = f"SELECT nombrepersonal FROM personalfeban_locadores WHERE nombrepersonal='{_autoriza}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_NuevoAutoriza_locadores(_autoriza,_areavisitada):
    conn = create_connection()
    sql = """ INSERT INTO personalfeban_locadores (nombrepersonal,area) 
                                                                
                VALUES(?,?)
    """

    try:
        data=(_autoriza,_areavisitada)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Autoriza agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarAreasDelBn():
    conn = create_connection()
    sql = "SELECT DISTINCT nombrearea FROM AreaTabla_locadores "

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

##*////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
def ExisteEntidad_locadores(_entidad):
    conn = create_connection()
    sql = f"SELECT nombreentidad FROM EntidadTabla_locadores WHERE nombreentidad='{_entidad}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoEntidad_locadores(_nombreentidad):
    conn = create_connection()
    sql = """ INSERT INTO EntidadTabla_locadores (nombreentidad) 
                                                                
                VALUES(?)
    """

    try:
        data=(_nombreentidad,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Entidad agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
##*////////////////////////////////////////////////////////////////

def UpdateVisitante_locadores(_dni, nombrevisitanteNuevo):
    conn = create_connection()

    sql = f""" UPDATE visitantes_locadores SET  
                            nombre = ?           
            WHERE DNI = '{_dni}'
    """
    data=(nombrevisitanteNuevo,)
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("VisitantesTable Actualizado 444")
        return True
    except Error as e:
        print("Error updating VisitantesTable: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def UpdateAutoriza_locadores(_nombreautoriza, area):
    conn = create_connection()

    sql = f""" UPDATE personalfeban_locadores SET  
                            area = ?           
            WHERE nombrepersonal = '{_nombreautoriza}'
    """
    data=(area,)
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("VisitantesTable Actualizado")
        return True
    except Error as e:
        print("Error updating VisitantesTable: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def BuscarUsuario_locadores(_nombreusuario):
    conn = create_connection()
    sql = f"SELECT password FROM UsuariosTabla_locadores WHERE usuario='{_nombreusuario}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        cur.execute(sql)
        usuarios = cur.execute(sql).fetchall()
        if len(usuarios)==0:
            return ""
        else:
            return usuarios[0]
    except Error as e:
        print("EL USUARIO NO EXISTE!: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
###############################################################################################

#################################### MANTENIMIENTO ############################################

def insert_book_mantenimiento(data):
    conn = create_connection()
    sql = """ INSERT INTO books_mantenimiento (fecha, dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada, piso,horaingreso,horasalida,observaciones,estado) 
                                                                
                VALUES(?, ?, ?, ?, ?,?,?,?,?,?,?,?,?)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def update_book_mantenimiento(_id, data):
    conn = create_connection()

    sql = f""" UPDATE books_mantenimiento SET  
                            fecha = ?,
                            dni = ?,
                            visitante = ?,
                            entidadempresa = ?,
                            motivovisita = ?,
                            aquienvisita = ?,
                            autoriza = ?,
                            areavisitada = ?,
                            piso = ?,
                            horaingreso = ?,
                            horasalida = ?,
                            observaciones=?,
                            estado = ?
            WHERE book_id = {_id}
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Libro Actualizado")
        return True
    except Error as e:
        print("Error updating book: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book_mantenimiento(_id):
    conn = create_connection()
    sql = f"DELETE FROM books_mantenimiento WHERE book_id = {_id}"


    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_books_mantenimiento():
    conn = create_connection()
    sql = "SELECT * FROM   books_mantenimiento  ORDER  BY Substr(fecha, 7, 4) DESC, Substr(fecha, 4, 2) DESC, Substr(fecha, 0, 3) DESC , horaingreso DESC LIMIT 500"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_personalFeban_mantenimiento():
    conn = create_connection()
    sql = "SELECT nombrepersonal FROM personalfeban_mantenimiento ORDER BY nombrepersonal ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_all_areaTabla_mantenimiento():
    conn = create_connection()
    sql = "SELECT nombrearea FROM AreaTabla_mantenimiento ORDER BY nombrearea ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_EntidadTabla_mantenimiento():
    conn = create_connection()
    sql = "SELECT nombreentidad FROM EntidadTabla_mantenimiento ORDER BY nombreentidad ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_motivoTabla_mantenimiento():
    conn = create_connection()
    sql = "SELECT nombremotivo FROM motivoTabla_mantenimiento ORDER BY nombremotivo ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_visitantesNombres_mantenimiento():
    conn = create_connection()
    sql = "SELECT nombre FROM visitantes_mantenimiento ORDER BY nombre ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_visitantesDNI_mantenimiento():
    conn = create_connection()
    sql = "SELECT DNI FROM visitantes_mantenimiento ORDER BY DNI ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_id_mantenimiento(_id):
    conn = create_connection()
    sql = f"SELECT * FROM books_mantenimiento WHERE book_id = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        book = cur.fetchone()
        return book
    except Error as e:
        print("Error selecting book by id: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_title_mantenimiento(dni):
    conn = create_connection()
    sql = f"SELECT * FROM books_mantenimiento WHERE dni LIKE '%{dni}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting book by title: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_category_mantenimiento(category):
    conn = create_connection()
    sql = f"SELECT * FROM books_mantenimiento WHERE category LIKE '%{category}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error Selecting book by category: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def generar_data_excel_hoy_mantenimiento(fechastr):
    
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    print("date and time =", dt_string)
    dt_string=dt_string.replace(':','_')
    dt_string=dt_string.replace('/','-')
    workbook = Workbook('REPORTES/REPORTE MANTENIMIENTO '+dt_string+'.xlsx')
    worksheet = workbook.add_worksheet()

    header_data = ['Fecha','Doc. Identidad','APELLIDOS Y NOMBRES','Entidad o Empresa','Motivo de la visita','Persona que Visita','Autorizado por:','Área de la persona visitada','Piso','Hora   de ingreso','Hora de salida','Observaciones']

    header_format = workbook.add_format({'bold': True,
                                        'border': 1,
                                        'font_color':'white',
                                        'font_name': 'Cambria',
                                        'font_size':10,
                                        'bg_color': '#4F81BD',
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})

    for col_num, data in enumerate(header_data):
        worksheet.write(0, col_num, data, header_format)
       

    formatogeneral=workbook.add_format({'font_name': 'Cambria',
                                        'border': 1,
                                        'font_size':10,
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})
    conn = create_connection()
    c=conn.cursor()
    #c.execute(f"select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books WHERE fecha= '{fecha_hoy}'")
    mysel=c.execute(f"select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books_mantenimiento WHERE fecha= '{fechastr}'")
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i+1, j, value,formatogeneral)
    
    worksheet.set_column(0, 0, 12.43)
    worksheet.set_column(1,1, 11.57)
    worksheet.set_column(2,2 , 37.14)
    worksheet.set_column(3,3 , 25.43)
    worksheet.set_column(4,4 , 21.43)
    worksheet.set_column(5,5 , 22.86)
    worksheet.set_column(6,6 , 20.71)
    worksheet.set_column(7,7 , 22.29)
    worksheet.set_column(8,8 , 7)
    worksheet.set_column(9,9 , 7)
    worksheet.set_column(10,10 , 6)
    worksheet.set_column(11,11 , 36.29)
    worksheet.set_zoom(80)
    workbook.close()


def generar_data_excel_fechas_mantenimiento(fechainicio, fechafinal):
    
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    dt_string=dt_string.replace(':','_')
    dt_string=dt_string.replace('/','-')
    workbook = Workbook('REPORTES/REPORTE FILTRADO MANTENIMIENTO '+dt_string+'.xlsx')

    #TRANSFORMANDO EL FORMATO DE FECHAS

    worksheet = workbook.add_worksheet()

    header_data = ['Fecha','Doc. Identidad','APELLIDOS Y NOMBRES','Entidad o Empresa','Motivo de la visita','Persona que Visita','Autorizado por:','Área de la persona visitada','Piso','Hora   de ingreso','Hora de salida','Observaciones']

    header_format = workbook.add_format({'bold': True,
                                        'border': 1,
                                        'font_color':'white',
                                        'font_name': 'Cambria',
                                        'font_size':10,
                                        'bg_color': '#4F81BD',
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})

    for col_num, data in enumerate(header_data):
        worksheet.write(0, col_num, data, header_format)
       

    formatogeneral=workbook.add_format({'font_name': 'Cambria',
                                        'border': 1,
                                        'font_size':10,
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})
    conn = create_connection()
    c=conn.cursor()
    #c.execute(f"select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books WHERE fecha= '{fecha_hoy}'")1/01/2021       2021-01-01' and '2021-12-12
    #2021-01-01' and '2021-12-12
    CadenaFechaInicial= fechainicio.split('/')
    CadenaFechaFinal= fechafinal.split('/')
    NuevaFechaFinal=CadenaFechaFinal[2]+"-"+CadenaFechaFinal[1]+"-"+CadenaFechaFinal[0]
    NuevaFechaInicial=CadenaFechaInicial[2]+"-"+CadenaFechaInicial[1]+"-"+CadenaFechaInicial[0]
    myData=(NuevaFechaInicial,NuevaFechaFinal)
    q="select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books_mantenimiento WHERE (substr(fecha, 7, 4) || '-' || substr(fecha, 4, 2) || '-' || substr(fecha, 1, 2)) between ? and ?"
    mysel=c.execute(q,myData)
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i+1, j, value,formatogeneral)
    
    worksheet.set_column(0, 0, 12.43)
    worksheet.set_column(1,1, 11.57)
    worksheet.set_column(2,2 , 37.14)
    worksheet.set_column(3,3 , 25.43)
    worksheet.set_column(4,4 , 21.43)
    worksheet.set_column(5,5 , 22.86)
    worksheet.set_column(6,6 , 20.71)
    worksheet.set_column(7,7 , 22.29)
    worksheet.set_column(8,8 , 7)
    worksheet.set_column(9,9 , 7)
    worksheet.set_column(10,10 , 6)
    worksheet.set_column(11,11 , 36.29)
    worksheet.set_zoom(80)
    workbook.close()

def select_book_by_all_mantenimiento(parameterDni,parameterPiso,parameterVisitante,parameterFecha,parameterMotivo,parameterEstado):
    conn = create_connection()
    sql = f"SELECT * FROM books_mantenimiento WHERE dni LIKE '%{parameterDni}%' AND piso LIKE '%{parameterPiso}%' AND visitante LIKE '%{parameterVisitante}%' AND fecha LIKE '%{parameterFecha}%' AND motivovisita LIKE '%{parameterMotivo}%' AND estado LIKE '%{parameterEstado}%' "

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error Selecting book by category: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def ExisteDni_mantenimiento(_dni):
    conn = create_connection()
    sql = f"SELECT dni FROM visitantes_mantenimiento WHERE dni='{_dni}'"

    try:


        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True    
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarDni_mantenimiento(_dni):
    conn = create_connection()
    sql = f"SELECT nombre FROM visitantes_mantenimiento WHERE dni='{_dni}'"

    try:
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        if len(dniencontrado)==0:
            dniencontrado.append('0');
        print("ESTE ES EL DNI ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def EncontrarAutorizaArea_mantenimiento(_nombreautoriza):
    conn = create_connection()
    sql = f"SELECT area FROM personalfeban_mantenimiento WHERE nombrepersonal='{_nombreautoriza}'"

    try:
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        areaencontrada = cur.execute(sql).fetchall()
        if len(areaencontrada)==0:
            areaencontrada.append('0');
        print("ESTE ES EL areaencontrada: "+str(areaencontrada[0]))
        return areaencontrada[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()







def ExisteNombreVisitante_mantenimiento(_nombre):
    conn = create_connection()
    sql = f"SELECT nombre FROM visitantes_mantenimiento WHERE nombre='{_nombre}'"

    try:


        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True    
    except Error as e:
        print("Error Selecting book by NombreVisitante: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarNombreVisitante_mantenimiento(_nombre):
    conn = create_connection()
    sql = f"SELECT dni FROM visitantes_mantenimiento WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL NombreVisitante ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarEntidadVisitante_mantenimiento(_nombre):
    conn = create_connection()
    sql = f"SELECT entidad FROM visitantes_mantenimiento WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL entidad ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarMotivoVisitante_mantenimiento(_nombre):
    conn = create_connection()
    sql = f"SELECT motivo FROM visitantes_mantenimiento WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL motivo ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarVisitaVisitante_mantenimiento(_nombre):
    conn = create_connection()
    sql = f"SELECT visita FROM visitantes_mantenimiento WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL visita ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarAutorizaVisitante_mantenimiento(_nombre):
    conn = create_connection()
    sql = f"SELECT autoriza FROM visitantes_mantenimiento WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL autoriza ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarAreaVisitante_mantenimiento(_nombre):
    conn = create_connection()
    sql = f"SELECT area FROM visitantes_mantenimiento WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL area ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarPisoVisitante_mantenimiento(_nombre):
    conn = create_connection()
    sql = f"SELECT piso FROM visitantes_mantenimiento WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL area ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoDNI_mantenimiento(_dni,_visitante,_entidadempresa,_motivovisita,_aquienvisita,_autoriza,_areavisitada,_piso):
    conn = create_connection()
    sql = """ INSERT INTO visitantes_mantenimiento (DNI,nombre,entidad,motivo,visita,autoriza,area,piso) 
                                                                
                VALUES(?, ?,?,?,?,?,?,?)
    """

    try:
        data=(_dni,_visitante,_entidadempresa,_motivovisita,_aquienvisita,_autoriza,_areavisitada,_piso,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Visitantes agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

#//////////////////////////////////////////////////////////////////
def ExisteMotivo_mantenimiento(_nombremotivo):
    conn = create_connection()
    sql = f"SELECT nombremotivo FROM motivoTabla_mantenimiento WHERE nombremotivo='{_nombremotivo}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoMotivo_mantenimiento(_nombremotivo):
    conn = create_connection()
    sql = """ INSERT INTO motivoTabla_mantenimiento (nombremotivo) 
                                                                
                VALUES(?)
    """

    try:
        data=(_nombremotivo,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Motivo agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
##*////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
def ExisteVisita_mantenimiento(_aquienVisita):
    conn = create_connection()
    sql = f"SELECT nombrepersonal FROM personalfeban_mantenimiento WHERE nombrepersonal='{_aquienVisita}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoVisita_mantenimiento(_aquienVisita):
    conn = create_connection()
    sql = """ INSERT INTO personalfeban_mantenimiento (nombrepersonal) 
                                                                
                VALUES(?)
    """

    try:
        data=(_aquienVisita,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro AquienVisita agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
##*////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
def ExisteAutoriza_mantenimiento(_autoriza):
    conn = create_connection()
    sql = f"SELECT nombrepersonal FROM personalfeban_mantenimiento WHERE nombrepersonal='{_autoriza}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_NuevoAutoriza_mantenimiento(_autoriza,_areavisitada):
    conn = create_connection()
    sql = """ INSERT INTO personalfeban_mantenimiento (nombrepersonal,area) 
                                                                
                VALUES(?,?)
    """

    try:
        data=(_autoriza,_areavisitada)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Autoriza agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
##*////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
def ExisteEntidad_mantenimiento(_entidad):
    conn = create_connection()
    sql = f"SELECT nombreentidad FROM EntidadTabla_mantenimiento WHERE nombreentidad='{_entidad}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoEntidad_mantenimiento(_nombreentidad):
    conn = create_connection()
    sql = """ INSERT INTO EntidadTabla_mantenimiento (nombreentidad) 
                                                                
                VALUES(?)
    """

    try:
        data=(_nombreentidad,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Entidad agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
##*////////////////////////////////////////////////////////////////

def UpdateVisitante_mantenimiento(_dni, nombrevisitanteNuevo):
    conn = create_connection()

    sql = f""" UPDATE visitantes_mantenimiento SET  
                            nombre = ?           
            WHERE DNI = '{_dni}'
    """
    data=(nombrevisitanteNuevo,)
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("VisitantesTable Actualizado")
        return True
    except Error as e:
        print("Error updating VisitantesTable: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def UpdateAutoriza_mantenimiento(_nombreautoriza, area):
    conn = create_connection()

    sql = f""" UPDATE personalfeban_mantenimiento SET  
                            area = ?           
            WHERE nombrepersonal = '{_nombreautoriza}'
    """
    data=(area,)
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("VisitantesTable Actualizado")
        return True
    except Error as e:
        print("Error updating VisitantesTable: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def BuscarUsuario_mantenimiento(_nombreusuario):
    conn = create_connection()
    sql = f"SELECT password FROM UsuariosTabla_mantenimiento WHERE usuario='{_nombreusuario}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        cur.execute(sql)
        usuarios = cur.execute(sql).fetchall()
        if len(usuarios)==0:
            return ""
        else:
            return usuarios[0]
    except Error as e:
        print("EL USUARIO NO EXISTE!: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
#################################################################################################


#################################### PERSONAL__ ############################################

def insert_book_personal(data):
    conn = create_connection()
    sql = """ INSERT INTO books_personal (fecha, dni,visitante,entidadempresa,motivovisita,aquienvisita,autoriza,areavisitada, piso,horaingreso,horasalida,observaciones,estado) 
                                                                
                VALUES(?, ?, ?, ?, ?,?,?,?,?,?,?,?,?)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def update_book_personal(_id, data):
    conn = create_connection()

    sql = f""" UPDATE books_personal SET  
                            fecha = ?,
                            dni = ?,
                            visitante = ?,
                            entidadempresa = ?,
                            motivovisita = ?,
                            aquienvisita = ?,
                            autoriza = ?,
                            areavisitada = ?,
                            piso = ?,
                            horaingreso = ?,
                            horasalida = ?,
                            observaciones=?,
                            estado = ?
            WHERE book_id = {_id}
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Libro Actualizado")
        return True
    except Error as e:
        print("Error updating book: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book_personal(_id):
    conn = create_connection()
    sql = f"DELETE FROM books_personal WHERE book_id = {_id}"


    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_books_personal():
    conn = create_connection()
    sql = "SELECT * FROM   books_personal  ORDER  BY Substr(fecha, 7, 4) DESC, Substr(fecha, 4, 2) DESC, Substr(fecha, 0, 3) DESC , horaingreso DESC LIMIT 500"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_personalFeban_personal():
    conn = create_connection()
    sql = "SELECT nombrepersonal FROM personalfeban_personal ORDER BY nombrepersonal ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def select_all_areaTabla_personal():
    conn = create_connection()
    sql = "SELECT nombrearea FROM AreaTabla_personal ORDER BY nombrearea ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_EntidadTabla_personal():
    conn = create_connection()
    sql = "SELECT nombreentidad FROM EntidadTabla_personal ORDER BY nombreentidad ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_motivoTabla_personal():
    conn = create_connection()
    sql = "SELECT nombremotivo FROM motivoTabla_personal ORDER BY nombremotivo ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_visitantesNombres_personal():
    conn = create_connection()
    sql = "SELECT nombre FROM visitantes_personal ORDER BY nombre ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_visitantesDNI_personal():
    conn = create_connection()
    sql = "SELECT DNI FROM visitantes_personal ORDER BY DNI ASC"

    try:
        
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
    except Error as e:
        print("Error selecting all books: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_id_personal(_id):
    conn = create_connection()
    sql = f"SELECT * FROM books_personal WHERE book_id = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        book = cur.fetchone()
        return book
    except Error as e:
        print("Error selecting book by id: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_title_personal(dni):
    conn = create_connection()
    sql = f"SELECT * FROM books_personal WHERE dni LIKE '%{dni}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error selecting book by title: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_category_personal(category):
    conn = create_connection()
    sql = f"SELECT * FROM books_personal WHERE category LIKE '%{category}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error Selecting book by category: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def generar_data_excel_hoy_personal(fechastr):
    
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    print("date and time =", dt_string)
    dt_string=dt_string.replace(':','_')
    dt_string=dt_string.replace('/','-')
    workbook = Workbook('REPORTES/REPORTE PERSONAL '+dt_string+'.xlsx')
    worksheet = workbook.add_worksheet()

    header_data = ['Fecha','Doc. Identidad','APELLIDOS Y NOMBRES','Entidad o Empresa','Motivo de la visita','Persona que Visita','Autorizado por:','Área de la persona visitada','Piso','Hora   de ingreso','Hora de salida','Observaciones']

    header_format = workbook.add_format({'bold': True,
                                        'border': 1,
                                        'font_color':'white',
                                        'font_name': 'Cambria',
                                        'font_size':10,
                                        'bg_color': '#4F81BD',
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})

    for col_num, data in enumerate(header_data):
        worksheet.write(0, col_num, data, header_format)
       

    formatogeneral=workbook.add_format({'font_name': 'Cambria',
                                        'border': 1,
                                        'font_size':10,
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})
    conn = create_connection()
    c=conn.cursor()
    #c.execute(f"select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books WHERE fecha= '{fecha_hoy}'")
    mysel=c.execute(f"select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books_personal WHERE fecha= '{fechastr}'")
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i+1, j, value,formatogeneral)
    
    worksheet.set_column(0, 0, 12.43)
    worksheet.set_column(1,1, 11.57)
    worksheet.set_column(2,2 , 37.14)
    worksheet.set_column(3,3 , 25.43)
    worksheet.set_column(4,4 , 21.43)
    worksheet.set_column(5,5 , 22.86)
    worksheet.set_column(6,6 , 20.71)
    worksheet.set_column(7,7 , 22.29)
    worksheet.set_column(8,8 , 7)
    worksheet.set_column(9,9 , 7)
    worksheet.set_column(10,10 , 6)
    worksheet.set_column(11,11 , 36.29)
    worksheet.set_zoom(80)
    workbook.close()


def generar_data_excel_fechas_personal(fechainicio, fechafinal):
    
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    dt_string=dt_string.replace(':','_')
    dt_string=dt_string.replace('/','-')
    workbook = Workbook('REPORTES/REPORTE FILTRADO PERSONAL '+dt_string+'.xlsx')

    #TRANSFORMANDO EL FORMATO DE FECHAS

    worksheet = workbook.add_worksheet()

    header_data = ['Fecha','Doc. Identidad','APELLIDOS Y NOMBRES','Entidad o Empresa','Motivo de la visita','Persona que Visita','Autorizado por:','Área de la persona visitada','Piso','Hora   de ingreso','Hora de salida','Observaciones']

    header_format = workbook.add_format({'bold': True,
                                        'border': 1,
                                        'font_color':'white',
                                        'font_name': 'Cambria',
                                        'font_size':10,
                                        'bg_color': '#4F81BD',
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})

    for col_num, data in enumerate(header_data):
        worksheet.write(0, col_num, data, header_format)
       

    formatogeneral=workbook.add_format({'font_name': 'Cambria',
                                        'border': 1,
                                        'font_size':10,
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'text_wrap':True})
    conn = create_connection()
    c=conn.cursor()
    #c.execute(f"select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books WHERE fecha= '{fecha_hoy}'")1/01/2021       2021-01-01' and '2021-12-12
    #2021-01-01' and '2021-12-12
    CadenaFechaInicial= fechainicio.split('/')
    CadenaFechaFinal= fechafinal.split('/')
    NuevaFechaFinal=CadenaFechaFinal[2]+"-"+CadenaFechaFinal[1]+"-"+CadenaFechaFinal[0]
    NuevaFechaInicial=CadenaFechaInicial[2]+"-"+CadenaFechaInicial[1]+"-"+CadenaFechaInicial[0]
    myData=(NuevaFechaInicial,NuevaFechaFinal)
    q="select fecha, dni, visitante, entidadempresa, motivovisita, aquienvisita, autoriza, areavisitada, piso, horaingreso, horasalida, observaciones from books_personal WHERE (substr(fecha, 7, 4) || '-' || substr(fecha, 4, 2) || '-' || substr(fecha, 1, 2)) between ? and ?"
    mysel=c.execute(q,myData)
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i+1, j, value,formatogeneral)
    
    worksheet.set_column(0, 0, 12.43)
    worksheet.set_column(1,1, 11.57)
    worksheet.set_column(2,2 , 37.14)
    worksheet.set_column(3,3 , 25.43)
    worksheet.set_column(4,4 , 21.43)
    worksheet.set_column(5,5 , 22.86)
    worksheet.set_column(6,6 , 20.71)
    worksheet.set_column(7,7 , 22.29)
    worksheet.set_column(8,8 , 7)
    worksheet.set_column(9,9 , 7)
    worksheet.set_column(10,10 , 6)
    worksheet.set_column(11,11 , 36.29)
    worksheet.set_zoom(80)
    workbook.close()

def select_book_by_all_personal(parameterDni,parameterPiso,parameterVisitante,parameterFecha,parameterMotivo,parameterEstado):
    conn = create_connection()
    sql = f"SELECT * FROM books_personal WHERE dni LIKE '%{parameterDni}%' AND piso LIKE '%{parameterPiso}%' AND visitante LIKE '%{parameterVisitante}%' AND fecha LIKE '%{parameterFecha}%' AND motivovisita LIKE '%{parameterMotivo}%' AND estado LIKE '%{parameterEstado}%' "

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books
    except Error as e:
        print("Error Selecting book by category: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def ExisteDni_personal(_dni):
    conn = create_connection()
    sql = f"SELECT dni FROM visitantes_personal WHERE dni='{_dni}'"

    try:


        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True    
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarDni_personal(_dni):
    conn = create_connection()
    sql = f"SELECT nombre FROM visitantes_personal WHERE dni='{_dni}'"

    try:
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        if len(dniencontrado)==0:
            dniencontrado.append('0');
        print("ESTE ES EL DNI ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def EncontrarAutorizaArea_personal(_nombreautoriza):
    conn = create_connection()
    sql = f"SELECT area FROM personalfeban_personal WHERE nombrepersonal='{_nombreautoriza}'"

    try:
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        personal = cur.execute(sql).fetchall()
        
        return personal
        '''
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        areaencontrada = cur.execute(sql).fetchall()
        if len(areaencontrada)==0:
            areaencontrada.append('0');
        print("ESTE ES EL areaencontrada: "+str(areaencontrada[0]))
        return areaencontrada[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()







def ExisteNombreVisitante_personal(_nombre):
    conn = create_connection()
    sql = f"SELECT nombre FROM visitantes_personal WHERE nombre='{_nombre}'"

    try:


        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True    
    except Error as e:
        print("Error Selecting book by NombreVisitante: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarNombreVisitante_personal(_nombre):
    conn = create_connection()
    sql = f"SELECT dni FROM visitantes_personal WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL NombreVisitante ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarEntidadVisitante_personal(_nombre):
    conn = create_connection()
    sql = f"SELECT entidad FROM visitantes_personal WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL entidad ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarMotivoVisitante_personal(_nombre):
    conn = create_connection()
    sql = f"SELECT motivo FROM visitantes_personal WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL motivo ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarVisitaVisitante_personal(_nombre):
    conn = create_connection()
    sql = f"SELECT visita FROM visitantes_personal WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL visita ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarAutorizaVisitante_personal(_nombre):
    conn = create_connection()
    sql = f"SELECT autoriza FROM visitantes_personal WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL autoriza ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarAreaVisitante_personal(_nombre):
    conn = create_connection()
    sql = f"SELECT area FROM visitantes_personal WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL area ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def EncontrarPisoVisitante_personal(_nombre):
    conn = create_connection()
    sql = f"SELECT piso FROM visitantes_personal WHERE nombre='{_nombre}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        dniencontrado = cur.execute(sql).fetchall()
        print("ESTE ES EL area ENCONTRADO: "+str(dniencontrado[0]))
        return dniencontrado[0]
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoDNI_personal(_dni,_visitante,_entidadempresa,_motivovisita,_aquienvisita,_autoriza,_areavisitada,_piso):
    conn = create_connection()
    sql = """ INSERT INTO visitantes_personal (DNI,nombre,entidad,motivo,visita,autoriza,area,piso) 
                                                                
                VALUES(?, ?,?,?,?,?,?,?)
    """

    try:
        data=(_dni,_visitante,_entidadempresa,_motivovisita,_aquienvisita,_autoriza,_areavisitada,_piso,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Visitantes agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

#//////////////////////////////////////////////////////////////////
def ExisteMotivo_personal(_nombremotivo):
    conn = create_connection()
    sql = f"SELECT nombremotivo FROM motivoTabla_personal WHERE nombremotivo='{_nombremotivo}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoMotivo_personal(_nombremotivo):
    conn = create_connection()
    sql = """ INSERT INTO motivoTabla_personal (nombremotivo) 
                                                                
                VALUES(?)
    """

    try:
        data=(_nombremotivo,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Motivo agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
##*////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
def ExisteVisita_personal(_aquienVisita):
    conn = create_connection()
    sql = f"SELECT nombrepersonal FROM personalfeban_personal WHERE nombrepersonal='{_aquienVisita}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoVisita_personal(_aquienVisita):
    conn = create_connection()
    sql = """ INSERT INTO personalfeban_personal (nombrepersonal) 
                                                                
                VALUES(?)
    """

    try:
        data=(_aquienVisita,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro AquienVisita agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
##*////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
def ExisteAutoriza_personal(_autoriza):
    conn = create_connection()
    sql = f"SELECT nombrepersonal FROM personalfeban_personal WHERE nombrepersonal='{_autoriza}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def insert_NuevoAutoriza_personal(_autoriza,_areavisitada):
    conn = create_connection()
    sql = """ INSERT INTO personalfeban_personal (nombrepersonal,area) 
                                                                
                VALUES(?,?)
    """

    try:
        data=(_autoriza,_areavisitada)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Autoriza agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
##*////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////
def ExisteEntidad_personal(_entidad):
    conn = create_connection()
    sql = f"SELECT nombreentidad FROM EntidadTabla_personal WHERE nombreentidad='{_entidad}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        if len(books)==0:
            return False
        else:
            return True
    except Error as e:
        print("Error Selecting book by DNI: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_NuevoEntidad_personal(_nombreentidad):
    conn = create_connection()
    sql = """ INSERT INTO EntidadTabla_personal (nombreentidad) 
                                                                
                VALUES(?)
    """

    try:
        data=(_nombreentidad,)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Registro Entidad agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Inserting new book:" + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def insert_usuario(usuario, password, estado):
    conn = create_connection()
    sql = """ INSERT INTO UsuariosTabla (usuario, password, estado) 
            VALUES(?,?,?)
    """
    try:
        data = (usuario, password, estado)
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo Usuario agregado!")
        return True, cur.lastrowid
    except Error as e:
        print("Error Insertando nuevo usuario:", str(e))
        return False, None
    finally:
        if conn:
            conn.close()


##*////////////////////////////////////////////////////////////////

def UpdateVisitante_personal(_dni, nombrevisitanteNuevo):
    conn = create_connection()

    sql = f""" UPDATE visitantes_personal SET  
                            nombre = ?           
            WHERE DNI = '{_dni}'
    """
    data=(nombrevisitanteNuevo,)
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("VisitantesTable Actualizado")
        return True
    except Error as e:
        print("Error updating VisitantesTable: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def UpdateAutoriza_personal(_nombreautoriza, area):
    conn = create_connection()

    sql = f""" UPDATE personalfeban_personal SET  
                            area = ?           
            WHERE nombrepersonal = '{_nombreautoriza}'
    """
    data=(area,)
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("VisitantesTable Actualizado")
        return True
    except Error as e:
        print("Error updating VisitantesTable: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def BuscarUsuario_personal(_nombreusuario):
    conn = create_connection()
    sql = f"SELECT password FROM UsuariosTabla_personal WHERE usuario='{_nombreusuario}'"

    try:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        cur.execute(sql)
        usuarios = cur.execute(sql).fetchall()
        if len(usuarios)==0:
            return ""
        else:
            return usuarios[0]
    except Error as e:
        print("EL USUARIO NO EXISTE!: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_geografica_central(_emp,_cent,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Central_Generacion_Vertice_Perimetro_Coordenadas_Geograficas WHERE COD_EMP = ? AND COD_CENTRAL = ? AND SECUENCIA = ?'''


    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_geografica_subestacion(_emp,_cent,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Subestacion_Vertice_Perimetro_Coordenadas_Geograficas WHERE COD_EMP = ? AND COD_SE = ? AND SECUENCIA = ?'''

    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_plano_central(_emp,_cent,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Central_Generacion_Vertice_Perimetro_Plano_Planta WHERE COD_EMP = ? AND COD_CENTRAL = ? AND SECUENCIA = ?'''


    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_plano_subestacion(_emp,_cent,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Subestacion_Vertice_Perimetro_Plano_Planta WHERE COD_EMP = ? AND COD_SE = ? AND SECUENCIA = ?'''


    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_esquema_celda_central(_emp,_cent,_celda,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Celda_Central_Generacion_Ubicacion_Esquema WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_CELDA = ? AND SECUENCIA = ?'''

    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_celda,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_plano_celda_central(_emp,_cent,_celda,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Celda_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_CELDA = ? AND SECUENCIA = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_celda,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_esquema_celda_subestacion(_emp,_cent,_celda,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Celda_Ubicacion_Esquema WHERE COD_EMP = ? AND COD_SE = ? AND COD_CELDA = ? AND SECUENCIA = ?'''

    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_celda,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_plano_celda_subestacion(_emp,_cent,_celda,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Celda_Ubicacion_Plano_Planta WHERE COD_EMP = ? AND COD_SE = ? AND COD_CELDA = ? AND SECUENCIA = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_celda,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

##12
def delete_esquema_barra_subestacion(_emp,_cent,_celda,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Barra_Ubicacion_Esquema WHERE COD_EMP = ? AND COD_SE = ? AND COD_BARRA = ? AND SECUENCIA = ?'''
    print("VARIABLES:"+_emp+" __ "+_cent+" __ "+_celda+" __ "+_sec)
    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_celda,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_plano_barra_subestacion(_emp, _cent, _celda, _sec):
    conn = create_connection()
    sql = '''DELETE FROM Barra_Ubicacion_Plano_Planta WHERE COD_EMP = ? AND COD_SE = ? AND COD_BARRA = ? AND SECUENCIA = ?'''
    
    print("VARIABLES:")
    print("_emp:", _emp)
    print("_cent:", _cent)
    print("_celda:", _celda)
    print("_sec:", _sec)
   
    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp, _cent, _celda, _sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:", str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

##12
def delete_esquema_barra_central(_emp,_cent,_celda,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Barra_Central_Generacion_Ubicacion_Esquema WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_BARRA = ? AND SECUENCIA = ?'''

    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_celda,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_plano_barra_central(_emp,_cent,_celda,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Barra_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_BARRA = ? AND SECUENCIA = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_celda,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
##12
def delete_esquema_conductor_central(_emp,_cent,_celda,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Conductor_Central_Generacion_Ubicacion_Esquema WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_CONDUCTOR = ? AND SECUENCIA = ?'''

    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_celda,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_plano_conductor_central(_emp,_cent,_celda,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Conductor_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_EMP = ? AND COD_CENTRAL = ? AND COD_CONDUCTOR = ? AND SECUENCIA = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_celda,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

##12
def delete_esquema_conductor_subestacion(_emp,_cent,_celda,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Conductor_Ubicacion_Esquema WHERE COD_EMP = ? AND COD_SE = ? AND COD_CONDUCTOR = ? AND SECUENCIA = ?'''

    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_celda,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_plano_conductor_subestacion(_emp,_cent,_celda,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Conductor_Ubicacion_Plano_Planta WHERE COD_EMP = ? AND COD_SE = ? AND COD_CONDUCTOR = ? AND SECUENCIA = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_celda,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_ubicacion_tramo_linea(_emp,_cent,_celda,_sec):
    conn = create_connection()
    sql = '''DELETE FROM Tramo_Linea_Vertice_Ubicacion_Geografica WHERE COD_EMP = ? AND COD_LINEA = ? AND COD_TRAMO = ? AND SECUENCIA = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, (_emp,_cent,_celda,_sec))
        conn.commit()
        print(" - Libro Eliminado - ")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
##FINAL
##FINAL
##FINAL
def delete_book_Central_Generacion(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Central_Generacion WHERE COD_CENTRAL = ?",
        "DELETE FROM Central_Generacion_Vertice_Perimetro_Coordenadas_Geograficas WHERE COD_CENTRAL = ?",
        "DELETE FROM Central_Generacion_Vertice_Perimetro_Plano_Planta WHERE COD_CENTRAL = ?",
        "DELETE FROM Generador_Central_Generacion WHERE COD_CENTRAL = ?",
        "DELETE FROM Generador_Central_Generacion_Ubicacion_Esquema WHERE COD_CENTRAL = ?",
        "DELETE FROM Generador_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ?",
        "DELETE FROM Barra_Central_Generacion WHERE COD_CENTRAL = ?",
        "DELETE FROM Barra_Central_Generacion_Ubicacion_Esquema WHERE COD_CENTRAL = ?",
        "DELETE FROM Barra_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ?",
        "DELETE FROM Celda_Central_Generacion WHERE COD_CENTRAL = ?",
        "DELETE FROM Celda_Central_Generacion_Ubicacion_Esquema WHERE COD_CENTRAL = ?",
        "DELETE FROM Celda_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ?",
        "DELETE FROM Portico_Central_Generacion WHERE COD_CENTRAL = ?",
        "DELETE FROM Portico_Central_Generacion_Estructura WHERE COD_CENTRAL = ?",
        "DELETE FROM Portico_Central_Generacion_Travesano WHERE COD_CENTRAL = ?",
        "DELETE FROM Interruptor_Central_Generacion WHERE COD_CENTRAL = ?",
        "DELETE FROM Interruptor_Central_Generacion_Ubicacion_Esquema WHERE COD_CENTRAL = ?",
        "DELETE FROM Interruptor_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ?",
        "DELETE FROM Seccionador_Central_Generacion WHERE COD_CENTRAL = ?",
        "DELETE FROM Seccionador_Central_Generacion_Ubicacion_Esquema WHERE COD_CENTRAL = ?",
        "DELETE FROM Seccionador_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ?",
        "DELETE FROM Transformador_Central_Generacion WHERE COD_CENTRAL = ?",
        "DELETE FROM Transformador_Central_Generacion_Ubicacion_Esquema WHERE COD_CENTRAL = ?",
        "DELETE FROM Transformador_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ?",
        "DELETE FROM Pararrayo_Central_Generacion WHERE COD_CENTRAL = ?",
        "DELETE FROM Pararrayo_Central_Generacion_Ubicacion_Esquema WHERE COD_CENTRAL = ?",
        "DELETE FROM Pararrayo_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ?",
        "DELETE FROM Transformador_Medicion_Central_Generacion WHERE COD_CENTRAL = ?",
        "DELETE FROM Transformador_Medicion_Central_Ubicacion_Esquema WHERE COD_CENTRAL = ?",
        "DELETE FROM Transformador_Medicion_Central_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ?",
        "DELETE FROM Conductor_Central_Generacion WHERE COD_CENTRAL = ?",
        "DELETE FROM Conductor_Central_Generacion_Ubicacion_Esquema WHERE COD_CENTRAL = ?",
        "DELETE FROM Conductor_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CENTRAL = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_usuario(_id):
    conn = create_connection()
    sql = "DELETE FROM UsuariosTabla WHERE usuario = ?"

    print("EL ID A ELIMINAR ES: "+str(_id))
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book_Subestacion(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Subestacion WHERE COD_SE = ?",
        "DELETE FROM Subestacion_Vertice_Perimetro_Coordenadas_Geograficas WHERE COD_SE = ?",
        "DELETE FROM Subestacion_Vertice_Perimetro_Plano_Planta WHERE COD_SE = ?",
        "DELETE FROM Barra WHERE COD_SE = ?",
        "DELETE FROM Barra_Ubicacion_Esquema WHERE COD_SE = ?",
        "DELETE FROM Barra_Ubicacion_Plano_Planta WHERE COD_SE = ?",
        "DELETE FROM Portico WHERE COD_SE = ?",
        "DELETE FROM Portico_Estructura WHERE COD_SE = ?",
        "DELETE FROM Portico_Travesanio WHERE COD_SE = ?",
        "DELETE FROM Celda WHERE COD_SE = ?",
        "DELETE FROM Celda_Ubicacion_Esquema WHERE COD_SE = ?",
        "DELETE FROM Celda_Ubicacion_Plano_Planta WHERE COD_SE = ?",
        "DELETE FROM Transformador_Potencia WHERE COD_SE = ?",
        "DELETE FROM Transformador_Potencia_Ubicacion_Esquema WHERE COD_SE = ?",
        "DELETE FROM Transformador_Potencia_Ubicacion_Plano_Planta WHERE COD_SE = ?",
        "DELETE FROM Interruptor_Potencia WHERE COD_SE = ?",
        "DELETE FROM Interruptor_Potencia_Ubicacion_Esquema WHERE COD_SE = ?",
        "DELETE FROM Interruptor_Potencia_Ubicacion_Plano_Planta WHERE COD_SE = ?",
        "DELETE FROM Seccionador WHERE COD_SE = ?",
        "DELETE FROM Seccionador_Ubicacion_Esquema WHERE COD_SE = ?",
        "DELETE FROM Seccionador_Ubicacion_Plano_Planta WHERE COD_SE = ?",
        "DELETE FROM Pararrayo WHERE COD_SE = ?",
        "DELETE FROM Pararrayo_Ubicacion_Esquema WHERE COD_SE = ?",
        "DELETE FROM Pararrayo_Ubicacion_Plano_Planta WHERE COD_SE = ?",
        "DELETE FROM Transformador_Medicion WHERE COD_SE = ?",
        "DELETE FROM Transformador_Medicion_Ubicacion_Esquema WHERE COD_SE = ?",
        "DELETE FROM Transformador_Medicion_Ubicacion_Plano_Planta WHERE COD_SE = ?",
        "DELETE FROM Bobina_Bloqueo WHERE COD_SE = ?",
        "DELETE FROM Bobina_Bloqueo_Ubicacion_Esquema WHERE COD_SE = ?",
        "DELETE FROM Bobina_Bloqueo_Ubicacion_Plano_Planta WHERE COD_SE = ?",
        "DELETE FROM Conductor WHERE COD_SE = ?",
        "DELETE FROM Conductor_Ubicacion_Esquema WHERE COD_SE = ?",
        "DELETE FROM Conductor_Ubicacion_Plano_Planta WHERE COD_SE = ?",
        "DELETE FROM Compensador_Reactivo WHERE COD_SE = ?",
        "DELETE FROM Compensador_Reactivo_Ubicacion_Esquema WHERE COD_SE = ?",
        "DELETE FROM Compensador_Reactivo_Ubicacion_Plano_Planta WHERE COD_SE = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Linea_Transmision(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Linea_Transmision WHERE COD_LINEA = ?",
        "DELETE FROM Tramo_Linea_Transmision WHERE COD_LINEA = ?",
        "DELETE FROM Tramo_Linea_Vertice_Ubicacion_Geografica WHERE COD_LINEA = ?",
        "DELETE FROM Estructura WHERE COD_LINEA = ?",
        "DELETE FROM Estructura_Ubicacion_Geografica WHERE COD_LINEA = ?",
        "DELETE FROM Estructura_Ubicacion_Plano_Planta_Central_Generacion WHERE COD_LINEA = ?",
        "DELETE FROM Estructura_Ubicacion_Plano_Planta_Subestacion WHERE COD_LINEA = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book_Generador_Central_Generacion(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Generador_Central_Generacion WHERE COD_GENERADOR = ?",
        "DELETE FROM Central_Generacion_Vertice_Perimetro_Coordenadas_Geograficas WHERE COD_GENERADOR = ?",
        "DELETE FROM Central_Generacion_Vertice_Perimetro_Plano_Planta WHERE COD_GENERADOR = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Celda_Central_Generacion(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Celda_Central_Generacion WHERE COD_CELDA = ?",
        "DELETE FROM Celda_Central_Generacion_Ubicacion_Esquema WHERE COD_CELDA= ?",
        "DELETE FROM Celda_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CELDA= ?",
        "DELETE FROM Interruptor_Central_Generacion WHERE COD_CELDA= ?",
        "DELETE FROM Interruptor_Central_Generacion_Ubicacion_Esquema WHERE COD_CELDA= ?",
        "DELETE FROM Interruptor_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CELDA = ?",
        "DELETE FROM Seccionador_Central_Generacion WHERE COD_CELDA= ?",
        "DELETE FROM Seccionador_Central_Generacion_Ubicacion_Esquema WHERE COD_CELDA= ?",
        "DELETE FROM Seccionador_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CELDA= ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Interruptor_Central_Generacion(_id):
    conn = create_connection()
    sql = "DELETE FROM Interruptor_Central_Generacion WHERE COD_INTERRUPTOR = ?"
    print("EL ID A ELIMINAR ES: "+str(_id))
    
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book_Seccionador_Central_Generacion(_id):
    conn = create_connection()
    sql = "DELETE FROM Seccionador_Central_Generacion WHERE COD_SECCIONADOR = ?"
    print("EL ID A ELIMINAR ES: "+str(_id))
    
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book_Barra_Central_Generacion(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Barra_Central_Generacion WHERE COD_BARRA = ?",
        "DELETE FROM Barra_Central_Generacion_Ubicacion_Esquema WHERE COD_BARRA = ?",
        "DELETE FROM Barra_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_BARRA = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Portico_Central_Generacion(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Portico_Central_Generacion WHERE COD_PORTICO = ?",
        "DELETE FROM Portico_Central_Generacion_Estructura WHERE COD_PORTICO = ?",
        "DELETE FROM Portico_Central_Generacion_Travesano WHERE COD_PORTICO = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Portico_Central_Generacion_Estructura(_id):
    conn = create_connection()
    sql = "DELETE FROM Portico_Central_Generacion_Estructura WHERE COD_ESTRUCTURA = ?"
    print("EL ID A ELIMINAR ES: "+str(_id))
    
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book_Transformador_Central_Generacion(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Transformador_Central_Generacion WHERE COD_TRANSF = ?",
        "DELETE FROM Transformador_Central_Generacion_Ubicacion_Esquema WHERE COD_TRANSF = ?",
        "DELETE FROM Transformador_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_TRANSF = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Pararrayo_Central_Generacion(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Pararrayo_Central_Generacion WHERE COD_PARARRAYO = ?",
        "DELETE FROM Pararrayo_Central_Generacion_Ubicacion_Esquema WHERE COD_PARARRAYO = ?",
        "DELETE FROM Pararrayo_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_PARARRAYO = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def delete_book_Transformador_Medicion_Central_Generacion(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Transformador_Medicion_Central_Generacion WHERE COD_TRANSF = ?",
        "DELETE FROM Transformador_Medicion_Central_Ubicacion_Esquema WHERE COD_TRANSF = ?",
        "DELETE FROM Transformador_Medicion_Central_Ubicacion_Plano_Planta WHERE COD_TRANSF = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Conductor_Central_Generacion(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Conductor_Central_Generacion WHERE COD_CONDUCTOR = ?",
        "DELETE FROM Conductor_Central_Generacion_Ubicacion_Esquema WHERE COD_CONDUCTOR = ?",
        "DELETE FROM Conductor_Central_Generacion_Ubicacion_Plano_Planta WHERE COD_CONDUCTOR = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Barra(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Barra WHERE COD_BARRA = ?",
        "DELETE FROM Barra_Ubicacion_Esquema WHERE COD_BARRA = ?",
        "DELETE FROM Barra_Ubicacion_Plano_Planta WHERE COD_BARRA = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Portico(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Portico WHERE COD_PORTICO = ?",
        "DELETE FROM Portico_Estructura WHERE COD_PORTICO = ?",
        "DELETE FROM Portico_Travesanio WHERE COD_PORTICO = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Portico_Estructura(_id,_codest):
    conn = create_connection()
    sql = "DELETE FROM Portico_Estructura WHERE COD_PORTICO = ? AND COD_ESTRUCTURA = ?"
    print("EL ID A ELIMINAR ES: "+str(_id))
    
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,_codest))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book_Celda(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Celda WHERE COD_CELDA = ?",
        "DELETE FROM Celda_Ubicacion_Esquema WHERE COD_CELDA = ?",
        "DELETE FROM Celda_Ubicacion_Plano_Planta WHERE COD_CELDA = ?",
        "DELETE FROM Interruptor_Potencia WHERE COD_CELDA = ?",
        "DELETE FROM Interruptor_Potencia_Ubicacion_Esquema WHERE COD_CELDA = ?",
        "DELETE FROM Interruptor_Potencia_Ubicacion_Plano_Planta WHERE COD_CELDA = ?",
        "DELETE FROM Seccionador WHERE COD_CELDA = ?",
        "DELETE FROM Seccionador_Ubicacion_Esquema WHERE COD_CELDA = ?",
        "DELETE FROM Seccionador_Ubicacion_Plano_Planta WHERE COD_CELDA = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Interruptor_Potencia(_id):
    conn = create_connection()
    sql = "DELETE FROM Interruptor_Potencia WHERE COD_INTERRUPTOR = ?"
    print("EL ID A ELIMINAR ES: "+str(_id))
    
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book_Seccionador(_id):
    conn = create_connection()
    sql = "DELETE FROM Seccionador WHERE COD_SECCIONADOR = ?"
    print("EL ID A ELIMINAR ES: "+str(_id))
    
    try:
        cur = conn.cursor()
        cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book_Transformador_Potencia(_id):
    conn = create_connection()
    sql = "DELETE FROM Transformador_Potencia WHERE COD_TRANSF = ?"
    sql_statements = [
        "DELETE FROM Transformador_Potencia_Ubicacion_Esquema WHERE COD_TRANSF = ?",
        "DELETE FROM Transformador_Potencia_Ubicacion_Plano_Planta WHERE COD_TRANSF = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        # Delete from main table
        cur.execute(sql, (_id,))
        
        # Delete from related tables
        for sql_stmt in sql_statements:
            cur.execute(sql_stmt, (_id,))
        
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Pararrayo(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Pararrayo WHERE COD_PARARRAYO = ?",
        "DELETE FROM Pararrayo_Ubicacion_Esquema WHERE COD_PARARRAYO = ?",
        "DELETE FROM Pararrayo_Ubicacion_Plano_Planta WHERE COD_PARARRAYO = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Transformador_Medicion(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Transformador_Medicion WHERE COD_TRANSF = ?",
        "DELETE FROM Transformador_Medicion_Ubicacion_Esquema WHERE COD_TRANSF = ?",
        "DELETE FROM Transformador_Medicion_Ubicacion_Plano_Planta WHERE COD_TRANSF = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Bobina_Bloqueo(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Bobina_Bloqueo WHERE COD_BOBINA = ?",
        "DELETE FROM Bobina_Bloqueo_Ubicacion_Esquema WHERE COD_BOBINA = ?",
        "DELETE FROM Bobina_Bloqueo_Ubicacion_Plano_Planta WHERE COD_BOBINA = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_compensador(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Compensador_Reactivo WHERE COD_COMP = ?",
        "DELETE FROM Compensador_Reactivo_Ubicacion_Esquema WHERE COD_COMP = ?",
        "DELETE FROM Compensador_Reactivo_Ubicacion_Plano_Planta WHERE COD_COMP = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



def delete_book_Conductor(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Conductor WHERE COD_CONDUCTOR = ?",
        "DELETE FROM Conductor_Ubicacion_Esquema WHERE COD_CONDUCTOR = ?",
        "DELETE FROM Conductor_Ubicacion_Plano_Planta WHERE COD_CONDUCTOR = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Tramo_Linea_Transmision(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Tramo_Linea_Transmision WHERE COD_TRAMO = ?",
        "DELETE FROM Tramo_Linea_Vertice_Ubicacion_Geografica WHERE COD_TRAMO = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def delete_book_Estructura(_id):
    conn = create_connection()
    sql_statements = [
        "DELETE FROM Estructura WHERE COD_ESTRUCTURA = ?",
        "DELETE FROM Estructura_Ubicacion_Geografica WHERE COD_ESTRUCTURA = ?",
        "DELETE FROM Estructura_Ubicacion_Plano_Planta_Central_Generacion WHERE COD_ESTRUCTURA = ?",
        "DELETE FROM Estructura_Ubicacion_Plano_Planta_Subestacion WHERE COD_ESTRUCTURA = ?"
    ]

    print("EL ID A ELIMINAR ES: " + str(_id))
    try:
        cur = conn.cursor()
        for sql in sql_statements:
            cur.execute(sql, (_id,))
        conn.commit()
        print("Libro Eliminado")
        return True
    except Error as e:
        print("Error Deleting book: " + str(e))
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

#################################################################################################