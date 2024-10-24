<template>
    <v-card class="h-100 d-flex" variant="flat">

       <v-row no-gutters class="flex-column gap">
        <v-col class="flex-grow-0 bg-teal-lighten-5 pa-0 w100">
            <span class="font-weight-medium text-button text-teal-darken-4 cursor-default">
                {{title}} 
        </span>
          
        </v-col>
        <v-col class="d-flex flex-column pa-0">
            <slot name="filling_feedback"></slot>
        </v-col>
       </v-row>
          
    </v-card>
    </template>
    
    <script>
    export default {
        props: {
    
    title: {
        type: String,
        default: ''
    },
}
    }
    </script>
    
    <style>
    
    </style>