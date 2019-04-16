<template>
  <div>
    <v-layout row>
      <v-flex xs12 lg6>
        <v-card>
          <v-form>
            <v-container>
              <v-text-field v-model="info.function" :color="color" label="Function"></v-text-field>
              <v-layout row wrap>
                <v-flex xs6 sm6 md3>
                  <v-text-field v-model="info.x" :color="color" label="x0"></v-text-field>
                </v-flex>
                <v-flex xs6 sm6 md3>
                  <v-text-field v-model="info.tol" :color="color" label="Tolerance"></v-text-field>
                </v-flex>
                <v-flex xs6 sm6 md3>
                  <v-text-field v-model="info.n" :color="color" label="Max Iterations"></v-text-field>
                </v-flex>
                <v-flex xs6 sm6 md3>
                  <v-text-field v-model="info.var" :color="color" label="Var"></v-text-field>
                </v-flex>
                <v-flex xs6 sm6 md3 v-if="accel == 'NewtonMul'">
                  <v-text-field v-model="info.mul" :color="color" label="Multiplicity"></v-text-field>
                </v-flex>
                <v-flex xs12 sm12 md12>
                  <h6 class="title">Acceleration</h6>
                  <v-radio-group v-model="accel" class="justify-center" row>
                    <v-radio :color="color" label="Normal" value="Newton"></v-radio>
                    <v-radio :color="color" label="Multiplicity" value="NewtonMul"></v-radio>
                    <v-radio :color="color" label="1/f '" value="NewtonDiff"></v-radio>
                  </v-radio-group>
                </v-flex>
              </v-layout>
            </v-container>
            <v-container>
              <v-btn :loading="loading" :color="color" large @click="run(accel)">Run</v-btn>
            </v-container>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs12>
        <vue-mathjax class="title" v-if="showTable" :formula="getFormula"></vue-mathjax>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs12>
        <vue-mathjax class="title" v-if="showTable" :formula="getResult"></vue-mathjax>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs12>
        <table-result v-if="showTable" :headers="headers" :data="values"></table-result>
      </v-flex>
    </v-layout>
  </div>
</template>
<script>
import Table from "./Table.vue";

import { PythonShell } from "python-shell";
import { VueMathjax } from "vue-mathjax";

export default {
  components: {
    "table-result": Table,
    "vue-mathjax": VueMathjax
  },

  props: ["color", "method"],

  data: () => ({
    info: {
      x: 0,
      tol: 0.001,
      n: 10,
      function: "cos(x)",
      var: "x",
      mul: 1
    },

    accel: "Newton",

    headers: [
      { text: "k", align: "center", sortable: false, value: "k" },
      { text: "x", align: "center", sortable: false, value: "x" }
    ],

    values: [],

    formula: "$$ \\cos{\\left (x \\right )} $$",

    showTable: false,

    loading: false
  }),

  computed: {
    computeFormula: function() {
      let options = {
        mode: "text",
        pythonOptions: ["-u"],
        args: [this.info.function]
      };

      PythonShell.run(`methods/ToLatex.py`, options, (err, result) => {
        if (err) throw err;

        this.formula = `$$ f(x) = ${result[0]} $$`;
      });
    },

    getFormula: function() {
      return this.formula;
    },

    getResult: function() {
      return `$$ x_${this.values.length - 1} = ${
        this.values[this.values.length - 1].x
      } $$`;
    }
  },

  methods: {
    run: function(script) {
      this.values = [];
      this.showTable = false;
      this.loading = true;

      let options = {
        mode: "text",
        pythonOptions: ["-u"],
        args: [
          this.info.x,
          this.info.function,
          this.info.tol,
          this.info.n,
          this.info.var
        ]
      };

      let pyshell = new PythonShell(`methods/${script}.py`, options);

      pyshell.on("message", message => {
        const result = message.split(" ");

        const newValue = {
          k: result[0],
          x: result[1]
        };

        this.values.push(newValue);
      });

      pyshell.end((err, code, signal) => {
        this.computeFormula;

        this.loading = false;
        this.showTable = true;
      });
    }
  }
};
</script>
<style>
</style>


