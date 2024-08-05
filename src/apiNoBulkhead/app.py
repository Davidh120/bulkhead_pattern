from flask import Flask, jsonify, request
from models import inicializar_bd
import services

app = Flask(__name__)

@app.route('/productos', methods=['GET'])
def obtener_productos_endpoint():
    productos = services.obtener_productos()
    return jsonify(productos)

@app.route('/producto/<int:id>', methods=['GET'])
def obtener_producto_endpoint(id):
    producto = services.obtener_producto(id)
    if producto:
        return jsonify(producto)
    else:
        return jsonify({'message': 'Producto no encontrado'}), 404

@app.route('/agregar_producto', methods=['POST'])
def agregar_producto_endpoint():
    data = request.json
    nombre = data.get('nombre')
    precio = data.get('precio')
    producto_id = services.agregar_producto(nombre, precio)
    return jsonify({'message': 'Producto agregado exitosamente', 'producto_id': producto_id})

@app.route('/pago', methods=['POST'])
def realizar_pago_endpoint():
    data = request.json
    producto_id = data.get('producto_id')
    cancelado = data.get('cancelado')
    pago_id = services.realizar_pago(producto_id, cancelado)
    return jsonify({'message': 'Pago registrado exitosamente', 'pago_id': pago_id})

@app.route('/eliminar_producto', methods=['DELETE'])
def eliminar_producto_endpoint():
    data = request.json
    producto_id = data.get('producto_id')
    if services.eliminar_producto(producto_id):
        return jsonify({'message': 'Producto eliminado exitosamente'})
    else:
        return jsonify({'message': 'Producto no encontrado'}), 404

@app.route('/eliminar_todos_productos', methods=['DELETE'])
def eliminar_todos_productos_endpoint():
    services.eliminar_todos_productos()
    return jsonify({'message': 'Todos los productos han sido eliminados'})

@app.route('/pagos', methods=['GET'])
def obtener_pagos_endpoint():
    pagos = services.obtener_pagos()
    return jsonify(pagos)

@app.route('/eliminar_todos_pagos', methods=['DELETE'])
def eliminar_todos_pagos_endpoint():
    services.eliminar_todos_pagos()
    return jsonify({'message': 'Todos los pagos han sido eliminados'})

if __name__ == '__main__':
    # Inicializar la base de datos y poblar con datos de ejemplo
    inicializar_bd()
    app.run(debug=True, port=5001)