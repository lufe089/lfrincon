all: compilar
compilar: producto tienda cliente menu main
		g++ -o tienda producto.o cliente.o tienda.o menu.o main.o
cliente: cliente.cpp cliente.h
		g++ -c cliente.cpp
producto: producto.cpp producto.h
		g++ -c producto.cpp
tienda: tienda.cpp tienda.h
		g++ -c tienda.cpp
menu: menu.cpp menu.h
		g++ -c menu.cpp
main: main.cpp menu.h tienda.h producto.h 
	  g++ -c main.cpp
clean: 
	delete producto.o Cliente.o tienda.o menu.o main.o