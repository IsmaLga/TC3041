// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
//import the vue instance
import Vue from 'vue'
//import the App component
import App from './App'
//import the vue router
import VueRouter from 'vue-router'
//import semantic-ui-vue
import SuiVue from 'semantic-ui-vue'
//import semantic-ui-vue-css
import 'semantic-ui-css/semantic.min.css'
import Tweet from 'vue-tweet-embed/tweet'
//tell vue to use the router
Vue.use(VueRouter)
Vue.use(SuiVue)
Vue.component('Tweet', Tweet)
//define your routes
//import the hello component
import HelloWorld from './components/HelloWorld'
import About from './components/About'
import AMLO from './components/candidates/AMLO'
import Meade from './components/candidates/Meade'
import Anaya from './components/candidates/Anaya'
import Zavala from './components/candidates/Zavala'
import Bronco from './components/candidates/Bronco'
//define your routes
const routes = [
//define the root url of the application.
{ path: '/', component: HelloWorld },
{path: '/about', component: About},
{path: '/amlo', component: AMLO},
{path: '/meade', component: Meade},
{path: '/zavala', component: Zavala},
{path: '/anaya', component: Anaya},
{path: '/bronco', component: Bronco}
]

// Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = new VueRouter({
  routes, // short for routes: routes
  mode: 'history'
})
//instatinat the vue instance
new Vue({
//define the selector for the root component
  el: '#app',
  //pass the template to the root component
  template: '<App/>',
  //declare components that the root component can access
  components: { App },
  //pass in the router to the Vue instance
  router
}).$mount('#app')//mount the router on the app