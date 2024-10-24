<template>
<v-container fluid class="d-flex mx-0 pa-0"> 
  <v-row class="ma-2">
    <v-col
      class="d-flex flex-column"
      lg=7
      md=12
      cols=12
    >
    <v-row class="flex-grow-0">
      <v-col class="pa-1">
        <Carousel-list/>
      </v-col>
    </v-row>
    <v-row  style="height:250px">
      <v-col class="d-flex flex-column pa-1">
        <!-- <event-calendar/> -->
      </v-col>
    </v-row>
    </v-col>
    <v-col
      class="d-flex flex-column"
      lg=5
      md=12
      cols=12
    >
      <v-row>
        <v-col class="d-flex flex-column">
          <v-row >
            <v-col
              lg=4
              md=2
              cols=12
              class="pa-1"
              style="min-height:250px"
            >
              <digital-letna/>
            </v-col>
            <v-col
              class="d-flex flex-column pa-1"
              lg=8
              md=10
              cols=12
              style="min-height:550px"
            >
              <v-card class="h-100 d-flex flex-column">
              <v-row class="d-flex justify-md-center">
                <v-col class="flex-column d-flex">
                  <news-home/>
                </v-col>
              </v-row>
            </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
      <v-row class="flex-grow-0">
        <v-col class="pa-1">
          <v-card class="flex-colmn">
            <v-sheet
              class="mx-auto "
              :class="favorit.length>10?'mx-n3':''"
              max-width="800"
            >
              <v-slide-group
                show-arrows
              >
                <v-slide-group-item
                  v-for="x in favorit"
                  :key="x"
                >
                  <v-btn-toggle
                    v-model="toggle"
                    divided
                    variant="outlined"
                  >
                    <v-tooltip
                    
               
                      :text="x.pages__page"
                      location="top"
                    >
                      <template v-slot:activator="{ props }">
                        <v-btn
                          v-bind="props"
                          :icon="x.pages__ico"
                          :to="x.pages__fullPath"
                        />
                      </template>
                    </v-tooltip>
                  </v-btn-toggle>
                </v-slide-group-item>
              </v-slide-group>
            </v-sheet>
           
          </v-card>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</v-container>
</template>

<script>
  import { ref, onMounted } from 'vue'
  import {useAppStore} from '@/store/app'
  import {useAccountStore} from '@/store/AccountStore'
  import {pagecounter} from '@/utils/universal_functions'

  import CarouselList from '@/components/carousel-list.vue'
  import CarouselNumbers from '@/components/carousel-numbers.vue'


  import NewsHome from '@/components/news-home.vue'
  import LoadRound from '@/components/load-round.vue'
  import DigitalLetna from '@/components/digital-letna.vue'
  import { axiosApiInstance } from '@/utils/axios-api'

  import EventCalendar from '@/components/calendar_of_events/event-calendar.vue'

  export default {

    components: {

      CarouselList,
      CarouselNumbers,


      LoadRound,
      DigitalLetna,
      EventCalendar,
      NewsHome
    },



    setup(){
      const appStore = useAppStore()  
      const favorit = ref([])
      const toggle = ref(null)
      
      const accountStore = useAccountStore()
      pagecounter()

      onMounted(() => { 
        favoritLinks()

      })

      const favoritLinks = () => {
        

        axiosApiInstance.get(`api/watcher/selectedlinks/`)
        .then(data => {
 
          favorit.value = data.data
        })
      }




  
      return {
        accountStore,
        appStore,
        favoritLinks,
        favorit,

        toggle

      }
    }
  }
 
</script>

<style lang="scss">

.v-picker-title, .v-picker__header, .v-picker__actions {
  display: none;
}



.pik {
  height: 84vh;
  /*height: 85.3vh;*/
  // height: 98.6%;
}

.hicard {
  height: 40%!important;
  overflow: auto;
}

.fg {
  height: 240px;
  overflow: auto;
}



.fixed-bar {
  position: sticky;
  position: -webkit-sticky; /* for Safari */
  top: 0em;
  z-index: 2;
}

.bgCard {
    /* #ffffff6b #ffffff8c*/
    background: #ffffff38 ;
}

.bgText {
    background:  #ffffffb0;
   line-height: 2.1rem!important;
 
}
 
</style>
