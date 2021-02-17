all: compilar
compilar: rectangulo main
		g++ -o Salida Rectangulo.o Main.o 
rectangulo: Rectangulo.cpp Rectangulo.h
		g++ -c Rectangulo.cpp
main: Main.cpp Rectangulo.h
		g++ -c Main.cpp
