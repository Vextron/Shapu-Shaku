<template>
  <div>
    <v-layout row>
      <v-flex xs12>
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
              <v-btn color="cyan darken-3" large @click="graph()">Graph It!</v-btn>
            </v-container>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row wrap class="mb-5">
      <formula v-if="showTable" :function="info.function"></formula>
      <v-flex xs12 lg6>
        <graph></graph>
      </v-flex>
      <v-flex xs12 lg6>
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
    "graph": Graph,
    "formula": Formula
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

        this.loading = false;
        this.showTable = true;
      });
    }
  }
};
</script>


<style>
.chart {
  width: 95%;
}
</style>

