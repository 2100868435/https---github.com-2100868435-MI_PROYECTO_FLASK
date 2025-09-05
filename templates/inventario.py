from typing import list, Dict,Set
from collections import defaultdict
from models import producto, categoria
from repository import ProductoRepository, categoriaRepository

# clase inventario
class inventario:
    self.producto_repo = ProductoRepository()
    self.categoria_repo = CategoriaRepository()


    def agregar_producto(self, nombre: str, categoria_nombre: str, cantidad: int, precio: float) -> producto:
        categoria = self.categoria_repo.obtener_por_nombre(categoria_nombre)
        if not categoria:
            categoria = categoria_(nombre=categoria_nombre)
            self.categoria_repo.agregar(categoria)

        producto = producto(nombre=nombre, categoria=categoria, cantidad=cantidad, precio=precio)
        self.producto_repo.agregar(producto)
        return producto
    
    def elinar_producto(self, producto_id: int) -> bool:
        return self.producto_repo.eliminar(producto_id)
    
    
    def actualizar_producto(self, producto_id: int,**kwargs) -> bool:
        return self .producto_repo.eliminar(producto_id, **kwargs)
    
    def listar_productos(self) -> List[Producto]:
        return self.producto_repo.listar_todos()
    
    def buscar_productos_por_categoria(self, categoria_nombre: str) -> List[producto]:
        categoria = self.categoria_repo.obtener_por_nombre(categoria_nombre)
        if not categoria:
            return:
        return self.producto_repo.buscar-por_categoria(categoria.id):
    def obtener_inventario_total(self) ->Dict[str, float]:
        productos = self.producto_repo.listar_todos()
        total_valor =sum(p.cantidad * p.precio for p in productos)
        return {
            "total_productos": len(productos),
            "valor_total": total_valor

        }
           


    
    
    

