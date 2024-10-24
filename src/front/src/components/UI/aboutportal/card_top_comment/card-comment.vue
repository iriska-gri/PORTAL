<template>
    <v-card max-width='400' density="compact" class="bg-transparent">
        <v-card-text class="pb-0">Оставлено комментариев</v-card-text>
        <v-card-subtitle>Последний комментарий оставлен {{formaComaTime(comment.time_create)}}</v-card-subtitle>
        
        <v-card-text class="text-caption">
            {{comment.comment}}
        </v-card-text>
        <!-- <v-card-title class="text-wrap"></v-card-title> -->
    </v-card>
</template>

<script>
import {formaComaTime} from '@/utils/universal_functions'

export default {

    props: {
        comment: {
            type: Object,
            default: () => {}
        }
    },

    setup() { 

        return {
            formaComaTime
        }
    }

}
</script>

<style>

</style>