import Vue from "vue";
import App from "./App.vue";
import "@3yourmind/kotti-style";
import VueYodify from '@3yourmind/vue-yodify';

Vue.use(VueYodify);

new Vue({
  el: "#app",
  render: h => h(App)
});
