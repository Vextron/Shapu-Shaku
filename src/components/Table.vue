<template>
  <v-data-table :headers="headers" :items="data" class="elevation-1 mb-5">
    <template v-slot:items="props">
        <td class="text-xs-right" v-for="value in props.item" :key="value">{{value}}</td>
    </template>
  </v-data-table>
</template>
<script>
export default {
  name: 'Table',

  props: ["headers", "data"],

  data: () => ({

      
  })
};
</script>
<style>
</style>

