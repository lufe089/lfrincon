
#include "tienda.h"

//CONSTRCUTORES TIENDA

Tienda::Tienda()
{
    this->nombre = "La Farra";
    this->nombreDueno = "POO";
    this->setDummyData();
}

void Tienda::setDummyData()
{
    this->listaCliente.push_back(Cliente("Luisa", "lufe089@gmail.com", 1020, "20202"));
    this->listaProductos.push_back(Producto("Pantene", "Shampoo", 01, 10, 8520));
}

//METODOS TIENDA

void Tienda::mostrarTodosProducto()
{

    //  list<Clase_a_recorrer>:: iterator nombre_iterador = nombre_lista_de_Clase.begin(); it != nombre_lista_de_Clase.end(); i++;

    for (list<Producto>::iterator producto = listaProductos.begin(); producto != listaProductos.end(); producto++)
    {
        producto->mostrarProducto();
    }
}

void Tienda::mostrarTodosCliente()
{

    for (list<Cliente>::iterator it = listaCliente.begin(); it != listaCliente.end(); it++)
    {
        it->mostrarCliente();
    }
}

void Tienda::agregarProducto()
{
    string marca, tipoProducto;
    int codigo, existencia;
    float valorProducto;

    cout << "Digite marca: " << endl;
    cin >> marca;

    cout << "Digite tipo del producto: " << endl;
    cin >> tipoProducto;

    cout << "Digite codigo: " << endl;
    cin >> codigo;

    cout << "Digite existencia: " << endl;
    cin >> existencia;

    cout << "Digite valor del producto: " << endl;
    cin >> valorProducto;

    listaProductos.push_back(Producto(marca, tipoProducto, codigo, existencia, valorProducto));
}

void Tienda::vender()
{
    // Se vende hasta que el cajero escriba menos uno

    // Se pide el codigo del producto
    // Se  busca el producto por código
    // Se pregunta cuantos se van a vender de ese producto
    // Verifican que exista el número en el inventario
    // Se calcula el valor total de la venta de ese producto
    // Se agrega a la lista de detalle
    // Se agrega el valor total al gran total
    // Se agrega el valor total del IVA a la suma del IVA
    // Se mofica la existencia del producto ( hacer setExistencia)

    // Una vez terminado de agregar productos
    // Se pide el numero del cliente
    // Se busca el cliente
    // Se calcula la fecha y hora actual
    // Se crea un numero de factua
    // Se asocia la lista del detalle de la factura
    // Se crea el objeto venta, en la lista de ventas de la tienda.  (relación de composicion.)
    cout << "Lo siento no estoy implementado";
}