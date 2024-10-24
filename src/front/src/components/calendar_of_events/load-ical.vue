<template>
  
  <div>
    <v-btn @click="f_feedbackdata"> ical</v-btn>

    <v-file-input
      :show-size="1000"
      color="deep-purple-accent-4"
      label="File input"
      placeholder="Select your files"
      prepend-icon="mdi-paperclip"
      variant="outlined"
      counter
      multiple
      accept=".ics"
      @input="handleFilesUpload"
    />
  </div>
</template>

<script>
import { axiosApiInstance } from "@/utils/axios-api";
import { ref, onMounted } from "vue";

import ical from "ical.js";
import { useWeekendsStore } from '@/store/WeekendsStore'

// const burl = baseURL.slice(0, -1);

export default {
  setup() {
    const week= useWeekendsStore()
    const drawer_right = ref(false);
    const cal = ref(null)
    const participant = ref("");
    const calendar = ref("");
    const calendarEvents = ref([]);
    const selectdate = ref(new Date())
    const hol = ['2024-05-09', '2024-05-11']




    onMounted(()=>{
     
      cal.value.$el.querySelectorAll(".v-date-picker-month__day").forEach((e)=>{
        if (hol.includes(e.getAttribute("data-v-date"))) {
        e.querySelectorAll("span").forEach(n=>{n.classList.add("text-red")})
        
      
      }
      })
    
    })

    function f_feedbackdata() {
      axiosApiInstance
        .post(`api/calendar_of_events/calendarEvents/`, {
          participants: participant.value,
          calendar: calendar.value,
        })
   
    }

    const handleFilesUpload = (event) => {
      const file = event.target.files[0];

      if (file) {
        readFile(file);
      }
    };

    const readFile = (file) => {
      const reader = new FileReader();
      reader.readAsText(file);
      reader.onload = (event) => {
        parseICS(event.target.result);
      };
    };
    const parseICS = (text) => {
      const jcalData = ical.parse(text);
      const icalComponent = new ical.Component(jcalData);
      const name = icalComponent.getFirstPropertyValue("x-wr-calname");

      const events = icalComponent
        .getAllSubcomponents("vevent")
        .map((vevent) => new ical.Event(vevent));

      const calendarEvents = events.map((event) => {
        let attendees = [];
        event.attendees.map((att) => {
          attendees.push(att.jCal[1].cn);
        });
        return {
          name: event.summary,
          description: event.description,
          // organizer: event.organizer, Может, удалить?
          startdate: event.startDate.toJSDate(),
          enddate: event.endDate.toJSDate(),
          place: event.location,
          // attendees: attendees, ? Такая же история 0 в базе нет
          cdate: new Date(event.component.jCal[1][6][3]),
          content: "",
        };
      });

      participant.value = name;
      calendar.value = calendarEvents;
    };

    return {
      handleFilesUpload,
      calendarEvents,
      f_feedbackdata,
      drawer_right,
      selectdate,
      cal
    };
  },
};
</script>

<style>

</style>
