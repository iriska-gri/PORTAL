<template>
    <div>
        <v-card 
            class="bg-transparent" 
            density="compact" 
            :prepend-avatar="checkremote(`${spravURL}${author.login}.jpg`)"
            :title="author.fio" 
            :subtitle="author.post" 
            variant="text" @click="open=true"
        />
        <info-user-card
            :author=author
            :opendialog = open
            @update:opendialog="open = $event"
        />
    </div>
       
</template>

<script>
import { ref } from 'vue'
import {checkremote} from '@/utils/universal_functions'
import { spravURL } from '@/utils/axios-api'

export default {
    props: {
        author: {
            type: Object,
            default: {}
        },
    },
    setup(){

      const open = ref(false)
      return {
        open, 
        checkremote,
        spravURL
    }
    }
}
</script>

<style>

</style>