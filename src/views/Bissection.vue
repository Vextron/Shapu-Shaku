<template>
  <v-container grid-list-xl text-xs-center>
    <v-layout row>
      <v-flex xs12>
        <v-card>
          <v-form>
            <v-container>
              <v-text-field v-model="info.function" color="amber" label="Function"></v-text-field>
              <v-layout row wrap>
                <v-flex xs6 sm6 md3>
                  <v-text-field v-model="info.a" color="amber" label="A"></v-text-field>
                </v-flex>
                <v-flex xs6 sm6 md3>
                  <v-text-field v-model="info.b" color="amber" label="B"></v-text-field>
                </v-flex>
                <v-flex xs6 sm6 md3>
                  <v-text-field v-model="info.tol" color="amber" label="Tolerance"></v-text-field>
                </v-flex>
                <v-flex xs6 sm6 md3>
                  <v-text-field v-model="info.n" color="amber" label="Max Iterations"></v-text-field>
                </v-flex>
                <v-flex xs6 sm6 md3>
                  <v-text-field v-model="info.var" color="amber" label="Var"></v-text-field>
                </v-flex>
              </v-layout>
              <v-btn :loading="loading" color="amber" light large @click="run()">Run</v-btn>
            </v-container>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
    <v-data-table v-if="showTable" :headers="headers" :items="values" class="elevation-1">
      <template v-slot:items="props">
        <td>{{ props.item.k }}</td>
        <td class="text-xs-right">{{ props.item.a }}</td>
        <td class="text-xs-right">{{ props.item.b }}</td>
        <td class="text-xs-right">{{ props.item.p }}</td>
        <td class="text-xs-right">{{ props.item.f }}</td>
      </template>
    </v-data-table>
    
  </v-container>
</template>

<script>
import { PythonShell } from "python-shell";

export default {

  name: "Bissection",

  data: () => ({

    info: {

      a: 0,
      b: 0,
      tol: 0,
      n: 0,
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

    run: function() {

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

      let pyshell = new PythonShell("methods/Bissection.py", options);

      pyshell.on("message", message => {

        const result = message.split(" ");

        const newValue = {k: result[0], a: result[1], b: result[2], p: result[3], f: result[4]}

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
</style>

