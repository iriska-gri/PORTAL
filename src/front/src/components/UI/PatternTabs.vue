<template>
  <v-row no-gutters class="flex-column gap pa-1">
    <v-col class="v-col-auto">
      <v-card>
        <v-tabs
          v-model="tab"
          bg-color="teal-darken-1"
          slider-color="teal-lighten-3"
          selected-class="active-tab"
          :grow="true"
        >
          <v-tab
            v-for="(tabitem, key) in tabs"
            :value="tabitem.value"
            :key="key"
            
          >
            {{ tabitem.title }}
          </v-tab>
        </v-tabs>
     
      </v-card>
    </v-col>
    <v-col class="">
      <v-window v-model="tab" class="h-100">
        <slot name="item" />
      </v-window>
    </v-col>
  </v-row>
</template>

<script>
import { ref } from "vue";

export default {
  props: {
    tabs: {
      type: Object,
      default: () => {},
    },
  },

  setup() {
    return {
      tab: ref(null),
    };
  },
};
</script>

<style></style>
