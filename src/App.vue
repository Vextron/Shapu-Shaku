<template>
  <v-app dark>
    <Menu/>
    <router-view></router-view>
  </v-app>
</template>

<script>
import Menu from './components/Menu'

export default {
  name: 'App',
  components: {
    Menu
  },
  data () {
    return {
      //
    }
  }
}
</script>
