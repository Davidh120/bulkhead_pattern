from models import session, Producto, Pago

def obtener_productos():
    productos = session.query(Producto).all()
    return [{'id': p.id, 'nombre': p.nombre, 'precio': p.precio} for p in productos]

def obtener_producto(id):
    producto = session.query(Producto).filter_by(id=id).first()
    if producto:
        return {'id': producto.id, 'nombre': producto.nombre, 'precio': producto.precio}
    else:
        return None

def agregar_producto(nombre, precio):
    nuevo_producto = Producto(nombre=nombre, precio=precio)
    session.add(nuevo_producto)
    session.commit()
    return nuevo_producto.id

def realizar_pago(producto_id, cancelado):
    pago = Pago(producto_id=producto_id, cancelado=cancelado)
    session.add(pago)
    session.commit()
    return pago.id

def eliminar_producto(producto_id):
    producto = session.query(Producto).filter_by(id=producto_id).first()
    if producto:
        session.delete(producto)
        session.commit()
        return True
    else:
        return False

def eliminar_todos_productos():
    session.query(Producto).delete()
    session.commit()

def obtener_pagos():
    pagos = session.query(Pago).all()
    return [{'id': p.id, 'producto_id': p.producto_id, 'cancelado': p.cancelado} for p in pagos]

def eliminar_todos_pagos():
    session.query(Pago).delete()
    session.commit()