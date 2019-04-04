import Vue from 'vue'
import Router from 'vue-router'

import Bissection from './views/Bissection.vue';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/bisect',
      component: Bissection
    }
  ]
})
