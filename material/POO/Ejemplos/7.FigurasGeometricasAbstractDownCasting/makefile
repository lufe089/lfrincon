#
VIEW := View
CONTROLLER := Controller
MODEL := Model

debug := -ggdb3

all: programa
programa: figura circulo rectangulo triangulo controlador vista main
	g++ ${debug} -o Ejecutable FiguraGeometrica.o Circulo.o Rectangulo.o Triangulo.o FigurasController.o View.o Main.o
controlador: ${CONTROLLER}/FigurasController.cpp ${CONTROLLER}/FigurasController.h ${MODEL}/Circulo.h ${MODEL}/Rectangulo.h ${MODEL}/Triangulo.h
	g++ -c ${debug} ${CONTROLLER}/FigurasController.cpp
circulo: ${MODEL}/Circulo.cpp ${MODEL}/Circulo.h
	g++ -c ${debug} ${MODEL}/Circulo.cpp
rectangulo: ${MODEL}/Rectangulo.cpp ${MODEL}/Rectangulo.h
	g++ -c ${debug} ${MODEL}/Rectangulo.cpp
triangulo: ${MODEL}/Triangulo.cpp ${MODEL}/Triangulo.h
	g++ -c ${debug} ${MODEL}/Triangulo.cpp
figura:${MODEL}/FiguraGeometrica.cpp ${MODEL}/FiguraGeometrica.h
	g++ -c ${debug} ${MODEL}/FiguraGeometrica.cpp
vista: ${VIEW}/View.cpp ${VIEW}/View.h ${CONTROLLER}/FigurasController.h
	g++ -c ${debug} ${VIEW}/View.cpp
main: Main.cpp ${VIEW}/View.h
	g++ -c ${debug} Main.cpp
clean: #comando para borrar los .o
	@echo "limpio los archivos intermediosd de las carpetas ..."+ ${MODEL} + ${VIEW}
	del *.o, del *.exe