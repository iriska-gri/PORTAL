<template>
  <pattern-card
    :title="'Посещаемость портала'"
    :ico="'mdi-walk'"
  >
    <template v-slot:filling>
      <v-table class="text-subtitle-2 table_traffic pt-1">
        <thead>
          <tr>
            <th class="pr-0"></th>
            <th class="text-center px-1">сегодня</th>
            <th class="text-center">за период</th>
          </tr>
        </thead>
        <tbody class="text-button">
          <tr> 
            <td>
              <tooltip-ico :info=traffic.user />
            </td> 
            <td :class="csstext()">
            <!-- -->
              <tooltip-user :info=traffic.user.today />
            </td>
            <td :class="csstext()">
              <tooltip-user :info=traffic.user.period />
            </td>
          </tr> 
          <tr> 
            <td>
              <tooltip-ico :info=traffic.proc />
            </td> 
            <td :class="cssproc()">
            {{traffic.proc.today}}%
            </td>
            <td :class="cssproc()">
              {{traffic.proc.period}}%
            </td>
          </tr>       
          <tr> 
            <td>
              <tooltip-ico :info=traffic.before />
            </td> 
            <td >

            </td>
            <td :class="cssproc()">
              <v-icon
                v-if="parseFloat((traffic.user.period.length * 100 /traffic.before.period).toFixed(2))-100 != 'Infinity' && parseFloat((traffic.user.period.length * 100 /traffic.before.period).toFixed(2))-100 != 0"
                size="x-small"
                :class="traffic.before.period<traffic.user.period.length?'pb-1':'pt-0'"
                :color="traffic.before.period<traffic.user.period.length?'green-darken-2':'deep-orange-darken-4'"
                :icon="traffic.before.period<traffic.user.period.length?'mdi-arrow-up-bold':'mdi-arrow-down-bold'"
              />
     
              <span v-if="traffic.before.period!=0">

                {{parseFloat(((traffic.user.period.length * 100 /traffic.before.period)-100).toFixed(2))}} %
              </span>
              <span v-else>
                0%
              </span>
            
            </td>
          </tr>    
          
          
        </tbody>
      </v-table>
    </template>
  </pattern-card>
</template>

<script>
import PatternCard from '@/components/UI/aboutportal/pattern-card.vue'
import { ref, computed } from 'vue'
import {formatDash, splitname, checking_for_entry} from '@/utils/universal_functions'
import { usePortalFilterStore } from '@/store/AboutPortalFilter'
import moment from 'moment'
import TooltipIco from '@/components/UI/aboutportal/tooltip-ico.vue'
import TooltipUser from '@/components/UI/aboutportal/tooltip-user.vue'
export default {

  components: {
    PatternCard,
    TooltipIco,
    TooltipUser
  },

    props: {

      alldata: {
        type: Object,
            default: () => {return {period: [], staff: 0}}
      },

       
},
    setup(props) {
      const filterStore = usePortalFilterStore()
      const traffic = computed({
        get() {


let res = {
  "user": {
    "tooltip": "Уникальные пользователи",
    "today": [],
    "period": [],
    "ico": "mdi-account-box",
    "color" : "indigo"
  },
  "proc": {
    "tooltip": "% от штата",
    "today": 0,
    "period": 0,
    "ico": "mdi-chart-pie",
    "color" : "green"
  },

  "before": {
    "tooltip":"По сравнению предыдущим периодом",
    "today": "",
    "period": 0,
    "ico": "mdi-elevation-rise",
    "color" : "pink-darken-4"
  }
  
}


          
          props.alldata.period.forEach(e => { 
        
            if (e.visitdate == formatDash(new Date())) {
                checking_for_entry(res.user.today, splitname(e.user)) 
            }
            if (new Date(e.visitdate) <= filterStore.date_period.enddate) {
              checking_for_entry(res.user.period, splitname(e.user)) 
            }
            
          })
        //   res.before.user=res.period.user
          res.proc.today = parseFloat(((res.user.today.length * 100) / props.alldata.staff).toFixed(2))
          res.proc.period = parseFloat(((res.user.period.length * 100) / props.alldata.staff).toFixed(2))
          // res.proc.tooltip =`% от штата (${props.alldata.staff} сотрудников не конец выбранного периода)` 
          let data1 = moment(filterStore.date_period.enddate)
          let data2 = moment(filterStore.date_period.startdate)
          let between = data1.diff(data2, 'days') + 1
  
          
          props.alldata.beforperiod.filter( e=> data2.diff(moment(e.visitdate), 'days') <  between).reduce((acc, item) => {
            res.before.period += item.user.length
            return acc
          }, res.before.period)

         return res
        }
      })
      const csstext = () => {
        return 'text-center px-0 font-weight-bold text-subtitle-1 cursor-help text-grey-darken-3'
      }

      const cssproc = () => {
        return 'text-center font-weight-bold text-subtitle-1 text-grey-darken-3 cursor-default'
      }

        return {
          traffic,
          csstext,
          cssproc
        }
    }

}
</script>

<style>
.v-table > .v-table__wrapper > table > tbody > tr > td 
{
  padding: 0 0 0px;
}
</style>