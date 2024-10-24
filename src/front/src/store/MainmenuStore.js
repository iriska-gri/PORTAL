import { defineStore } from 'pinia'
import {ref, watch} from 'vue'
import { clearAxios } from '@/utils/axios-api'

export const useMainmenuStore = defineStore('MainmenuStore',  () => {
      const portallinks = ref([])

    const loadlinks=async()=>{
        const res = await clearAxios.get('api/navigation/links/') 
        portallinks.value=res.data
    }
    return {portallinks,loadlinks}
})
