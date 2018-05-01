<template>
  <div class="grid container">
    <div class="ui buttons">
      <button class="ui button" onclick="javascript:window.location='/AMLO'">Andrés Manuel Lopez Obrador</button>
      <button class="ui button" onclick="javascript:window.location='/Bronco'" >Jaime Rodríguez Calderón</button>
      <button class="ui button" onclick="javascript:window.location='/Meade'">José Antonio Meade K.</button>
      <button class="ui button" onclick="javascript:window.location='/Zavala'">Margarita Zavala Gómez</button>
      <button class="ui button" onclick="javascript:window.location='/Anaya'">Ricardo Anaya Cortés</button>
    </div>
    <h1 class="ui header">Andrés Manuel López Obrador</h1>
    <h2 class="ui header">Candidato a la Presidencia de la Coaliación Juntos Haremos Historia (Morena - PT - PES)</h2>
    <br>
    <div class="ui left aligned middle aligned four column grid container">
    <div class="column">
      <img class="ui medium rounded image" src="../../images/Amlo.jpg">
    </div>
    <div class="ui eight wide column">
      <p>Nacido en 1953 y originario de Tabasco. Es fundador y militante del partido Movimiento Regeneración Nacional (Morena). Inició su carrera política en 1976 apayando la candidatura del poeta tabasqueño Carlos Pellicer para Senador por el estado de Tabasco.
      </p>
      <p>
        Durante su carrera política se ha desempeñado como presidente nacional del Partido de la Revolución Democrática (PRD) de 1996 a 1999, Jefe de Gobierno del Distrito Federal de 2000 a 2005, candidato a la Presidencia de México por la Coalición Por el Bien de Todos en las elecciones federales de 2006 y por la coalición Movimiento Progresista en las elecciones de 2012.
      </p>
      <p>
        Es el candidato a la Presidencia de la República de la coalición "Juntos Haremos Historia" conformada por Morena, el Partido del Trabajo (PT) y el Partido Encuentro Social (PES)
      </p>
    </div>
    <div class="column">
      <h5 class="ui header">Experiencia Relevante:</h5>
      <p> Jefe de Gobierno de la CDMX, Presidente del partido MORENA.</p>
      <h5 class="ui header">Educación:</h5>
      <p>Licenciado en Ciencias Políticas y Administración Pública, UNAM.</p>
      <h5 class="ui header">Twitter:</h5>
      <a href="http://www.twitter.com/LopezObrador_">@LopezObrador_</a>
      <h5 class="ui header">Sitio web de la plataforma política:</h5>
      <a href="http://www.proyecto18.mx/">www.proyecto18.mx</a>
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