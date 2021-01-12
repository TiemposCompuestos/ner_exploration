# Exploración de _NER_ / NER exploration


## Explicación

La mayoría de los modelos preentrenados de reconocimiento de entidades disponibles manejan cuatro categorías estandarizadas, PER (persona), ORG (organización), LOC (lugar) y MISC (miscelánea), con algún grado de variación, pero sin desviarse mucho de estos tipos básicos. Eso hace que, cuando se necesita un modelo que reconozca otras categorías, haya que entrenar con datos personalizados. 

En este repo quiero entrenar un NER partiendo de un conjunto de reseñas de Yelp en inglés. El objetivo es, para aquellas reseñas que sean de un establecimiento gastronómico, extraer el nombre del establecimiento, la ocasión de la visita al mismo (almuerzo, desayuno, cena) y los platos que hayan sido consumidos durante la visita.

Por lo pronto este repositorio contiene los datos crudos en formato 
