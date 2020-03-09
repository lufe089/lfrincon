all: programa
programa: Cadenas StructMemStatica StructMemDinamica Main
		gcc -o Structs Cadenas.o StructMemoriaEstatica.o StructMemoriaDinamica.o Main.o
Cadenas: Cadenas.c Cadenas.h
		gcc -c Cadenas.c
StructMemStatica: StructMemoriaEstatica.c Structs.h Cadenas.h
		gcc -c StructMemoriaEstatica.c
StructMemDinamica: StructMemoriaDinamica.c Structs.h Cadenas.h
		gcc -c StructMemoriaDinamica.c
Main:	Main.c Structs.h Cadenas.h
		gcc -c Main.c
