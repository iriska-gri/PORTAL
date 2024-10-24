<template>
  <v-row no-gutters class="h-100">
    <v-col class="align-self-center flex-grow-0">
      <span class="vertext text-button my-1 pb-13">{{ sText }}</span>
    </v-col>

    <v-col class="w100">
      <v-row no-gutters class="text-center text-button py-2" v-if="sText == 'Руководство'">
      </v-row>
      <v-row no-gutters class="text-center text-button py-2" v-else>
      </v-row>
      <v-row no-gutters class="h-100">
        <slot name="cardboss"></slot>
      </v-row>
    </v-col>

  </v-row>
</template>

<script>
import { spravURL } from "@/utils/axios-api";
import { checkremote } from "@/utils/universal_functions";

export default {
  props: {
    sText: {
      type: String,
      default: "",
    },
  },
  setup() {
    return {
      checkremote,
      spravURL,
    };
  },
};
</script>

<style>

</style>
