
from hashlib import new
from flask_controller import FlaskController
from flaskr.app import app
from flask import render_template
from flaskr.models import db, categorias, productos, facturas, facturas_productos
from flask import request, redirect, url_for, flash

class CategoriasController(FlaskController):   
    @app.route("/categorias")
    def categorias():
        resultcategorias = categorias.obtener_categorias()
        ##resultcategorias = categorias.obtener_categorias()
        return render_template('categorias.html', titulo='Gestión de categorias', lista_categorias=resultcategorias)
    
    @app.route("/crear_categoria", methods=['GET','POST'])
    def crear_categoria():
        if request.method == 'POST':
            categoria = request.form.get('categoria')
           
            if not categoria:
                flash('La Categoria es un campo obligatorio')   
            else:          
                categoria = categorias.Categorias(categoria)
                categorias.crear_categoria(categoria=categoria)
                return redirect(url_for('categorias'))
        return render_template('crear_categoria.html', titulo='Nueva categoria')
    
    
    
