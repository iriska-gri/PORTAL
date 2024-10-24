// Utilities
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAppStore = defineStore('app',  () => {
  const loading = ref(false)
  const countvisitor = ref({ "totalvisit": 0,
                              "visittoday":0,
                              "uniqtoday" : 0,
                              "visitdate" : '2024-01-01'
                            })
  return  {loading,countvisitor}
 
  },
)
