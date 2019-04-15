<template>
  <v-flex xs12 lg12>
    <vue-mathjax class="title" :formula="getFormula"></vue-mathjax>
    <vue-mathjax class="title" :formula="getResult"></vue-mathjax>
  </v-flex>
</template>
<script>
import { VueMathjax } from "vue-mathjax";
import { PythonShell } from "python-shell";

export default {
  data: () => ({
    formula: ""
  }),

  props: ["funcion"],

  computed: {
    getFormula: function() {
      return this.formula;
    },

    getResult: function() {
      return `$$ x_{${this.values.length}} = ${
        this.values[this.values.length - 1].p
      } $$`;
    }
  },

  methods: {
    computeFormula: function() {
      let options = {
        mode: "text",
        pythonOptions: ["-u"],
        args: [this.function]
      };

      PythonShell.run(`methods/ToLatex.py`, options, (err, result) => {
        if (err) throw err;

        this.formula = `$$ f(x) = ${result[0]} $$`;
      });
    }
  }
};
</script>
<style>
</style>
