<template>
  <v-locale-provider locale="ru">
    <v-calendar
      ref="calendar"
      :events="returnPeriod"
      :view-mode="type"
      :month="monthNow"
      :year="YearNow"
      :model-value="selectDay"
      class="h-100"
    >
      <template v-slot:header>
        <v-col class="d-flex flex-column">
          <v-row no-gutters class="gap">
            <v-col class="flex-grow-0" lg="2">
              <v-btn
                class="text-subtitle-1"
                variant="outlined"
                @click="todayDay"
              >
                Сегодня
              </v-btn>
              <v-btn icon="mdi-menu-left" variant="text" @click="returnDate" />

              <v-btn icon="mdi-menu-right" variant="text" @click="nextDay" />
            </v-col>
            <v-col class="text-h6 align-self-center ml-n6">
              <span class="text-capitalize">
                {{ getMonthName(monthNow + 1) }}
              </span>

              {{ YearNow }} г.
            </v-col>
            <v-col class="text-end align-self-center">
              <v-btn
                v-for="x in types"
                :key="x"
                :active="type != null && type == x.type"
                variant="text"
                @click="switchCalendar(x.type)"
                class="text-subtitle-1"
                :color="
                  type != null && type == x.type ? 'btn_text' : 'text_grey'
                "
              >
                {{ x.text }}
              </v-btn>
            </v-col>
          </v-row>
        </v-col>
      </template>

      <template v-slot:event="{ day, event }">
        <v-chip
          v-show="
            (!event.disable &&
              new Date(day.date).setHours(0, 0, 0, 0) !=
                new Date(event.end).setHours(0, 0, 0, 0)) ||
            (event.disable &&
              !(
                new Date(day.date).setHours(0, 0, 0, 0) !=
                new Date(event.end).setHours(0, 0, 0, 0)
              ))
          "
          class="w-100"
          density="compact"
          :class="funRoundet(event, day)"
          :color="event.color"
          @click="whatDay(event)"
        >
          {{ event.title }}
        </v-chip>
      </template>
    </v-calendar>
  </v-locale-provider>
</template>

<script>
import { ref, computed } from "vue";
import { RRule } from "rrule";

export default {
  props: {
    allEvent: {
      type: Object,
      default: () => {},
    },
  },

  setup(props, { emit }) {
    const type = ref("month");
    const types = [
      { type: "day", text: "День" },
      { type: "week", text: "Неделя" },
      { type: "month", text: "Месяц" },
      { type: "modntdh", text: "Год" },
      { type: "modnth", text: "Расписание" },
    ];

    const switchCalendar = (t) => {
      type.value = t;
    };

    const propsAllEvent = computed({
      get: () => props.allEvent,
      set: (value) => emit("update:allEvent", value),
    });

    const returnPeriod = computed({
      get() {
        let select = [];

        propsAllEvent.value.forEach((e) => {
          e.events.forEach((i) => {
            if (i.period == null && new Date(i.date_end) > dayNextMonth.value)
              i.date_end = dayNextMonth.value;

            let objRule = JSON.parse(i.period);


            if (objRule != null) {
              let startnew =
                objRule.origOptions.dtstart.split("T")[1].split(":")[0] != 21 &&
                i.allday == false
                  ? new Date(objRule.origOptions.dtstart)
                  : new Date(objRule.origOptions.dtstart.split("T")[0]);

              let rule = new RRule({
                ...objRule.origOptions,

                dtstart: new Date(startnew),
                until:
                  "until" in objRule.origOptions
                    ? new Date(objRule.origOptions.until)
                    : dayNextMonth.value,
              });

              let actRule = rule.all();
              console.log(actRule, '--------------------------------actRule')

              let lastDateMonth = new Date(
                new Date(dayNextMonth.value).setDate(
                  new Date(dayNextMonth.value).getDate() - 1
                )
              );

              actRule
                .filter(
                  (date) =>
                    new Date(date).getMonth() ===
                      new Date(lastDateMonth).getMonth() &&
                    new Date(date).getYear() ===
                      new Date(lastDateMonth).getYear()
                )
                .forEach((r) => {
                  let ev = {
                    rule: objRule.origOptions,
                    title: i.name,
                    color: e.cl_color,
                    start: new Date(r),
                    start_event: new Date(i.date_start),
                    end: new Date(i.date_end),
                    id: i.id,
                    disable:
                      new Date(r).setHours(0, 0, 0, 0) ==
                      new Date(i.date_end).setHours(0, 0, 0, 0),
                  };

                  select.push(ev);
                });
            } else {
              let dates = getDatesBetweenDates(
                new Date(i.date_start),
                new Date(i.date_end)
              );

              dates.forEach((d) => {
                let ev = {
                  rule: "",
                  title: i.name,
                  color: e.cl_color,
                  start: new Date(d),
                  end: new Date(i.date_end),
                  id: i.id,
                  disable:
                    new Date(d).setHours(0, 0, 0, 0) ==
                    new Date(i.date_end).setHours(0, 0, 0, 0),
                };
                select.push(ev);
              });
            }
          });
        });

        return select;
      },
    });

    const getDatesBetweenDates = (startDate, endDate) => {
      let dates = [];
      let currentDate = new Date(startDate);

      while (currentDate <= endDate) {
        dates.push(new Date(currentDate));
        currentDate.setDate(currentDate.getDate() + 1);
      }

      return dates;
    };

    const selectDay = ref([new Date()]);
    const monthNow = ref(new Date().getMonth());
    const YearNow = ref(new Date().getFullYear());
    const endWeek = computed({
      get() {
        return 8 - new Date(selectDay.value).getDay();
      },
    });

    const returnDate = () => {
      if (type.value == "month") {
        if (monthNow.value != 0) {
          monthNow.value--;
        } else {
          monthNow.value = 11;
          YearNow.value -= 1;
        }
      } else if (type.value == "day") {
        selectDay.value = new Date(
          new Date(selectDay.value).setDate(
            new Date(selectDay.value).getDate() - 1
          )
        );
      } else {
        selectDay.value = new Date(
          new Date(selectDay.value).setDate(
            new Date(selectDay.value).getDate() - endWeek.value
          )
        );
      }
    };

    const nextDay = () => {
      if (type.value == "month") {
        if (monthNow.value < 11) {
          monthNow.value++;
        } else {
          monthNow.value = 0;
          YearNow.value += 1;
        }
      } else if (type.value == "day") {
        selectDay.value = new Date(
          new Date(selectDay.value).setDate(
            new Date(selectDay.value).getDate() + 1
          )
        );
      } else {
        selectDay.value = new Date(
          new Date(selectDay.value).setDate(
            new Date(selectDay.value).getDate() + endWeek.value
          )
        );
      }
    };

    const todayDay = () => {
      monthNow.value = new Date().getMonth();
      YearNow.value = new Date().getFullYear();
      selectDay.value = new Date();
    };

    const getMonthName = (monthNumber) => {
      const date = new Date();
      date.setMonth(monthNumber - 1);

      return date.toLocaleString("ru", {
        month: "long",
      });
    };

    const whatDay = (e) => {
      emit("getEvent", e.id);
    };

    const zeroTime = (date) => {
      return new Date(date).setHours(0, 0, 0, 0);
    };

    const funRoundet = (ev, day) => {

      if (ev.rule.freq == 3) {
        if (
          zeroTime(day.date) != zeroTime(ev.start_event) &&
          zeroTime(day.date) != zeroTime(ev.end)
        ) {
          return "rounded-sm";
        } else if (
          zeroTime(day.date) == zeroTime(ev.start_event) &&
          zeroTime(day.date) == zeroTime(ev.end)
        ) {
          return "";
        } else if (zeroTime(day.date) != zeroTime(ev.start_event)) {
          return "rounded-s-lg";
        } else if (zeroTime(day.date) == zeroTime(ev.start_event)) {
          return "rounded-e-lg";
        }
      }

      if (ev.rule.freq == 2) {
        let weeknumS =
          ev.rule.byweekday[0].weekday == 6
            ? 0
            : ev.rule.byweekday[0].weekday + 1;
        let weeknumE =
          ev.rule.byweekday[ev.rule.byweekday.length - 1].weekday == 6
            ? 0
            : ev.rule.byweekday[ev.rule.byweekday.length - 1].weekday + 1;
 
        if (day.date.getDay() == weeknumS && weeknumS != weeknumE) {
          return "rounded-e-lg";
        } else if (day.date.getDay() == weeknumE && weeknumS != weeknumE) {
          return "rounded-s-lg";
        } else if (
          day.date.getDay() != weeknumS &&
          day.date.getDay() != weeknumE
        ) {
          return "rounded-sm";
        } else {
          return "rounded-lg";
        }

  
      }
      if (ev.rule.freq == 0) {
        console.log(ev, 'ev')
       if (zeroTime(day.date) == zeroTime(ev.start_event)) {
        return  "rounded-e-lg"
       }
        // let weeknumS =
        //   ev.rule.byweekday[0].weekday == 6
        //     ? 0
        //     : ev.rule.byweekday[0].weekday + 1;
        // let weeknumE =
        //   ev.rule.byweekday[ev.rule.byweekday.length - 1].weekday == 6
        //     ? 0
        //     : ev.rule.byweekday[ev.rule.byweekday.length - 1].weekday + 1;
 
        // if (day.date.getDay() == weeknumS && weeknumS != weeknumE) {
        //   return "rounded-e-lg";
        // } else if (day.date.getDay() == weeknumE && weeknumS != weeknumE) {
        //   return "rounded-s-lg";
        // } else if (
        //   day.date.getDay() != weeknumS &&
        //   day.date.getDay() != weeknumE
        // ) {
        //   return "rounded-sm";
        // } else {
        //   return "rounded-lg";
        // }

        return "rounded-sm"
      }
    };

    const dayNextMonth = computed({
      get() {
        const firstDayOfNextMonth = new Date(
          YearNow.value,
          monthNow.value + 1,
          1
        );

        return firstDayOfNextMonth;
      },
    });

    return {
      type,
      types,
      switchCalendar,

      monthNow,
      YearNow,
      returnDate,
      getMonthName,
      propsAllEvent,
      whatDay,
      nextDay,
      todayDay,
      selectDay,
      returnPeriod,
      funRoundet,
      dayNextMonth,
    };
  },
};
</script>

<style>
.v-calendar__container {
  overflow: auto;
  height: 87vh;
}
</style>
