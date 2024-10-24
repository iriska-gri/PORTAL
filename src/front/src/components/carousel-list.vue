<template>
  <v-carousel
    cycle
    interval="10000"
    cover
    height="450"
    hide-delimiters
    hide-delimiter-background
    :show-arrows="carous.length<2?false:'hover'"
    color="white"
  >

    <v-carousel-item
      v-for="(x, i) in carous"
      :key="i"
      :src="`${burl}${x.link}`"
      cover
      eager
    >

      <v-container
        fill-height
        fluid
        pa-0
        ma-0
        pb-3
        class="flex-column h-100 d-flex"
      >
        <v-card
          v-if="x.text != '' || x.title != null"
          class="bgCard h-100 d-flex flex-column"
        >
          <v-card-title
            v-if="x.title != null"
            class="text-h3 text-uppercase titles text-text_carous ma-1 mb-0"
          >
            <v-row no-gutters>
              <v-col class="align-self-center">
                {{ x.title }}
              </v-col>
              <v-col class="flex-grow-0">
                <v-img
                  width="50"
                  :aspect-ratio="1"
                  :src="`${burl}${x.sender}`"
                  cover
                />
              </v-col>
            </v-row>
          </v-card-title>
          <v-card-text
            v-if="x.text != ''"
            class="w-50 flex-grow-0 text-h6 bgText overflow-auto ma-1 pa-0"
          >
            <v-textarea
              class="text-text_caroustext-black textareas font-weight-medium nocursor"
              :model-value="x.text"
              variant="solo"
              readonly
              auto-grow
              rows="1"
              hide-details
              flat
              bg-color="transparent"
            />
          </v-card-text>
        </v-card>
      </v-container>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
import { ref } from "vue";
import { baseURL } from "@/utils/axios-api";
import { axiosApiInstance } from "@/utils/axios-api";
import { useAlertStore } from "@/store/useAlertStore";

export default {
  setup() {
    const burl = baseURL.slice(0, -1);

    const carous = ref([{ link: `/media/newsimage/scales.jpg`, "title": null, "text": "" }]);
    const feedalert = useAlertStore().alert;

    const getfromserver = () => {
      axiosApiInstance.get("api/navigation/carousels/").then((result) => {
        if (result.data.mess != "") {
          feedalert.alert = true;
          feedalert.text = result.data.mess;
          feedalert.color = "red-darken-2";
          feedalert.ico = "mdi-alert-outline";
        }

        if (result.data.result.length > 0) {
          carous.value = result.data.result;
        }
        
      });
    };

    getfromserver();

    return {
      burl,
      carous,
    };
  },
};
</script>

<style>
.titles {
  font-family: cursive !important;
  background: #ffffff8c;
}

.textareas .v-field__input {
  font-size: 1.3em !important;
}

.nocursor textarea {
  cursor: default !important;
}
</style>
