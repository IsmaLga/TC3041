<template>
  <div class="grid container">
    <div class="ui buttons">
      <button class="ui button" onclick="javascript:window.location='/AMLO'">Andrés Manuel Lopez Obrador</button>
      <button class="ui button" onclick="javascript:window.location='/Bronco'" >Jaime Rodríguez Calderón</button>
      <button class="ui button" onclick="javascript:window.location='/Meade'">José Antonio Meade K.</button>
      <button class="ui button" onclick="javascript:window.location='/Zavala'">Margarita Zavala Gómez</button>
      <button class="ui button" onclick="javascript:window.location='/Anaya'">Ricardo Anaya Cortés</button>
    </div>
    <h1 class="ui header">Ricardo Anaya Cortés</h1>
    <h2 class="ui header">Candidato a la Presidencia de la Coaliación Por México Al Frente (PAN - PRD - MC)</h2>
    <br>
    <div class="ui left aligned middle aligned four column grid container">
    <div class="column">
      <img class="ui medium rounded image" src="../../images/Anaya.jpg">
    </div>
    <div class="ui eight wide column">
      <p>Nacido en 1979 en Querétaro. Se ha desempeñado como Coordinador de Desarrollo Humano del Gobierno del Estado de Querétaro de 2008 a 2009 y Presidente del PAN de 2015 a 2017.
      </p>
      <p>
          En su carrera como servidor público ha sido diputado local de la LVI Legislatura del Estado de Querétaro, Subsecretario de Planeación Turística de la Secretaría de Turismo en la administración de Felipe Calderón y Diputado Federal de la LXII Legislatura durante el periodo 2012 - 2015 por el Estado de Querétaro. 
      </p>
      <p>
        Es candidato a la presidencia de México por la coalición Por México Al Frente conformada por el Partido Acción Nacional (PAN), el Partido de la Revolución Democrática (PRD) y el Partido Movimiento Ciudadano (MC).​
      </p>
    </div>
    <div class="column">
      <h5 class="ui header">Experiencia Relevante:</h5>
      <p> Presidente del PAN, Diputado Federal por Querétaro.</p>
      <h5 class="ui header">Educación:</h5>
      <p>Doctor en Ciencias Políticas y Sociales, UNAM. Licenciatura en Derecho, Universidad Autónoma de Querétaro.</p>
      <h5 class="ui header">Twitter:</h5>
      <a href="https://twitter.com/RicardoAnayaC">@RicardoAnayaC</a>
      <h5 class="ui header">Sitio web de la plataforma política:</h5>
      <a href="https://ricardoanaya.com.mx/">www.ricardoanaya.com.mx</a>
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
  name: 'Anaya',
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
        .get(`http://localhost:3000/candidates/ricardoanayac`)
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