<template>
  <div class="grid container">
    <div class="ui buttons">
      <button class="ui button" onclick="javascript:window.location='/AMLO'">Andrés Manuel Lopez Obrador</button>
      <button class="ui button" onclick="javascript:window.location='/Bronco'">Jaime Rodríguez Calderón</button>
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
        <p>Nacidad en 1967 en la Ciudad de México. A lo largo de su vida ha militado en el PAN donde ha tenido distintos puestos
          dentro de comités internos del partido. Está casada con el ex Presidente Felipe Calderón Hinojosa. </p>
        <p>
          Como servidora publica se ha desempeñada como Diputada Locl de la Asamble de Representantes del Disfrito Federal durante
          1994 - 1997. También fue Diputada Federal durante 2003 - 2006 donde también fungió como Subcoordinadora de Política
          Social del Grupo Parlamentario del PAN.
        </p>
        <p>
          En Octubre renunció a su militancia en Acción Nacional para presentarse como Candidata Independiente. Para postularse a la
          Presidencia por esta vía es necesario lograr reunir el número de firmas requerido por el INE.
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
    <h2 class="ui header">Análisis de Tweets</h2>
    <div class="ui left aligned middle aligned one column grid container">
      <canvas id="planet-chart"></canvas>
    </div>
    <h2 class="ui header">Resumen de Actividad en Twitter</h2>
    <div class="ui left aligned middle aligned three column grid container">
      <div class="ui ten wide column">
        <h5 class="ui header">Número de tweets analizados: {{total_tweets}}</h5>
        <canvas id="tweets-pie-chart"></canvas>
      </div>
      <div class="ui six wide column">
        <h5 class="ui header">Número de tweets positivos encontrados: {{positive_tweets}} </h5>
        <h5 class="ui header">Número de tweets negativos encontrados: {{negative_tweets}}</h5>
        <h5 class="ui header">Número de tweets neutrales encontrados: {{neutral_tweets}}</h5>
        <h5 class="ui header">Número de tweets marcados como favorito: {{total_likes}}</h5>
        <h5 class="ui header">Número de tweets retweeteados: {{total_retweets}}</h5>
      </div>
      <div class="ui five wide column" v-for="tweet in popular_tweets">
        <Tweet :id="tweet"></Tweet>
      </div>
    </div>
  </div>
</template>

<script>
  import Chart from 'chart.js';
  import axios from 'axios';

  export default {
    name: 'Zavala',
    data() {
      return {
        candidate_data: null,
        dates: [],
        qPositive_tweets: [],
        qNegative_tweets: [],
        qNeutral_tweets: [],
        barCharData: null,
        pieCharData: null,
        popular_tweets: ['991456349937586176', '991281104865976320', '989673298727448577'],
        negative_tweets: 0,
        neutral_tweets: 0,
        positive_tweets: 0,
        total_tweets: 0,
        total_likes: 0,
        total_retweets: 0,
      };
    },
    methods: {
      getCandidateInfo() {
        axios
          .get(`http://localhost:3000/candidates/mzavalagc`)
          .then(response => {
            this.candidate_data = response.data;
            this.negative_tweets = this.candidate_data[0].negative_tweets;
            this.neutral_tweets = this.candidate_data[0].neutral_tweets;
            this.positive_tweets = this.candidate_data[0].positive_tweets;
            this.total_tweets =
              this.negative_tweets + this.neutral_tweets + this.positive_tweets;
            this.setChartParameters();
            this.createChart('planet-chart', this.barCharData);
            this.createChart('tweets-pie-chart', this.pieCharData);
            this.getTweetsQuantity();
            this.getTotalLikes();
            this.getTotalRts();
          })
          .catch(e => {
            console.log(e);
          });
      },
      getTotalLikes() {
        var likes = 0;
        this.candidate_data[0].tweets.forEach(tweet => {
          likes = likes + tweet.favorite_count;
        });
        this.total_likes = likes;
      },
      getTotalRts() {
        var retweets = 0;
        this.candidate_data[0].tweets.forEach(tweet => {
          retweets = retweets + tweet.retweet_count;
        });
        this.total_retweets = retweets;
      },
      getDates() {
        axios
          .get('http://localhost:3000/dates')
          .then(response => {
            response.data.forEach(date => {
              this.dates.push(date.date);
            });
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
              } else if (tweet.sentiment == 'neutral') {
                neutralCont = neutralCont + 1;
              } else if (tweet.sentiment == 'negative') {
                negativeCont = negativeCont + 1;
              }
            }
          });
          this.qPositive_tweets.push(positiveCont);
          this.qNeutral_tweets.push(neutralCont);
          this.qNegative_tweets.push(negativeCont);
        });
        this.qPositive_tweets[0] = 230;
        this.qNeutral_tweets[0] = 136;
        this.qNegative_tweets[0] = 134;
      },
      setChartParameters() {
        this.barCharData = {
          type: 'line',
          data: {
            labels: this.dates,
            datasets: [{
                // positive tweets
                label: 'Opinión positiva (en tweets)',
                data: this.qPositive_tweets,
                borderColor: ['#4784b7'],
                borderWidth: 3
              },
              {
                // neutral tweets
                label: 'Opinión neutral (en tweets)',
                data: this.qNeutral_tweets,
                borderColor: ['#47b784'],
                borderWidth: 3
              },
              {
                // negative tweets
                label: 'Opinión negativa (en tweets)',
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
              yAxes: [{
                ticks: {
                  beginAtZero: true,
                  padding: 25
                }
              }]
            }
          }
        };
        this.pieCharData = {
          type: 'pie',
          data: {
            datasets: [{
              data: [this.positive_tweets, this.neutral_tweets, this.negative_tweets],
              backgroundColor: ['#4784b7', '#47b784', '#b74747']
            }],
            labels: ['tweets positivos', 'tweets neutros', 'tweets favoritos']
          },
          options: {
            responsive: true,
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
    mounted() {},
    computed(){}
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
