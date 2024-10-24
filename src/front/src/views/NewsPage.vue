<template>
    <v-row class="justify-center ma-0 ">
        <v-col 
            class="flex-column d-flex"
           
        >
   
        <news-crossroad/>

        </v-col>
    </v-row>
</template>

<script>

import {pagecounter} from '@/utils/universal_functions'
import newsCrossroad from '../components/news-crossroad.vue'
// import NewsListNews from '../components/news-list-news.vue'

export default {
    components: {
        newsCrossroad

    },
    setup(){
    pagecounter()
}

}
</script>


<style>
/* .bg {
  background: url("@/assets/1.jpg") center center;
 } */
</style>