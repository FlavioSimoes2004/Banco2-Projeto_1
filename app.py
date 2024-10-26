from flask import Flask, render_template, request, jsonify
from json import JSONEncoder
import json
import sys
sys.path.append("./myflask/lib/python3.12/site-packages")
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'administrador'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'Restaurante'

mysql = MySQL(app)

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
app.json_encoder = CustomJSONEncoder
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clientes', methods=['GET'])
def getClientes():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cliente')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/pratos', methods=['GET'])
def getPratos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM prato')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/fornecedores', methods=['GET'])
def getFornecedores():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM fornecedor')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/ingredientes', methods=['GET'])
def getIngredientes():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM ingredientes')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/usos', methods=['GET'])
def getUsos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usos')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/vendas', methods=['GET'])
def getVendas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM venda')
    data = cur.fetchall()
    cur.close()
#    return jsonify(data)
    return json.dumps(data, indent=4, sort_keys=True, default=str)

@app.route('/menosvendido', methods=['get'])
def getMenosVendido():
    cur = mysql.connection.cursor()
    cur.execute("""
                SELECT p.nome, SUM(v.valor) AS valor_total
                FROM venda v
                INNER JOIN prato p ON v.id_prato = p.id
                GROUP BY p.id
                ORDER BY valor_total ASC
                LIMIT 1;

                """)
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/mesesvendas', methods=['get'])
def getMesesVenda():
    cur = mysql.connection.cursor()
    cur.execute("""
                    SET @produto_menos_vendido = (
                    SELECT p.id
                    FROM venda v
                    INNER JOIN prato p ON v.id_prato = p.id
                    GROUP BY p.id
                    ORDER BY SUM(v.valor) ASC
                    LIMIT 1
                )
                """)
    cur.execute("""
                    SELECT 
                    MONTH(v.dia) AS mes,
                    COUNT(*) AS quantidade_vendas
                    FROM venda v
                    WHERE v.id_prato = @produto_menos_vendido
                    GROUP BY MONTH(v.dia)
                    ORDER BY quantidade_vendas DESC, MONTH(v.dia) ASC
                """)
    data = cur.fetchall()
    cur.close()
    return jsonify(data)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

