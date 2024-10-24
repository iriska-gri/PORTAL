<template>
  <v-expansion-panels
    class="calendar"
    variant="accordion"
    flat
    tile
    static
    v-model="openGroup"
  >
    <v-expansion-panel elevation="0" flat tile static>
      <v-expansion-panel-title flat tile static class="py-0 px-3">
        <div @click.stop="">
          <span class="text-subtitle-2"> {{ title }} </span>
        </div>

        <v-btn
          v-if="title == 'Мои календари'"
          size="x-small"
          icon="mdi-plus"
          variant="text"
          class="pa-0"
          @click.stop="editCreatedCalendar()"
        ></v-btn>
      </v-expansion-panel-title>
      <v-expansion-panel-text flat tile static>
        <template v-if="Object.keys(calendars).length > 0">
          <v-list-item
            v-for="(x, i) in calendars"
            :key="i"
            :value="x.cl_name"
            @mouseenter="hover = i"
            @mouseleave="hover = null"
            :class="{ trasitlist: hover === i }"
            class="pa-0 cursor-default"
          >
            <template v-slot:prepend>
              <v-checkbox-btn
                class="text-caption"
                :class="`text-${x.cl_color}`"
                v-model="x.visible"
                :color="x.cl_color"
                @update:modelValue="chekUpdate(x)"
              ></v-checkbox-btn>
            </template>
            <template v-slot:title>
              <span class="text-body-2"> {{ x.cl_name }} </span>
            </template>

            <template v-slot:append>
       
              <transition name="fade">
                <v-btn
                  v-if="
                    x.author == accountStore.user.is_idEmployee ||
                    x.participant.some(
                      (e) =>
                        e.editor == true &&
                        e.participant_calendar ==
                          accountStore.user.is_idEmployee
                    )
                  "
                  size="x-small"
                  icon="mdi-pen"
                  variant="text"
                  class="transitbtn"
                  @click.stop="editCreatedCalendar(x)"
                ></v-btn>
              </transition>
            </template>
          </v-list-item>
        </template>
        <template v-else>
          <div class="text-caption text-grey text-center">Календарей нет</div>
        </template>
      </v-expansion-panel-text>
    </v-expansion-panel>
    <v-dialog v-model="showDialog" min-width="636" max-width="800"> 
    <calendar-create
      @closeDialog = "showDialog = false"
      :calendar="calendar"
      @update:calendar="calendar = $event"
      @getCalendar="$emit('getCalendar')"
    />
    </v-dialog>
  </v-expansion-panels>
</template>

<script>
import { ref } from "vue";
import calendarCreate from "@/components/calendar_of_events/calendar-create.vue";
import { useAccountStore } from "@/store/AccountStore";
export default {
  components: { calendarCreate },

  props: {
    calendars: {
      type: Array,
      default: () => [],
    },

    title: {
      typr: String,
      default: "",
    },
  },

  setup(props, { emit }) {
    const showDialog = ref(false);
    const accountStore = useAccountStore();
    const calendar = ref({});
    const openGroup = ref([0]);
    const trans = ref(false);
    const hover = ref(0);

    const editCreatedCalendar = (cal) => {

      if (cal === undefined) {
        calendar.value = {
          cl_name: "",
          participant: [{ editor: true, participant_calendar: accountStore.user.is_idEmployee }],
          cl_color: "red",
          cl_descr: "",
        };
      } else {
       
        calendar.value = cal;
      }
      showDialog.value = true;
    };

    const chekUpdate = (cal) => {
      let setcal = new Set(accountStore.calendar);
      if (cal.visible == false) {
        setcal.add(cal.id);
      } else {
        setcal.delete(cal.id);
      }
      accountStore.calendar = Array.from(setcal);
    };

    return {
      showDialog,
      calendar,
      editCreatedCalendar,
      chekUpdate,
      accountStore,
      openGroup,
      trans,
      hover,
    };
  },
};
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.1s;
}
.fade-enter,
.fade-leave-to {
  transition: opacity 0.2s;
  opacity: 0;
}

.calendar .v-expansion-panel-text__wrapper {
  padding: 0 !important;
  padding-right: 10px !important;
}
.trasitlist:hover .transitbtn {
  animation-fill-mode: forwards;
  /* transition: opacity 0.1s; */
  animation-duration: 0.5s;
  animation-name: filli;
}

@keyframes filli {
  from {
    margin-left: 100%;
    opacity: 0;
  }

  to {
    margin-left: 0%;
    opacity: 1;
  }
}

.transitbtn {
  opacity: 0;

  /* animation-direction: reverse; */
  /* animation-duration: 0.1s;
  animation-name: filli; */
}
</style>
