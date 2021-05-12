//
// Created by lufe0 on 7/05/2021.
//

#ifndef CASINO_VIEW_H
#define CASINO_VIEW_H
#include "../Controller/Controller.h"

class View
{
private:
    // Objeto de tipo controller para enlazar la logica
    Controller controller;
    // Privado pues son de uso interno
    int mostrarMenu();
    void pedirUsuario();
    void jugarView(long idJugador);
    void agregarJugador();
    void retirarJugador();
    void mostrarJugador();

public:
    View();
    void verPrincipal();
};

#endif //CASINO_VIEW_H
