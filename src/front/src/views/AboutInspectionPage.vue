<template>
  <pattern-tabs :tabs="tabs_items">
    <template v-slot:item>
      <v-window-item class="gap h-100" value="mainInfo">
        <general-information />
      </v-window-item>
      <v-window-item class="gap h-100" value="structureInspection">
        <structure-inspection />
      </v-window-item>
      <v-window-item class="gap h-100" value="openVacancies">
       <open-vacancies/>
      </v-window-item>
      <v-window-item class="gap h-100" value="contactInfo">
        <contact-info />
      </v-window-item>
    </template>
  </pattern-tabs>
</template>

<script>
import StructureInspection from "@/components/about_inspection/structure/StructureInspection.vue";
import ContactInfo from "@/components/about_inspection/contacts/ContactInfo.vue";
import { pagecounter } from "@/utils/universal_functions";
import PatternTabs from "@/components/UI/PatternTabs.vue";
import GeneralInformation from "@/components/about_inspection/general_information/GeneralInformation.vue";
import OpenVacancies from '@/components/about_inspection/open_vacancies/OpenVacancies.vue';

export default {
  components: {
    StructureInspection,
    ContactInfo,
    PatternTabs,
    GeneralInformation,
    OpenVacancies
  },

  setup() {
 
       pagecounter();
    return {
      tabs_items: [
        { title: "Общая информация", value: "mainInfo" },
        { title: "Структура инспекции", value: "structureInspection" },
        { title: "Открытые вакансии", value: "openVacancies" },
        { title: "Контактная информация", value: "contactInfo" },
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
