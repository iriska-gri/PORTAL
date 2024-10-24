<template>
    <pattern-card 
        :title="'Обратная связь'"
        :ico="'mdi-comment-multiple-outline'"
    >
        <template v-slot:filling>
            <v-row no-gutters class="flex-column gap">
                <v-col lg=1 class="w100">
                    <v-card variant="flat" class="text-subtitle-1 font-weight-regular cursor-default">
                        Последний комментарий оставлен: <br> <span class="text-subtitle-1 font-weight-bold">{{formaComaTime(feedback.last_comment.time_create)}}</span> 
                    </v-card>
                </v-col>
                <v-col lg=2 class="w100">
                <statistik-like :rating=feedback.criteria />

             
                </v-col>
                <v-col
                    class="w100 flex-grow-0"  
                    v-for=" x in feedback.data" 
                    :key=x
                >
                <card-feedback :data="x"/>
            </v-col>
            <v-col class="d-flex  flex-column">
                <card-top-comment :top=dataTopUser />
            </v-col>

        </v-row>

    </template>
      </pattern-card>
   
</template>

<script>
import { ref, watch, computed  } from 'vue'
import {formaComaTime, splitname} from '@/utils/universal_functions'


import CardTotal from '@/components/UI/aboutportal/card-total.vue'
import TopUser from '@/components/UI/aboutportal/top-user.vue'
import PatternCard from '@/components/UI/aboutportal/pattern-card.vue'
import CardFeedback from '@/components/UI/aboutportal/card-feedback.vue'
import CardTopComment from '@/components/UI/aboutportal/card-top-comment.vue'
import FeedstarLike from '@/components/UI/feedback/feedstar-like.vue'
import StatistikLike from '@/components/UI/feedback/statistik-like.vue'

export default {

    components: { 
        CardTotal,
        TopUser,
        PatternCard,
        CardFeedback,
        CardTopComment,
        FeedstarLike,
        StatistikLike
    },

    props: 
        {
        feedback: {
            type: Object,
            default: () => {return {feed:[], last_comment:{time_create:'1990-01-01'}}}
        }
    },

        setup(props) {



            const dataTopUser = computed({
                get() {
                    let ob = {}
                    let tuser = {comment:[{time_create:'1990-01-01', comment: ''}], score: 0}

                    props.feedback.feed.forEach((e) => {

                        
                    
                        if (!ob[e.author.id]) {
                            ob[e.author.id] = 0
                        }
                        ob[e.author.id] += 1
                    })
                    
                    if (Object.keys(ob).length > 0){

                     
                        let top = Object.keys(ob).reduce((a,b) => ob[a] > ob[b] ? a: b)
                        
                        let puser = props.feedback.feed.filter(e=> e.author.id == top)
                        tuser=Object.assign({},puser[puser.length-1])
                        tuser.fio=splitname(tuser.author)
                        tuser.score = puser.length
                     
                        tuser.comment = puser.filter(e=>e.comment.length>0).sort((a,b)=> {return b.id-a.id})
                    }
                    
                     
                    return tuser


                }
            }) 


            
            return {
                formaComaTime,
                dataTopUser,
       
            }
            }
        }

</script>

<style>

</style>