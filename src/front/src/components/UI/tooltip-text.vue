<template>
    <v-tooltip
        location="bottom"
    >
        <template v-slot:activator="{ props }">
            <span v-bind="props" class="cursor-help">
                {{text}}
            </span>                     
        </template>
        <v-row 
            no-gutters 
        >
            <v-col>
                <slot name="tooltip"></slot>
            </v-col>
        </v-row>
    </v-tooltip>
</template>
  
<script>
  
export default {
    name: "TooltipText",
    props: {
        
        text: {
         
        },

    },
}
  
</script>

<style>

</style>