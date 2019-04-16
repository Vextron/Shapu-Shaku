<template>
  <v-flex v-if="loaded" xs12 lg12>
    <vue-mathjax class="title" :formula="getFormula"></vue-mathjax>
    <vue-mathjax class="title" :formula="getResult"></vue-mathjax>
  </v-flex>
</template>
<script>
import { VueMathjax } from "vue-mathjax";
import { PythonShell } from "python-shell";

export default {

  components: {

    "vue-mathjax": VueMathjax
  },

  data: () => ({
    formula: ""
  }),

  props: ["data", "loaded"],

  computed: {
    getFormula: function() {
      return this.formula;
    },

    getResult: function() {
      return `$$ x_{${this.data.size}} = ${
        this.data.value.p
      } $$`;
    }
  },

  methods: {
    computeFormula: function(fun) {
      let options = {
        mode: "text",
        pythonOptions: ["-u"],
        args: [fun]
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
