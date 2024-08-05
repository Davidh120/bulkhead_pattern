from flask import Flask, jsonify, request
from concurrent.futures import ThreadPoolExecutor
from models import inicializar_bd
import services

app = Flask(__name__)

# Pools separadas por tipo de servicio
executor_get = ThreadPoolExecutor(max_workers=40)  # Ajustar según las necesidades
executor_add = ThreadPoolExecutor(max_workers=40)   # Ajustar según las necesidades
executor_delete = ThreadPoolExecutor(max_workers=40) # Ajustar según las necesidades

@app.route('/productos', methods=['GET'])
def obtener_productos_endpoint():
    future = executor_get.submit(services.obtener_productos)
    return jsonify(future.result())

@app.route('/producto/<int:id>', methods=['GET'])
def obtener_producto_endpoint(id):
    future = executor_get.submit(services.obtener_producto, id)
    result = future.result()
    if result:
        return jsonify(result)
    else:
        return jsonify({'message': 'Producto no encontrado'}), 404

@app.route('/agregar_producto', methods=['POST'])
def agregar_producto_endpoint():
    data = request.json
    nombre = data.get('nombre')
    precio = data.get('precio')
    future = executor_add.submit(services.agregar_producto, nombre, precio)
    producto_id = future.result()
    return jsonify({'message': 'Producto agregado exitosamente', 'producto_id': producto_id})

@app.route('/pago', methods=['POST'])
def realizar_pago_endpoint():
    data = request.json
    producto_id = data.get('producto_id')
    cancelado = data.get('cancelado')
    future = executor_add.submit(services.realizar_pago, producto_id, cancelado)
    pago_id = future.result()
    return jsonify({'message': 'Pago registrado exitosamente', 'pago_id': pago_id})

@app.route('/eliminar_producto', methods=['DELETE'])
def eliminar_producto_endpoint():
    data = request.json
    producto_id = data.get('producto_id')
    future = executor_delete.submit(services.eliminar_producto, producto_id)
    if future.result():
        return jsonify({'message': 'Producto eliminado exitosamente'})
    else:
        return jsonify({'message': 'Producto no encontrado'}), 404

@app.route('/eliminar_todos_productos', methods=['DELETE'])
def eliminar_todos_productos_endpoint():
    future = executor_delete.submit(services.eliminar_todos_productos)
    future.result()
    return jsonify({'message': 'Todos los productos han sido eliminados'})

@app.route('/pagos', methods=['GET'])
def obtener_pagos_endpoint():
    future = executor_get.submit(services.obtener_pagos)
    return jsonify(future.result())

@app.route('/eliminar_todos_pagos', methods=['DELETE'])
def eliminar_todos_pagos_endpoint():
    future = executor_delete.submit(services.eliminar_todos_pagos)
    future.result()
    return jsonify({'message': 'Todos los pagos han sido eliminados'})

if __name__ == '__main__':
    # Inicializar la base de datos y poblar con datos de ejemplo
    inicializar_bd()
    app.run(debug=True, port=5002)