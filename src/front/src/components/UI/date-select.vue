<template>
    <v-menu
        v-model="menudate"
        :close-on-content-click="false"
        :nudge-right="40"
        transition="scale-transition"
        offset-y
    >
        <template v-slot:activator="{ props }">
            <v-textarea
                v-model="selectedDate"
                :value="formatComa(datedefault)"
                no-resize
                class="my-textarea"
                rows="1"
                hide-details
                style="width:119px"
                variant="plain"
                density="compact"
                v-bind="props"
            >
                <template v-slot:prepend-inner>                
                    <v-icon
                        v-bind="props" 
                        icon='mdi-calendar-today'
                        color="cyan-darken-3"
                        size="x-small"
                        
                    />                                
                </template>
            </v-textarea>
        </template>
        <v-locale-provider locale="ru">
            <v-date-picker
                v-model="selectedDate"
                show-adjacent-months
                hide-header
                @update:modelValue="dateStart"
                border
                :max="formatDash(new Date())"
                :min="formatDash(appStore.countvisitor.visitdate)"
            />

        </v-locale-provider>
    </v-menu>
</template>

<script>

import { ref } from 'vue'
import {formatComa, formatDash} from '@/utils/universal_functions'
import { useAppStore } from '@/store/app'
export default {

    props: {
        datedefault: {
            type: Date,
            default: ''
        }
    },

    

    setup(props, {emit}) {
        const appStore = useAppStore()
        const maxdate = formatDash(new Date())
        const menudate = ref(false)
        const selectedDate = ref(null)
             
        const dateStart = () => {
            emit('returndate', selectedDate.value)
            menudate.value=false
        }



        return {
            menudate,
            selectedDate,
            dateStart,
            formatComa,
            formatDash,
            appStore,
        }
    }

}
</script>

<style>
.my-textarea textarea {
    color: rgb(28, 28, 41) !important;
    font-size: 18px;
    text-align-last: center;
    font-weight: bold;
    }

    .my-textarea .v-field__prepend-inner > .v-icon {
        opacity: 1;
    }

    .v-field__prepend-inner {
    align-items: center!important;
    }
</style>