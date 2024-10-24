<template>
    <div>
        <v-row
            v-for="(x, key) in rating.basecrit"
            :key = key
            class="align-center"
        >
            <v-col
                class="pl-5"
                lg=5
            >
                <v-icon
                    size="large"
                    :color="x.color"
                    :icon="x.ico"
                />
                    {{x.name}}
            </v-col>
            <v-col lg=6 class="pa-0">
                <v-rating
                    v-model="message[key].rating"
                    :hover="typeof(key) == 'number'"
                    half-increments
                    color="yellow"
                    :density="'comfortable'"
                />
            </v-col>
            <v-divider/>
        </v-row>
    </div>
</template>

<script>

import { computed } from 'vue'

export default {

    props: {
        rating: {
            type: Object,
            default: () => {}
        },
    },

    setup(props, { emit }) { 
        

        const message = computed({ 
          get: () => props.rating.nowrating, 
          set: (value) => emit('update:rating', value) 
        }) 
    
        
    
        return { 
          message
        } 
    
    }    

}
</script>

<style>

</style>