// Utilities
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const usePortalFilterStore = defineStore('filter',  () => {

  const date_period = ref({ "startdate": new Date(new Date().getFullYear(), 0, 1),
                            "enddate": new Date(),
                        })

                                         
  return  { date_period }
  },


  
)


