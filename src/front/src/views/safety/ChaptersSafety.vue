<template>
  <pattern-tabs :tabs="tabs_items">
    <template v-slot:item>
      <v-window-item class="gap  h-100  " value="mainInfo">
        <MainInfoSafety
          :formainpage="safetyData.mainpage_file"
          :responsibility="safetyData.type_resp"
          :commitee="safetyData.type_comm"
        ></MainInfoSafety>
      </v-window-item>
      <v-window-item class="gap h-100" value="document">
        <documentation-safety  :docSections = "safetyData"  />
      </v-window-item>
      <!-- <v-window-item class="gap h-100" value="testings">
        <TestSafety></TestSafety>
      </v-window-item> -->
    </template>
  </pattern-tabs>
</template>

<script>
import { ref, onMounted, onUpdated } from "vue";

import { pagecounter } from "@/utils/universal_functions";
import PatternTabs from "@/components/UI/PatternTabs.vue";
import { useRoute } from "vue-router";
import TestSafety from "@/views/safety/TestSafety.vue";
import MainInfoSafety from "@/views/safety/MainInfoSafety.vue";
import { axiosApiInstance } from "@/utils/axios-api";
import DocumentationSafety from "./DocumentationSafety.vue";

export default {
  components: {
    PatternTabs,
    TestSafety,
    MainInfoSafety,
    DocumentationSafety,
  },

  setup() {
    pagecounter();

    const safetyData = ref({});
    const loading = ref(false);
    const route = useRoute();
    const getSafety = () => {
      axiosApiInstance
        .get(`api/safety/?chapter=${route.params.chapter}`)
        .then((result) => {
          safetyData.value = result.data;
          loading.value = true;
        });
    };
    getSafety()
    // onMounted(() => getSafety())
    onUpdated(() => getSafety())

    return {
      safetyData,

      tabs_items: [
        { title: "Основная информация", value: "mainInfo" },
        { title: "Документация", value: "document" },
        // { title: "Тестирование", value: "testings" },
      ],
    };
  },
};
</script>
<style>
.active-tab {
  background-color: #e0f2f1;
  color: #004d40;
}

a {
  color: inherit;
}
</style>
