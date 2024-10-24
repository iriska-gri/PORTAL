<template>
  <div class="pa-0 align-self-center">
    <v-menu
      v-model="menu"
      :close-on-content-click="false"
      :max-width="800"
      offset-x
    >
      <template v-slot:activator="{ on, attrs }">
        <v-icon
          v-bind="attrs"
          v-on="on"
          size="large"
          color="indigo"
          icon="mdi-owl"
          @click="menu = !menu"
        ></v-icon>
      </template>

      <v-card class="whmy overflow-auto overflow-x-hidden">
        <v-row class="ma-3">
          <v-col>
            <pre
              >{{ pretext }}
</pre
            >
          </v-col>
        </v-row>
      </v-card>
    </v-menu>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  name: "myHelper",

  props: {
    pretext: {
      type: Object,
      default: () => {},
    },
  },

  setup() {
    const menu = ref(false);

    return { menu };
  },

  // data: () => ({

  //   menu: false,

  // }),
};
</script>

<style>
.whmy {
  height: 950px !important;
}
</style>
