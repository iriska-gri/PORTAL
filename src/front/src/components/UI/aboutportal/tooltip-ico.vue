<template>
  
  <v-tooltip location="top" >
                <template v-slot:activator="{ props }">
                  <span v-bind="props" >
                    <v-icon
                      class="cursor-help "
                        size="large"
                        :color="info.color"
                        :icon="info.ico"
                    />
                  </span>
                </template>
                <v-row 
        
                >
                  <v-col >
                    {{info.tooltip}}
                  </v-col>
                </v-row>
              </v-tooltip>
</template>

<script>
export default {
props: {
    info: {
        type: Object,
        default: () => {return {tooltip: '', ico: '', color: ''}}
    }

    
},

    setup(props) {

        return {
          
        }
    }

}
</script>

<style>

</style>