import Vue from 'vue'
import Router from 'vue-router'

import LinearSingleEquation from './views/LinearSingleEquation.vue';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/linequa',
      component: LinearSingleEquation
    }
  ]
})
