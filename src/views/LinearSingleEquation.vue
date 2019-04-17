<template>
  <div>
    <v-container>
      <h1 class="display-3">{{method}}</h1>
    </v-container>
    <v-container grid-list-xl text-xs-center>
      <v-layout row>
        <methods v-on:update="method = $event" :color="color" :choices="choices"></methods>
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

import MethodsGroup from "../components/MethodsGroup.vue";

export default {
  components: {
    "bissect-false": BissectFalsePos,
    newton: Newton,
    methods: MethodsGroup
  },

  data: () => ({
    method: "Bissection",

    color: "cyan",

    choices: [
      {
        label: "Bissection",
        value: "Bissection"
      },
      {
        label: "False Position",
        value: "FalsePosition"
      },
      {
        label: "Newton's",
        value: "Newton"
      },
      {
        label: "Secant",
        value: "Secant"
      },
      {
        label: "Fixed Point",
        value: "Fixed Point"
      }
    ]
  }),

  methods: {}
};
</script>

<style>
</style>
