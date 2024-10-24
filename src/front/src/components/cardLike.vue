<template>
  <v-card class="pt-2">
    <v-card-title>
      <span class="text-h5">Обратная связь</span>
    </v-card-title>
    <v-card-text class="px-2 py-0"> 
      <v-container>
        <v-row>
          <v-col class="flex-grow-0 py-0  text-no-wrap align-self-center text-button">
            Оцените сайт 
            
          </v-col>
          <v-divider class="pb-3"/>
        </v-row>
        <feedstar-like
          :rating=feedbackdata
          @update:rating="feedbackdata.nowrating = $event"
        />
        <v-row class="mt-6">
          <v-col class="pa-0 px-3">
                <v-textarea
              label="Ваши комментарии сделают портал лучше"
              hide-details
              variant="outlined"
              rows="5"
              row-height="15"
              v-model="feedbackdata.nowcomment.comment"
            />
          </v-col>
        </v-row>
      </v-container>
    </v-card-text>
    <v-card-actions class="pt-0">
      <small v-if="average < 5 || feedbackdata.nowcomment.id!=null" class="pl-5">
        Вы оценили сайт на <span class="font-weight-black">{{average}}</span> {{myLabel()}}
      </small>
      <v-spacer/>
      <v-btn
        color="modal_btn"
        variant="text"
        text="Закрыть"
        @click="menusCloses"
      />
      <v-btn
        color="modal_btn"
        variant="text"
        :text="feedbackdata.nowcomment.id==null?'Отправить':'Обновить'"
        @click="feedSend"
      />
 
      
    </v-card-actions>

  </v-card>
  
</template>

<script>
import { ref, onMounted, computed } from 'vue'
import { axiosApiInstance } from '@/utils/axios-api'

import FeedstarLike from '@/components/UI/feedback/feedstar-like.vue'
import { useAlertStore } from '@/store/useAlertStore'

export default {
  components: { FeedstarLike },

  props: {
    LikeDialog: {
      type: Boolean,
      default: false
    }
  },

  

  setup(props, {emit}) {
    const feedalert = useAlertStore().alert
    const feedbackdata= ref({nowcomment: {comment: '' }, nowrating: []})

  function f_feedbackdata() {
    axiosApiInstance.get('api/feedback/feedbackdata/')
    .then(data => {
      feedbackdata.value = data.data
      if (feedbackdata.value.nowrating.length == 0) {
        for (let x of feedbackdata.value.basecrit) {
          feedbackdata.value.nowrating.push({rating: x.rating, crit: x.id, id: null})
        }
      }
      if (feedbackdata.value.nowcomment === null) {
        feedbackdata.value.nowcomment = { comment: '', id: null}         
      }
    })
  }  

  onMounted(() => { 
    f_feedbackdata()
  })

  const average = computed(()=> {
    const sum = feedbackdata.value.nowrating.reduce((total, obj)=> total + obj.rating, 0)
    const sumlen = sum/feedbackdata.value.nowrating.length
    const ukr = Number.isInteger(sumlen)?sumlen:sumlen.toFixed(1)
    return ukr
  })

  function myLabel()  {
    let labels = ''
    if (average.value > 0 && average.value <= 3) 
      labels = 'УПС-С! Мы обязательно все исправим'
    else if (average.value > 2 && average.value <= 4) 
      labels = 'Спасибо за обратную связь, мы обратим на это внимание'
    else if (average.value > 4 && average.value < 5) 
      labels = 'Класс, будем стараться до 5'          
    else 
      labels = "Спасибо за отзыв и высокую оценку ^__^"
    return labels
  }

  function menusCloses() {
    emit('menusClose')
  }

  function feedSend() {

      axiosApiInstance.post(`api/feedback/feedbackdata/`, {
        nowrating: feedbackdata.value.nowrating,
        nowcomment: feedbackdata.value.nowcomment
      }).then(data => {})
      feedalert.alert = true
      textFromAlert()
      menusCloses()
 
  }

  const textFromAlert = () => {
    if (feedbackdata.value.nowcomment.id ==null) {
      feedalert.text = "Оценка отправлена, спасибо за участие"
      feedalert.ico = "mdi-redo-variant"
      feedalert.color = "green-darken-4"
    }

    else  {
      feedalert.text = "Оценка обновлена"
      feedalert.ico = "mdi-refresh"
      feedalert.color="light-blue-darken-4"
    }
  }
  

  return {
      feedbackdata,
      average,
      menusCloses,
      myLabel,
      feedSend,
      feedalert
    
    }
  
  }

}

</script>

<style>
.custom_subtitle  {
    opacity: 1;
}

.v-selection-control__input {
    width: 46%!important;
    height: 46%!important;
    border-radius: 0!important;
}

</style>