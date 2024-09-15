from sqlite3 import Error
from .connection_temp import create_connection_temp
from xlsxwriter.workbook import Workbook
from datetime import datetime


def update_database(_id):
    conn = create_connection_temp()
    try:
        with conn:
            cursor = conn.cursor()

            queries = [
""" UPDATE Central_Generacion SET TIPO_CENTRAL='H' where TIPO_CENTRAL='Hidroeléctrica';
UPDATE Central_Generacion SET TIPO_CENTRAL='T' where TIPO_CENTRAL='Térmica';
UPDATE Central_Generacion SET TIPO_CENTRAL='E' where TIPO_CENTRAL='Eólica';
UPDATE Central_Generacion SET TIPO_CENTRAL='S' where TIPO_CENTRAL='Solar';
UPDATE Central_Generacion SET TIPO_SISTEMA='I' where TIPO_CENTRAL='Interconectado';
UPDATE Central_Generacion SET TIPO_SISTEMA='A' where TIPO_CENTRAL='Aislado';
UPDATE Central_Generacion SET AREA_OPERATIVA='N' where AREA_OPERATIVA='Norte';
UPDATE Central_Generacion SET AREA_OPERATIVA='C' where AREA_OPERATIVA='Centro';
UPDATE Central_Generacion SET AREA_OPERATIVA='S' where AREA_OPERATIVA='Sur';
UPDATE Central_Generacion SET AREA_OPERATIVA='L' where AREA_OPERATIVA='Lima';
UPDATE Central_Generacion SET REGION_GEOGRAFICA='CO' where REGION_GEOGRAFICA='Costa';
UPDATE Central_Generacion SET REGION_GEOGRAFICA='SI' where REGION_GEOGRAFICA='Sierra';
UPDATE Central_Generacion SET REGION_GEOGRAFICA='SE' where REGION_GEOGRAFICA='Selva';
UPDATE Central_Generacion SET ZONA='U' where ZONA='Urbana';
UPDATE Central_Generacion SET ZONA='R' where ZONA='Rural';
UPDATE Central_Generacion SET ESTADO='N' where ESTADO='Nuevo';
UPDATE Central_Generacion SET ESTADO='E' where ESTADO='Existente';
UPDATE Central_Generacion SET ESTADO='X' where ESTADO='Eliminado';
UPDATE Central_Generacion SET ESTADO='M' where ESTADO='Modificado';
UPDATE Central_Generacion SET ESTADO='P' where ESTADO='Proyectado';""",

"""UPDATE Generador_Central_Generacion SET TIPO_TURBINA='PE' WHERE TIPO_TURBINA='Pelton';
UPDATE Generador_Central_Generacion SET TIPO_TURBINA='FR' WHERE TIPO_TURBINA='Francis';
UPDATE Generador_Central_Generacion SET TIPO_TURBINA='KA' WHERE TIPO_TURBINA='Kaplan';
UPDATE Generador_Central_Generacion SET TIPO_TURBINA='TV' WHERE TIPO_TURBINA='Turbovapor';
UPDATE Generador_Central_Generacion SET TIPO_TURBINA='TG' WHERE TIPO_TURBINA='Turbogas';
UPDATE Generador_Central_Generacion SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Generador_Central_Generacion SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Generador_Central_Generacion SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Generador_Central_Generacion SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Generador_Central_Generacion SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Barra_Central_Generacion SET TIPO_ARREGLO='SB' WHERE TIPO_ARREGLO='Simple Barra';
UPDATE Barra_Central_Generacion SET TIPO_ARREGLO='DB' WHERE TIPO_ARREGLO='Doble Barra';
UPDATE Barra_Central_Generacion SET TIPO_ARREGLO='AN' WHERE TIPO_ARREGLO='Anillo';
UPDATE Barra_Central_Generacion SET TIPO_ARREGLO='IM' WHERE TIPO_ARREGLO='Interruptor y Medio';
UPDATE Barra_Central_Generacion SET TIPO_INSTALACION='I' WHERE TIPO_INSTALACION='Interior';
UPDATE Barra_Central_Generacion SET TIPO_INSTALACION='E' WHERE TIPO_INSTALACION='Exterior';
UPDATE Barra_Central_Generacion SET BARRA_REFERENCIA='S' WHERE BARRA_REFERENCIA='Si';
UPDATE Barra_Central_Generacion SET BARRA_REFERENCIA='N' WHERE BARRA_REFERENCIA='No';
UPDATE Barra_Central_Generacion SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Barra_Central_Generacion SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Barra_Central_Generacion SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Barra_Central_Generacion SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Barra_Central_Generacion SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Celda_Central_Generacion SET TIPO_CELDA='LI' WHERE TIPO_CELDA='LÍNEA';
UPDATE Celda_Central_Generacion SET TIPO_CELDA='TR' WHERE TIPO_CELDA='TRANSFORMACIÓN';
UPDATE Celda_Central_Generacion SET TIPO_CELDA='LT' WHERE TIPO_CELDA='LÍNEA TRANSFORMADOR';
UPDATE Celda_Central_Generacion SET TIPO_CELDA='AC' WHERE TIPO_CELDA='ACOPLAMIENTO';
UPDATE Celda_Central_Generacion SET TIPO_CELDA='LA' WHERE TIPO_CELDA='ACOPLAMIENTO LONGITUDINAL';
UPDATE Celda_Central_Generacion SET TIPO_CELDA='MD' WHERE TIPO_CELDA='MEDICIÓN';
UPDATE Celda_Central_Generacion SET TIPO_CELDA='AL' WHERE TIPO_CELDA='ALIMENTADOR';
UPDATE Celda_Central_Generacion SET TIPO_CELDA='RE' WHERE TIPO_CELDA='REACTOR';
UPDATE Celda_Central_Generacion SET TIPO_CELDA='CV' WHERE TIPO_CELDA='COMPENSADOR SVC';
UPDATE Celda_Central_Generacion SET TIPO_CELDA='CS' WHERE TIPO_CELDA='COMPENSADOR SÍNCRONO';
UPDATE Celda_Central_Generacion SET TIPO_CELDA='CC' WHERE TIPO_CELDA='COMPENSADOR';
UPDATE Celda_Central_Generacion SET TIPO_INSTALACION='I' WHERE TIPO_INSTALACION='Interior';
UPDATE Celda_Central_Generacion SET TIPO_INSTALACION='E' WHERE TIPO_INSTALACION='Exterior';
UPDATE Celda_Central_Generacion SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Celda_Central_Generacion SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Celda_Central_Generacion SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Celda_Central_Generacion SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Celda_Central_Generacion SET ESTADO='P' WHERE ESTADO='Proyectado';""",


"""UPDATE Portico_Central_Generacion SET TIPO='AC' WHERE TIPO='Acero';
UPDATE Portico_Central_Generacion SET TIPO='CO' WHERE TIPO='Concreto';
UPDATE Portico_Central_Generacion SET TIPO='MA' WHERE TIPO='Madera';
UPDATE Portico_Central_Generacion SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Portico_Central_Generacion SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Portico_Central_Generacion SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Portico_Central_Generacion SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Portico_Central_Generacion SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Interruptor_Central_Generacion SET TIPO_INSTALACION='I' WHERE TIPO_INSTALACION='Interior';
UPDATE Interruptor_Central_Generacion SET TIPO_INSTALACION='E' WHERE TIPO_INSTALACION='Exterior';
UPDATE Interruptor_Central_Generacion SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Interruptor_Central_Generacion SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Interruptor_Central_Generacion SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Interruptor_Central_Generacion SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Interruptor_Central_Generacion SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Seccionador_Central_Generacion SET TIPO_SECCIONADOR='AC' WHERE TIPO_SECCIONADOR='Apertura Central';
UPDATE Seccionador_Central_Generacion SET TIPO_SECCIONADOR='RC' WHERE TIPO_SECCIONADOR='Rotación Central';
UPDATE Seccionador_Central_Generacion SET TIPO_SECCIONADOR='AV' WHERE TIPO_SECCIONADOR='Apertura Vertical';
UPDATE Seccionador_Central_Generacion SET TIPO_SECCIONADOR='PA' WHERE TIPO_SECCIONADOR='Pantógrafo';
UPDATE Seccionador_Central_Generacion SET TIPO_SECCIONADOR='SP' WHERE TIPO_SECCIONADOR='Semipantógrafo';
UPDATE Seccionador_Central_Generacion SET TIPO_SECCIONADOR='PH' WHERE TIPO_SECCIONADOR='Pantógrafo Horizontal';
UPDATE Seccionador_Central_Generacion SET TIPO_INSTALACION='I' WHERE TIPO_INSTALACION='Interior';
UPDATE Seccionador_Central_Generacion SET TIPO_INSTALACION='E' WHERE TIPO_INSTALACION='Exterior';
UPDATE Seccionador_Central_Generacion SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Seccionador_Central_Generacion SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Seccionador_Central_Generacion SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Seccionador_Central_Generacion SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Seccionador_Central_Generacion SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Transformador_Central_Generacion SET TIPO_TRANSF='T' WHERE TIPO_TRANSF='Trifásico';
UPDATE Transformador_Central_Generacion SET TIPO_TRANSF='M' WHERE TIPO_TRANSF='Monofásico';
UPDATE Transformador_Central_Generacion SET TIPO_TRANSF='B' WHERE TIPO_TRANSF='Banco';
UPDATE Transformador_Central_Generacion SET TIPO_TRANSF='A' WHERE TIPO_TRANSF='Autotransformador';
UPDATE Transformador_Central_Generacion SET TIPO_TRANSF='Z' WHERE TIPO_TRANSF='Zigzag';
UPDATE Transformador_Central_Generacion SET TIPO_INSTALACION='I' WHERE TIPO_INSTALACION='Interior';
UPDATE Transformador_Central_Generacion SET TIPO_INSTALACION='E' WHERE TIPO_INSTALACION='Exterior';
UPDATE Transformador_Central_Generacion SET DISPONIBILIDAD='O' WHERE DISPONIBILIDAD='Operación';
UPDATE Transformador_Central_Generacion SET DISPONIBILIDAD='R' WHERE DISPONIBILIDAD='Reserva';
UPDATE Transformador_Central_Generacion SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Transformador_Central_Generacion SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Transformador_Central_Generacion SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Transformador_Central_Generacion SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Transformador_Central_Generacion SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Pararrayo_Central_Generacion SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Pararrayo_Central_Generacion SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Pararrayo_Central_Generacion SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Pararrayo_Central_Generacion SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Pararrayo_Central_Generacion SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Transformador_Medicion_Central_Generacion SET TIPO_TRANSF='C' WHERE TIPO_TRANSF='Corriente';
UPDATE Transformador_Medicion_Central_Generacion SET TIPO_TRANSF='T' WHERE TIPO_TRANSF='Tensión';
UPDATE Transformador_Medicion_Central_Generacion SET TIPO_TRANSF='M' WHERE TIPO_TRANSF='Medida Combinado';
UPDATE Transformador_Medicion_Central_Generacion SET TIPO_INSTALACION='I' WHERE TIPO_INSTALACION='Interior';
UPDATE Transformador_Medicion_Central_Generacion SET TIPO_INSTALACION='E' WHERE TIPO_INSTALACION='Exterior';
UPDATE Transformador_Medicion_Central_Generacion SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Transformador_Medicion_Central_Generacion SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Transformador_Medicion_Central_Generacion SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Transformador_Medicion_Central_Generacion SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Transformador_Medicion_Central_Generacion SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Conductor_Central_Generacion SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Conductor_Central_Generacion SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Conductor_Central_Generacion SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Conductor_Central_Generacion SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Conductor_Central_Generacion SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Subestacion SET COD_CALIFICACION='P' WHERE COD_CALIFICACION='Principal';
UPDATE Subestacion SET COD_CALIFICACION='S' WHERE COD_CALIFICACION='Secundario';
UPDATE Subestacion SET COD_CALIFICACION='G' WHERE COD_CALIFICACION='Garantizado';
UPDATE Subestacion SET COD_CALIFICACION='C' WHERE COD_CALIFICACION='Complementario';
UPDATE Subestacion SET TIPO_SISTEMA='I' WHERE TIPO_SISTEMA='Interconectado';
UPDATE Subestacion SET TIPO_SISTEMA='A' WHERE TIPO_SISTEMA='Aislado';
UPDATE Subestacion SET TECNOLOGIA_SE='C1' WHERE TECNOLOGIA_SE='Convencional';
UPDATE Subestacion SET TECNOLOGIA_SE='C2' WHERE TECNOLOGIA_SE='Compacta';
UPDATE Subestacion SET TECNOLOGIA_SE='EN' WHERE TECNOLOGIA_SE='Encapsulada';
UPDATE Subestacion SET TECNOLOGIA_SE='MC' WHERE TECNOLOGIA_SE='Metal Clad';
UPDATE Subestacion SET AREA_OPERATIVA='N' where AREA_OPERATIVA='Norte';
UPDATE Subestacion SET AREA_OPERATIVA='C' where AREA_OPERATIVA='Centro';
UPDATE Subestacion SET AREA_OPERATIVA='S' where AREA_OPERATIVA='Sur';
UPDATE Subestacion SET AREA_OPERATIVA='L' where AREA_OPERATIVA='Lima';
UPDATE Subestacion SET REGION_GEOGRAFICA='CO' where REGION_GEOGRAFICA='Costa';
UPDATE Subestacion SET REGION_GEOGRAFICA='SI' where REGION_GEOGRAFICA='Sierra';
UPDATE Subestacion SET REGION_GEOGRAFICA='SE' where REGION_GEOGRAFICA='Selva';
UPDATE Subestacion SET ZONA='U' where ZONA='Urbana';
UPDATE Subestacion SET ZONA='R' where ZONA='Rural';
UPDATE Subestacion SET FUNCION='T' WHERE FUNCION='Transformación';
UPDATE Subestacion SET FUNCION='S' WHERE FUNCION='Seccionamiento';
UPDATE Subestacion SET ATENDIDA='S' WHERE ATENDIDA='Si';
UPDATE Subestacion SET ATENDIDA='N' WHERE ATENDIDA='No';
UPDATE Subestacion SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Subestacion SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Subestacion SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Subestacion SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Subestacion SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Barra SET TIPO_BARRA='F' WHERE TIPO_BARRA='Flexible';
UPDATE Barra SET TIPO_BARRA='R' WHERE TIPO_BARRA='Rígido';
UPDATE Barra SET COD_CALIFICACION='P' WHERE COD_CALIFICACION='Principal';
UPDATE Barra SET COD_CALIFICACION='S' WHERE COD_CALIFICACION='Secundario';
UPDATE Barra SET COD_CALIFICACION='G' WHERE COD_CALIFICACION='Garantizado';
UPDATE Barra SET COD_CALIFICACION='C' WHERE COD_CALIFICACION='Complementario';
UPDATE Barra SET BARRA_REFERENCIA='S' WHERE BARRA_REFERENCIA='Si';
UPDATE Barra SET BARRA_REFERENCIA='N' WHERE BARRA_REFERENCIA='No';
UPDATE Barra SET TIPO_ARREGLO='SB' WHERE TIPO_ARREGLO='Simple Barra';
UPDATE Barra SET TIPO_ARREGLO='DB' WHERE TIPO_ARREGLO='Doble Barra';
UPDATE Barra SET TIPO_ARREGLO='AN' WHERE TIPO_ARREGLO='Anillo';
UPDATE Barra SET TIPO_ARREGLO='IM' WHERE TIPO_ARREGLO='Interruptor y Medio';
UPDATE Barra SET TIPO_INSTALACION='I' WHERE TIPO_INSTALACION='Interior';
UPDATE Barra SET TIPO_INSTALACION='E' WHERE TIPO_INSTALACION='Exterior';
UPDATE Barra SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Barra SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Barra SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Barra SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Barra SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Portico SET COD_CALIFICACION='P' WHERE COD_CALIFICACION='Principal';
UPDATE Portico SET COD_CALIFICACION='S' WHERE COD_CALIFICACION='Secundario';
UPDATE Portico SET COD_CALIFICACION='G' WHERE COD_CALIFICACION='Garantizado';
UPDATE Portico SET COD_CALIFICACION='C' WHERE COD_CALIFICACION='Complementario';
UPDATE Portico SET TIPO='AC' WHERE TIPO='Acero';
UPDATE Portico SET TIPO='MA' WHERE TIPO='Madera';
UPDATE Portico SET TIPO='CO' WHERE TIPO='Concreto';
UPDATE Portico SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Portico SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Portico SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Portico SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Portico SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Celda SET COD_CALIFICACION='P' WHERE COD_CALIFICACION='Principal';
UPDATE Celda SET COD_CALIFICACION='S' WHERE COD_CALIFICACION='Secundario';
UPDATE Celda SET COD_CALIFICACION='G' WHERE COD_CALIFICACION='Garantizado';
UPDATE Celda SET COD_CALIFICACION='C' WHERE COD_CALIFICACION='Complementario';
UPDATE Celda SET TIPO_CELDA='LI' WHERE TIPO_CELDA='LÍNEA';
UPDATE Celda SET TIPO_CELDA='TR' WHERE TIPO_CELDA='TRANSFORMACIÓN';
UPDATE Celda SET TIPO_CELDA='LT' WHERE TIPO_CELDA='LÍNEA TRANSFORMADOR';
UPDATE Celda SET TIPO_CELDA='AC' WHERE TIPO_CELDA='ACOPLAMIENTO';
UPDATE Celda SET TIPO_CELDA='LA' WHERE TIPO_CELDA='ACOPLAMIENTO LONGITUDINAL';
UPDATE Celda SET TIPO_CELDA='MD' WHERE TIPO_CELDA='MEDICIÓN';
UPDATE Celda SET TIPO_CELDA='AL' WHERE TIPO_CELDA='ALIMENTADOR';
UPDATE Celda SET TIPO_CELDA='RE' WHERE TIPO_CELDA='REACTOR';
UPDATE Celda SET TIPO_CELDA='CV' WHERE TIPO_CELDA='COMPENSADOR SVC';
UPDATE Celda SET TIPO_CELDA='CS' WHERE TIPO_CELDA='COMPENSADOR SÍNCRONO';
UPDATE Celda SET TIPO_CELDA='CC' WHERE TIPO_CELDA='COMPENSADOR';
UPDATE Celda SET TIPO_INSTALACION='I' WHERE TIPO_INSTALACION='Interior';
UPDATE Celda SET TIPO_INSTALACION='E' WHERE TIPO_INSTALACION='Exterior';
UPDATE Celda SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Celda SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Celda SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Celda SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Celda SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Transformador_Potencia SET COD_CALIFICACION='P' WHERE COD_CALIFICACION='Principal';
UPDATE Transformador_Potencia SET COD_CALIFICACION='S' WHERE COD_CALIFICACION='Secundario';
UPDATE Transformador_Potencia SET COD_CALIFICACION='G' WHERE COD_CALIFICACION='Garantizado';
UPDATE Transformador_Potencia SET COD_CALIFICACION='C' WHERE COD_CALIFICACION='Complementario';
UPDATE Transformador_Potencia SET TIPO_TRANSF='T' WHERE TIPO_TRANSF='Trifásico';
UPDATE Transformador_Potencia SET TIPO_TRANSF='M' WHERE TIPO_TRANSF='Monofásico';
UPDATE Transformador_Potencia SET TIPO_TRANSF='B' WHERE TIPO_TRANSF='Banco';
UPDATE Transformador_Potencia SET TIPO_TRANSF='A' WHERE TIPO_TRANSF='Autotransformador';
UPDATE Transformador_Potencia SET TIPO_TRANSF='Z' WHERE TIPO_TRANSF='Zigzag';
UPDATE Transformador_Potencia SET TIPO_INSTALACION='I' WHERE TIPO_INSTALACION='Interior';
UPDATE Transformador_Potencia SET TIPO_INSTALACION='E' WHERE TIPO_INSTALACION='Exterior';
UPDATE Transformador_Potencia SET DISPONIBILIDAD='O' WHERE DISPONIBILIDAD='Operación';
UPDATE Transformador_Potencia SET DISPONIBILIDAD='R' WHERE DISPONIBILIDAD='Reserva';
UPDATE Transformador_Potencia SET REGULA_TEN_TIPO='M' WHERE REGULA_TEN_TIPO='Manual';
UPDATE Transformador_Potencia SET REGULA_TEN_TIPO='A' WHERE REGULA_TEN_TIPO='Automático';
UPDATE Transformador_Potencia SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Transformador_Potencia SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Transformador_Potencia SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Transformador_Potencia SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Transformador_Potencia SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Interruptor_Potencia SET COD_CALIFICACION='P' WHERE COD_CALIFICACION='Principal';
UPDATE Interruptor_Potencia SET COD_CALIFICACION='S' WHERE COD_CALIFICACION='Secundario';
UPDATE Interruptor_Potencia SET COD_CALIFICACION='G' WHERE COD_CALIFICACION='Garantizado';
UPDATE Interruptor_Potencia SET COD_CALIFICACION='C' WHERE COD_CALIFICACION='Complementario';
UPDATE Interruptor_Potencia SET TIPO_INSTALACION='I' WHERE TIPO_INSTALACION='Interior';
UPDATE Interruptor_Potencia SET TIPO_INSTALACION='E' WHERE TIPO_INSTALACION='Exterior';
UPDATE Interruptor_Potencia SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Interruptor_Potencia SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Interruptor_Potencia SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Interruptor_Potencia SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Interruptor_Potencia SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Seccionador SET COD_CALIFICACION='P' WHERE COD_CALIFICACION='Principal';
UPDATE Seccionador SET COD_CALIFICACION='S' WHERE COD_CALIFICACION='Secundario';
UPDATE Seccionador SET COD_CALIFICACION='G' WHERE COD_CALIFICACION='Garantizado';
UPDATE Seccionador SET COD_CALIFICACION='C' WHERE COD_CALIFICACION='Complementario';
UPDATE Seccionador SET TIPO_SECCIONADOR='AC' WHERE TIPO_SECCIONADOR='Apertura Central';
UPDATE Seccionador SET TIPO_SECCIONADOR='RC' WHERE TIPO_SECCIONADOR='Rotación Central';
UPDATE Seccionador SET TIPO_SECCIONADOR='AV' WHERE TIPO_SECCIONADOR='Apertura Vertical';
UPDATE Seccionador SET TIPO_SECCIONADOR='PA' WHERE TIPO_SECCIONADOR='Pantógrafo';
UPDATE Seccionador SET TIPO_SECCIONADOR='SP' WHERE TIPO_SECCIONADOR='Semipantógrafo';
UPDATE Seccionador SET TIPO_SECCIONADOR='PH' WHERE TIPO_SECCIONADOR='Pantógrafo Horizontal';
UPDATE Seccionador SET TIPO_INSTALACION='I' WHERE TIPO_INSTALACION='Interior';
UPDATE Seccionador SET TIPO_INSTALACION='E' WHERE TIPO_INSTALACION='Exterior';
UPDATE Seccionador SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Seccionador SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Seccionador SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Seccionador SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Seccionador SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Pararrayo SET COD_CALIFICACION='P' WHERE COD_CALIFICACION='Principal';
UPDATE Pararrayo SET COD_CALIFICACION='S' WHERE COD_CALIFICACION='Secundario';
UPDATE Pararrayo SET COD_CALIFICACION='G' WHERE COD_CALIFICACION='Garantizado';
UPDATE Pararrayo SET COD_CALIFICACION='C' WHERE COD_CALIFICACION='Complementario';
UPDATE Pararrayo SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Pararrayo SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Pararrayo SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Pararrayo SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Pararrayo SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Transformador_Medicion SET COD_CALIFICACION='P' WHERE COD_CALIFICACION='Principal';
UPDATE Transformador_Medicion SET COD_CALIFICACION='S' WHERE COD_CALIFICACION='Secundario';
UPDATE Transformador_Medicion SET COD_CALIFICACION='G' WHERE COD_CALIFICACION='Garantizado';
UPDATE Transformador_Medicion SET COD_CALIFICACION='C' WHERE COD_CALIFICACION='Complementario';
UPDATE Transformador_Medicion SET TIPO_TRANSF='C' WHERE TIPO_TRANSF='Corriente';
UPDATE Transformador_Medicion SET TIPO_TRANSF='T' WHERE TIPO_TRANSF='Tensión';
UPDATE Transformador_Medicion SET TIPO_TRANSF='M' WHERE TIPO_TRANSF='Medida Combinado';
UPDATE Transformador_Medicion SET TIPO_INSTALACION='I' WHERE TIPO_INSTALACION='Interior';
UPDATE Transformador_Medicion SET TIPO_INSTALACION='E' WHERE TIPO_INSTALACION='Exterior';
UPDATE Transformador_Medicion SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Transformador_Medicion SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Transformador_Medicion SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Transformador_Medicion SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Transformador_Medicion SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Bobina_Bloqueo SET COD_CALIFICACION='P' WHERE COD_CALIFICACION='Principal';
UPDATE Bobina_Bloqueo SET COD_CALIFICACION='S' WHERE COD_CALIFICACION='Secundario';
UPDATE Bobina_Bloqueo SET COD_CALIFICACION='G' WHERE COD_CALIFICACION='Garantizado';
UPDATE Bobina_Bloqueo SET COD_CALIFICACION='C' WHERE COD_CALIFICACION='Complementario';
UPDATE Bobina_Bloqueo SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Bobina_Bloqueo SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Bobina_Bloqueo SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Bobina_Bloqueo SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Bobina_Bloqueo SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Conductor SET COD_CALIFICACION='P' WHERE COD_CALIFICACION='Principal';
UPDATE Conductor SET COD_CALIFICACION='S' WHERE COD_CALIFICACION='Secundario';
UPDATE Conductor SET COD_CALIFICACION='G' WHERE COD_CALIFICACION='Garantizado';
UPDATE Conductor SET COD_CALIFICACION='C' WHERE COD_CALIFICACION='Complementario';
UPDATE Conductor SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Conductor SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Conductor SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Conductor SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Conductor SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Compensador_Reactivo SET COD_CALIFICACION='P' WHERE COD_CALIFICACION='Principal';
UPDATE Compensador_Reactivo SET COD_CALIFICACION='S' WHERE COD_CALIFICACION='Secundario';
UPDATE Compensador_Reactivo SET COD_CALIFICACION='G' WHERE COD_CALIFICACION='Garantizado';
UPDATE Compensador_Reactivo SET COD_CALIFICACION='C' WHERE COD_CALIFICACION='Complementario';
UPDATE Compensador_Reactivo SET TIPO_COMP='BP' WHERE TIPO_COMP='Banco Capacitivo';
UPDATE Compensador_Reactivo SET TIPO_COMP='BS' WHERE TIPO_COMP='Compensador Serie';
UPDATE Compensador_Reactivo SET TIPO_COMP='SV' WHERE TIPO_COMP='SVC';
UPDATE Compensador_Reactivo SET TIPO_COMP='RE' WHERE TIPO_COMP='Reactor';
UPDATE Compensador_Reactivo SET TIPO_COMP='CS' WHERE TIPO_COMP='Compensador Sincrono';
UPDATE Compensador_Reactivo SET TIPO_INSTALACION='I' WHERE TIPO_INSTALACION='Interior';
UPDATE Compensador_Reactivo SET TIPO_INSTALACION='E' WHERE TIPO_INSTALACION='Exterior';
UPDATE Compensador_Reactivo SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Compensador_Reactivo SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Compensador_Reactivo SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Compensador_Reactivo SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Compensador_Reactivo SET ESTADO='P' WHERE ESTADO='Proyectado';""",

"""UPDATE Linea_Transmision SET TIPO_SISTEMA='I' WHERE TIPO_SISTEMA='Interconectado';-------------
UPDATE Linea_Transmision SET TIPO_SISTEMA='A' WHERE TIPO_SISTEMA='Aislado';
UPDATE Tramo_Linea_Transmision SET TIPO_CIRCUITO='D' WHERE TIPO_CIRCUITO='Derivación';
UPDATE Tramo_Linea_Transmision SET TIPO_CIRCUITO='T' WHERE TIPO_CIRCUITO='Troncal';
UPDATE Tramo_Linea_Transmision SET AREA_OPERATIVA='N' WHERE AREA_OPERATIVA='Norte';
UPDATE Tramo_Linea_Transmision SET AREA_OPERATIVA='C' WHERE AREA_OPERATIVA='Centro';
UPDATE Tramo_Linea_Transmision SET AREA_OPERATIVA='S' WHERE AREA_OPERATIVA='Sur';
UPDATE Tramo_Linea_Transmision SET AREA_OPERATIVA='L' WHERE AREA_OPERATIVA='Lima';
UPDATE Tramo_Linea_Transmision SET REGION_GEOGRAFICA='CO' WHERE REGION_GEOGRAFICA='Costa';
UPDATE Tramo_Linea_Transmision SET REGION_GEOGRAFICA='SI' WHERE REGION_GEOGRAFICA='Sierra';
UPDATE Tramo_Linea_Transmision SET REGION_GEOGRAFICA='SE' WHERE REGION_GEOGRAFICA='Selva';
UPDATE Tramo_Linea_Transmision SET ZONA='U' WHERE ZONA='Urbana';
UPDATE Tramo_Linea_Transmision SET ZONA='R' WHERE ZONA='Rural';
UPDATE Tramo_Linea_Transmision SET TIPO_RED='A' WHERE TIPO_RED='Aéreo';
UPDATE Tramo_Linea_Transmision SET TIPO_RED='S' WHERE TIPO_RED='Subterráneo';
UPDATE Tramo_Linea_Transmision SET DISPOSICION_FASES='V' WHERE DISPOSICION_FASES='Vertical';
UPDATE Tramo_Linea_Transmision SET DISPOSICION_FASES='H' WHERE DISPOSICION_FASES='Horizontal';
UPDATE Tramo_Linea_Transmision SET DISPOSICION_FASES='T' WHERE DISPOSICION_FASES='Triangular';
UPDATE Tramo_Linea_Transmision SET NUM_CABLE_GUARDA='0' WHERE NUM_CABLE_GUARDA='Ninguno';
UPDATE Tramo_Linea_Transmision SET NUM_CABLE_GUARDA='1' WHERE NUM_CABLE_GUARDA='Uno';
UPDATE Tramo_Linea_Transmision SET NUM_CABLE_GUARDA='2' WHERE NUM_CABLE_GUARDA='Dos';
UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='AAAC' WHERE TIPO_CONDUCTOR='AAAC';
UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='ACSR' WHERE TIPO_CONDUCTOR='ACSR';
UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='ACAR' WHERE TIPO_CONDUCTOR='ACAR';
UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='AAACE' WHERE TIPO_CONDUCTOR='AAACE';
UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='AASC' WHERE TIPO_CONDUCTOR='AASC';
UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='ALDREY' WHERE TIPO_CONDUCTOR='ALDREY';
UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='ALMELEC' WHERE TIPO_CONDUCTOR='ALMELEC';
UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='CU' WHERE TIPO_CONDUCTOR='Cable de Cobre';
UPDATE Tramo_Linea_Transmision SET TIPO_CONDUCTOR='AL' WHERE TIPO_CONDUCTOR='Cable de Aluminio';
UPDATE Tramo_Linea_Transmision SET MAT_CABLE_GUARDA='AG' WHERE MAT_CABLE_GUARDA='Acero Galvanizado';
UPDATE Tramo_Linea_Transmision SET MAT_CABLE_GUARDA='AW' WHERE MAT_CABLE_GUARDA='Alumoweld (Acero aleado con aluminio)';
UPDATE Tramo_Linea_Transmision SET MAT_CABLE_GUARDA='AA' WHERE MAT_CABLE_GUARDA='Aleación de Aluminio';
UPDATE Tramo_Linea_Transmision SET MAT_CABLE_GUARDA='AR' WHERE MAT_CABLE_GUARDA='Aluminio con Acero reforzado';
UPDATE Tramo_Linea_Transmision SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Tramo_Linea_Transmision SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Tramo_Linea_Transmision SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Tramo_Linea_Transmision SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Tramo_Linea_Transmision SET ESTADO='P' WHERE ESTADO='Proyectado';
UPDATE Tramo_Linea_Transmision SET COD_CALIFICACION='P' WHERE COD_CALIFICACION='Principal';
UPDATE Tramo_Linea_Transmision SET COD_CALIFICACION='S' WHERE COD_CALIFICACION='Secundario';
UPDATE Tramo_Linea_Transmision SET COD_CALIFICACION='G' WHERE COD_CALIFICACION='Garantizado';
UPDATE Tramo_Linea_Transmision SET COD_CALIFICACION='C' WHERE COD_CALIFICACION='Complementario';""",

"""UPDATE Estructura SET TIPO='AC' WHERE TIPO='Postes de Concreto y Acero';
UPDATE Estructura SET TIPO='PC' WHERE TIPO='Postes de Concreto';
UPDATE Estructura SET TIPO='PM' WHERE TIPO='Postes de Madera';
UPDATE Estructura SET TIPO='TA' WHERE TIPO='Torresde Acero';
UPDATE Estructura SET TIPO='PA' WHERE TIPO='Postes de Acero';
UPDATE Estructura SET TIPO='AM' WHERE TIPO='Postes de Madera y Acero';
UPDATE Estructura SET TIPO='SS' WHERE TIPO='Instalación Subterránea';
UPDATE Estructura SET TIPO='SE' WHERE TIPO='Sin Estructura o Red Compartida';
UPDATE Estructura SET COD_CALIFICACION='P' WHERE COD_CALIFICACION='Principal';
UPDATE Estructura SET COD_CALIFICACION='S' WHERE COD_CALIFICACION='Secundario';
UPDATE Estructura SET COD_CALIFICACION='G' WHERE COD_CALIFICACION='Garantizado';
UPDATE Estructura SET COD_CALIFICACION='C' WHERE COD_CALIFICACION='Complementario';
UPDATE Estructura SET FUNCION='S' WHERE FUNCION='Suspensión';
UPDATE Estructura SET FUNCION='A' WHERE FUNCION='Angulo';
UPDATE Estructura SET FUNCION='R' WHERE FUNCION='Retención Intermedia';
UPDATE Estructura SET FUNCION='T' WHERE FUNCION='Terminal';
UPDATE Estructura SET FUNCION='TR' WHERE FUNCION='Transposición';
UPDATE Estructura SET FUNCION='D' WHERE FUNCION='Derivación';
UPDATE Estructura SET NUM_CIRCUITOS='1' WHERE NUM_CIRCUITOS='Un Circuito';
UPDATE Estructura SET NUM_CIRCUITOS='2' WHERE NUM_CIRCUITOS='Dos Circuitos';
UPDATE Estructura SET NUM_CIRCUITOS='3' WHERE NUM_CIRCUITOS='Tres Circuitos';
UPDATE Estructura SET NUM_CABLE_GUARDA='0' WHERE NUM_CABLE_GUARDA='Ninguno';
UPDATE Estructura SET NUM_CABLE_GUARDA='1' WHERE NUM_CABLE_GUARDA='Uno';
UPDATE Estructura SET NUM_CABLE_GUARDA='2' WHERE NUM_CABLE_GUARDA='Dos';
UPDATE Estructura SET ESTADO='N' WHERE ESTADO='Nuevo';
UPDATE Estructura SET ESTADO='E' WHERE ESTADO='Existente';
UPDATE Estructura SET ESTADO='X' WHERE ESTADO='Eliminado';
UPDATE Estructura SET ESTADO='M' WHERE ESTADO='Modificado';
UPDATE Estructura SET ESTADO='P' WHERE ESTADO='Proyectado';
UPDATE Estructura SET FORMACION_FASE='1' WHERE FORMACION_FASE='Simple';
UPDATE Estructura SET FORMACION_FASE='2' WHERE FORMACION_FASE='Duplex';
UPDATE Estructura SET FORMACION_FASE='3' WHERE FORMACION_FASE='Triplex';
UPDATE Estructura SET FORMACION_FASE='4' WHERE FORMACION_FASE='Cuádruplex';


    """
 ]

            for query in queries:
                cursor.executescript(query)

    except Error as e:
        print(f"Error {e.args[0]} occurred")
    finally:
        if conn:
            conn.close()
