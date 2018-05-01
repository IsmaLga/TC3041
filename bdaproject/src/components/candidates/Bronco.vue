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
import Chart from 'chart.js';
import axios from 'axios';

export default {
  name: 'Bronco',
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
        .get(`http://localhost:3000/candidates/JaimeRdzNL`)
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