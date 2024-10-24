<template>
    <v-row>
        <v-col cols="12">
            <v-card>
                <v-window v-model="step">
                    <v-window-item v-for="(item, index) in data" :key="index">
                        <v-card v-if="item.question" :title="item.question">
                            <v-radio-group v-model="radios" label="Выберите вариант ответа">
                                <v-radio v-for="answer in item.answers" :label="answer" :value="answer"></v-radio>
                            </v-radio-group>
                        </v-card>
                        <v-card v-if="item.checkQuestion" :title="item.checkQuestion">
                            <v-checkbox
                                v-for="answer in item.answers" 
                                v-model="checks"
                                :label="answer"
                                :value="answer">
                            </v-checkbox>
                        </v-card>
                    </v-window-item>
                </v-window>
                <v-card-actions>
                    <v-btn
                        v-if="step > 0"
                        variant="text"
                        @click="step--">
                            Back
                    </v-btn>
                    <v-spacer></v-spacer>
                    <v-btn
                        v-if="step < data.length"
                        variant="text"
                        @click="step++">
                        Next
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-col>
    </v-row>
    <v-row>
        <v-col>
            <v-card title="Результат">
                <v-container>
                    <p>Количество баллов: {{ selected }}</p>
                </v-container>
            </v-card>
        </v-col>
    </v-row>
</template>

<script setup>
import { ref } from 'vue';

// TODO...
//  Рабочий вариант с пропсами, пытаюсь реализовать компонент на пропсах
defineProps({
    data: Array
})

const data = ref([
    {
        question: 'Вопрос 1',
        answers: ['1', '2', '3', '4']
    }, 
    {
        question: 'Вопрос 2',
        answers: ['Rer', 'LoL', 'Fort', 'FullG']
    },
    {
        checkQuestion: 'Вопрос с чексбоксом',
        answers: ['Кукумбер', 'Сикельд']
    }
])

const radios = ref('')
const checks = ref([])
const selected = ref([])
const step = ref(0)
</script>