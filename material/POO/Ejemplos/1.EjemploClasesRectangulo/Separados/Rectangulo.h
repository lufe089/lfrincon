//#ifndef RECTANGULO_H
// Guardas
//#define RECTANGULO_H
class Rectangulo
{
private: //Atributos
    float largo, ancho;

public:                       //Metodos
    Rectangulo(float, float); //Constructor
    void calcularPerimetro();
    void calcularArea();
};
//#endif /* !RECTANGULO_H */