#include "producto.h"

//**************  METODOS PRODUCTO ******************//
Producto::Producto()
{
}

//este constructor es para crear cada producto y añadirlo a la lista
Producto::Producto(string marca, string tipoProducto, int codigo, int exs, float valorProducto)
{
    this->marca = marca;
    this->tipoProducto = tipoProducto;
    this->codigoProducto = codigo;
    this->existencia = exs;
    this->valorProducto = valorProducto;
}

void Producto::mostrarProducto()
{

    cout << "==================" << endl;
    cout << "Marca: " << this->marca << endl;
    cout << "Tipo: " << this->tipoProducto << endl;
    cout << "Codigo: " << this->codigoProducto << endl;
    cout << "Existencia: " << this->existencia << endl;
    cout << "Valor producto: " << this->valorProducto << "$" << endl;
}