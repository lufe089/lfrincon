all: programa

programa: Ordenamientos Main
	gcc -o ordenamientosExe Main.o OrdenamientosIterativos.o

Main: Main.c OrdenamientosIterativos.h
	gcc -c Main.c

Ordenamientos: OrdenamientosIterativos.c OrdenamientosIterativos.h
	gcc -c OrdenamientosIterativos.c