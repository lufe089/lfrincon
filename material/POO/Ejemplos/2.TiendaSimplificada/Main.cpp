#include <string>
#include <iostream>

// Declaraciones
class Producto
{
private:
    std::string nombre;

public:
    Producto();
    Producto(std::string);
    void mostrarProducto();
};

class Tienda
{
private:
    Producto listaProductos[10];
    std::string nombreDueno;

public:
    Tienda();
    void mostrarTodosProductos();
};

// Implementación métodos de la clase producto
Producto::Producto() {}

Producto::Producto(std::string nombre)
{
    this->nombre = nombre;
}

void Producto::mostrarProducto()
{
    std::cout << "El producto es " << this->nombre;
}

// Implementacion metodos de la tienda
Tienda::Tienda()
{
    this->listaProductos[0] = Producto("producto1");
    this->listaProductos[1] = Producto("producto2");
    std::cout << "Cree la tienda" << std::endl;
}

void Tienda::mostrarTodosProductos()
{

    for (int i = 0; i < 2; i++)
    {
        //Se usa el  método que tiene cada producto para mostrar su informació
        listaProductos[i].mostrarProducto();
    }
}

int main()
{
    // Crear la tienda
    Tienda laFarra;

    //Usar uno de los metodos de la tienda, que permite también luego
    // mostrar los productos
    laFarra.mostrarTodosProductos();
    return 0;
}