<template>
<v-card class="d-flex ml-3">
    <v-sheet
    class="mx-auto"
    elevation="0"
    max-width="813"
  
  >
    <v-slide-group
      v-model="model"
      class="pa-0"
      selected-class="bg-primary"
      mandatory
      show-arrows
      
    >

      <v-slide-group-item
        v-for="n in digitalData"
        :key="n"
   
      >


                <v-card
          
          class="ma-2 mt-4 d-flex  flex-column"
          height="100"
          width="169"
          elevation="0"
         
        >
                 <!-- <v-img
          height="100"
          :src="`${burl}${n.img}`"
          cover
          class="text-white"
        > -->
        <v-card  class="h-100 text-center g text-black_grey">
      <v-card-title class="statstyle my-2 py-0 text-overline font-weight-bold">
            {{n.status}} 
        </v-card-title>
        <v-card-text class="numstyle mt-4 py-0  font-weight-bold"> 
           <vue3-autocounter ref='counter' :startAmount='0' :endAmount='Number(n.num)' :duration='1'/>
         </v-card-text>
        </v-card>
          
   <!-- </v-img> -->
        </v-card>
      

      </v-slide-group-item>
    </v-slide-group>
  </v-sheet>
  </v-card>
</template>

<script>
import { ref } from 'vue'
import { baseURL } from '@/utils/axios-api'


export default {


  
    props: {
        digitalData: {
            type: Object,
            default: {}
        }
    },

    setup() {
        const burl = baseURL.slice(0,-1)
        const model = ref(false)
       

        return {model, burl}
    }
}
</script>

<style>
.numstyle {
    font-size: 2.875rem!important;
    line-height: 2.5rem!important;
     font-family: cursive !important;
     background:  #ffffffb0;
}

.statstyle {
    background:  #ffffffb0;
     font-size: 1rem!important;
}

.g {
    /* background-color: rgb(240 248 255 / 35%);; */
  background-color: rgb(255 255 255);;
}
</style>