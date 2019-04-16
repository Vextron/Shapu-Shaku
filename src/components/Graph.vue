<template>
  <v-card color="grey darken-4">
    <line-chart  :chartData="dataCollection" :options="options" class="chart ma-auto"></line-chart>
  </v-card>
</template>
<script>

import LineChart from "../charts/LineChart.js";
import { PythonShell } from "python-shell";

export default {

  components: {

    "line-chart": LineChart
  },

  data: () => ({
    data: false,
    dataLoading: false,

    dataCollection: null,
    options: {

      scales: {

        xAxes: [{
            gridLines: {
                display: false
            },
            ticks: {
                display: false
            }
        }],
        yAxes: [{
            gridLines: {
                 display: false
            }   
        }]
      }
    }

  }),

  methods: {
    graph: function(args, fun) {
      this.data = false;
      this.dataLoading = true;

      let options = {
        mode: "text",
        pythonOptions: ["-u"],
        args: args
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
              label: fun,
              data: dataset.data,
              borderColor: "#FF8F00",
              backgroundColor: "rgba(255,171,0,0.1)",
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
  .chart {

    width: 65%;
  }
</style>
