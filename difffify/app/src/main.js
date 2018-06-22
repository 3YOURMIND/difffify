import Vue from "vue";
import App from "./App.vue";
import "@3yourmind/kotti-style";
import Notifications from 'vue-notification'

Vue.use(Notifications)

new Vue({
  el: "#app",
  render: h => h(App)
});
