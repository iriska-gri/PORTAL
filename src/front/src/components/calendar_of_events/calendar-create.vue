<template>
  <dialog-create
    :title="titleCard"
    :newOrOld="newCalendar"
    @closeDialog="$emit('closeDialog')"
    @delObject="delCalendar(propsCalendar.id)"
    @postData="postCalendar"
  >
    <template v-slot:card_text>
      <v-row no-gutters class="flex-column">
        <v-col class="d-flex flex-column">
          <v-row no-gutters class="align-center">
            <v-col class="text-body-2 text-text_grey pb-5" lg="2">

              Название
            </v-col>
            <v-col>
              <v-textarea
                density="compact"
                label="Описание"
                row-height="25"
                rows="1"
                variant="outlined"
                v-model="propsCalendar.cl_name"
                :rules="rules.cl_name"
              ></v-textarea></v-col
          ></v-row>
          <v-row no-gutters class="align-center pb-3">
            <v-col class="text-body-2 text-text_grey" lg="2"> Цвет </v-col>
            <v-col v-for="(x, key) in color" :key="key">
              <v-avatar
                class="cursor-pointer"
                @click="colorPik(x, key)"
                size="x-small"
                :color="x"
                :variant="
                  propsCalendar.cl_color === null
                    ? 'flat'
                    : propsCalendar.cl_color === x
                    ? 'flat'
                    : 'tonal'
                "
              /> </v-col
          ></v-row>

          <v-row no-gutters class="align-center pb-3">
            <v-col class="text-body-2 text-text_grey" lg="2"> Участники </v-col>
            <v-col>
              <calendar-create-select
                :staff="newStaff"
                @returnIdParticant="returnIdParticant"
              /> </v-col
          ></v-row>
        </v-col>
        <v-col class="d-flex flex-grow-0">
          <v-textarea
            density="compact"
            label="Описание"
            row-height="25"
            rows="4"
            variant="outlined"
            shaped
            no-resize
            :rules="rules.cl_descr"
            v-model="propsCalendar.cl_descr"
          ></v-textarea>
        </v-col>
        <v-row no-gutters class="align-center">
          <v-col class="text-body-2 text-text_grey" lg="2"> Редакторы </v-col>
          <v-col>
            <calendar-create-select
              :staff="newStaff"
              :okey="'editor'"
              @returnIdParticant="returnIdParticant"
            />
          </v-col>
          <v-col lg="1" class="text-center">
            <v-tooltip location="top">
              <template v-slot:activator="{ props }">
                <v-icon v-bind="props" icon="mdi-help-circle-outline" />
              </template>
              <div class="custom-tooltip">
                Участники с доступом редактирования смогут изменять поля
                календаря, а также редактировать и удалять события
              </div>
            </v-tooltip>
          </v-col>
        </v-row>
      </v-row>
    </template>
  </dialog-create>
</template>

<script>
import { computed, ref } from "vue";
import { axiosApiInstance } from "@/utils/axios-api";
import calendarCreateSelect from "@/components/calendar_of_events/calendar-create-select.vue";
import { useAlertStore } from "@/store/useAlertStore";
import DialogCreate from "./UI_calendar/dialogCreate.vue";
import { useAccountStore } from "@/store/AccountStore";

export default {
  components: { calendarCreateSelect, DialogCreate },

  props: {
    calendar: {
      type: Object,
      default: {},
    },
  },

  setup(props, { emit }) {
    const accountStore = useAccountStore();

    const returnIdParticant = (idPart) => {

      idPart.staff.forEach((e) => {
        let indx = propsCalendar.value.participant.findIndex(
          (l) => l.participant_calendar == e.id
        );
        let ind = propsCalendar.value.participant.find(
          (l) => l.participant_calendar == e.id
        );
        if (idPart.okey == "editor") {
          ind.editor = e.editor;
        } else {
          if (e.selected == true) {
            if (e.id != accountStore.user.is_idEmployee) {
              if (indx == -1) {
                propsCalendar.value.participant.push({
                  editor: false,
                  participant_calendar: e.id,
                });
              }
            }
          } else {
            let ind = propsCalendar.value.participant.findIndex(
              (l) => l.participant_calendar == e.id
            );

            if (ind != -1) {
              propsCalendar.value.participant.splice(ind, 1);
            }
          }
        }
      });

    };

    const propsCalendar = computed({
      get: () => props.calendar,
      set: (value) => emit("update:calendar", value),
    });

    const feedalert = useAlertStore().alert;

    const rules = {

      cl_name: [(val) => req(val)],
      cl_descr: [(val) => req(val)],
    };

    const titleCard = ref("");
    const newCalendar = ref(false);

    const calendarNewOrOld = () => {
      if (propsCalendar.value.hasOwnProperty("id")) {
        titleCard.value = "Редактирование календаря";
        if (propsCalendar.value.author != accountStore.user.is_idEmployee)
          newCalendar.value = true;
      } else {
        titleCard.value = "Новый календарь";

        newCalendar.value = true;
      }
    };
    calendarNewOrOld();

    const postCalendar = (val) => {
      if (val) {
        axiosApiInstance
          .post(`api/calendar_of_events/my_calendars/`, {
            ...props.calendar,
            participant: propsCalendar.value.participant,
          })
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

    const staff = ref([]);

    axiosApiInstance

      .get("api/calendar_of_events/get_employees/")
      .then((res) => {
        staff.value = res.data.filter((e) => e.employees.length > 0);
      });

    const newStaff = computed({
      get() {
        staff.value.forEach((e) => {
          if (propsCalendar.value.participant.length > 0) {
            e.employees.forEach((empl) => {
              let ab = propsCalendar.value.participant.find(
                (a) => a.participant_calendar === empl.id
              );
              if (ab) {
                empl.selected = true;
                empl.editor = ab.editor;
              } else {
                empl.selected = false;
                empl.editor = false;
              }
            });
          }
        });

        return staff.value;
      },
    });

    const color = [
      "red",
      "pink",
      "deep-orange",
      "amber",
      "yellow",
      "lime",
      "light-green",
      "green",
      "light-blue",
      "blue",
      "indigo",
      "deep-purple",
      "purple",
      "blue-grey",
      "brown",
    ];

    const colorPik = (col) => {
      if (propsCalendar.value.cl_color === col) {
        propsCalendar.value.cl_color = null;
      } else {
        propsCalendar.value.cl_color = col;
      }
    };

    const delCalendar = (idcal) => {
      axiosApiInstance
        .delete(`api/calendar_of_events/my_calendars/?delid=${idcal}`)
        .then((result) => {
          feedalert.alert = true;
          feedalert.text = result.data.mess;
          feedalert.ico = "mdi-check";
          feedalert.color = "orange-accent-1";
          emit("getCalendar");
        });
      emit("closeDialog");
    };

    const req = (val) => {

      return !!val || "Поле обязательно";
    };

    return {
      postCalendar,
      color,
      colorPik,
      returnIdParticant,
      propsCalendar,
      delCalendar,
      rules,
      titleCard,
      newCalendar,
      newStaff,
    };
  },
};
</script>

<style>
.custom-tooltip {
  max-width: 350px; /* Установка максимальной ширины для подсказки */
}
</style>
