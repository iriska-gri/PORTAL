<template>
    <v-row>
        <v-col class="d-flex flex-column">
            <v-row class=" flex-grow-1 pa-1 d-flex h-0 overflow-auto">
                <v-col
                    v-for="(x, key) in newsAll"
                    :key="key"
                    xl=3
                    lg=4
                    md=12
                    sm=12
                    xs=12
                    cols=12
                    class="d-flex pa-1 flex-column "
                >
                    <news-card :news="x"/>
                   {{aNewsAll}}
                </v-col>
            </v-row>
            <v-row class="flex-grow-0 ">
                <v-col class="pa-0"  >
                    <v-pagination
                        v-model="page"
                        :length=visiblePage
                        :total-visible="7"
                        @update:modelValue="loadNewsAll"
                    />
                </v-col>
                <v-col class="flex-grow-0 py-0">
                    <v-select
                        style="width:53px"
                        hide-details
                        hide-selected
                        density="compact"
                        v-model="countpage"
                        rounded
                        variant="underlined"
                        :items="[8, 16, 24, 32, 40]"
                        @update:modelValue="loadNewsAll"
                    />
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
        const visiblePage = ref(0)

        const loadNewsAll = () => {
            axiosApiInstance.get( `api/navigation/newscrossroad/?name=${route.path}&page=${page.value-1}&countpage=${countpage.value}`).then(result => {  
          
                newsAll.value= result.data.result
                countetnews.value = result.data.countpage/countpage.value
                visiblePage.value = countetnews.value <= 1 ? 1 : countetnews.value+1
             }
            )
        }      

        loadNewsAll()

    return {
        newsAll,

        countetnews,
        page,
        countpage,
        visiblePage,
        loadNewsAll,
    }
    }
}

</script>

<style>

</style>