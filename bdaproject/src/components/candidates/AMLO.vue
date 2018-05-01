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
import Chart from 'chart.js';
import axios from 'axios';

export default {
  name: 'AMLO',
  data() {
    return {
      negative_tweets: 0,
      neutral_tweets: 0,
      positive_tweets: 0,
      total_tweets: 0,
      candidate_data: null,
      dates: [],
      qPositive_tweets: [],
      qNegative_tweets: [],
      qNeutral_tweets: [],
      planetChartData: null
    };
  },
  methods: {
    getCandidateInfo() {
      axios
        .get(`http://localhost:3000/candidates/lopezobrador_`)
        .then(response => {
          this.candidate_data = response.data;
          console.log(this.candidate_data);
          this.negative_tweets = this.candidate_data[0].negative_tweets;
          this.neutral_tweets = this.candidate_data[0].neutral_tweets;
          this.positive_tweets = this.candidate_data[0].positive_tweets;
          this.total_tweets =
            this.negative_tweets + this.neutral_tweets + this.positive_tweets;
          this.getTweetsQuantity();
        })
        .catch(e => {
          console.log(e);
        });
    },
    getDates() {
      axios
        .get('http://localhost:3000/dates')
        .then(response => {
          response.data.forEach(date => {
            this.dates.push(date.date);
          });
          this.setChartParameters();
          this.createChart('planet-chart', this.planetChartData);
        })
        .catch(error => {
          console.log(error);
        });
    },
    getTweetsQuantity() {
      this.dates.forEach(date => {
        var positiveCont = 0;
        var neutralCont = 0;
        var negativeCont = 0;
        this.candidate_data[0].tweets.forEach(tweet => {
          if (tweet.date == date) {
            if (tweet.sentiment == 'positive') {
              positiveCont = positiveCont + 1;
            }
            else if (tweet.sentiment == 'neutral') {
              neutralCont = neutralCont + 1;
            }
            else if (tweet.sentiment == 'negative') {
              negativeCont = negativeCont + 1;
            }
          }
        });
        this.qPositive_tweets.push(positiveCont);
        this.qNeutral_tweets.push(neutralCont);
        this.qNegative_tweets.push(negativeCont);
      });
    },
    setChartParameters() {
      this.planetChartData = {
        type: 'line',
        data: {
          labels: this.dates,
          datasets: [
            {
              // positive tweets
              label: 'Positive Opinion (in tweets)',
              data: this.qPositive_tweets,
              borderColor: ['#4784b7'],
              borderWidth: 3
            },
            {
              // neutral tweets
              label: 'Neutral Opinion (in tweets)',
              data: this.neutral_tweets,
              borderColor: ['#47b784'],
              borderWidth: 3
            },
            {
              // negative tweets
              label: 'Negative Opinion (in tweets)',
              data: this.qNegative_tweets,
              borderColor: ['#b74747'],
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
      };
    },
    createChart(chartId, chartData) {
      const ctx = document.getElementById(chartId);
      const myChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options
      });
    }
  },
  created() {
    this.getCandidateInfo();
    this.getDates();
  },
  mounted() {}
};
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