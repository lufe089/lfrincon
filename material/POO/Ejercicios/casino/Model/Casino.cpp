//
// Created by lufe0 on 7/05/2021.
//

#include "Casino.h"

// Constructor que inicializa las ganancias y perdidas en cero
Casino::Casino() {
    cout <<"Inicialice casino";
    jugadoresMap.clear(); // Se limpian los jugadores del casino
}


void Casino::agregarJuego(Juego * juego) {
    juegosDisponibles.push_back(juego);
}



void Casino::agregarJugador(Jugador *pJugador) {
    // Se agrega el jugador al mapa de jugadores del casino
   cout << "Por implementar \n";
}

bool Casino::verExisteJugador(long id) {

    // Si el jugador se encuentra en el mapa retorna true, de lo contrario retorna false
    cout << "Por implementar \n";
}

Jugador *Casino::consultarJugador(long id) {
    return jugadoresMap[id]; // Retora el apuntador a jugador.
}

double Casino::convertirPesosAGonzos(double dinero) {

    // Cada 10 mil pesos equivalen a 100 Gonzos
    cout << "Por implementar \n";
    return 0;
}

vector<Juego *> &Casino::consultarJuegos() {
    return juegosDisponibles;
}

void Casino::retirarJugador(long id) {
    // Pendiente por implementar
    // Investigue como remover el jugador del mapa
    cout << "Fase dos, por hacer \n";
}


double Casino::convertirGonzosPesos(float gonzos) {
    // Pendiente por implementar
    cout << "Fase dos, por hacer \n";
    return 0;
}

Casino::~Casino() {

}