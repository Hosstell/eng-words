import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import MyApolloClient from './plugins/apollo-client'
import VueApollo from 'vue-apollo'

Vue.use(VueApollo)
Vue.config.productionTip = false;

const apolloProvider = new VueApollo({
  defaultClient: MyApolloClient,
})

new Vue({
  vuetify,
  router,
  apolloProvider,
  render: h => h(App)
}).$mount("#app");
