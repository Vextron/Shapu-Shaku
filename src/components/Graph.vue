<template>
  <v-card color="grey darken-4">
    <line-chart v-if="data" :chartData="dataCollection" class="chart ma-auto"></line-chart>
  </v-card>
</template>
<script>

import LineChart from "../charts/LineChart.js";

export default {

    props: ["pyargs"],

  data: () => ({
    data: false,
    dataLoading: false,

    dataCollection: null
  }),

  methods: {
    graph: function() {
      this.data = false;
      this.dataLoading = true;

      let options = {
        mode: "text",
        pythonOptions: ["-u"],
        args: this.pyargs
      };

      let dataset = {
        label: [],
        data: []
      };

      let pyshell = new PythonShell(`methods/GraphData.py`, options);

      pyshell.on("message", message => {
        let point = message.split(" ");

        dataset.label.push(Number(point[0]));
        dataset.data.push(Number(point[1]));
      });

      pyshell.end((err, code, signal) => {
        this.dataCollection = {
          labels: dataset.label,
          datasets: [
            {
              label: this.info.function,
              data: dataset.data,
              borderColor: "#FF8F00",
              pointRadius: 0
            }
          ]
        };

        this.dataLoading = false;
        this.data = true;
      });
    }
  }
};
</script>
<style>
</style>
