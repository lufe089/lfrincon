all: programa

programa: Archivos Main
	gcc -o archivos Main.o Archivos.o

Main: Main.c Archivos.h
	gcc -c Main.c

Archivos: Archivos.c Archivos.h
	gcc -c Archivos.c