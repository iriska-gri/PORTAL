<template>
    <v-row class="align-center">
        <v-col 
            class="mt-4 text--lighten-1 font-weight-light"
        >
             <v-item-group mandatory>
    <v-container>
      <v-row class="justify-center ">
        <v-col
          v-for="n in activates"
          :key="n"
          cols="4"
          md="2"
        >
          <v-item v-slot="{ isSelected, toggle }">
            <v-btn
                :color="isSelected ? 'primary' : ''"
                class="d-flex align-center pa-6"
                dark
                :href="n.link" 
                :target="n.link?'_blank':''" 
            >
              <v-scroll-y-transition>
                <div
                  class="text-h5 text-grey flex-grow-1 text-center"
                  
                >
                
                 
                 {{n.name}}
                </div>
              </v-scroll-y-transition>
            </v-btn>
          </v-item>
        </v-col>
      </v-row>
    </v-container>
  </v-item-group>
        </v-col>
    </v-row>
</template>

<script>
import {pagecounter} from '@/utils/universal_functions'

export default {
    setup(){
      pagecounter()
        const activates = [
            {name: 'Комиссии', link: 'http://10.252.44.33/accounting6/SOTRYDNIKI.php#tab_committees'},
            {name: 'Ответственность', link: 'http://10.252.44.33/accounting6/SOTRYDNIKI.php#tab_departments'},
            ]

        return {activates}
    }
}
</script>

<style>

</style>