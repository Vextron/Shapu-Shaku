<template>
  <div>
    <v-btn fab dark color="amber accent-4 mt-3 ml-3" :fixed="true" @click.stop="drawer = !drawer">
      <v-icon class="white--text">menu</v-icon>
    </v-btn>

    <v-navigation-drawer absolute temporary v-model="drawer" class="grey darken-4">
      <div class="mt-4">
        <v-list-group class="white--text" v-for="topic in sections" :key="topic.name" no-action>
          <template v-slot:activator class="white">
            <v-hover>
              <v-list-tile slot-scope="{ hover }" :class="`${hover ? 'amber' : 'white'}--text`">
                <v-list-tile-title>{{topic.name}}</v-list-tile-title>
              </v-list-tile>
            </v-hover>
          </template>

          <v-list sub-group>
            <div v-for="subTopic in topic.subSections" :key="subTopic.name">
              <v-hover>
                <v-list-tile slot-scope="{ hover }" >
                  <router-link to="/bisect" :class="`${hover ? 'amber' : 'white'}--text`"><v-list-tile-title>{{subTopic.name}}</v-list-tile-title></router-link>
                </v-list-tile>
              </v-hover>
            </div>
          </v-list>

          <v-divider v-if="topic.divider"></v-divider>
        </v-list-group>
      </div>
    </v-navigation-drawer>
  </div>
</template>

<script>
import { PythonShell } from "python-shell";

PythonShell.runString("x=1+2;print(x)", null, function(err) {
  if (err) throw err;
  console.log("finished");
});

export default {
  data: () => ({
    drawer: false,
    sections: [
      {
        name: "Equações não Lineares",
        subSections: [
          { name: "Método da Bisseção" },
          { name: "Método da Secante" },
          { name: "Método do Ponto Fixo" },
          { name: "Método de Newton" }
        ],
        divider: true
      },
      {
        name: "Sistemas de Equações Lineares",
        subSections: [
          { name: "Método de Gauss" },
          { name: "Método de Gauss Jordan" },
          { name: "LU" },
          { name: "Método de Doolitle" },
          { name: "Método de Crout" },
          { name: "Método de Choleski" },
          { name: "Método de Jacobi" },
          { name: "Método de Gauss-Seidel" }
        ],
        divider: true
      },
      {
        name: "Sistemas de Equações Não Lineares",
        subSections: [
          { name: "Método de Newton" },
          { name: "Método do Gradiente Conjugado" }
        ],
        divider: true
      },
      { name: "Interpolação", 
        subSections: [
          { name: "Polinómios de Lagrange" },
          { name: "Polinómios de Chebychev" },
          { name: "Splines" }
        ], divider: true
      },
      {
        name: "Derivação e Integração Numérica",
        subSections: [
          { name: "Diferenças Finitas" },
          { name: "Regra do Trapézio" },
          { name: "Regra de Simpson" },
          { name: "Regras Compostas" }
        ],
        divider: true
      },
      {
        name: "Equações Diferenciais Ordinárias",
        subSections: [
          { name: "Método de Euler" },
          { name: "Método de Runge-Kutta" }
        ],
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
