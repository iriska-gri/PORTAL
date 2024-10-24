<template>
    <v-toolbar
        density="compact"
        class="text-h6 font-weight-regular"
    >
        <v-icon
            icon="mdi-poll"
            color="cyan-darken-3"
            class="mx-2"
        />
            Статистика портала за период с
        <div class="px-2 pb-1">
            <date-select
                @returndate="returnstart"
                :datedefault = "filterStore.date_period.startdate"
            />
        </div>
            по
        <div class="px-2 pb-1">
            <date-select
                @returndate="returnend"
                :datedefault = "filterStore.date_period.enddate"
            />
        </div>
        <div  class="text-caption font-weight-regular">
       ({{nStaff}} активных учетных записей)
        </div>
    </v-toolbar>
</template>

<script>
import DateSelect from '@/components/UI/date-select.vue'
import { usePortalFilterStore } from '@/store/AboutPortalFilter'

export default {
    components: {
        DateSelect
    },

    props: {
        nStaff: {
            type: Number,
            default: 0
        }
        // alldata: {
        //     type: Object,
        //     default: () => {return {period: [], staff: 0}}
        // },
},
    setup(){

        const filterStore = usePortalFilterStore()

        const returnstart = (dates) => {
            filterStore.date_period.startdate = dates
        }

        const returnend = (dates) => {
            filterStore.date_period.enddate = dates        
        }

    return {
        returnstart,
        returnend,
        filterStore
    }
    
    }
}
</script>

<style>

</style>