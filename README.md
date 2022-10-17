# Hackathon - Jornada de Talent Digital 
## Data Science - Grup 4 
Este repositorio es la parte de data science de la Hackathon Jornada de Talent Digital.

##### Table of Contents  
[· Introdución](#Introducción)

[· Paso a paso](#Pasoapaso)

[· Problemas encontrados por el camino](#problemas)

[· Ideas de futuro](#ideas)

[· Conclusión](#conclusion)

<a name="Introducción"/>

## Introducción

La parte de data science de la hackathon Jornada de Talent Digital, era la encargada de recoger todos los datos proporcionados por el ayuntamiento, transformarlos y prepararlos para el equipo de Backend. Estos datos venian en formato de pdf por cada uno de los barrios.

Dentro de la web nos encontrabamos con esta tabla:

<p align="center">
  <img src="/Addings/tabla_datos.png" style="width:500px; aling:center;"/>
</p>

Y si entrabas al link te llevaba a este pdf:

<p align="center">
  <img src="/Addings/Datos.PNG" style="width:500px; aling:center;"/>
</p>

De aqui teniamos que sacar todos los datos. Como?

<a name="Pasoapaso"/>

## Paso a paso

El primer paso era averiguar como acceder a todos esos links que te llevaban al pdf con la informacion. Para eso utilizamos una libreria llamada urllib, con la que podiamos abrir links y acceder a su informacion. Con esta libreria pudimos acceder a una API de datos proporcionada por el ayuntamiento, donde aqui dentro se gurdaba el link hacia otra API de datos donde estaban todos los links a los pdf guardados.

Ahora sabemos donde estan todos los links, lo que queda es poder abrirlos y extraer la información. Para acceder al link utilizamos la misma libreria que antes, urllib, y una vez estaos en el link, utilizamos la libreria PyPDF2 para poder leer el contenido del pdf. 

Una vez el contenido leido, procedemos a extraer la información necesaria y añadirla barrio por barrio en un DataFrame, donde necesitamos la ayuda de la libreria Pandas. Una vez el dataframe montado, lo guardamos en un archivo .csv y se lo enviamos al equipo de backend

<a name="problemas"/>

## Problemas encontrados por el camino

Uno de los principales problemas que nos encontramos fue que los datos estuvieran guardados en pdf. Abrir un pdf desde una url, ver toda la informacion que contiene y extripar la necesaria, ha sido la parte mas compleja y que mas tiempo a llevado.

Otro problema fueron las API de datos, ya que nunca habiamso trabajo con una, se nos dificultó un poco el proceso de cogerla y ver la información que tenia dentro.

<a name="ideas"/>

## Ideas de futuro

Hemos observado que que dentro de la pagina web donde estaba la tabla de datos por barrios y los link a los pdf habia otra tabla donde aparecian datos de otros años:

<p align="center">
  <img src="/Addings/años.png" style="width:300px; aling:center;"/>
</p>

El problema es que los pdf de estos años eran inaccesibles :( :

<p align="center">
  <img src="/Addings/no.PNG" style="width:800px; aling:center;"/>
</p>

Si hubieramos podido acceder a estos datos, habriamos intentado hacer un modelo predictivo que, una vez entrenado, nos hubiera podido enseñar la predicción, de los datos recibidos, en los siguientes años para poder hacer una evaluación mas exhaustiva.

<a name="conclusion"/>

## Conclusión

Hemos aprendido mucho haciendo este proyecto, usar APIs de datos, leer PDF en python, añadir la informacion para enviarla al equipo de backend. Pero sobretodo, hemos aprendido a organizarnos en equipos y enviar el output que un equipo recibe como input.
