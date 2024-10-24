<template>
    <v-card class="text-center text-blue-grey-darken-4 d-flex h-100 flex-column cursor-default justify-center">
       
        <v-row no-gutters class="flex-grow-0 ">
            <v-col class="text-h5 font-weight-bold pl-5">
                {{indicator.title}}
                <v-tooltip width="250">
            <template v-slot:activator="{ props }">
                <v-icon
                    icon="mdi-information"
                    color="cyan-darken-3"
                    size="12"
                    v-bind="props"
                    class="align-self-end pr-2 pb-5 cursor-help"
                />
            </template>
            <span class="text-caption" >
                {{indicator.tooltip}}
            </span>
        </v-tooltip>
            </v-col>
        </v-row>
        <v-row no-gutters class="flex-grow-0">
            <v-col class="text-h6 font-weight-medium">
                {{indicator.abb}}
                
            </v-col>
        </v-row>
        <v-row no-gutters class="flex-grow-0 pt-3">
            <v-col  class="text-h3 text-grey-darken-3 text-center font-weight-regular align-self-center">

                <vue3-autocounter
                    v-if="!Number.isNaN(indicator.data)"
                    ref='counter'
                    :startAmount='0'
                    :endAmount='indicator.data'
                    :duration='1'
                    :decimals="Number.isInteger(indicator.data)?0:2"
                    :suffix="indicator.abb=='(PPV)'?'':'%'"
                />
              <div v-else>
                <v-row>
        
        <v-col 
            class="text-h6 text-grey text-center align-self-center text--lighten-1 font-weight-light"
        >
            Данных нет
        </v-col>
    </v-row>
              </div>
                <!--  -->
            </v-col>
        </v-row>
    </v-card>
</template>

<script>
export default {

    props: {
        indicator: {
            type: Object,
            default: {}
        },
    }

}
</script>

<style>

</style>