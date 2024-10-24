<template>
  <v-card class="text-center h-100 d-flex flex-column ">
    <v-row no-gutters class="flex-grow-0">
      <v-col class="d-flex flex-column pa-1">
        <v-chip
          color="light-blue-darken-4"
          label
          class="text-center text-cyan-darken-4 rounded-0 text-subtitle-1 font-weight-medium"
        >
        <v-icon start color="cyan-darken-4" :icon="ico"/>
       {{title}}
       
     </v-chip>
   </v-col>

 </v-row>
 <v-row no-gutters  >
  <v-col class="flex-column d-flex">

 
 <v-card-text class="px-3 py-1 flex-column d-flex h-0 overflow-x-auto overflow-x-hidden">
  <slot name="filling"></slot>
 </v-card-text>
</v-col>
 </v-row>
  </v-card>
</template>

<script>
export default {
  props: {
    
    title: {
        type: String,
        default: ''
    },

    ico: {
        type: String,
        default: ''
    }
  }
}
</script>

<style>

</style>