//
// Created by lufe0 on 7/05/2021.
//

#ifndef CASINO_CONTROLLER_H
#define CASINO_CONTROLLER_H
#include "../Model/Jugador.h"
#include "../Model/Casino.h"


#include <iostream>
#include <list>
#include <map>

using std::cin;
using std::cout;
using std::endl;
using std::list;

using std::string;

class Controller
{
private:

    Casino casino;

public:
    Controller();
    void agregarJugador(long id, string nombreJugador, double dinero);
    bool jugar(int idJuego, long idJugador, float gonzosApostar);
    bool verPuedeContinuar(int idJugador); // True si tiene saldo para jugar, false en caso contrario
    void verInfoJugador(long idJugador);
    void retirarJugador(long idJugador);
    void recargarGonzos(long idJugador);
};
#endif //CASINO_CONTROLLER_H
