---
# Course title, summary, and position.

# Page metadata.
title: Técnicas y prácticas de programación
date: "2020-01-28T00:00:00Z"
lastmod: "2020-01-28T00:00:00Z"
draft: false  # Is this a draft? true/false
toc: true  # Show table of contents? true/false
type: docs  # Do not modify.

# Add menu entry to sidebar.
# - name: Declare this menu item as a parent with ID `name`.
# - weight: Position of link in menu.
menu:
  example:
    name: Técnicas de programación
    weight: 2
---

## Intro curso
Curso práctico en el que se aprenderá sobre las principales estructuras de datos lineales, así como herramientas # importantes para implementar dichas estructuras de datos. Usaremos los lenguajes de programación C y C++
weight: 1

---

## Material

### Videos a revisar semana hasta el 28 de marzo del 2020 
* Structs: (https://ujaverianacali.hosted.panopto.com/Panopto/Pages/Sessions/List.aspx#folderID="ee0cb7a3-5329-4ba3-b3a0-ab8301830ebb") . Tiene cosas que ya vimos. Lo único nuevo es la memoria dinámica para los structs. Si tienen dudas lo ideal sería que los repasen.

* Enums: tema nuevo!. Hay un ejercicio sencillo para que completen el código. (https://ujaverianacali.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=176343a8-03b4-4096-be04-ab8200275d36)
* Recursión: esto es repaso del semestre anterior (https://ujaverianacali.hosted.panopto.com/Panopto/Pages/Sessions/List.aspx#folderID="f199947b-e46f-4d45-bc3f-ab8300378f68").
Si tiene los conceptos claros puede hacer directamente los ejercicios, sino entonces vea los videos. Los videos estan hechos para python pero el tema es el mismo y los ejemplos están subidos para C en el repositorio de ejercicios.

### Otro material
* Curso recomendado GIT [Udacity] (https://www.udacity.com/course/version-control-with-git--ud123)
* Diapositivas (https://github.com/lufe089/lfrincon/tree/master/material/Tecnicas/ClasesTutoriales)
* Ejercicios (https://github.com/lufe089/lfrincon/tree/master/material/Tecnicas/Ejercicios)


# Ejercicio arreglos
Dado un arreglo de 10 elementos, que llamaremos  arreglo uno, recorra el arreglo y guarde en las posiciones pares(iniciando en la cero) de otro arreglo, en adelante arreglo 2, todos los números que encuentre del arreglo 1 que sean primos. Si el número del arreglo 1 no es primo entonces guardelo en el arreglo 2, pero en las posiciones impares( iniciando en la posición 1). Además  considere que en el arreglo 2 no pueden quedar repetidos.  Inicialice el arreglo 2 en ceros. 

Tip. Separe el problema en operaciones para que sea más fácil la solución del enunciado.


Para verificar que el ejercicio es correcto tenga encuenta estos casos de prueba:  
Todos son primos, hay repetidos
Ninguno es primo, hay repetidos 
Hay primos y no primos , hay repetidos
Hay primos y no primos, no hay repetidos


Ejemplos ilustrativo

Caso 1:
Arreglo 1: 11 7 29 17 17 29 19 79 13 
Arreglo2: 11 0 7 0 29 0  17 0 19 0 79 0 13

Caso 2:
Arreglo 1:  21 12 15 18 36 44 46 98 44 2000
Arreglo2:  0 21 0 12 0 15 0 18 0 36 0 44 0 46 0 98 0 2000

Caso 3
Arreglo 1: 8 7 21 7 36  44 56 17 8 10
Arreglo 2: 7 8 17 21 0 36 0 44 0 56 0 10
