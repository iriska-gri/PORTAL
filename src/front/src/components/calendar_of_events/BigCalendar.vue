<template>
  <v-row no-gutters>
    <v-col class="flex-grow-0 d-flex flex-column">
      <v-card class="h-100 rounded-0 d-flex flex-colmn" width="250">
        <v-row no-gutters class="flex-column">
          <v-col class="flex-grow-0 px-2 pt-1">
            <v-text-field
              density="compact"
              clearable
              append-inner-icon="mdi-magnify"
              hide-details
              class="py-3"
              label="Найти событие"
              rows="1"
              no-resize
              variant="outlined"
            />
          </v-col>
          <v-col class="flex-grow-0 px-2">
            <v-btn
              type="submit"
              class="text-subtitle-1 font-weight-light"
              color="btn_text"
              block
              elevation="1"
              @click="createEvent()"
              >Создать событие</v-btn
            >
            <!-- {{eventFromCalendar}} -->
          </v-col>
          <v-col class="w100" lg="3">
            <v-locale-provider locale="ru">
              <v-date-picker
                ref="cal"
                v-model="selectdate"
                color="btn_text"
                class="rounded-0 minCal"
                max-width="250"
                hide-header
                show-adjacent-months
                @click="CheckingStore"
                @update:month="getMonth"
                @update:year="getYear"
              >
              </v-date-picker>
            </v-locale-provider>
          </v-col>

          <v-col class="flex-column d-flex">
            <v-row no-gutters class="h-0 overflow-auto flex-column flex-nowrap">
              <v-col>
                <calendar-my
                  :calendars="
                    calendarForMy.filter(
                      (e) => e.author == accountStore.user.is_idEmployee
                    )
                  "
                  title="Мои календари"
                  @getCalendar="getCalendar"
                />

                <calendar-my
                  :calendars="
                    calendarForMy.filter(
                      (e) => e.author != accountStore.user.is_idEmployee
                    )
                  "
                  title="Подписки"
                />
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
    <v-col class="d-flex flex-column">
      <calendar-full
        :allEvent="calendarForMy.filter((e) => e.events.length > 0)"
        @getEvent="createEvent"
        @update:allEvent="infoEvent($event)"
      />
    </v-col>

    <!-- <v-navigation-drawer
      v-model="drawer_right"
      floating
      permanent
      location="right"
      rail-width="400"
      rail
    >
    </v-navigation-drawer> -->
    <v-dialog v-model="showDialog" max-width="700">
      <event-create
        @closeDialog="showDialog = false"
        :eventCalendar="eventFromCalendar"
        @update:eventCalendar="eventFromCalendar = $event"
        @getCalendar="getCalendar"
        ref="createEvents"
      />
    </v-dialog>
  </v-row>
</template>

<script>
import { ref, onMounted, watch } from "vue";
import { useWeekendsStore } from "@/store/WeekendsStore";
import EventCreate from "@/components/calendar_of_events/event-create.vue";
import CalendarMy from "@/components/calendar_of_events/calendar-my.vue";
import { axiosApiInstance } from "@/utils/axios-api";
import { useAccountStore } from "@/store/AccountStore";
import CalendarFull from "@/components/calendar_of_events/UI_calendar/calendarFull.vue";

export default {
  components: { EventCreate, CalendarMy, CalendarFull },

  setup(props, { emit }) {
    const accountStore = useAccountStore();
    const showDialog = ref(false);
    const week = useWeekendsStore();
    const drawer_right = ref(false);
    const cal = ref(null);
    const selectdate = ref(new Date());
    const MyYear = ref(selectdate.value.getFullYear());
    const MyMonth = ref(selectdate.value.getMonth() + 1);
    const calendarForMy = ref([]);
    const eventFromCalendar = ref({});
    const createEvents = ref(null);

    const getMonth = (month) => {
      MyMonth.value = month + 1;
    };
    const getYear = (year) => {
      MyYear.value = year;
    };

    const getCalendar = () => {
      axiosApiInstance
        .get(`api/calendar_of_events/my_calendars/`)
        .then((res) => {
          res.data.forEach(
            (e) =>
              (e.visible = accountStore.calendar.includes(e.id) ? false : true)
          );
          calendarForMy.value = res.data;
        });
    };

    getCalendar();

    const getEvents = (idEvent, clik) => {
      axiosApiInstance
        .get(
          `api/calendar_of_events/my_events/${
            idEvent === undefined ? "" : `?id=${idEvent}`
          }`
        )
        .then((res) => {
          if (idEvent === undefined) {
            res.data.event = {
              name: "",
              participant: [accountStore.user.is_idEmployee],
              files: [],
              date_start: new Date(),
              date_end: new Date(),
              period: null,
              description: "",
              calendar: null,
            };
          }
          eventFromCalendar.value = res.data;

          if (clik) showDialog.value = true;
        });
    };

    getEvents();

    const createEvent = (idEv) => {
      getEvents(idEv, true);
      if (idEv) {
        getCalendar();
      }
    };

    const weekendsData = () => {
      cal.value.$el
        .querySelectorAll(".v-date-picker-month__day")
        .forEach((e) => {
          let datas = e.getAttribute("data-v-date");
          let weeks =
            new Date(datas).getDay() === 6 || new Date(datas).getDay() === 0;
          if (weeks) {
            e.querySelectorAll("span").forEach((n) => {
              n.classList.add("text-red");
            });
          }
          if (MyMonth.value in week.week[MyYear.value]) {
            if (week.week[MyYear.value][MyMonth.value].includes(datas)) {
              e.querySelectorAll("span").forEach((n) => {
                n.classList.add("text-red");
                if (n.classList.contains("text-red") && weeks) {
                  n.classList.replace("text-red", "text-black");
                }
              });
            }
          }
        });
    };

    onMounted(() => {
      week.getWeekend(MyYear.value);
    });

    watch(
      () => week.week,
      (newValue, oldValue) => {
        if (newValue) {
          weekendsData();
        }
      }
    );

    const CheckingStore = () => {
      if (MyYear.value in week.week) {
        weekendsData();
      } else {
        week.getWeekend(MyYear.value);
      }
    };

    const infoEvent = (i) => {
      console.log(i, "iiiiiiiiii");
    };

    return {
      drawer_right,
      selectdate,
      cal,
      getMonth,
      getYear,
      weekendsData,
      week,
      CheckingStore,
      showDialog,
      calendarForMy,
      accountStore,
      getCalendar,
      eventFromCalendar,
      createEvent,
      infoEvent,
      createEvents,
    };
  },
};
</script>

<style>
.minCal .v-date-picker-month__day {
  height: 31px;
  width: 31px;
}

.minCal .v-btn--icon.v-btn--density-default {
  width: calc(var(--v-btn-height) + 12px);
  height: calc(var(--v-btn-height) + 6px);
}

.minCal .v-btn__content {
  font-weight: 410;
}
</style>
