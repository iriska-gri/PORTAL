<template>
    <v-dialog
        v-model="mydialog"
        persistent
        width="600"
        class="mx-auto"
    > 
        <v-card height="500">
            <v-card-title class="pl-6">
                Информация
            </v-card-title>
            <v-divider/>
            <v-card-text>
                <v-row
                    no-gutters
                    class="flex-grow-0"
                >
                    <v-col lg=4>
                        <v-img
                            cover
                            min-height="222px"
                            max-height="222px"
                            :src="checkremote(`${spravURL}${author.login}.jpg`)"
                        />
                     
                    </v-col>
                    <v-col class="d-flex flex-column">
                        <v-row
                            no-gutters
                            class="flex-grow-0 mx-3 my-1"
                            v-for="n in basicInformation()"
                            :key="n"
                        >
                            <v-col>
                                <span class="font-weight-medium">
                                    {{n.title}}
                                </span>
                                <br/>
                                <span class="text-subtitle-1">
                                    {{n.info}}
                                </span>
                            </v-col>
                        </v-row>
                    </v-col>
                </v-row>
            </v-card-text>
            <v-divider/>
            <v-card-text class="d-flex flex-column py-2">
                <v-row
                    no-gutters
                    class="flex-grow-0"
                    v-for="n in subInformation()"
                    :key="n"
                >
                    <v-col>
                        <span class="font-weight-medium">
                            {{n.title}}
                        </span>
                        <span class="text-subtitle-1">
                            {{n.info}}
                        </span>
                    </v-col>
                </v-row>
            </v-card-text>
            <v-divider/>
            <v-card-actions class="align-self-end py-0">
                <v-btn
                    color="modal_btn"
                    variant="text"
                    @click= "$emit('update:opendialog', value)"
                >
                    Закрыть
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
import { computed } from 'vue'
import { checkremote } from '@/utils/universal_functions'
import { spravURL } from '@/utils/axios-api'

export default {

    name: "InfoUserCard",

    props: {

        opendialog: {
            type: Boolean,
            default: false
        },

        author: {
            type: Object,
            default: {}
        }
    },

    setup (props, {emit}) {

        const mydialog = computed({
            get: () => props.opendialog, 
            set: (value) => emit('update:opendialog', value) 
        }) 

        const basicInformation = () => [
            {title: 'Отдел:', info: props.author.department},
            {title: 'ФИО:', info: props.author.fio},
            {title: 'Должность:', info: props.author.post},
        ]

        const subInformation = () => [
            {title: 'E-mail: ', info: props.author.email},
            {title: 'Телефон: ', info: props.author.tel},
            {title: 'Комната: ', info: props.author.room},
            {title: 'Логин: ', info: props.author.login},
        ]

        return {
            mydialog,
            spravURL,
            checkremote,
            basicInformation,
            subInformation
        }
    }
}
</script>

<style>

</style>