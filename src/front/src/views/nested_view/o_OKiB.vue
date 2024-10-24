<template>
 <v-row v-if="accountStore.user.is_staff">
  <load-round/>
  
 </v-row>

       <v-row v-else>
        
        <v-col 
            class="text-h6 text-grey text-center align-self-center text--lighten-1 font-weight-light"
        >
           Отдел кадров и безопасности
        </v-col>
    </v-row>
 
 

</template>

<script>
import LoadRound from '@/components/load-round.vue'
import {pagecounter} from '@/utils/universal_functions'
import {useAccountStore} from '@/store/AccountStore'

export default {

    components: {
      LoadRound
    },

    setup(){
      
    pagecounter()
    const accountStore = useAccountStore()
    return {
        accountStore


      }
 
}

}
</script>


<style>

</style>