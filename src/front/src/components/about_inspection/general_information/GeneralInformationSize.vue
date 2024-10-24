<template>
    <v-card class="flex-grow-1 d-flex flex-column ">

                    <v-card-title class="text-h6 text-center text-uppercase">
                      {{title}} 
                    </v-card-title>
                    <template v-if="Object.keys(size).length > 0">
                      <!-- <v-card-text class="text-h2 text-center">
                       
                        <vue3-autocounter
                          ref="counter"
                          :startAmount="0"
                          :endAmount="size.statesize"
                          :duration="2"
                        />
                      </v-card-text> -->

                      <!-- <v-card-subtitle class="text-center"
                        >по состоянию на
                        {{
                          new Date(size.date_created).toLocaleDateString(
                            "ru-RU"
                          )
                        }}
                      </v-card-subtitle> -->
                      <v-card
                        class="h-100 flex-column d-flex align-center justify-center text-center elevation-0"
                      >
                      <vue3-autocounter
                          class="text-h2 font-weight-regular pb-2"
                          ref="counter"
                          :startAmount="0"
                          :endAmount="size.size"
                          :duration="2"
                        />
                      <!-- <v-card-text class="text-h2 text-center">
                      <vue3-autocounter
                      
                          ref="counter"
                          :startAmount="0"
                          :endAmount="size.size"
                          :duration="2"
                        />
                      </v-card-text> -->
                  
                      </v-card>
                      <v-card-subtitle class="text-center"
                        >по состоянию на
                        {{
                          new Date(size.date_created).toLocaleDateString(
                            "ru-RU"
                          )
                        }}
                      </v-card-subtitle>
                    </template>
                    <template v-else>
                      <v-card
                        class="h-100 d-flex align-center justify-center text-center"
                      >
                        <span class="text-subtitle-1 text-grey"
                          >Данных нет</span
                        >
                      </v-card>
                     
                    </template>
                  </v-card>
</template>

<script>
export default {
  props: {
    title: {
        type: String,
        default: ''
    },
    size: {
      type: Object,
      default: () => {},
    },
  },
};
</script>

<style></style>
