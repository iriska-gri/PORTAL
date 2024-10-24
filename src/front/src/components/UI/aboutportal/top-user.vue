<template>
  <pattern-card
    :title="'Самые активные пользователи'"
    :ico="'mdi-star-circle'"
  >

    <template v-slot:filling>

 

      <v-data-table-virtual
        v-model:expanded="expanded"
        :headers="dessertHeaders"
        :items="dataActivusers"
        item-value="user"
        show-expand
        class="h-0 cursor-default  bg-grey_white"     
        :sort-by="[{ key: 'info.count', order: 'desc' }]"
        density="comfortable"
      >
        <template v-slot:item.user="{ value }">
  
          <list-user
            :author=value
            :from_which = "'top-user'"
          />
        </template>

        <template v-slot:headers="{ columns, isSorted, getSortIcon, toggleSort }">
          <tr>
           
            <template v-for="column in columns" :key="column.key">
              <td class="pa-0 py-2 pb-3"  >
                
                <v-tooltip location="top" v-if="column.title!=''">
                  <template v-slot:activator="{ props }">
                    <v-btn
                      v-bind="props"
                    
                      :append-icon="isSorted(column)?getSortIcon(column):''"
                      variant="text"
                      class="text-caption"
                      @click="() => toggleSort(column)"
                    >
                    {{ column.title }}
                    
                      <template v-slot:append>
                        <v-icon size="x-small"></v-icon>
                      </template>
                      </v-btn>
                     
                    </template>
                  <span>{{ column.tooltip }} </span>
                </v-tooltip>
              
              </td>
            </template>
            
          </tr>
          
        </template>
        <template v-slot:expanded-row="{ columns, item }">

          <tr>
            
            <td :colspan="columns.length">
              
              <v-card class="my-2 elevation-0" color='grey'>
                <v-divider/>
                  <v-data-table
                    
                    :headers="subtable"
                    :items="item.tooltip"
                    items-per-page=-1
                    class="subtable cursor-default px-3 bg-grey-lighten-5 text-body-2"     
                    density="compact"
                    :sort-by="[{ key: 'count', order: 'desc' }]"
                  >
                  <template v-slot:headers="{ columns, isSorted, getSortIcon, toggleSort }">
          <tr>
            <template v-for="column in columns" :key="column.key">
              <td class="pa-0">
                <v-btn
                  :append-icon="isSorted(column)?getSortIcon(column):''"
                  variant="text"
                  class="text-caption"
                  @click="() => toggleSort(column)"
                >
                  {{ column.title }}
                  <template v-slot:append>
                    <v-icon size="x-small"></v-icon>
                  </template>
                </v-btn>
          
              </td>
            </template>
          </tr>
        </template>
        <template v-slot:item.count="{ value }">
        <span :class="'text-'+getColor2(value) " class="font-weight-medium text-subtitle-2">
          {{ value }}
        </span>
      </template>

      <template v-slot:item.unic="{ value }">
        <span :class="'text-'+getColor(value) " class="font-weight-medium text-subtitle-2">
          {{ value }}
        </span>
      </template>
      

              </v-data-table>
        </v-card>
          


        </td>
      </tr>
    </template>
        
        </v-data-table-virtual>
    </template>
  </pattern-card>
</template>

<script>
import { ref, computed } from 'vue'
import { spravURL } from '@/utils/axios-api'
import {checkremote} from '@/utils/universal_functions'
import PatternCard from '@/components/UI/aboutportal/pattern-card.vue'

export default {
  components: {
    PatternCard
  },

  props: {

    activusers: {
      type: Object,
      default: {}
    },


  },
  
  setup(props) {

    const desserts = [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: 1,
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: 1,
          }]
    
    const dataActivusers = computed({
      get() {
        let res = []
        
        props.activusers.forEach((e) => {
       
          let ind = res.findIndex(el => el.user.id == e.user.id)
          if (ind == -1) {
            res.push({user: e.user,
              info: {
                count: e.count,
                session:new Set([e.visitdate]),
                pages: 1
              },
              tooltip: [{
                  namepages: e.pages,
                  count: e.count,
                  unic: 1
                }]
            })
     
          }
          
          else {
            let ob =res[ind]
            ob.info.count += e.count,
            ob.info.session.add(e.visitdate)
            ob.info.pages += 1
           
            let indt = ob.tooltip.findIndex(elem => 
              elem.namepages === e.pages)
         
            if (indt == -1) {
              ob.tooltip.push({
                  namepages: e.pages,
                  count: e.count,
                  unic: 1
              })
            }
            else {

              ob.tooltip[indt].count += e.count
              ob.tooltip[indt].unic += 1
            }
          }
          
          
          
        })
        return res
      }
    })

    const expanded = ref([])

    const dessertHeaders = [
          {
            title: '',
            align: '',
            sortable: false,
            key: 'user',

          },

          { title: 'просмотры', align: 'start', key: 'info.count', tooltip: 'Количество посещенных страниц за период' },
          { title: 'сессии', align: 'start', key: 'info.session.size', tooltip: 'Сколько дней посещали Портал за период'},
          { title: 'страницы', align: 'start', key: 'info.pages', tooltip: 'Сколько суммарно посещено уникальных страниц за период' },

          
        ]

      const subtable = [
      {
            title: '',
            align: 'start',
            sortable: false,
            key: 'namepages',
            width: '60%',
            maxWidth: '60%', 
            minWidth: '60%',
          },        
          { title: 'всего', align: 'center', key: 'count', width: '20%', maxWidth: '20%'
            },
        { title:'уникальных' , align: 'center', key: 'unic', width: '20%', maxWidth: '20%'
           },



      ]




      const getColor = (pages) => {
        if (pages > 100) return 'green'
        else if (pages > 50) return 'orange'
        else return 'red'
      }

      const getColor2 = (pages) => {
        if (pages > 10) return 'green'
        else if (pages > 5) return 'orange'
        else return 'red'
      }

      

    return {
      checkremote,
      spravURL,
      expanded,
      dessertHeaders,
      dataActivusers,
      subtable,
      getColor,
      getColor2,
      desserts
 
    }
  }
}
</script>

<style>
.subtable .v-data-table-footer {
  display: none
}

.subtable tbody {
  text-align: start!important;
}


</style>