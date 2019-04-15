<template>
  <div>
    <v-container>
      <h1 class="display-3">{{method}}</h1>
    </v-container>
    <v-container grid-list-xl text-xs-center>
      <v-layout row wrap>
        <v-flex xs12>
          <v-card>
            <v-container>
              <h2 class="display-1">Methods</h2>
              <v-radio-group v-model="method" class="align-center" row>
                <v-radio :color="color" label="Bissection" value="Bissection"></v-radio>
                <v-radio :color="color" label="False Position" value="FalsePosition"></v-radio>
                <v-radio :color="color" label="Newton's" value="Newton"></v-radio>
                <v-radio :color="color" label="Secant" value="Secant"></v-radio>
                <v-radio :color="color" label="Fixed Point" value="Fixed Point"></v-radio>
              </v-radio-group>
            </v-container>
          </v-card>
        </v-flex>
      </v-layout>

      <bissect-false
        v-if="method == 'Bissection' || method == 'FalsePosition'"
        :method="method"
        :color="color"
      ></bissect-false>
      <newton v-if="method == 'Newton'" :method="method" :color="color"></newton>
    </v-container>
  </div>
</template>
<script>

import BissectFalsePos from "../components/BissectFalsePos.vue";
import Newton from "../components/Newton.vue";

export default {
  components: {
    "bissect-false": BissectFalsePos,
    "newton": Newton
  },

  data: () => ({
    method: "Bissection",

    color: "cyan",

    
  }),

  computed: {
    
  },

  methods: {

  }
};
</script>

<style>
</style>
