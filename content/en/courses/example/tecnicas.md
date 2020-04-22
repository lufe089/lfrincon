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

## Engregables: Para las clases virtuales

### Sabádo 2 de mayo.  Ejercicio ordenamientos y archivos 
*** Enunciado: ( https://github.com/lufe089/lfrincon/blob/master/material/Tecnicas/Ejercicios/EntregableOrdenamientoArchivos.docx )

### Sabádo 18 de abril.  
* Videos de ordenamientos. Subir los links a su repositorio

### Lunes 13 y martes 14 de abril.  
* Sustentación parciales ( yo los agendo)
* Asesorías para elaborar trabajo sobre ordenamientos recursivos e iterativos 

### Domingo 12 de abril del 2020 6:00 am
* Publicación del parcial vía blackboard. Fecha de entrega. Domingo 12 de abril 11:55 pm. Lo debe subir a su repositorio. 
* **Temas**: todo :)

### OJO Engregables pendientes hasta el 4 de abril del 2020 (11:55 pm)
* En su repositorio de github: ejercicio práctico grupal iniciado el 30 de marzo sobre conceptos anteriores + git ( revise para la entrega en github las condiciones actualizadas). La nota es individual, el trabajo es grupal. 
* Actualización de todo el código fuente del repositorio revisado con CPPCHECK. Debe arreglar "errores" "advertencias" y "advertencias de estilo". 

### (anterior) Engregables pendientes hasta el 28 de marzo del 2020 (11:55 pm)
* En su repositorio de github:* taller de git, cuento , ejercicio iniciado en la clase del 24 de marzo. 
* El enunciado de cada ejercicio está dentro del repositorio se explican las condiciones para cada entrega. (ver Aquí https://github.com/lufe089/lfrincon/tree/master/material/Tecnicas/Ejercicios) 
-->

## Agenda clases virtuales

### Abril 20 y 21
* Explicación errores más comunes encontrados durante el parcial
* Archivos  ( si no estuvo en la clase puede ver el video en este enlace https://ujaverianacali.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=5582e649-b517-40ea-af87-aba401623df0 )

### Marzo 30 y 31 del 2020
* Marzo 30:  Ejercicios de git/github/trabajo colaborativo parte 1
* Marzo 31:  Ejercicios de git/github/trabajo colaborativo parte 2 . Quiz de git sugerido ( https://learn.co/lessons/git-github-learn-quiz )


---

## Material

### Video clase 31 de marzo
* Revisión estática de código ( https://ujaverianacali.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f8bbbaa3-88b0-428f-bec8-ab8f017816da )

### Videos a revisar semana hasta el 28 de marzo del 2020 
* Structs: (https://ujaverianacali.hosted.panopto.com/Panopto/Pages/Sessions/List.aspx?folderID=ee0cb7a3-5329-4ba3-b3a0-ab8301830ebb ). Tiene cosas que ya vimos. Lo único nuevo es la memoria dinámica para los structs. Si tienen dudas lo ideal sería que repasen los temas en los que tienen dudas. Hagan los ejercicios propuestos
* Enums: tema nuevo! (https://ujaverianacali.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=176343a8-03b4-4096-be04-ab8200275d36 )
* Recursión: esto es repaso del semestre anterior (https://ujaverianacali.hosted.panopto.com/Panopto/Pages/Sessions/List.aspx?folderID=f199947b-e46f-4d45-bc3f-ab8300378f68 ).
Si tiene los conceptos claros puede hacer directamente los ejercicios, sino entonces vea los videos. Los videos estan hechos para python pero el tema es el mismo y los ejemplos están subidos para C en el repositorio de ejercicios.

### Otro material
* Curso recomendado GIT [Udacity] (https://classroom.udacity.com/courses/ud775)
* Diapositivas (https://github.com/lufe089/lfrincon/tree/master/material/Tecnicas/ClasesTutoriales)
* Ejercicios (https://github.com/lufe089/lfrincon/tree/master/material/Tecnicas/Ejercicios)
* Editor colaborativo de texto ( http://collabedit.com )


### Ejercicio arreglos
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
