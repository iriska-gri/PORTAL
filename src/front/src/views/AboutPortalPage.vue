<template>
    <v-row v-if="alldata.feedback.last_comment.time_create=='1990-01-01'">
    <v-col class="text-h6 text-grey text-center align-self-center text--lighten-1 font-weight-light">
      <v-progress-circular
      :size="150"
      :width="7"
      color="cyan-darken-3"
      indeterminate
    ></v-progress-circular>
        </v-col>
  </v-row>
<v-row v-else no-gutters class="gap ma-1 flex-column">
  <v-col class="d-flex flex-column w100 pa-0 flex-grow-0">
    <toolbar-filter :nStaff=alldata.staff />
   
</v-col>
<v-col class="d-flex " >
  <v-row no-gutters class="gap" >
    <v-col lg=2 class=" d-flex flex-column">
      <v-row no-gutters class="gap ma-0 flex-column">
        <v-col lg=4 class="flex-column d-flex w100">
          <portal-traffic :alldata=alldata />
        </v-col>
        <v-col class="flex-column d-flex w100">
          <v-row no-gutters class="flex-column gap" >
            <v-col v-for="x in cardtotal" :key=x>
              <card-total :indicator=x />
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
    <v-col class="d-flex flex-column">
      <v-row no-gutters class="flex-column gap">
        <v-col lg=4 class="w100">
          <line-chart 
            :key = "`${filterStore.date_period.startdate}-${filterStore.date_period.enddate}`"
            :dataLineChart="dataLineChart" 
            :period="{before:alldata.beforperiod,period:alldata.period}"
            :filter = filter
            @getCRR = "getCRR"
          />
        </v-col>
        <v-col class=" d-flex flex-column">
          <v-row no-gutters class="gap">
            <v-col>
              <rating-page :pages_count=alldata.period /> 
            </v-col>
            <v-col>
              <top-user
                    :activusers = alldata.period
                  />
            </v-col>
          </v-row>
        </v-col>

      </v-row>
    </v-col>
    <v-col lg=2 >
      <feedmodul
            :feedback="alldata.feedback"
          />
    </v-col>
  </v-row>
</v-col>
</v-row>
 

</template>

<script>
import { ref, watch } from 'vue'

import {pagecounter, splitname, formatDash} from '@/utils/universal_functions'

import { axiosApiInstance } from '@/utils/axios-api'
import { usePortalFilterStore } from '@/store/AboutPortalFilter'

import Feedmodul from '@/components/UI/aboutportal/feedmodul.vue'
import DateSelect from '@/components/UI/date-select.vue'
import TopUser from '@/components/UI/aboutportal/top-user.vue'
import LineChart from '@/components/UI/aboutportal/line-chart.vue'
import PortalTraffic from '@/components/UI/aboutportal/portal-traffic.vue'
import ToolbarFilter from '@/components/UI/aboutportal/toolbar-filter.vue'
import RatingPage from '@/components/UI/aboutportal/rating-page.vue'

import CardTotal from '@/components/UI/aboutportal/card-total.vue'
// import Feedmodul from '@/components/UI/aboutportal/feedmodul.vue'

export default {
  components: {
    Feedmodul,
    DateSelect,
    TopUser,
    LineChart,
    PortalTraffic,
    ToolbarFilter,
    RatingPage,

    CardTotal,
 
  },


setup(){


  const dataLineChart = ref({})
  const cardtotal = ref(
    {
  "crr": {
    "title": "Удержание",
    "abb": "(CRR)",
    "tooltip": "Customer retention rate - коэффициент удержания пользователей. Retention является одной из важнейших метрик продукта - он показывает, есть ли проблемы с вовлечением новых пользователей, и помогает спрогнозировать, будет ли проект успешным в перспективе",
    "data": 0
  },
  "br": {
    "title": "Отказы",
    "abb": "(BR)",
    "tooltip": "Bounce Rate - термин в веб-аналитике, обозначающий процентное соотношение количества посетителей, покинувших сайт прямо со страницы входа или просмотревших не более одной страницы сайта к общему количеству посетителей",
    "data": 0
  },
  "ppv": {
    "title": "Страниц за визит",
    "abb": "(PPV)",
    "tooltip": "Pages Per Visit - глубина просмотра страниц. Поведенческая метрика, которая показывает, сколько страниц на сайте в среднем просматривает пользователь",
    "data": 0
  }

  })





  const filterStore = usePortalFilterStore()
    const alldata =ref({period: [], staff: 0, beforperiod: [], feedback: {criteria: [], feed: [], last_comment:{time_create:'1990-01-01'}}})
    const visition = () => {

    axiosApiInstance.get(`api/watcher/dataforstatistics/?start=${formatDash(filterStore.date_period.startdate)}&end=${formatDash(filterStore.date_period.enddate)}`).then(result => {
    alldata.value = preparedata(result.data)

    totalfn()

    
  })}

  visition()
  const preparedata=(data)=>{
      let beforperiod = []
      data.beforperiod.forEach((e)=>{
        let ind = beforperiod.findIndex(el=>el.visitdate===e.visitdate)        
        if(ind>-1){
          beforperiod[ind].user.push(e.user__user_id)          
        }else{
          beforperiod.push({visitdate: e.visitdate, user:[e.user__user_id]})
        }
      })
      data.beforperiod=beforperiod

      return data
  }
  
  
  
  const totalfn = () => {
    let beforperiodusers = new Set([])
    alldata.value.beforperiod.forEach(e => beforperiodusers.add(...e.user)) 
    

    let periodusers = new Set([])
    let brdata = {}
    let filtr = alldata.value.period
   
   

    if  (formatDash(filterStore.date_period.enddate) !=formatDash(new Date())) {
      filtr = filtr.filter(e => e.visitdate != formatDash(new Date()))
      }

      filtr.forEach((e) => {
     
      periodusers.add(e.user.id)
      if (!brdata[e.visitdate]) {
        brdata[e.visitdate] =  {}

      }
      let user = splitname(e.user)
      if (!brdata[e.visitdate][user]) {
        brdata[e.visitdate][user] =  []
      }
      brdata[e.visitdate][user].push({page:e.fullPath, total:e.count})
      

    }) 

    let traffic ={}

    for (let [key, val] of Object.entries(brdata)) {
      traffic[key] ={unic: Object.keys(val), count: 0, br:0, pages: 0}

      let arr = Object.values(val)
      traffic[key].br = arr.filter(e=>e.length==1).length
      arr.forEach(e=> traffic[key].pages += e.length)
      arr.flat().reduce((acc, item) => {
        
        traffic[key].count +=item.total
       
        return acc
      },traffic[key].count)
      
    }


    sumtraffic(traffic)
    dataLineChart.value =  traffic
  }

  const getCRR = (val) => {
  
    cardtotal.value.crr.data = val
 
  }

  const sumtraffic= (data) => {

    let ob = {brtot:0, ppvtot: 0, unictot: 0, pagetot: 0}
    Object.values(data).flat().forEach((e) => {
      ob.brtot += e.br
      ob.ppvtot += e.count
      ob.unictot += e.unic.length
      ob.pagetot += e.pages
     
    }

    )

    cardtotal.value.br.data = ob.brtot/ob.unictot*100
    cardtotal.value.ppv.data = ob.pagetot/ob.unictot
    
  }

  watch(()=>filterStore.date_period,()=>{
   
        visition()

      
    }, {deep:true})

  pagecounter()

  

  return {
    alldata,
    cardtotal,
    dataLineChart,
    filterStore,
    getCRR,
    filter: ref('d'),
   
    
  }


 
}
   
}

</script>

<style>

</style>