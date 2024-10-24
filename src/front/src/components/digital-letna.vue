<template>
    <div class="d-flex h-100 ">

        <v-card
            v-if="t_daily.length > 0"
            class="h-100 w-100 d-flex flex-column"
        >

            <v-row
                v-for="x in t_daily"
                :key="x" 
                v-show="x.position!=6"
            > 
            <v-divider/>
                <v-col>
                    <v-card 
                        class="ma-2 d-flex flex-column"
                        height="100"
                        elevation="0"
                    >
                        <v-card class="h-100 text-center text-black_grey bg-black_and_white">
                            <v-card-title
                                class="statstyle py-0
                                text-xl-overline
                                text-lg-subtitle-1
                                text-md-h5 font-weight-bold bg-black_and_white">
                                {{x.position__name}} 
                            </v-card-title>
                            <v-card-text
                                @click="detailRound(x.position, x.position__name)"
                                class="numstyle mt-2 py-0 font-weight-bold cursor-pointer bg-black_and_white"
                            > 
                         
                                <vue3-autocounter
                                ref='counter'
                                :startAmount='0'
                                :endAmount='Number(x.user__count)'
                                :duration='2'
                                />
                            </v-card-text>
                        </v-card>
                    </v-card>
                </v-col>
            </v-row>
        </v-card>
        <v-card
            v-else class="h-100 w-100 d-flex justify-center flex-column"
            :image="`${burl}/media/default/didjlenta.jpg`">
  
        <v-row class="flex-grow-0">
            <v-col class="py-0">
                <v-switch
                    v-if="accountStore.user.is_staff"
                    v-model="changeData"
                    class="pl-3 d-flex justify-end"
                    color="white"
                    @click="changeData=!changeData">
                </v-switch>
            </v-col>
        </v-row>
        <v-row class="ma-3">
           
                <v-card-text class="d-flex flex-column align-self-center "  v-if="changeData">
         
                        <v-file-input

                            accept=".xlsx"
                            v-model="dailyfiles"
                            variant="underlined"
                            density="compact"
                           
                            hide-details
                            class="pt-2 ml-0 text-white"
                        />
            
                        <v-btn
                            class="align-self-center"
                            icon="mdi-google-play text-white"
                            size="x-large"
                            variant="text"
                            color="teal-darken-4"
                            :disabled="dailyfiles==0?true:false"
                            @click="onPickFile('roundfilse')"
                        />

              
                </v-card-text>
                <v-card-text  v-else class="w-100">
                 
    <v-row
        class="text-white text-center text-lg-h5 h-100"            
        align-content="center"
        justify="center"
    >
        Данные не загружены
    </v-row>
  
</v-card-text>
        
        </v-row>
      

        

        </v-card> 

        <div class="text-center">

<v-dialog
  v-model="dialogDetailRound"
  width="500"
>
    <dialog-search
        :idpos=idpos
        :namepos=namepos
        @searchClose="dialogDetailRound=!dialogDetailRound"
    />    



</v-dialog>

</div>


    </div>
    
</template>

<script>
 import { ref, onMounted,watch } from 'vue'
 import { axiosApiInstance } from '@/utils/axios-api'
 import {checkremote} from '@/utils/universal_functions'
 import { spravURL } from '@/utils/axios-api'

import DialogSearch from './dialog-search.vue'
import { baseURL } from '@/utils/axios-api'
import {useAccountStore} from '@/store/AccountStore'
export default {

    components: {
        DialogSearch
    },
    
    setup(){
        const t_daily = ref('')
        const idpos = ref('')
        const namepos = ref('')
        const dialogDetailRound = ref(false)
        const t_dailyRound = ref({})
        const dailyfiles = ref([])
        const info = ref({})
        const searchname = ref('')
        const menuGetUserDialog = ref(false)
        const iduser = ref('')
        const result = ref({})
        const changeData = ref(false)
        const accountStore = useAccountStore()


        const getcard = async (idus) => {
            menuGetUserDialog.value = true
            iduser.value = idus
        }

        const detailRound = (pos, name) => {
            idpos.value=pos
            namepos.value=name
            dialogDetailRound.value=!dialogDetailRound.value
            axiosApiInstance.get(`api/general_vacation/dailyload/?id=${pos}`).then(data => {             
                t_dailyRound.value = data.data

                result.value=JSON.parse(JSON.stringify(data.data.daily))

            })
        }

        const burl = baseURL.slice(0,-1)


        const onPickFile = (ex) => {
            const sdata = new FormData()
            sdata.append('dailyfiles', dailyfiles.value[0])
            axiosApiInstance.post(`api/general_vacation/dailyroundup/?excel=${ex}`, sdata).then(result => {  
                info.value = result.data
                dailyfun()
            })
              dailyfiles.value = ''
          }

          function dailyfun(){
    
    axiosApiInstance.get('api/general_vacation/dailyload/')
    .then(data => {
      t_daily.value = data.data.daily
    })

  }
//   bgimage()

  onMounted(() => { 

        dailyfun()
          })

        return {t_daily,
                detailRound,
                dialogDetailRound,
                t_dailyRound,
                dailyfiles,
                onPickFile,
                info,
                checkremote,
                searchname,
                spravURL,
                menuGetUserDialog,
                iduser,
                getcard, 
                result,
                idpos,
                namepos,
                changeData,
                baseURL,
                burl,
                accountStore
               
            }
    }

}
</script>

<style>
.fiction .v-input__control {
    display: none;
}
</style>