<template>
  <v-col class="pb-2 pt-2 d-flex flex-column ml-n3" lg="3">
    <v-row no-gutters class="gap">
      <v-col>
        <v-checkbox-btn
          v-model="newDate"
          color="indigo-darken-4"
          label="Весь день"
        />
      </v-col>
    </v-row>
  </v-col>
</template>

<script>
import { computed, ref } from "vue";

export default {
  props: {
    dateEventStart: {
      type: Object,
      default: () => {},
    },
  },
  setup(props, { emit }) {
    const newDate = computed({
      get() {
        return propsDateEvent.value.allday;
      },
      set(newValue) {
        propsDateEvent.value.allday = newValue;
        if (newValue == true)
          (propsDateEvent.value.date_end = new Date(
            new Date(propsDateEvent.value.date_end).setHours(23, 59, 0)
          )) &&
            (propsDateEvent.value.date_start = new Date(
              new Date(propsDateEvent.value.date_start).setHours(0, 0, 0)
            ));
      },
    });

    const propsDateEvent = computed({
      get: () => props.dateEventStart,
      set: (value) => emit("update:dateEventStart", value),
    });

    return {
      newDate,
    };
  },
};
</script>

<style></style>
