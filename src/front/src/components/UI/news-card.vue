<template>
    <v-card
        class="rounded-0 h-100 flex-column d-flex"
        min-height="410"
        max-height="410"
    >
        <v-card-title class="pb-1">
            {{news.title}}
        </v-card-title>
        <v-row class="flex-grow-0">
            <v-col class="d-flex flex-column ">
                <v-img
                    :src="`${burl}${news.link}`"
                    height="175px"
                    width="92%"
                    class="mx-auto"
                    cover
                    @click="openOneImg(news.link)"
                />
                  
            </v-col>
        </v-row>
        <v-divider/>
        <v-row class="ma-0 flex-grow-0">
                            <v-col
                                class="py-1 pl-4"
                                lg=5
                                md=12
                                sm=12
                            >

                            <ico-user :author="news.author"/>
                            </v-col>
                            <v-col
                                lg=7
                                md=12
                                sm=12
                                class="py-1 text-end pr-4">
                                <div class="justify-self-end">
                                <v-icon
                                    size="x-small"
                                    class="me-1"
                                    :icon="news.scores.filter(e=> e.user==accountStore.user.login && e.score == true).length>0?'mdi-thumb-up':'mdi-thumb-up-outline'"
                                    @click="toggleIncrementLike(news.id, true)"
                                />
                                <span class="subheading me-2">
                                    {{news.scores.filter(e=> e.score==true).length}}
                                </span>
                                <span class="me-1">
                                    ·
                                </span>
                                <v-icon
                                    size="x-small"
                                    class="me-1"
                                    :icon="news.scores.filter(e=> e.user==accountStore.user.login && e.score == false).length>0?'mdi-thumb-down':'mdi-thumb-down-outline'"
                                    @click="toggleIncrementLike(news.id, false)"
                                />
                                <span class="subheading me-2">
                                    {{news.scores.filter(e=> e.score==false).length}}
                                </span>
                                <span class="me-1">
                                    ·
                                </span>
                                <v-icon
                                    size="x-small"
                                    class="me-1"
                                    icon="mdi-message-text-outline"
                                />
                                <span class="subheading">
                                    {{ news.comment.length }}
                                </span>
                                <span class="me-1">
                                    ·
                                </span>
                                <v-icon
                                    size="x-small"
                                    class="me-1 mb-1"
                                    icon="mdi-image"
                                />
                                <span class="subheading">
                                    {{ news.gallery.length }}
                                </span>
                            </div>

                            </v-col>
                        </v-row> 
                        <v-divider/>
        <v-row class="ma-0 overflow-auto">
            <v-col
                class="py-0"
                :class="news.text.length==0?'align-self-center':'my-3'"
            >
                <v-card-text class="py-0 px-2">
                
                    <div v-if="news.text.length>0" v-html=limitText(news.text)></div>
                    <div v-else class="text-h6 text-grey text-center align-self-center text--lighten-1 font-weight-light">Без описания</div>
                </v-card-text>
            </v-col>
        </v-row>
        <v-divider/>
        <v-row class="flex-grow-0 ma-0">
            <v-col class="d-flex justify-space-between">
                <v-btn
                    color="more_details_btn"
                    variant="text"
                    :to='`/newsfull?id=${news.id}`'
                    size="small"    
                    append-icon="mdi-step-forward-2"
                >
                    Подробнее 
                </v-btn>
                <span class="text-caption align-self-center">{{formatDate(news.cdate)}}</span>
            </v-col>
        </v-row>
    </v-card>
    
</template>

<script>
import { baseURL } from '@/utils/axios-api'
import {useAccountStore} from '@/store/AccountStore'
import { axiosApiInstance } from '@/utils/axios-api'
import {splitname} from '@/utils/universal_functions'
import moment from 'moment'
import icoUser from '@/components/UI/fiousercard/icoUser.vue'

const accountStore = useAccountStore()


export default {
    
  components: { icoUser },

    props: {
        news: {
            type: Object,
            default: {}
        }
    },

    setup(props, {emit}){
        
        const burl = baseURL.slice(0,-1)

       
       

        const limitText=(text)=> {
            let parser = new DOMParser().parseFromString(text, "text/html");
            let doc = parser.body.textContent || ""
            doc = doc.replaceAll('src="/media/uploads', `src="${baseURL}media/uploads`)
            const t = doc.split(' ').slice(0, 50)
            return `${doc.split(' ').slice(0, 50).join(' ')} ${t.length<50?'':'...'}`
        }



        const toggleIncrementLike = (newss, scores) => {
            axiosApiInstance.post(`api/navigation/newscrossroad/`, {news: newss, scores: scores}).then(result => {  
                props.news.scores = result.data
        })
    
        }

        const openOneImg = () => {
            emit('openOneImg')
        }

        function formatDate(date) {
            return moment(date).format('DD.MM.YYYY')
        }

        return {
            accountStore,
            burl,
            limitText,
            splitname,
            toggleIncrementLike,
            openOneImg,
            formatDate
        }
    }

}
</script>

<style>

</style>