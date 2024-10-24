<template>
    <!-- <v-row class="pa-2">
        <v-col cols="5" class="d-flex flex-column justify-start h-screen gap">
            <v-card v-for="item in safetyData" :key="item.id" class="overflow-y-auto mb-2 h-auto">
                <v-card-title>{{ item.name }}</v-card-title>                
                    <v-container
                            v-for="category in item.categories" 
                            :key="item.id + category.id"
                            :fluid="true"
                            class="py-0">
                        <v-card-actions>
                            <v-btn @click="showMore[item.id + category.id] = !showMore[item.id + category.id]" variant="text">{{ category.name }}</v-btn>
                            <v-btn 
                                :icon="showMore[item.id + category.id] ? 'mdi-chevron-up' : 'mdi-chevron-down'" 
                                @click="showMore[item.id + category.id] = !showMore[item.id + category.id]">
                            </v-btn>
                        </v-card-actions>
                        <v-expand-transition>
                        <div v-show="showMore[item.id + category.id]">
                            <v-card-actions v-for="file in category.files" :key="file.id" class="overflow-y-auto">
                                <v-card-text>{{ file.name }}</v-card-text>
                                <v-btn icon="mdi-file-pdf-box" color="red" @click="openPDF(safetyURL + file.url), loading=true"></v-btn>                 
                                <v-btn  icon='mdi-file-download-outline' color="green" @click="downloadItem(safetyURL + file.url, file.name)"></v-btn>
                            </v-card-actions>
                        </div>
                        </v-expand-transition>
                    </v-container>
            </v-card>
        </v-col> 
        <v-col cols="7">
            <v-card v-show="showFile" class="h-screen overflow-y-auto">
                <v-container v-if="loading">
                <v-progress-linear
                    :rounded="5"
                    indeterminate
                    color="teal">
                </v-progress-linear>
                </v-container>
                <VuePdfEmbed :source="pdfSource" width="720" @rendered="loading = false"/>
                <v-card-actions>
                    <v-btn block @click="showFile = false">Закрыть</v-btn>
                </v-card-actions>
            </v-card>
        </v-col>
    </v-row> -->
    <!-- <v-dialog v-model="showFile" width="auto" height="auto">
        <v-card>
            <v-container v-if="loading">
                <v-progress-linear
                    :rounded="5"
                    indeterminate
                    color="teal">
                </v-progress-linear>
            </v-container>
                <VuePdfEmbed :source="pdfSource" width="725" height="400" @rendered="loading = false"/>
            <v-card-actions>
                <v-btn block @click="showFile = false">Закрыть</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog> -->
</template>

<script setup>
// import { ref, onBeforeMount } from 'vue';
// import { pagecounter } from '@/utils/universal_functions';
// import { axiosApiInstance, safetyURL } from '@/utils/axios-api';
// import { saveAs } from 'file-saver';
// import VuePdfEmbed from 'vue-pdf-embed';

// pagecounter();

// const safetyData = ref([]);
// const showMore = ref(false);
// const showFile = ref(false);
// let pdfSource = '';
// const loading = ref(false)

// onBeforeMount(() => {
//     axiosApiInstance.get(`api/safety/files/`).then(result => {
//         safetyData.value = result.data
//     })
// });

// // Проверяем по ID на какой категории срабатывает клик на раскрытии/скрытии, чтобы избежать срабатывания у всех категорий одновременно
// showMore.value = safetyData.value.reduce((acc, value) => {
//     acc[value.id] = false
//     return acc
// }, {});

// const downloadItem = (url, fileName) => {
//     axiosApiInstance.get(url, {responseType: 'blob'})
//     .then(response => {
//         saveAs(response.data, fileName)
//     })
// };

// function openPDF(url) {
//     showFile.value = true
//     if (showFile) {
//         return pdfSource = url
//     }
// };
</script>

<style>
</style>