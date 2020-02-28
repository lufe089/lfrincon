all: programa
programa: Main Cadenas
	gcc -o Cadenas Main.o Cadenas.o
Main: Main.c Cadenas.h
	gcc -c Main.c
Cadenas: Cadenas.c Cadenas.h
	gcc -c Cadenas.c