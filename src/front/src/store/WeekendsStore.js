import { axiosApiInstance } from "@/utils/axios-api";
import { defineStore } from "pinia";
import { ref } from "vue";

export const useWeekendsStore = defineStore("weekends", () => {
  
  const week = ref({});

  function getWeekend(year) {
    axiosApiInstance
      .get(`api/calendar_of_events/exclusion_dates/?year=${year}`, {})
      .then((data) => {
        week.value = data.data;
      });
  }
  return { week, getWeekend };
});
