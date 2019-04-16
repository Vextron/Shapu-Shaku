<template>
  <div>
    <v-layout row wrap>
      <v-flex xs12 lg6>
        <v-card>
          <v-form>
            <v-container>
              <v-text-field v-model="info.function" :color="color" label="Function"></v-text-field>
              <v-layout row wrap>
                <v-flex xs6 sm6 md3>
                  <v-text-field v-model="info.a" :color="color" label="A"></v-text-field>
                </v-flex>
                <v-flex xs6 sm6 md3>
                  <v-text-field v-model="info.b" :color="color" label="B"></v-text-field>
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
              </v-layout>
            </v-container>
            <v-container>
              <v-btn :loading="loading" :color="color" large @click="run(method)">Run</v-btn>
              <v-btn color="cyan darken-3" large @click="graphIt()">Graph It!</v-btn>
              <v-btn color="red darken-4" large >Get PDF</v-btn>
            </v-container>
          </v-form>
        </v-card>
      </v-flex>
      <v-flex xs12 lg6>
        <graph ref="graph"></graph>
      </v-flex>
    </v-layout>
    <v-layout row wrap class="mb-5">
      <formula
        ref="formula"
        :loaded="showTable"
        :data="{size: values.length, value: values[values.length - 1]}"
      ></formula>

      <v-flex xs12>
        <table-result v-if="showTable" :headers="headers" :data="values" class="ma-auto"></table-result>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import Table from "./Table.vue";
import Graph from "./Graph.vue";
import Formula from "./Formula.vue";

import { PythonShell } from "python-shell";

export default {
  components: {
    "table-result": Table,
    graph: Graph,
    formula: Formula
  },

  props: ["color", "method"],

  data: () => ({
    info: {
      a: 0,
      b: 1,
      tol: 0.001,
      n: 10,
      function: "cos(x)",
      var: "x"
    },

    headers: [
      { text: "k", align: "center", sortable: false, value: "k" },
      { text: "A", align: "center", sortable: false, value: "a" },
      { text: "B", align: "center", sortable: false, value: "b" },
      { text: "x", align: "center", sortable: false, value: "p" },
      { text: "F(x)", align: "center", sortable: false, value: "f" }
    ],

    values: [],

    showTable: false,

    loading: false
  }),

  methods: {
    run: function(script) {
      this.values = [];
      this.showTable = false;
      this.loading = true;

      let options = {
        mode: "text",
        pythonOptions: ["-u"],
        args: [
          this.info.a,
          this.info.b,
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
          a: result[1],
          b: result[2],
          p: result[3],
          f: result[4]
        };

        this.values.push(newValue);
      });

      pyshell.end((err, code, signal) => {
        this.$refs.formula.computeFormula(this.info.function);

        this.loading = false;
        this.showTable = true;
      });
    },

    graphIt: function() {
      this.$refs.graph.graph(
        [this.info.a, this.info.b, 0.01, this.info.function, this.info.var],
        this.info.function
      );
    }
  }
};
</script>


<style>
</style>

