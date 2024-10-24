<template>
  <v-row>
    <v-col class="flex-column pr-0">
      <v-card class="h-100">

        <vue-cal
          locale="ru"
          xsmall
          :selected-date="new Date()"
          hide-view-selector
          todayButton
          :events="events"
          active-view="month"
          :disable-views="['years', 'year', 'week', 'day']"
          @cell-focus="selectedDate = $event"
        >
          <template #arrow-prev>
            <v-icon icon="mdi-menu-left" />
          </template>
          <template #arrow-next>
            <v-icon icon="mdi-menu-right" />
          </template>
          <template #today-button>
            <v-tooltip text="Сегодня" location="bottom">
              <template v-slot:activator="{ props }">
                <v-icon
                  @click="selectedDate = new Date()"
                  v-bind="props"
                  icon="mdi-crosshairs-gps"
                  size="x-small"
                  class="pr-3"
                  color="more_details_btn"
                />
              </template>
            </v-tooltip>
          </template>
        </vue-cal>

        <event-dialog
          :event="selectedEvent"
          :opendialog="showDialog"
          @returnUpdateData="returnUpdateData"
          @update:opendialog="showDialog = $event"
        />
      </v-card>
    </v-col>
    <v-col>
      <v-card class="h-100">
        <v-card-title class="text-center"
          >События на {{ selData }}</v-card-title
        >

        <vue-cal
          locale="ru"
          hideTitleBar
          active-view="day"
          :disable-views="['years', 'year', 'month', 'week']"
          :selected-date="selectedDate"
          xsmall
          hide-view-selector
          :time="false"
          :events="events"
        >
          
          <template #cell-content="{ view, events }">
            <v-img
              v-if="['week', 'day'].includes(view.id) && !events.length"
              class="align-end text-white cursor-default"
              height="200"
              :src="`${burl}/media/newsimage/calendar_stub.jpg`"
              cover
            />
            <v-card v-else>
              <v-list lines="one">
                <v-list-item
                  @click="onEventClick(n)"
                  v-for="n in events"
                  :key="n.pk"
                  :title="n.name"
                  :subtitle="n.description"
                ></v-list-item>
              </v-list>
            </v-card>
          </template>
        </vue-cal>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";
import { ref, computed } from "vue";
import { baseURL } from "@/utils/axios-api";
import { axiosApiInstance } from "@/utils/axios-api";
import { formaDashTime } from "@/utils/universal_functions";
import EventDialog from "@/components/calendar_of_events/event-dialog.vue";
export default {
  components: { VueCal, EventDialog },

  setup() {
    const selectedEvent = ref({});
    const eventsCssClasses = ["bg-red", "bg-blue", "bg-green"];
    const showDialog = ref(false);
    const burl = baseURL.slice(0, -1);
    const events = ref([]);

    const onEventClick = (n) => {
      selectedEvent.value = n;
      showDialog.value = true;
    };

    function f_generalvacation() {
      // events.value = [];
      axiosApiInstance
        .get("api/calendar_of_events/calendarEvents/")
        .then((data) => {
          data.data.forEach((e) => {
            e.start = formaDashTime(e.start);
            e.end = e.start;
          });
          events.value = data.data;
          // icon: "mdi-book-open",
          // class: "bg-indigo-lighten-5 border-sm",
        });
    }

    const returnUpdateData = () => {
      f_generalvacation();
    };

    f_generalvacation();

    const selectedDate = ref(null);

    const selData = computed({
      get: () => {
        const d = new Date(selectedDate.value);
        let mess = "сегодня";
        if (d.getFullYear() != "1970") {
          mess = `${d.getDate()} число`;
        }

        return mess;
      },
    });

    return {
      selectedEvent,
      events,
      selectedDate,
      f_generalvacation,
      showDialog,
      onEventClick,
      eventsCssClasses,
      burl,
      returnUpdateData,
      selData,
    };
  },
};
</script>

<style>
/* Dot indicator */
.vuecal__cell-events-count {
  width: 20px;
  min-width: 0;
  height: 11px;
  padding: 0;
  color: transparent;
}

.vuecal {
  border-radius: 6px;
}

.vuecal__title-bar {
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
}

.vuecal__title-bar {
  background: var(--cards);
}
.vuecal__flex .vuecal__title {
  font-family: sans-serif;
}
.vuecal__cell-events-count {
  position: absolute;
  left: 50%;
  top: 65%;
  transform: translate(-50%);
  min-width: 15px;
  height: 15px;
  line-height: 15px;
  padding: 0;
  background: linear-gradient(
    to top right,
    rgba(19, 84, 122, 0.8),
    rgba(128, 208, 199, 0.8)
  );
  color: #f8fff9 !important;
  border-radius: 12px;
  font-size: 10px;
  box-sizing: border-box;
}

/* .vuecal__event {
  color: #666;
  background-color: transparent;
  padding: 10px;
  position: relative;
  box-sizing: border-box;
  left: 0;
  width: 100%;
  z-index: 1;
  transition: box-shadow 0.3s, left 0.3s, width 0.3s;
  overflow: hidden;
  text-align: justify;
} */

.vuecal--rounded-theme .vuecal__cell-content {
  width: 30px;
  height: 30px;
  flex-grow: 0;
  border: 1px solid #00a5bc00;
  background: #c2e9d78c;
  border-radius: 30px;
  color: #333;
}

.vuecal__cell-content {
  cursor: pointer;
}

.vuecal__body {
  position: relative;
  overflow: auto;
  height: 0;
}

.vuecal--no-time .vuecal__event {
  min-height: 20px;
}

.vuecal__cell--selected:before {
  border-color: rgba(30, 65, 49, 0.5);
}

.vuecal__cell--today,
.vuecal__cell--current {
  background-color: rgba(238, 181, 214, 0.548);
}

.vuecal__cell--selected:before {
  border-color: rgba(30, 65, 49, 0);
}

.vuecal__cell--selected {
  background-color: #3a97694a;
  z-index: 2;
}

.vuecal__event {
  cursor: pointer;
}

.vuecal__event-title {
  font-size: 1.2em;
  font-weight: bold;
  margin: 4px 0 8px;
}

.vuecal__event-time {
  display: inline-block;
  margin-bottom: 12px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
}

.vuecal__event-content {
  font-style: italic;
}

.vuecal__cell-content {
  cursor: default;
}
</style>
