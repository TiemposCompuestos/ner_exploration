# Exploración de _NER_ / NER exploration


## Introducción y contenido

La mayoría de los modelos preentrenados de reconocimiento de entidades disponibles manejan cuatro categorías estandarizadas, PER (persona), ORG (organización), LOC (lugar) y MISC (miscelánea), con algún grado de variación, pero sin desviarse mucho de estos tipos básicos. Eso hace que, cuando se necesita un modelo que reconozca otras categorías, haya que entrenar con datos personalizados. 

En este repo quiero entrenar un NER partiendo de un conjunto de reseñas de Yelp en inglés. El objetivo es, para aquellas reseñas que sean de un establecimiento gastronómico, extraer el nombre del establecimiento, la ocasión de la visita al mismo (almuerzo, desayuno, cena) y los platos que hayan sido consumidos durante la visita.

Las carpetas contienen lo siguiente:
- data/
  - raw/: Tiene los datos crudos en formato `.json`.
  - processed/
    - command_line/: Tiene los datos obtenidos usando herramientas de línea de comandos, que consisten en un archivo csv, `unique_samples.csv` con dos columnas, una para el id del lugar de la reseña y otra para el texto crudo de la review sin saltos de línea.
    - embeddings/: contiene la estructura necesaria para el entrenamiento de embeddings de Flair.
    - NER/
      - crf/: Contiene los datos necesarios para el entrenamiento de un NER usando _conditional random fields_.
      - flair/: Contiene los datos necesarios para el entrenamiento de un NER usando Flair.
    - sample_to_tag/: Contiene los datos necesarios para generar una muestra de reseñas para etiquetar manualmente.
  - tagged/: Tiene las muestras etiquetadas manualmente, que se preprocesan para generar los archivos en `data/processed/NER` y `data/processed/embeddings/'.
- output/: Contiene imágenes obtenidas de los scripts que describen distintos aspectos del corpus de reseñas.
- scripts/: Tiene algunas piezas de código necesarias para generar la mayoría del contenido de las carpetas data/ y output/.
- utils/: Scripts de bash para preprocesar datos.
- notebooks/: Notebooks con el código para entrenar y evaluar NER y embeddings.

El Makefile sirve para generar datos para etiquetar a partir de datos crudos y datos para entrenar a partir de datos etiquetados.
- `make` (o `make generate_to_tag`) genera los datos para etiquetar a partir de `data/raw/reviews.json`
- `make generate_to_train` genera los datos de entrenamiento de NER y embeddings a partir del contenido de `data/`.
- **IMPORTANTE**: dado que Github no permite archivos grandes, las reseñas crudas están separadas en seis archivos que hay que unir con el comando `make join_reviews` antes de ejecutar los demás.


## Introduction and contents

Most pretrained named entity recognition models recognize a standard set of four types, PER (person), ORG (organization), LOC (location) and MISC (miscellaneous), with some degree of variation, but without deviating too much from these basic types. Because of this, whenever a model that cant recognize some other set of classes is needed, it becomes necessary to train new model with custom data.

In this repo, I'm attempting to train a custom NER model using a corpus of Yelp reviews. The goal is, in reviews of food service establishments, to extract the establishment's name, the occasion in which the reviewer made a visit (lunch, brakfast, dinner), and the dishes ordered in said visit.

The folders have the following contents:
- data/
  - raw/: Raw data in `.json` format.
  - processed/
    - command_line/: Data obtained using the command line. It consists in a csv file, `unique_samples.csv` with two columns, one for the id of the reviewed place and the other for the review text without newlines.
    - embeddings/: Data structured according to Flair's embeddings trainng API..
    - NER/
      - crf/: Data to train a NER model using conditional random fields.
      - flair/: Data to train a NER model using Flair.
    - sample_to_tag/: Data to create a review sample to tag by hand.
  - tagged/: Hand tagged samples, to be processed in order to generate the files in `data/processed/NER` and `data/processed/embeddings/'
- output/: Images obtained from scripts/ describing different aspects of the review corpus.
- scripts/: Code snippets required to generate most of the content in`data/` and `output/`.
- utils/: Bash scripts for data preprocessing.
- notebooks/: Notebooks with code for training and evaluating NER and embeddings.

There's a Makefile in order to generate data for tagging from raw data and training data from tagged data.
- `make` (or `make generate_to_tag`) generates tagging data from `data/raw/reviews.json`
- `make generate_to_train` generates training data for NER and embeddings from the contents of `data/`.
- - **IMPORTANT**: since Github won't allow large files, the raw reviews are split across six files to be joined by the command `make join_reviews` before running anything else.
