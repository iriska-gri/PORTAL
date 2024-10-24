<template>

                <v-carousel
                
                    cover
                    :height="carushi"
                    hide-delimiters
                    hide-delimiter-background
                    show-arrows="hover"
                    color="white"
                 
    
                  
                  
                >
    
                
                <v-carousel-item
                  v-for="(x, i) in carous"  :key="i"
                  :src="`${burl}${x.link}`"
                  cover
                  eager
                >

                <v-container
                    fill-height
                    fluid
                    pa-0 ma-0 pb-3 
                    class="flex-column h-100 d-flex"
                >
                
                <v-card class="bgCard h-100 d-flex flex-column">
  <v-card-title class="ma-2 text-h3 text-uppercase titles py-5 flex-column">
                    <v-row>
                        <v-col class="pa-0 pl-1 align-self-center">{{x.title}} 
                         </v-col>
                      
                        <v-col class="flex-grow-0 pa-0 pr-1">
                            <v-img
       
        width="50"
        :aspect-ratio="1"
        :src="`${burl}${x.sender}`"
        cover
      />
                        </v-col>
                    </v-row>
                    
                    
                </v-card-title>
                    <v-card-text v-if="'text' in x && x.text.length>0" class="ml-2 mb-0 mb-2 flex-grow-0 pb-3 text-h6 h-100 pl-3 py-3 mr-1 ">
                    <v-row>

                   
                        <v-col cols=6 class=" bgText">
                        <v-textarea
                    class="mt-n3 text-black textareas pt-2 font-weight-medium"
                    :model-value=x.text
                    variant='plain'
                    readonly
                    auto-grow
                    rows="1"
                  
                    hide-details
                    
                    
      

                    />
                    
                    </v-col>
                    

                    <v-col cols=6 class=" bgText">
                        <v-img
       
      
       :aspect-ratio="1"
       :src="`${burl}${x.link2}`"
     
     />
                    
                    </v-col>
                    
         
                </v-row>
                  
                </v-card-text>
                </v-card>
                    
             
                        </v-container>
                        
                </v-carousel-item>
    
              </v-carousel>
    
    </template>
    
    <script>
    import { ref, computed } from 'vue'
    import {getfromserver} from '@/utils/universal_functions'
    import { baseURL } from '@/utils/axios-api'
    import { axiosApiInstance } from '@/utils/axios-api'
    
    
    
    export default {
    
        setup() {
            const burl = baseURL.slice(0,-1)
            const carous=ref([{link: ""}])
    
            axiosApiInstance.get(`api/fns/links/`).then(data => {      
                carous.value= data.data  
                  
                // t_dailyRound.value = data.data

                // result.value=JSON.parse(JSON.stringify(data.data.daily))

            })
        // getfromserver("api/fns/links/", carous)
        
        const carushi =  computed(()=> {
        
                return window.innerHeight-50
                
        })
     
            return { burl, carous, carushi}
        }

        

    
    }
    </script>
    
    <style>
    .bgCard {
        /* #ffffff6b #ffffff8c*/
        background: #ffffff38 ;
    }
    
    .bgText {
        background:  #ffffffb0;
       line-height: 3.1rem!important;
     
    }
    
    .titles {
        /* font-family: cursive !important; */
        background: #ffffff8c;
    }
    
    .textareas .v-field__input {
    
        font-size: 2.5em!important;
    }
    </style>