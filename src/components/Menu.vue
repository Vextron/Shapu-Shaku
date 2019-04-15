<template>
    <v-bottom-nav :value="true" fixed color="grey darken-4">
      <v-tooltip top v-for="item in sections" :key="item.short">
        <template v-slot:activator="{ on }">
          <router-link :to="item.route">
          <v-btn color="cyan" flat v-on="on">
            <span>{{item.short}}</span>
          </v-btn>
          </router-link>
        </template>
        <span>{{item.name}}</span>
      </v-tooltip>
    </v-bottom-nav>
  
</template>

<script>
export default {
  data: () => ({
    
    sections: [
      {
        name: "Non Linear Equations",
        route: "/linequa",
        short: "NLE",
        divider: true
      },
      {
        name: "Sistemas de Equações Lineares",
        route: "/linequa",
        short: "LES",
        divider: true
      },
      {
        name: "Sistemas de Equações Não Lineares",
        route: "/linequa",
        short: "NLES",
        divider: true
      },
      { name: "Interpolação", route: "/linequa", short: "INT", divider: true },
      {
        name: "Derivação e Integração Numérica",
        route: "/linequa",
        short: "NDI",
        divider: true
      },
      {
        name: "Equações Diferenciais Ordinárias",
        route: "/linequa",
        short: "ODE",
        divider: false
      }
    ]
  })
};
</script>

<style>
a {
  text-decoration: none;
  color: none;
}
</style>
