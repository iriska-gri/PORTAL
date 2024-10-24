<template>
    <v-card class="h-100 ">
        <Line
            v-if="data!==null"
            :data="data"
            ref ='linear'
            :options="options"
        />
    </v-card>
</template>

<script>

import moment from 'moment'
import {computed,ref} from 'vue'
import { usePortalFilterStore } from '@/store/AboutPortalFilter'
import {formatComa, formatDash} from '@/utils/universal_functions'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  TimeScale
} from 'chart.js'
import { Line } from 'vue-chartjs'
import ChartDataLabels from 'chartjs-plugin-datalabels'
import 'chartjs-adapter-moment'
ChartJS.register(
  ChartDataLabels,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  TimeScale
)

export default {

    components: {
        Line,
    },

    props: {

        dataLineChart: {
            type: Object,
            default: () => {}
        },

        period: {
            type: Object,
            default: () => {}
        },

        filter: {
            type: String,
            default: 'd'
        }
    }, 

    setup(props, {emit}) {
        const filterStore = usePortalFilterStore()
        const between = ref(0)
        const arrlines = {
            datasets: [
                {
                    label: 'Открыто страниц',
                    backgroundColor: '#C62828',
                    borderColor: '#C62828',
                    borderWidth: 3,
                    cubicInterpolationMode: 'monotone',
                    data: [], 
                    func: (val)=>{return val.count},
                    datakey:  "count",                     
                    tooltips: false   ,
                    hidden: true,
                    yAxisID: 'y'             
                },
                {
                    label: 'Активные пользователи',
                    backgroundColor: 'teal',
                    borderColor: 'teal',
                    borderWidth: 3,
                    cubicInterpolationMode: 'monotone',
                    data: [],
                    func: (val)=>{return val.unic.length},
                    datakey:  "unic", 
                    customlabel: [],
                    tooltips: true,
                    yAxisID: 'y'
                }
                ,
                {
                    label: 'CRR',
                    backgroundColor: '#673AB7',
                    borderColor: '#673AB7',
                    borderWidth: 3,
                    cubicInterpolationMode: 'monotone',
                    data: [],
                    func: (val, key)=>{ return  parseFloat(crrfunc(key).toFixed(2))},
                    hidden: true,
                    datakey:  "crr", 
                    customlabel: [],
                    tooltips: true,
                    yAxisID: 'y1'
                }
                ,
                {
                    label: 'BR',
                    backgroundColor: '#283593',
                    borderColor: '#283593',
                    borderWidth: 3,
                    cubicInterpolationMode: 'monotone',
                    data: [],
                    func: (val)=>{return parseFloat((val.br/val.unic.length*100).toFixed(2))},
                    datakey:  "br", 
                    hidden: true,
                    customlabel: [],
                    tooltips: true,
                    yAxisID: 'y1'
                }
                ,
                {
                    label: 'PPV',
                    backgroundColor: '#EF9A9A',
                    borderColor: '#EF9A9A',
                    borderWidth: 3,
                    cubicInterpolationMode: 'monotone',
                    data: [],
                    func: (val)=>{return parseFloat((val.pages/val.unic.length).toFixed(2))},
                    datakey:  "ppv", 
                    hidden: true,
                    customlabel: [],
                    tooltips: true,
                    yAxisID: 'y'
                }
            ]
        }

    const dataf=computed({get() {
        fullpercreate()        
        let data1 = moment(filterStore.date_period.enddate)
        let data2 = moment(filterStore.date_period.startdate)
        between.value = data1.diff(data2, 'days') + 1
        let res = null

        if (Object.keys(props.dataLineChart).length>0){
            res = arrlines
            res.labels=[]
            res.datasets.forEach((e) => {e.data =[]})
                for(let [key,val] of Object.entries(props.dataLineChart)) {
                    res.datasets.forEach((e) => {
                        e.data.push(e.func(val,key))          
                    });
                    res.labels.push(formatComa(key))
                }
            }
        return  res
    }})
       
    const  fullper = ref([])

    const fullpercreate = () => {
        let arr = []
        props.period.period.forEach((e) => {
            let ind = arr.findIndex(el => el.visitdate == e.visitdate)

            if (ind ==-1) {
                arr.push({visitdate: e.visitdate, user: Array.from(new Set([e.user.id]))})
            }
            else {
                arr[ind].user = Array.from(new Set(arr[ind].user).add(e.user.id))
            }
        })    

        fullper.value= [...props.period.before, ...arr]
    }
  
    const crrfunc = (date)=>{
     /**
     * Расчет значения crr, и передача в родительский компонент значения, на последнюю дату в периоде для компонента card-total
     * @constructor
     * @param {object} date - по каждому дню, в указанном периоде (пример - 2024-03-22)
     * @description Для расчетного периода с 04.03.2024 по 20.03.2024 выбирается три периода:
     * 30.01.2024 - 16.02.2024 - baseunic
     * 17.02.2024 - 03.03.2024 - crrunic
     * 04.03.2024 - 20.03.2024 - отсюда даты для расчета
     * bothuser - Пользователи которые были в baseunic и crrunic
     */
        
        let baseunic = unicperson(fullper.value.filter(e => new Date(e.visitdate) >moment(new Date(date)).subtract(between.value*2, 'd') &&  new Date(e.visitdate) <= moment(new Date(date)).subtract(between.value, 'd')))
        let crrunic = unicperson(fullper.value.filter(e => new Date(e.visitdate) >moment(new Date(date)).subtract(between.value, 'd') &&  new Date(e.visitdate) <= new Date(date)))
        let bothuser = new Set([...baseunic].filter(element => crrunic.has(element)))
      
        if (date ==formatDash(filterStore.date_period.enddate)) {
            editCRR(bothuser.size*100/baseunic.size)
        }
    
        return baseunic.size ==0?0:bothuser.size*100/baseunic.size 
    }  

    const editCRR  = (val) => {
      
        emit('getCRR', val)
    }
    
    const unicperson = (arr) => {
        
        let arrnew =[]
        arr.forEach(e => arrnew.push(...e.user) )
        return new Set(arrnew)
    }

    const data=computed({get() {
   
        return JSON.parse(JSON.stringify(dataf.value))
    }
        })
    const linear=ref(null)



    const options =  {

        plugins: {  
    
            datalabels: {
                color: 'grey',
                align: 'top',
                display: 'auto'
            },
            legend: {
                onHover: (event, chartElement) => {
                    event.native.target.style.cursor ='pointer' ;
                },
                onLeave: (event, chartElement) => {
                    event.native.target.style.cursor ='default' ;
                },
                position: 'bottom',
                labels: {
                    color: 'grey',
                    align: 'right',
              
                 

                    
                    
                 
                 
                }
            },


        },
        layout: {
            padding: {
                top: 35,
                bottom: 5,
                left: 20,
                right: 15
            }
        },
        scales: {
            x: {
                grid: {
                    color: 'white',
                }
            },

            y: {
                ticks: {
                    stepSize: 10,
                },
                offset: true,
                grid: {
                    color: 'white',
                }
            },
            y1: {
               
                type: 'linear',
                display: true,
                position: 'right',
            },
        },

        responsive: true,
        maintainAspectRatio: false

        }

       
    

            return {
                data,
                options,
                linear
            }
        }
}
</script>

<style>

canvas {
    flex: 1!important
}

.chartjs-legend {
    cursor: pointer
}
</style>