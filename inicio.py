from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/inicio')
def inicio():
    return render_template("inicio.html")

@app.route('/RT')
def RT():
    return render_template("RT.html")

@app.route('/agragar')
def contacto():
    return render_template("agragar.html")

@app.route('/IND')
def a():
    return render_template("IND.html")

@app.route('/compra')
def compra():
    return render_template("compra.html")

@app.route('/tabla')
def tabla():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='pro2')
    cursor=conn.cursor()
    cursor.execute('select id,product,numero,Descripcion,Precio,Liga from producto order by id')
    datos=cursor.fetchall()
    return render_template("tabla.html",comentarios = datos)

@app.route('/producto')
def producto():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='pro2')
    cursor=conn.cursor()
    cursor.execute('select id,product,numero,Descripcion,Precio,Liga from producto')
    datos = cursor.fetchall()
    return render_template("producto.html",comentar=datos)

@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_nombre = request.form['nombre']
        aux_contraseña = request.form['contraseña']
        aux_telefono = request.form['telefono']
        aux_direcion = request.form['direcion']
        aux_usuario = request.form['usuario']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='pro2' )
        cursor = conn.cursor()
        cursor.execute('insert into usuario (nombre,contraseña,telefono,direcion,usuario,Rango) values (%s,%s,%s,%s,%s,%s)',
                       (aux_nombre, aux_contraseña,aux_telefono,aux_direcion,aux_usuario,"Usuario"))
        conn.commit()
        return redirect(url_for('home'))

@app.route('/agrega_pro', methods=['POST'])
def agrega_pro():
    if request.method == 'POST':
        aux_product = request.form['product']
        aux_numero = request.form['numero']
        aux_Descripcion = request.form['Descripcion']
        aux_Precio = request.form['Precio']
        aux_Liga = request.form['Liga']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='pro2' )
        cursor = conn.cursor()
        cursor.execute('insert into producto (product,numero,Descripcion,Precio,Liga) values (%s,%s,%s,%s,%s)',
                       (aux_product, aux_numero,aux_Descripcion,aux_Precio,aux_Liga))
        conn.commit()
        return redirect(url_for('tabla'))
        
@app.route('/borrar/<string:id>')
def borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='pro2')
    cursor = conn.cursor()
    cursor.execute('delete from producto where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('tabla'))

@app.route('/editar_ta/<string:id>',methods=['POST'])
def editar_ta(id):
    if request.method == 'POST':
        product = request.form['product']
        numero = request.form['numero']
        Descripcion = request.form['Descripcion']
        Precio = request.form['Precio']
        Liga = request.form['Liga']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='pro2')
        cursor=conn.cursor()
        cursor.execute('update producto set product=%s,numero=%s,Descripcion=%s,Precio=%s,Liga=%s where id=%s',
                       (product,numero,Descripcion,Precio,Liga,id))
        conn.commit()
        return redirect(url_for('tabla'))

@app.route("/tala",methods=['POST'])
def la():
    if request.method =='POST':
        nombre=request.form['usuario']
        contraseña=request.form['contraseña']
        conn=pymysql.connect(host='localhost',user='root',passwd='',db='pro2')
        cursor=conn.cursor()
        if(cursor.execute('select usuario,contraseña from usuario where usuario =%s and contraseña =%s',(nombre,contraseña))):
            conn.commit()
            if(cursor.execute('Select usuario,Rango from usuario where Rango="Administrador" and usuario=%s',(nombre))):
                conn.commit()
                return redirect(url_for('inicio'))
            else:
                return redirect(url_for('home'))
        else:
            conn.commit()
            return render_template("IND.html",comentarios='Tu correo esta mal o tu contraseña')

        
@app.route('/editar/<string:id>')
def editar(id):
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='pro2')
        cursor=conn.cursor()
        cursor.execute('select id,product,numero,Descripcion,Precio,Liga from producto where id=%s',(id))
        datos = cursor.fetchall()
        return render_template("editar.html",comentar=datos[0])

@app.route('/insert', methods=['POST'])
def insert():
    data = request.form
    image = data.get('image')
    title = data.get('title')
    price = data.get('price')
    amount = data.get('amount')
    total_card = data.get('priceTotal')
    count_product = data.get('amountProduct')
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='pro2')
    cursor=conn.cursor()
    cursor.execute('INSERT INTO compra(image, title, price, amount, total_card, count_product) VALUES( %s, %s, %s, %s, %s, %s)'
                   ,(image,title,price,amount,total_card,count_product ))
    conn.commit()
    return redirect(url_for('home'))

            
if __name__ == "__main__":
    app.run(debug=True)

