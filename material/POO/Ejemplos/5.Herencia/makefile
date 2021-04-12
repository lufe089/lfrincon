#
VIEW := View
CONTROLLER := Controller
MODEL := Model

debug := -ggdb3

all: programa
programa: abuelo padre hijo view main
	g++ ${debug} -o Ejecutable Abuelo.o Padre.o Hijo.o View.o Main.o
hijo: ${MODEL}/Hijo.cpp ${MODEL}/Padre.h ${MODEL}/Abuelo.h
	g++ -c ${debug} ${MODEL}/Hijo.cpp
padre: ${MODEL}/Padre.cpp ${MODEL}/Padre.h ${MODEL}/Abuelo.h
	g++ -c ${debug} ${MODEL}/Padre.cpp
abuelo: ${MODEL}/Abuelo.cpp ${MODEL}/Abuelo.h
	g++ -c ${debug} ${MODEL}/Abuelo.cpp
view: ${VIEW}/View.cpp ${VIEW}/View.h ${MODEL}/Abuelo.h ${MODEL}/Padre.h ${MODEL}/Hijo.h
	g++ -c ${debug} ${VIEW}/View.cpp
main: Main.cpp ${VIEW}/View.h 
	g++ -c ${debug} Main.cpp
delete: #comando para borrar los .o
	@echo "limpio los archivos intermediosd de las carpetas ..."+ ${MODEL} + ${VIEW}
	del *.o, del *.exe