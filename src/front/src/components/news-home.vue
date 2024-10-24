<template>
    <v-row>
        <v-col class="flex-column d-flex">
            <v-row class="mt-0 h-0 overflow-auto ">
                <v-col
                    v-for="(x, key) in newsAll"
                    :key="key"
                    class="pb-1 pt-0"
                    lg=12
                    md=6
                    sm=6
                >
                    <news-card :news="x"/>


                    <v-dialog
      v-model="dialogfotoOne"
      width="w-100"
      height="900"
      class="flex-column "
    >
      <v-card class="pa-4 h-100 flex-column d-flex">
              <v-row class="flex-grow-0 justify-end">
              <v-col class="pa-0 flex-grow-0">
                <v-btn
                  density="compact"
                  variant="text"
                  icon="mdi-close"
                  @click="dialogfotoOne = false"
           
             
                />
              </v-col>
            </v-row>
        <v-row>

          <v-col  class="flex-column h_cards pa-0">
            <v-img      
              class="d-flex"
              :src="`${burl}${galleryimges}`"
            />
            
          </v-col>

        </v-row>

      </v-card>
    </v-dialog>

                </v-col>
            </v-row>
            <v-divider class="mt-3"/>
            <v-row class="flex-grow-0 ma-0 align-items-center">
                <v-col class="flex-column d-flex pa-0 align-end">
                    <v-btn
                        size="small"
                        variant="text"
                        icon="mdi-newspaper"
                        color="blue-darken-4"
                        :to='`/news`'
                    />
                </v-col>
                <v-col class="py-0 pl-0 flex-grow-0 text-end align-self-center text-caption font-weight-bold text-no-wrap">
                    Всего новостей: {{countetnews}} 
                    
                </v-col>
            </v-row>
        </v-col>
    </v-row>
</template>

<script>
import { ref } from 'vue'
import { axiosApiInstance } from '@/utils/axios-api'
import { useRoute } from 'vue-router'
import newsCard from './UI/news-card.vue'

export default {

    components: { 
        newsCard
    },

    setup(){

        const newsAll=ref([])
        const countetnews = ref(0)
        const page = ref(1)
        const countpage = ref(8)
        const route = useRoute()
        const galleryimges=ref('')
        const dialogfotoOne  = ref(false)

        const loadNewsAll = () => {
            axiosApiInstance.get( `api/navigation/newscrossroad/?name=${route.path}&page=${page.value-1}&countpage=${countpage.value}`).then(result => {  
                newsAll.value= result.data.result
                countetnews.value = result.data.countpage
             }
            )
        }

        loadNewsAll()

        const openOneImg = (idimg) => {
        dialogfotoOne.value = true 
        galleryimges.value = idimg
    

    }

    return {
        newsAll,
        countetnews,
        page,
        countpage,
        loadNewsAll,
        galleryimges,
        dialogfotoOne,
        
    }
    }
}

</script>

<style>

</style>