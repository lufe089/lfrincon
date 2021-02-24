#include <iostream>

class Rectangulo
{
private:
    // Pepito es una variable que estoy usando de ejemplo para demostrar que puedo tener
    // tantas variables como necesite como parte de las varibles de instancia
    float largo, ancho, pepito; // variables de instancia o atributos de instancia

public:
    Rectangulo(float, float); //Constructor
    Rectangulo(float, float, float);
    void calcularPerimetro();
    void calcularArea();
    float getLargo();     // Me permite ver el largo de un rectangulo
    void setLargo(float); // Me permite cambiar el valor del largo.
};

/*
// Asi se usa cuando cambio el nombre e las variables en los parámetros
Rectangulo::Rectangulo(float largo1, float ancho1)
{
    // Inicializar las varibles de instancia.
    //Todo lo que tenga que inicializar
    largo = largo1;
    ancho = ancho1;
    std::cout << "Entre y me cree" << std::endl;
}*/

// Versión favorita :), usa el operador this para diferenciar las
// variables de instancia de las variables locales que tienen el mismo nombre
Rectangulo::Rectangulo(float largo, float ancho)
{
    // Inicializar las varibles de instancia.
    //Todo lo que tenga que inicializar
    this->largo = largo;
    this->ancho = ancho;
    std::cout << "Entre y me cree" << std::endl;
}

// Ejemplo de constructor con tres arametros. Busca ilustrar qe puedo tener varios contructores
// si cambio el número de parametros o el tipo de datos entre los parametros
Rectangulo::Rectangulo(float largo, float ancho, float pepito)
{
    // Inicializar las varibles de instancia.
    //Todo lo que tenga que inicializar
    this->largo = largo;
    this->ancho = ancho;
    this->pepito = pepito;
    std::cout << "Entre y me cree" << std::endl
              << "el valor de pepito es " << pepito;
}

// TO-DO pedir los datos al usuario.

void Rectangulo::setLargo(float largo)
{
    this->largo = largo;
}

float Rectangulo::getLargo()
{
    return this->largo;
}

void Rectangulo::calcularPerimetro()
{
    float perimetro; // variable local
    perimetro = (2 * largo) + (2 * ancho);
    pepito++;
    std::cout << "El perimetro es: " << perimetro << std::endl;
}

void Rectangulo::calcularArea()
{
    float area;           // variable local
    area = largo * ancho; // son variables de instancia
    std::cout << "El area es: " << area << std::endl;
}

int main()
{
    //Instanciar --> crear objetos de una clase
    int valor;

    ///Mi primer objeto
    Rectangulo miRectangulo(2, 2); // sobrecarga....
    //calculo el area
    miRectangulo.calcularArea();

    // Cambio el largo a otro valor
    miRectangulo.setLargo(50);

    // Calculo el área
    miRectangulo.calcularArea();

    std::cout << "El largo es " << miRectangulo.getLargo();

    // std::cout << "Con el nuevo objeto, miren pues cambian los valores" << std::endl;
    Rectangulo miRectanguloNuevo(1, 5);
    miRectanguloNuevo.calcularArea();
    //calcular el perimetro
    //miRectangulo.calcularPerimetro();

    // Mi segundo objeto
    Rectangulo miRectangulo1(3, 3, 3);
    return 0;
}
