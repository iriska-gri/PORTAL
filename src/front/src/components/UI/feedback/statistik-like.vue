<template>
    <pattern-card-feed
        :title="'Средняя оценка'"
    >
        <template v-slot:filling_feedback>
            <div v-if="rating.length!=0" class="pt-1">
                <v-row no-gutters>
                    <v-col class="text-h4 font-weight-medium">
                        {{avgcriteria}}
                    </v-col>
                </v-row>
                <v-row
                    class="align-center flex-column scoreheight"
                    no-gutters
                >
                    <div class="flex-column d-flex  pa-0"
                        v-for="(x, key) in rating"
                        :key = key
                    >
                        <v-col lg=1 class="text-subtitle-1 font-weight-regular cursor-default w100 pa-0">
                            <v-tooltip
                                :text=x.name
                                location="left"
                            >
                                <template v-slot:activator="{ props }">
                                    <v-icon
                                    class="pb-4 pr-3"
                                        v-bind="props"
                                        size="small"
                                        :color="x.color"
                                        :icon="x.ico"
                                    />
                                </template>
                            </v-tooltip>
                       
                            <!-- {{x.name}} -->
                       
                            <v-rating
                                v-model="x.ratings"
                                :hover="typeof(key) == 'number'"
                                half-increments
                                readonly
                                :size="25"
                                color="yellow"
                                :density="'comfortable'"
                            />
                        </v-col>
                    </div>
                </v-row>
            </div>
            <div class="d-flex flex-column" v-else>
                <v-row
                    class="align-center flex-column scoreheight gap mt-n2"
                    no-gutters
                >
                    <v-col class="text-h6 pt-8 text-grey text-center align-self-center text--lighten-1 font-weight-light"
                    >
                        За выбранный период оценок нет
                    </v-col>
                </v-row>
            </div>  
        </template>
    </pattern-card-feed>
</template>

<script>
import PatternCardFeed from '@/components/UI/aboutportal/pattern-card-feed.vue'
import { computed } from 'vue'

export default {

    props: {
        rating: {
            type: Object,
            default: () => {}
        },
    },

    components: { 
        PatternCardFeed,
    },

    setup(props) {

        const avgcriteria = computed({
                get() {
                    let avgcrit = 0
                    props.rating.forEach((e)=> {
                        avgcrit += e.ratings
                    })
                return parseFloat(avgcrit/props.rating.length).toFixed(2)
                }
            })
    
        return {
            avgcriteria
        }
    }

   

}
</script>

<style>

</style>