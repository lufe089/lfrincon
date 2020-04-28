all: programa

programa: Main OrdenamientoRecursivo

	gcc -o Ordenamientos Main.o OrdenamientoRecursivo.o

Main: Main.c OrdenamientoRecursivo.h

	gcc -c Main.c

OrdenamientoRecursivo: OrdenamientoRecursivo.c OrdenamientoRecursivo.h

	gcc -c OrdenamientoRecursivo.c