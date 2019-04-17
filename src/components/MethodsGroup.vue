<template>
  <v-flex xs12>
    <v-card>
      <v-container>
        <h2 class="display-1">Methods</h2>
        <v-radio-group v-model="method" v-on:change="updateTitle()" class="justify-center" row>
          <v-radio
            v-for="item in choices"
            :color="color"
            :label="item.label"
            :value="item.value"
            :key="item.value"
          ></v-radio>
        </v-radio-group>
      </v-container>
    </v-card>
  </v-flex>
</template>
<script>
export default {
  props: ["color", "choices"],

  data: () => ({
    method: ""
  }),

  methods: {
    updateTitle: function() {
      this.$emit("update", this.method);
    }
  }
};
</script>
<style>
</style>


