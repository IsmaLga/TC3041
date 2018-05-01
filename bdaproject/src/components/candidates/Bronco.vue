<template>
  <div class="grid container">
    <div class="ui buttons">
      <button class="ui button" onclick="javascript:window.location='/AMLO'">Andrés Manuel Lopez Obrador</button>
      <button class="ui button" onclick="javascript:window.location='/Bronco'" >Jaime Rodríguez Calderón</button>
      <button class="ui button" onclick="javascript:window.location='/Meade'">José Antonio Meade K.</button>
      <button class="ui button" onclick="javascript:window.location='/Zavala'">Margarita Zavala Gómez</button>
      <button class="ui button" onclick="javascript:window.location='/Anaya'">Ricardo Anaya Cortés</button>
    </div>
    <h1 class="ui header">Jaime Rodriguez Calderón 'El Bronco'</h1>
    <h2 class="ui header">Candidato Independiente</h2>
    <br>
    <div class="ui left aligned middle aligned four column grid container">
    <div class="column">
      <img class="ui medium rounded image" src="../../images/Bronco.jpg">
    </div>
    <div class="ui eight wide column">
      <p>
        Nacido en 1957 en Nuevo León, es Ingeniero Agrónomo por parte de la UANL. Fue el primer gobernador electo con una candidatura independiente en México.
      </p>
      <p>
        En su carrera como servidor público se ha desempeñado como diputado federal por parte del PRI, diputado local en Nuevo León, Presidente municipal de García, Nuevo León. Durante 2015 buscó la gubernatura en Nuevo León por la vía independiente y fue la sorpresa de los comicios al ser el ganador de la elección para gobernador.
      </p>
      <p>
          En enero de 2018 renuncia a su puesto como gobernador para buscar contender en la elección presidencial por la vía independiente. Su participación en el proceso ha sido polémica debido a que el INE dictaminó que no juntó las firmas necesarias para poder ser candidato pero el Tribunal Electoral ordenó la participación del bronco en las elecciones.
      </p>
    </div>
    <div class="column">
      <h5 class="ui header">Experiencia Relevante:</h5>
      <p> Diputado federal y local. Gobernador de Nuevo León. </p>
      <h5 class="ui header">Educación:</h5>
      <p>Ingeniería Agrónoma, UANL.</p>
      <h5 class="ui header">Twitter:</h5>
      <a href="https://twitter.com/JaimeRdzNL">@JaimeRdzNL</a>
      <h5 class="ui header">Sitio web de la plataforma política:</h5>
      <a href="https://jaimerodriguez.mx/">www.jaimerodriguez.mx</a>
    </div>
    </div>
  <h2 class="ui header">Resumen de Actividad en Twitter</h2>
    <div class="ui left aligned middle aligned three column grid container">
      <div class="ui six wide column">
        <h5 class="ui header">Número de tweets analizados:</h5>
        <h5 class="ui header">Número de tweets positivos encontrados:</h5>
        <h5 class="ui header">Número de tweets negativos encontrados:</h5>
        <h5 class="ui header">Número de tweets neutrales encontrados:</h5>
        <h5 class="ui header">Número de veces que los tweets fueron marcados como favorito:</h5>
        <h5 class="ui header">Número de veces que los tweets fueron retweeteados:</h5>

      </div>
      <div class="ui five wide column">
        <Tweet :id="'990315832826912770'"></Tweet>
      </div>
      <div class="ui five wide column">
        <Tweet :id="'989944808461520897'"></Tweet>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'about'
}
</script>
<!-- styling for the component -->
<style>
#about {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>