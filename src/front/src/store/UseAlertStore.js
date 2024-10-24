import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAlertStore = defineStore('uniAlert',  () => {

    const alert = ref({ "alert": false,
                        "text": '',
                        "ico": 'mdi-plus',
                        "color": ''
                      })
                         
    return  { alert }

})