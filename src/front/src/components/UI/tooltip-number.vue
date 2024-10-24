<template>
  <v-tooltip
    location="bottom"
    v-if="number>0"
  >
    <template v-slot:activator="{ props }">
      <span v-bind="props">
        {{number}}
      </span>                     
    </template>
    <v-row 
        no-gutters v-for="n in tooltip"
        :key="n"
      >
        <v-col>
            {{n}}
        </v-col>
    </v-row>
  </v-tooltip>
  <span v-else>
    0
  </span>
</template>

<script>

export default {

  props: {
    
    tooltip: {
        type: Array,
        default: () => []
    },

    number: {
      type: Number,
      default: 0
    }

  },
}

</script>

<style>

</style>