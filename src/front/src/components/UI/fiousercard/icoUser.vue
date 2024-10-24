<template>
    <div>
        <v-icon
            size="x-small"
            class="me-1"
            icon="mdi-account"
            @click="open=true"
        />
            <span class="text-caption me-2">
                {{splitname(author)}} 
            </span>
            <info-user-card
                :author=author
                :opendialog = open
                @update:opendialog="open = $event"
            />
    </div>

</template>

<script>
import {splitname} from '@/utils/universal_functions'
import { ref } from 'vue'

export default {
    props: {
        author: {
            type: Object,
            default: {}
        }
    },
    setup() {
        const open = ref(false)
        return {
            splitname,
            open
        }
    }
}
</script>

<style>

</style>