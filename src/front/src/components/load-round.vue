<template>
    <v-row no-gutters class="gap ma-3 flex-column">
        <v-col lg=2 class='w100  d-flex flex-column'>
            <v-row no-gutters class="gap">
                <v-col lg=4>
                    <v-card class="h-100">
                        <v-card-title>
                            Ежедневная статистика по сотрудникам 
                        </v-card-title>
                        <v-row no-gutters class="gap">
                            <v-col class="flex-grow-0">
                                <v-card-subtitle class="mt-2 align-self-end">
                                    1. Скачать файл ежедневной статистики 
                                </v-card-subtitle>
                            </v-col>
                            <v-col class="flex-grow-0">
                                <v-icon
                                    icon="mdi-file-excel" 
                                    color="green-darken-3"
                                    @click="excelOp('excround')"
                                />
                            </v-col>
                        </v-row>
                        <v-row no-gutters class="gap mt-5">
                            <v-col class="flex-grow-0">
                                <v-card-subtitle class="mt-3 align-self-end">
                                    2. Загрузить данные на сервер  
                                </v-card-subtitle>
                            </v-col>
                            <v-col >
                                <v-file-input 
                                    accept=".xlsx"
                                    v-model="dailyfiles"
                                    variant="underlined"
                                    density="compact"
                                    label="Прикрепить файл" 
                                    hide-details
                                />
                            </v-col>
                            <v-col class="flex-grow-0 pr-2">
                                <v-icon
                                    icon="mdi-chevron-double-right"
                                    color="blue-grey-darken-2"
                                    @click="onPickFile('roundfilse')"
                                />
                            </v-col>
                        </v-row>
                    </v-card>
                </v-col>         
            </v-row>
        </v-col>
    </v-row>
</template>

<script>
import { ref } from 'vue'
import { baseURL } from '@/utils/axios-api'
import { axiosApiInstance } from '@/utils/axios-api'
import { useAlertStore } from '@/store/useAlertStore'

export default {

    setup(){ 

        const dailyfiles = ref([])
        const feedalert = useAlertStore().alert

        const excelOp = (ex) => {
            axiosApiInstance.get(`api/general_vacation/dailyroundup/?excel=${ex}`).then(result => {  
                let link = document.createElement("a")
                link.href = baseURL+result.data.path
                link.click()
                link.remove()
            })
        }

        const onPickFile = (ex) => {
            const sdata = new FormData()
            sdata.append('dailyfiles', dailyfiles.value[0])

            axiosApiInstance.post(`api/general_vacation/dailyroundup/?excel=${ex}`, sdata).then(result => {  
                textFromAlert(result.data['mess'])
            })
            dailyfiles.value = []
        }

        const textFromAlert = (info) => {
            feedalert.alert = true
            if (info == "Файл загружен") {
                feedalert.text = "Файл загружен"
                feedalert.ico = "mdi-check"
                feedalert.color ="green-darken-4"
            }
            else  {
                feedalert.text = "Ошибка загрузки"
                feedalert.ico = "mdi-alert-circle-outline"
                feedalert.color="pink-accent-4"
            }
        }

    return {
        excelOp,
        baseURL,
        dailyfiles,
        onPickFile,
        feedalert
        }
    }

}
</script>

<style>
.mhight {
    height: 150px;
}


</style>