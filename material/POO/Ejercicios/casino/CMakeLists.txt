cmake_minimum_required(VERSION 3.19)
project(casino)

set(CMAKE_CXX_STANDARD 14)

add_executable(casino main.cpp Model/Jugador.cpp Controller/Controller.h Controller/Controller.cpp View/View.cpp View/View.h Model/Casino.cpp Model/Casino.h Model/Juego.cpp Model/Juego.h  Model/Mayor13.cpp Model/Mayor13.h Model/DosColores.cpp Model/DosColores.h)