<template>
    
    <!-- :title="'Оставлено комментариев'" -->
    <pattern-card-feed
        :title="data.title"
    >   
        <template v-slot:filling_feedback>
        <v-row no-gutters class="flex-column gap">
                <v-col>
                    <v-table density="compact" class="px-7">
                        <thead>
                            <tr >
                                <th class="text-center text-subtitle-1 font-weight-regular">
                                всего  
                                </th>
                                <th class="text-center text-subtitle-1 font-weight-regular">
                                за период
                                </th>
                            </tr>
                        </thead>
                        <tbody >
                           <tr >
                            <th class="text-center text-h6 font-weight-bold">{{data.all}}</th>
                            <th class="text-center text-h6 font-weight-bold">{{data.period}}</th>
                           </tr>
                        </tbody>
                    </v-table>
                </v-col>
            </v-row>
        </template>
    </pattern-card-feed>
</template>

<script>
import PatternCardFeed from '@/components/UI/aboutportal/pattern-card-feed.vue'
export default {
    components: { 
        PatternCardFeed,
    }, 
    props: {
    
    data: {
        type: Object,
        default: () => {}
    },
}
}
</script>

<style>

</style>