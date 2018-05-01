<template>
  <div class="grid container">
    <div class="ui buttons">
      <button class="ui brown button" onclick="javascript:window.location='/AMLO'">Andrés Manuel Lopez Obrador</button>
      <button class="ui purple button" onclick="javascript:window.location='/Bronco'" >Jaime Rodríguez Calderón</button>
      <button class="ui red button" onclick="javascript:window.location='/Meade'">José Antonio Meade K.</button>
      <button class="ui blue button" onclick="javascript:window.location='/Zavala'">Margarita Zavala Gómez</button>
      <button class="ui orange button" onclick="javascript:window.location='/Anaya'">Ricardo Anaya Cortés</button>
    </div>
    <h1 class="ui header">Margarita Zavala Gómez</h1>
    <h2 class="ui header">Candidata Independiente</h2>
    <br>
    <div class="ui left aligned middle aligned four column grid container">
      <div class="column">
        <img class="ui medium rounded image" src="../../images/Margarita.jpg">
      </div>
      <div class="ui eight wide column">
        <p>Nacidad en 1967 en la Ciudad de México. A lo largo de su vida ha militado en el PAN donde ha tenido distintos puestos dentro de comités internos del partido. Está casada con el ex Presidente Felipe Calderón Hinojosa. </p>
        <p>
          Como servidora publica se ha desempeñada como Diputada Locl de la Asamble de Representantes del Disfrito Federal durante 1994 - 1997. También fue Diputada Federal durante 2003 - 2006 donde también fungió como Subcoordinadora de Política Social del Grupo Parlamentario del PAN. 
        </p>
        <p>
          En Octubre renunció a su militancia en Acción Nacional para presentarse como Candidata Independiente. Para postularse a la Presidencia por esta vía es necesario lograr reunir el número de firmas requerido por el INE.
        </p>
      </div>
      <div class="column">
        <h5 class="ui header">Experiencia Relevante:</h5>
        <p> Diputa Local en el DF, Diputada Federal, Presidenta del DIF durante 2006-2012.</p>
        <h5 class="ui header">Educación:</h5>
        <p>Licenciatura en Derecho, Escuela Libre de Derecho.</p>
        <h5 class="ui header">Twitter:</h5>
        <a href="https://twitter.com/Mzavalagc">@Mzavalagc</a>
        <h5 class="ui header">Sitio web de la plataforma política:</h5>
        <a href="http://www.margaritazavala.com">www.margaritazavala.com</a>
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