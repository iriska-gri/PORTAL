<template>
   <v-tooltip location="top" >
                <template v-slot:activator="{ props }">
                  <span v-bind="props" >
                    {{ info.length }}
                  </span>
                </template>
                <v-row 
                  no-gutters v-for="n in info"
                  :key="n"
                >
                  <v-col >
                      {{n}}
                  </v-col>
                </v-row>
              </v-tooltip>
</template>

<script>
export default {
    props: {
    info: {
        type: Array,
        default: () => []
    }
}
}
</script>

<style>

</style>