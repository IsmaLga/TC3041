<template>
  <div class="grid container">
    <div class="ui buttons">
      <button class="ui button" onclick="javascript:window.location='/AMLO'">Andrés Manuel Lopez Obrador</button>
      <button class="ui button" onclick="javascript:window.location='/Bronco'" >Jaime Rodríguez Calderón</button>
      <button class="ui button" onclick="javascript:window.location='/Meade'">José Antonio Meade K.</button>
      <button class="ui button" onclick="javascript:window.location='/Zavala'">Margarita Zavala Gómez</button>
      <button class="ui button" onclick="javascript:window.location='/Anaya'">Ricardo Anaya Cortés</button>
    </div>
    <h1 class="ui header">José Antonio Meade Kuribreña</h1>
    <h2 class="ui header">Candidato a la Presidencia de la Coaliación Todos por México (PRI - Partido Verde - Nueva Alianza)</h2>
    <br>
    <div class="ui left aligned middle aligned four column grid container">
    <div class="column">
      <img class="ui medium rounded image" src="../../images/Meade.jpg">
    </div>
    <div class="ui eight wide column">
      <p>Nacido en 1969 en la Ciudad de México. Se ha desempeñado como servidor pública durante su vida. Inició su carrera en la Comisión Nacional del Sistema de Ahorro para el Retiro (CONSAR).

      </p>
      <p>
          En la administración pública se ha desempeñado en sexenios panistas como priistas y ha sido titular de 4 Secretarías de Estado. Las Secretarías que ha dirigido incluyen: Hacienda y Crédito Público, Desarrollo Social, Relaciones Exteriores, Energía. Es el único servidor público que ha encabezado Secretarías en gabinetes con Presidente de diferente partido.
      </p>
      <p>
        Es candidato a la presidencia de México por la coalición Todos por México, conformada por el Partido Revolucionario Institucional (PRI), el Partido Verde Ecologista de México (PVEM) y el Partido Nueva Alianza (PANAL).​
      </p>
    </div>
    <div class="column">
      <h5 class="ui header">Experiencia Relevante:</h5>
      <p> Secretario de Hacienda y Crédito Público, Secretario de Desarrollo Social.</p>
      <h5 class="ui header">Educación:</h5>
      <p>Doctorado en Economía, Yale. Licenciatura en Derecho, UNAM. Licenciado en Economía, ITAM.</p>
      <h5 class="ui header">Twitter:</h5>
      <a href="https://twitter.com/JoseAMeadeK">@JoseAMeadeK</a>
      <h5 class="ui header">Sitio web de la plataforma política:</h5>
      <a href="https://meade18.com/">www.meade18.com</a>
    </div>
    </div>
  <h2 class="ui header">Análisis de Tweets</h2>
  <canvas id="planet-chart"></canvas>
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
import Chart from 'chart.js';
export default {
  name: 'about',
  data(){
    return {
      planetChartData: {
        type: 'line',
        data: {
          labels: [
            'Mercury',
            'Venus',
            'Earth',
            'Mars',
            'Jupiter',
            'Saturn',
            'Uranus',
            'Neptune'
          ],
          datasets: [
            {
              // another line graph
              label: 'Planet Mass (x1,000 km)',
              data: [4.8, 12.1, 12.7, 6.7, 139.8, 116.4, 50.7, 49.2],
              backgroundColor: [
                'rgba(71, 183,132,.5)' // Green
              ],
              borderColor: ['#47b784'],
              borderWidth: 3
            }
          ]
        },
        options: {
          responsive: true,
          lineTension: 1,
          scales: {
            yAxes: [
              {
                ticks: {
                  beginAtZero: true,
                  padding: 25
                }
              }
            ]
          }
        }
      }
    }},
    methods: {
      createChart(chartId, chartData) {
        const ctx = document.getElementById(chartId);
        const myChart = new Chart(ctx, {
          type: chartData.type,
          data: chartData.data,
          options: chartData.options
        });
      },
      mounted() {
        this.createChart('planet-chart', this.planetChartData);
      }
    }
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