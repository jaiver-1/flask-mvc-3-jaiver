from flaskr.models import db
from flaskr.models import *

class Categorias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(128), unique=True, nullable=False)
    
def obtener_categorias():
    conexion = obtener_conexion()
    categorias = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, categoria FROM categorias")
        categorias = cursor.fetchall()
    conexion.close()
    return categorias

def crear_categoria(_categoria):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO categorias (categoria) VALUES('{}')"\
            .format(_categoria.categoria)
        cursor.execute(consulta)
        conexion.commit()
    conexion.close()