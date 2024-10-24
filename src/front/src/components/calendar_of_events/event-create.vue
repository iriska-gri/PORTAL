<template>
  <dialog-create
    :title="titleCard"
    :newOrOld="newEvent"
    @postData="postData"
    @closeDialog="$emit('closeDialog')"
    @delObject="delEvent(propsEvent.event.id)"
    ref="createDialog"
  >
    <template v-slot:card_text>
      <v-row no-gutters class="flex-column">
        <v-col class="d-flex flex-column">
          <v-row no-gutters class="align-center">
            <!-- <my-helper :pretext="propsEvent.event" /> -->

            <v-col class="text-body-2 text-text_grey pb-5" lg="2">
              Название
            </v-col>

            <v-col>
              <v-textarea
                density="compact"
                label="Добавить название"
                row-height="25"
                rows="1"
                variant="outlined"
                v-model="propsEvent.event.name"
                :rules="rules.name"
              ></v-textarea> </v-col
          ></v-row>

          <v-row no-gutters class="align-center">
            <v-col class="text-body-2 text-text_grey pb-5" lg="2">
              Участники
            </v-col>
            <v-col>
              <calendar-create-select
                :staff="newStaff"
                @returnIdParticant="returnIdParticant"
              /> </v-col
          ></v-row>

          <v-row no-gutters class="align-center pb-3">
            <v-col class="text-body-2 text-text_grey" lg="2"> Календарь</v-col>
            <v-col>
              <v-autocomplete
                v-model="calendar"
                :items="propsEvent.mycalendars"
                label="Выберите календарь или найдите по названию"
                item-title="cl_name"
                item-value="id"
                hide-details
                variant="outlined"
                density="compact"
                class="py-3"
                return-object
                :disabled="'id' in propsEvent.event"
              >
                <template v-slot:selection="{ item }">
                  <v-avatar
                    class="cursor-pointer"
                    size="8"
                    :color="item.raw.cl_color"
                  />
                  <span class="pl-2">
                    {{ item.title }}
                  </span>
                </template>
                <template v-slot:item="{ item }">
                  <v-list-item
                    :key="item.title"
                    :value="item"
                    color="primary"
                    @click.stop="calendar = item"
                  >
                    <template v-slot:prepend>
                      <v-avatar
                        class="cursor-pointer"
                        size="8"
                        :color="item.raw.cl_color"
                      />
                    </template>
                    {{ item.title }}
                  </v-list-item>
                </template>
              </v-autocomplete>
            </v-col></v-row
          >
          <v-row no-gutters class="align-top">
            <v-col class="text-body-2 text-text_grey pt-3" lg="2">
              Дата и время
            </v-col>
            <v-col class="d-flex flex-column">
              <v-row no-gutters class="gap">
                <time-select
                  :rule="
                    returnPeriod != repeatRules[0].type
                      ? returnPeriod.rule.freq
                      : -1
                  "
                  :chek="propsEvent.event.allday"
                  :order="[2, 1]"
                  :dateEvent="String(propsEvent.event.date_start)"
                  :limitation="String(propsEvent.event.date_end)"
                  @update:dateEvent="propsEvent.event.date_start = $event"
                />
                <v-col class="order-3 flex-grow-0">
                  <v-icon icon="mdi-minus pt-4" color="grey-darken-1" />
                </v-col>
                <time-select
                  :rule="
                    returnPeriod != repeatRules[0].type
                      ? returnPeriod.rule.freq
                      : -1
                  "
                  :chek="propsEvent.event.allday"
                  :order="[4, 5]"
                  :dateEvent="String(propsEvent.event.date_end)"
                  :limitation="String(propsEvent.event.date_start)"
                  @update:dateEvent="propsEvent.event.date_end = $event"
                />
              </v-row>
              <v-row no-gutters>
                <period-events
                  :dateEventStart="propsEvent.event"
                  @update:dateEventStart="propsEvent.event = $event"
                />
                <v-col lg="7" class="pt-2 ml-5">
                  <v-autocomplete
                    v-model="returnPeriod"
                    :items="repeatRules"
                    variant="outlined"
                    density="compact"
                    return-object
                    item-title="type"
                    item-value="id"
                  >
                    <template v-slot:item="{ props, item }">
                      <v-list-item
                        v-bind="props"
                        :key="item.title"
                        :value="item"
                        color="primary"
                        :disabled="periodDisplayRule(item.raw.id)"
                        @click="returnPeriod = item.raw"
                      />
                    </template>
                  </v-autocomplete>
                </v-col>
              </v-row> </v-col
          ></v-row>
        </v-col>
        <v-row no-gutters class="align-top flex-grow-0">
          <v-col class="text-body-2 text-text_grey pt-3 h-0" lg="2">
            Напоминание
          </v-col>
          <v-col class="d-flex flex-column">
            <v-row no-gutters class="gap flex-grow-0">
              <reminder-event />
            </v-row>
            <v-row no-gutters class="flex-grow-0">
              <v-col>
                <v-btn
                  disabled
                  prepend-icon="mdi-plus"
                  variant="text"
                  class="text-body-2 text-text_grey"
                >
                  Добавить уведомление
                </v-btn>
              </v-col>
            </v-row>
          </v-col></v-row
        >
        <v-row no-gutters class="align-center">
          <v-col class="text-body-2 text-text_grey pb-5" lg="2"> Файлы </v-col>

          <uploading-file
            :files="propsEvent.event.files"
            @update:files="propsEvent.event.files = $event"
            @postFiles="postFiles"
          />
        </v-row>
        <v-row no-gutters class="align-center">
          <v-col>
            <v-textarea
              density="compact"
              label="Дополнительное описание"
              row-height="25"
              rows="3"
              variant="outlined"
              v-model="propsEvent.event.description"
            ></v-textarea> </v-col
        ></v-row>
      </v-row>
    </template>
  </dialog-create>
</template>

<script>
import { computed, ref } from "vue";
import { axiosApiInstance } from "@/utils/axios-api";
import DialogCreate from "@/components/calendar_of_events/UI_calendar/dialogCreate.vue";
import calendarCreateSelect from "@/components/calendar_of_events/calendar-create-select.vue";
import { formatComa } from "@/utils/universal_functions";
import TimeSelect from "@/components/calendar_of_events/UI_calendar/timeSelect.vue";
import { useAccountStore } from "@/store/AccountStore";
import UploadingFile from "@/components/UI/defaultportal/uploading-file.vue";
import ReminderEvent from "@/components/calendar_of_events/UI_calendar/reminderEvent.vue";
import PeriodEvents from "@/components/calendar_of_events/UI_calendar/periodEvents.vue";
import { useAlertStore } from "@/store/useAlertStore";
import { RRule } from "rrule";

export default {
  components: {
    calendarCreateSelect,
    DialogCreate,
    TimeSelect,
    UploadingFile,
    ReminderEvent,
    PeriodEvents,
  },

  props: {
    eventCalendar: {
      type: Object,
      default: () => {},
    },
  },

  setup(props, { emit }) {
    const createDialog = ref(null);

    const propsEvent = computed({
      get: () => {
        return props.eventCalendar;
      },

      set: (value) => emit("update:eventCalendar", value),
    });

    const repeatRules = [
      { type: "Не повторять", rule: {}, id: 1 },
      { type: "Каждый день", rule: { freq: 3 }, id: 2 },
      { type: "Каждую неделю", rule: { freq: 2 }, id: 3 },
      { type: "Каждый месяц", rule: { freq: 1 }, id: 4 },
      { type: "Каждый год", rule: { freq: 0 }, id: 5 },
    ];

    const returnPeriod = computed({
      get() {
        let select = "";
        if (propsEvent.value.event.period != null) {
          let objRule = JSON.parse(propsEvent.value.event.period);
          if (objRule != null) {
            drawingRule(objRule.origOptions);
            repeatRules.findIndex(
              (e) => e.rule.freq == objRule.origOptions.freq
            );
            select =
              repeatRules[
                repeatRules.findIndex(
                  (e) => e.rule.freq == objRule.origOptions.freq
                )
              ];
          }
        } else {
          select = repeatRules[0].type;
        }

        calendarNewOrOld();

        return select;
      },
      set(newValue) {
        drawingRule(newValue.rule);
      },
    });

    const drawingRule = (value) => {
      let newRulse;
      if (value.freq == 3) {
        newRulse = new RRule({
          ...value,
          dtstart: new Date(propsEvent.value.event.date_start),
          until: new Date(propsEvent.value.event.date_end),
        });
      }

      if (value.freq == 2) {
        newRulse = new RRule({
          ...value,
          dtstart: new Date(propsEvent.value.event.date_start),
          byweekday: getWeekNumbersBetweenDates(),
        });
      }
      if (value.freq == 1) {
        newRulse = new RRule({
          ...value,
          bymonthday: getMonthBetweenDates(),
          dtstart: new Date(propsEvent.value.event.date_start),
        });
      }
      if (value.freq == 0) {
        newRulse = new RRule({
          ...value,
          bymonthday: getYearBetweenDates(),
          dtstart: new Date(propsEvent.value.event.date_start),
          bymonth: getNumberMonth(),
        });
      }
      // byweekday: getWeekNumbersBetweenDates(),
      Object.keys(value).length == 0
        ? (propsEvent.value.event.period = null)
        : (propsEvent.value.event.period = JSON.stringify(newRulse));
    };

    const rulleWeek = [
      RRule.SU,
      RRule.MO,
      RRule.TU,
      RRule.WE,
      RRule.TH,
      RRule.FR,
      RRule.SA,
    ];

    const feedalert = useAlertStore().alert;

    const req = (val) => {
      return !!val || "Поле обязательно";
    };

    const rules = {
      name: [(val) => req(val)],
    };

    const staff = ref([]);

    axiosApiInstance

      .get("api/calendar_of_events/get_employees/")
      .then((res) => {
        staff.value = res.data.filter((e) => e.employees.length > 0);
      });

    const accountStore = useAccountStore();

    const newStaff = computed({
      get() {
        let ns = [];

        let indCal = propsEvent.value.mycalendars.findIndex(
          (e) => e.id == calendar.value[0].id
        );

        staff.value.forEach((e) => {
          let emp = { ...e };
          emp.employees = e.employees.filter((n) => {
            if (
              n.id == accountStore.user.is_idEmployee ||
              propsEvent.value.event.participant.some((e) => n.id == e)
            ) {
              n.selected = true;
            }

            return propsEvent.value.mycalendars[indCal].participant.some(
              (part) => part.id === n.id
            );
          });

          if (emp.employees.length > 0) ns.push(emp);
        });
        return ns;
      },
    });

    const delEvent = (idev) => {
      axiosApiInstance
        .delete(`api/calendar_of_events/my_events/?delid=${idev}`)
        .then((result) => {
          feedalert.alert = true;
          feedalert.text = result.data.mess;
          feedalert.ico = "mdi-check";
          feedalert.color = "orange-accent-1";
          emit("getCalendar");
        });
      emit("closeDialog");
    };

    const files = ref([]);
    const postFiles = (f) => {
      files.value = f;
    };

    const calendar = computed({
      get() {
        let selected = [];
        if (propsEvent.value.event.calendar) {
          let ind = propsEvent.value.mycalendars.findIndex(
            (e) => e.id == propsEvent.value.event.calendar
          );
          selected.push({
            cl_name: propsEvent.value.mycalendars[ind].cl_name,
            cl_color: propsEvent.value.mycalendars[ind].cl_color,
            id: propsEvent.value.mycalendars[ind].id,
          });
        } else {
          selected.push({
            cl_name: propsEvent.value.mycalendars[0].cl_name,
            cl_color: propsEvent.value.mycalendars[0].cl_color,
            id: propsEvent.value.mycalendars[0].id,
          });
        }
        if (propsEvent.value.event.calendar == null)
          propsEvent.value.event.calendar = propsEvent.value.mycalendars[0].id;

        return selected;
      },

      set(newValue) {
        propsEvent.value.event.calendar = newValue.value;
      },
    });

    const titleCard = ref("");
    const newEvent = ref(false);

    const calendarNewOrOld = () => {
      if (propsEvent.value.event.hasOwnProperty("id")) {
        titleCard.value = "Редактирование события";
        newEvent.value = false;
      } else {
        titleCard.value = "Новое событие";
        newEvent.value = true;
      }
    };

    const returnIdParticant = (idPart) => {
      idPart.staff.forEach((e) => {
        if (
          e.selected == true &&
          !propsEvent.value.event.participant.includes(e.id)
        ) {
          propsEvent.value.event.participant.push(e.id);
        } else {
          let ind = propsEvent.value.event.participant.findIndex(
            (l) => l == e.id
          );

          if (ind != -1) {
            propsEvent.value.event.participant.splice(ind, 1);
          }
        }
      });
    };

    const cbSelect = (item, arr) => {
      item.forEach((e) => {
        if (!("employees" in e)) {
          if (!propsEvent.value.event.participant.includes(e.id)) {
            propsEvent.value.event.participant.push(e.id);
          }
        }
        if ("employees" in e) {
          cbSelect(e.employees);
        }
      });
    };

    const dateEvent = computed({
      get() {
        return formatComa(new Date(propsEvent.value.event.date_start));
      },

      set(newValue) {
        let dateParts = newValue.split(".");

        // let d = new Date(propsEvent.value.event.date_start).setFullYear(parseInt(dateParts[2], 10), parseInt(dateParts[1], 10), parseInt(dateParts[0], 10))
        // let d = new Date(propsEvent.value.event.date_start).setDate(new Date(2024,01,01))
        // propsEvent.value.event.date_start = new Date(2024,01,01);
      },
    });

    const menudate = ref(false);

    const postData = (validate) => {
      if (validate) {
        let postEvent = new FormData();
        postEvent.append(
          "event",
          JSON.stringify({ ...propsEvent.value.event })
        );
        if (propsEvent.value.event.files !== null) {
          files.value.forEach((e) => postEvent.append("files", e));
        }

        axiosApiInstance
          .post("api/calendar_of_events/my_events/", postEvent)
          .then((result) => {
            feedalert.alert = true;
            feedalert.text = result.data.mess;
            feedalert.ico = "mdi-check";
            feedalert.color = "green-darken-4";
            emit("getCalendar");
            emit("closeDialog");
          });
      }
    };

    const getWeekNumbersBetweenDates = () => {
      const start = new Date(propsEvent.value.event.date_start);
      const end = new Date(propsEvent.value.event.date_end);
      let s = start.getDay();
      let e = end.getDay();
      const weekNumbers = [];
      if (start.getDay() > end.getDay()) {
        e = 6;
        for (let x = s; x <= e; x++) {
          weekNumbers.push(x);
        }
      }
      if (start.getDay() != end.getDay() && start.getDay() > end.getDay()) {
        s = 0;

        for (let x = s; x <= end.getDay(); x++) {
          weekNumbers.push(x);
        }
      }
      if (start.getDay() < end.getDay()) {
        for (let x = s; x <= end.getDay(); x++) {
          weekNumbers.push(x);
        }
      }
      if (start.getDay() == end.getDay()) {
        weekNumbers.push(start.getDay());
      }
      let rulesWeek = [];
      weekNumbers.forEach((i) => {
        rulesWeek.push(rulleWeek[i]);
      });

      return rulesWeek;
    };

    const getMonthBetweenDates = () => {
      const start = new Date(propsEvent.value.event.date_start);
      const end = new Date(propsEvent.value.event.date_end);
      let s = start.getDate();
      let e = end.getDate();

      const dateNumbers = [];
      for (let x = s; x <= e; x++) {
        dateNumbers.push(x);
      }
      console.log(dateNumbers.length, "дни в месяце");
      return dateNumbers;
    };

    const getYearBetweenDates = () => {

      const start = new Date(propsEvent.value.event.date_start);
      const end = new Date(propsEvent.value.event.date_end);
      let dates = getDatesBetweenDates(start, end);
      let date = [];
      dates.forEach((e) => date.push(new Date(e).getDate()));
      return date;
    };

    const getNumberMonth = () => {
      const start = new Date(propsEvent.value.event.date_start);
      const end = new Date(propsEvent.value.event.date_end);
      let sm = start.getMonth();
      let em = end.getMonth();
      let month = [];
      month.push(sm + 1);

      if (!month.includes(em + 1)) month.push(em + 1);
      console.log(month, "month");
      return month;
    };

    const getDatesBetweenDates = (startDate, endDate) => {
      let dates = [];
      let currentDate = new Date(startDate);

      while (currentDate <= endDate) {
        dates.push(new Date(currentDate));
        currentDate.setDate(currentDate.getDate() + 1);
      }

      return dates;
    };

    const what = (w) => {
      console.log(w, "?????????????????????????????????");
    };

    const periodDisplayRule = (idItem) => {
      if (getNumberOfDays.value >= 7 && idItem == 3) {
        return true;
      } else return false;
    };

    const getNumberOfDays = computed({
      get() {
        const start = new Date(propsEvent.value.event.date_start);
        const end = new Date(propsEvent.value.event.date_end);
        const oneDay = 1000 * 60 * 60 * 24;
        const diffInTime = end.getTime() - start.getTime();
        const diffInDays = Math.round(diffInTime / oneDay);

        return diffInDays;
      },
    });

    return {
      menudate,
      titleCard,
      newEvent,
      propsEvent,
      dateEvent,
      calendar,
      staff,
      newStaff,
      returnIdParticant,
      postFiles,
      postData,
      rules,
      delEvent,

      repeatRules,
      returnPeriod,
      periodDisplayRule,
      what,

      createDialog,
      getMonthBetweenDates,
    };
  },
};
</script>

<style></style>
