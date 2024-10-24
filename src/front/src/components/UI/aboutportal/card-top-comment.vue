<template>
    <pattern-card-feed 
        :title="'Самый активный критик'"
    >
        <template v-slot:filling_feedback>


<v-row no-gutters v-if="top.comment[0].time_create != '1990-01-01'">
    <v-col lg=5 class="bg-teal-lighten-4 align-self-center">
        <list-user
            :author= "top.author" 
            :from_which="'top_comment'"
        />
    </v-col>
    <v-col class="align-self-center pl-0">
       
        <v-table density="compact" class="pa-0">
                        <thead>
                            <tr >
                                <th class="text-center text-caption font-weight-medium">
                                    <v-tooltip location="top">
                                        <template v-slot:activator="{ props }">
                                            <span v-bind="props">
                                                <v-icon
                                                    class="cursor-help"
                                                    icon="mdi-comment-text-outline"
                                                    color='cyan-darken-4'
                                                    size="x-large"
                                                />
                                            </span>
                                        </template>
                                        <card-comment :comment=top.comment[0] />
                                    </v-tooltip>
                                </th>
                                <th class="text-center text-caption font-weight-medium">
                                    <v-tooltip location="top">
                                        <template v-slot:activator="{ props }">
                                            <span v-bind="props">
                                                <v-icon
                                                    class="cursor-help"
                                                    icon="mdi-star"
                                                    color="orange"
                                                    size="x-large"
                                                />
                                            </span>
                                        </template>
Поставлено оценок
                                    </v-tooltip>
                                </th>
                            </tr>
                        </thead>
                        <tbody >
                           <tr >
                            <th class="text-center text-h6 font-weight-bold">{{top.comment.length}}</th>
                            <th class="text-center text-h6 font-weight-bold">{{top.score}}</th>
                           
                           </tr>
                        </tbody>
                    </v-table>
    
    </v-col>
</v-row>
<v-row v-else
         
         class="align-center flex-column
         
         gap mt-n2"
         no-gutters
     >
     <v-col 
            class="text-h6 pt-8 text-grey text-center align-self-center text--lighten-1 font-weight-light"
        >
        За выбранный период комментариев нет
        </v-col>
       
            </v-row>
    </template>
  </pattern-card-feed>
</template>

<script>
import PatternCardFeed from '@/components/UI/aboutportal/pattern-card-feed.vue'
import TooltipText from '@/components/UI/tooltip-text.vue'
import CardComment from './card_top_comment/card-comment.vue'

export default {
    components: { 
        PatternCardFeed,
        TooltipText,
        CardComment
    },

    props: 
        {
        top: {
            type: Object,
            default: () => {}
        },

    },

 
}
</script>

<style>

</style>