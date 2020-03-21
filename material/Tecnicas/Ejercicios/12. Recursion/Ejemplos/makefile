all: programa
programa: Recursion Main
	gcc -o Recursion Main.o Recursion.o
Main: Main.c Recursion.h
	gcc -c Main.c
Recursion: Recursion.c Recursion.h
	gcc -c Recursion.c