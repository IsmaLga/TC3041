<template>
  <div class="grid container">
    <div class="ui buttons">
      <button class="ui button" onclick="javascript:window.location='/AMLO'">Andrés Manuel Lopez Obrador</button>
      <button class="ui button" onclick="javascript:window.location='/Bronco'" >Jaime Rodríguez Calderón</button>
      <button class="ui button" onclick="javascript:window.location='/Meade'">José Antonio Meade K.</button>
      <button class="ui button" onclick="javascript:window.location='/Zavala'">Margarita Zavala Gómez</button>
      <button class="ui button" onclick="javascript:window.location='/Anaya'">Ricardo Anaya Cortés</button>
    </div>
    <h1 class="ui header">Margarita Zavala Gómez</h1>
    <h2 class="ui header">Candidata Independiente</h2>
    <br>
    <div class="ui left aligned middle aligned four column grid container">
    <div class="column">
      <img class="ui medium rounded image" src="../../images/Margarita.jpg">
    </div>
    <div class="ui eight wide column">
      <p>Nacido en 1979 en Querétaro. Se ha desempeñado como Coordinador de Desarrollo Humano del Gobierno del Estado de Querétaro de 2008 a 2009 y Presidente del PAN de 2015 a 2017.
      </p>
      <p>
          En su carrera como servidor público ha sido diputado local de la LVI Legislatura del Estado de Querétaro, Subsecretario de Planeación Turística de la Secretaría de Turismo en la administración de Felipe Calderón y Diputado Federal de la LXII Legislatura durante el periodo 2012 - 2015 por el Estado de Querétaro. 
      </p>
      <p>
        Es candidata a la presidencia de México por la vía independiente, su registro fue realizado de acuerdo al proceso de recolección de firmas del INE.​
      </p>
    </div>
    <div class="column">
      <h5 class="ui header">Experiencia Relevante:</h5>
      <p> Directora Jurídica del Comité Ejecutivo Nacional del PAN, Presidenta del DIF durante 2006-2012.</p>
      <h5 class="ui header">Educación:</h5>
      <p>Licenciatura en Derecho, Escuela Libre de Derecho.</p>
      <h5 class="ui header">Twitter:</h5>
      <a href="https://twitter.com/Mzavalagc">@Mzavalagc</a>
      <h5 class="ui header">Sitio web de la plataforma política:</h5>
      <a href="http://www.margaritazavala.com">www.margaritazavala.com</a>
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