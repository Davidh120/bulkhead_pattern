from locust import HttpUser, TaskSet, task, between

class MyTaskSet(TaskSet):

    @task
    def obtener_productos(self):
        self.client.get("/productos")
    
    @task
    def obtener_producto(self):
        self.client.get("/producto/1")

    @task
    def agregar_producto(self):
        self.client.post("/agregar_producto", json={"nombre": "Producto de prueba", "precio": 123})
    
    @task
    def realizar_pago(self):
        self.client.post("/pago", json={"producto_id": 1, "cancelado": True})
    
    @task
    def eliminar_producto(self):
        self.client.delete("/eliminar_producto", json={"producto_id": 1})

    @task
    def eliminar_todos_productos(self):
        self.client.delete("/eliminar_todos_productos")

    @task
    def obtener_pagos(self):
        self.client.get("/pagos")

    @task
    def eliminar_todos_pagos(self):
        self.client.delete("/eliminar_todos_pagos")

class MyUser(HttpUser):
    tasks = [MyTaskSet]
    wait_time = between(1, 5)