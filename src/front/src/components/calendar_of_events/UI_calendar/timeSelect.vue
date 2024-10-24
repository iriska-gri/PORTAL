<template>
  <v-col lg="3" :class="`order-${order[0]}`">
    <v-menu
      v-model="menudate"
      :close-on-content-click="false"
      :nudge-right="40"
      transition="scale-transition"
      offset-y
    >
      <template v-slot:activator="{ props }">
        <v-textarea
          v-model="modelDate"
          :value="formatComa(modelDate)"
          density="compact"
          no-resize
          row-height="25"
          rows="1"
          variant="outlined"
          v-bind="props"
          readonly
          hide-details
        >
          <template v-slot:prepend-inner>
            <v-icon
              v-bind="props"
              icon="mdi-calendar-today"
              color="cyan-darken-3"
              size="x-small"
            />
          </template>
        </v-textarea>
      </template>

      <v-locale-provider locale="ru">
        <v-date-picker
          v-model="modelDate"
          show-adjacent-months
          hide-header
          border
          no-time
          :max="order[0] == 2 ? new Date(limitation) : endMax()"
          :min="order[0] == 2 ? startMin() : minData()"
        />
      </v-locale-provider>
    </v-menu>
  </v-col>
  <v-col class="flex-grow-0" :class="`order-${order[1]}`">
    <v-textarea
      density="compact"
      no-resize
      row-height="25"
      width="75"
      rows="1"
      readonly
      variant="outlined"
      v-model="timeEvent"
      :active="menutime"
      :focus="menutime"
      hide-details
      :disabled="chek"
    >
    </v-textarea>
    <v-menu
      v-model="menutime"
      :close-on-content-click="false"
      activator="parent"
      transition="scale-transition"
    >
      <v-time-picker
        v-if="menutime"
        v-model="timeEvent"
        full-width
        format="24hr"
      ></v-time-picker>
    </v-menu>
  </v-col>
</template>

<script>
import { ref, computed } from "vue";
import { formatComa, formatDash } from "@/utils/universal_functions";
export default {
  props: {
    dateEvent: {
      type: String,
      default: "",
    },

    limitation: {
      type: String,
      default: "",
    },

    order: {
      type: Array,
      default: [0, 0],
    },
    chek: {
      type: Boolean,
      default: false,
    },
    rule: {
      type: Number,
      default: -1,
    },
  },

  setup(props, { emit }) {
    const menudate = ref(false);
    const menutime = ref(false);

    const propsDateEvent = computed({
      get: () => new Date(props.dateEvent),
      set: (value) => emit("update:dateEvent", value),
    });

    const modelDate = computed({
      get() {
        return propsDateEvent.value;
      },
      set(newValue) {
        creatwdDate(newValue, timeEvent.value);
      },
    });

    const timeEvent = computed({
      get() {
        return `${new Date(propsDateEvent.value).getHours()}:${String(
          new Date(propsDateEvent.value).getMinutes()
        ).padStart(2, "0")}`;
      },

      set(newValue) {
        creatwdDate(modelDate.value, newValue);
      },
    });

    const creatwdDate = (date, time) => {
      let tzero = time.split(":");
      time = tzero[0].padStart(2, "0") + ":" + tzero[1];

      if (props.order[0] == 4) {
        if (time == "0:00") {
          propsDateEvent.value = date;
        } else if (
          new Date(formatDash(date) + "T" + time) >= new Date(props.limitation)
        ) {
          propsDateEvent.value = new Date(formatDash(date) + "T" + time);
        } else {
          propsDateEvent.value = new Date(props.limitation);
        }
      } else {
        propsDateEvent.value =
          time == "0:00" ? date : new Date(formatDash(date) + "T" + time);
      }
    };

    const minData = () => {
      let h = `${new Date(props.limitation).getHours()}:${String(
        new Date(props.limitation).getMinutes()
      ).padStart(2, "0")}`;
      let min =
        h == "0:00"
          ? new Date(props.limitation)
          : new Date(
              new Date(props.limitation).setDate(
                new Date(props.limitation).getDate() - 1
              )
            );
      return new Date(min);
    };

    const startMin = () => {
      if (props.rule == 2) {
        return new Date(
          new Date(props.limitation).setDate(
            new Date(props.limitation).getDate() - 7
          )
        );
      }
      return false;
    };

    const endMax = () => {
      if (props.rule == 2) {
        return new Date(
          new Date(props.limitation).setDate(
            new Date(props.limitation).getDate() + 6
          )
        );
      }
      return false;
    };

    return {
      propsDateEvent,
      menudate,
      menutime,
      modelDate,
      formatComa,
      timeEvent,
      minData,
      startMin,
      endMax,
    };
  },
};
</script>

<style></style>
