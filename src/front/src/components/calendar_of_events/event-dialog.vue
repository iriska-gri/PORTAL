<template>
  <v-dialog v-model="mydialog" max-width="700">
    <v-card>
    
      <v-card-title>
        <v-icon
          :icon="editEvent ? 'mdi-book-open-variant' : 'mdi-pencil'"
          color="indigo-darken-3"
          class="pb-1"
          @click="modeEvent"
        />

      </v-card-title>
    </v-card>
    <!--  mdi-check-->
    <!-- <event-dialog-edit
      v-if="editEvent"
      :event="event"
      @returnUpdateData="returnUpdateData"
      /> -->
    <!-- <event-dialog-info :event="event" v-else /> -->
    <component 
      :is = "editEvent ? 'eventDialogEdit':'eventDialogInfo'"
      :event="event"
      @returnUpdateData="returnUpdateData" 

      />
  </v-dialog>
</template>

<script>
import { computed, ref } from "vue";
import eventDialogEdit from "@/components/calendar_of_events/event-dialog-edit.vue";
import eventDialogInfo from "@/components/calendar_of_events/event-dialog-info.vue";
import {  axiosApiInstance } from "@/utils/axios-api";

export default {
  components: { eventDialogEdit, eventDialogInfo },
  props: {
    opendialog: {
      type: Boolean,
      default: false,
    },

    event: {
      type: Object,
      default: () => {},
    },
  },

  setup(props, { emit }) {
    const editEvent = ref(false);

    const mydialog = computed({
      get: () => props.opendialog,
      set: (value) => emit("update:opendialog", value),
    });


    const modeEvent = () => {
      editEvent.value=!editEvent.value
    
    }

    const chekEvent = () => {

        
    

     
    };
    const returnUpdateData = () => {
      mydialog.value= false
      emit('returnUpdateData')
      
    }

    return {
      mydialog,
      editEvent,
      chekEvent,
      modeEvent,
      returnUpdateData
    };
  },
};
</script>

<style></style>
