<template>
  <v-row no-gutters class="flex-column h-100 gap">
    <v-col>
      <v-row no-gutters class="flex-column h-100 gap">
        <v-col class="w100 flex-grow-0">
          <v-card class="text-center">
            <v-card-text class="font-weight-medium text-lg-h6">
              Межрегиональная инспекция Федеральной налоговой службы по
              централизованной обработке данных №2

              <p class="font-weight-medium text-lg-subtitle-1 text-sm-caption">
                создана 01.02.2018 года в соответствии с приказом ФНС России от
                27.12.2017 №ММВ-7-4/1102
              </p>

              <p class="mt-3">
                <a class="text-decoration-none" :href="caCuratorLink"
                  >Работа МИ ФНС России по ЦОД №2 координируется заместителем
                  руководителя ФНС России Будариным Андреем Владимировичем</a
                >
              </p>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col class="d-flex">
          <v-row no-gutters class="gap">
            <v-col lg="3" class="flex-column">
              <v-row no-gutters class="gap flex-column h-100">
                <v-col class="w100">
                  <v-card class="h-100">
                    <v-card-title class="text-h6 text-uppercase text-center">
                      Начальник инспекции</v-card-title
                    >
                    <v-divider class="mb-3" />

                    <v-img
                      :src="checkremote(`${spravURL}${userlinks.login}.jpg`)"
                      height="200"
                    />

                    <v-card-title class="text-h6 text-center">{{
                      userlinks.fio
                    }}</v-card-title>
                    <v-card-text class="text-center text-body-2">
                      <p>
                        Государственный советник Российской Федерации 2 класса
                      </p>
                    </v-card-text>
                  </v-card>
                </v-col>
                <v-col class="w100 flex-column d-flex">
                  <general-information-size
                  :size="getfactsize"
                    :title="'Фактическая численнность'"
                  />
                </v-col>
                <v-col class="w100 flex-column d-flex">
                  <general-information-size
                  :size="getstatesize"
                   
                    :title="'Штатная численность'"
                  />
                </v-col>
              </v-row>
            </v-col>
            <v-col>
              <v-card class="h-100 flex-column d-flex">
                <v-card-title class="text-h6 text-uppercase text-center">
                  Основные направления деятельности инспекции
                </v-card-title>
                <v-divider class="pb-3" />

                <v-row
                  no-gutters
                  class="gap"
                  :class="lgAndUp ? 'h-0 overflow-auto' : ''"
                >
                  <v-col class="flex-column d-flex">
                    <v-col
                      class="px-3 py-2 flex-grow-0"
                      v-for="direction in directionworks"
                      :key="direction.id"
                    >
                      <v-card class="d-flex" :elevation="3">
                        <v-col class="d-flex align-center v-col-auto">
                          <v-avatar
                            class="elevation-10 text-teal-darken-4"
                            color="teal-lighten-5"
                          >
                            <v-icon :icon="direction.icon_name"></v-icon>
                          </v-avatar>
                        </v-col>
                        <v-col
                          class="d-flex align-center justify-start text-h6"
                        >
                          {{ direction.direction_title }}
                        </v-col>
                      </v-card>
                    </v-col>
                  </v-col>
                  <!-- <v-col
                    lg="12"
                    class="px-3"
                    v-for="direction in 10"
                    :key="direction.id"
                  >
                    <v-card class="d-flex" :elevation="3">
                      <v-col class="d-flex align-center justify-center">
                        <v-avatar
                          class="elevation-10 text-teal-darken-4"
                          color="teal-lighten-5"
                        >
                          <v-icon :icon="direction.icon_name"></v-icon>
                        </v-avatar>
                      </v-col>
                      <v-col
                        lg="11"
                        class="d-flex align-center justify-start text-h6"
                      >
                        {{ direction.direction_title }}
                      </v-col>
                    </v-card>
                  </v-col> -->
                </v-row>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row></v-col
    >
  </v-row>
</template>

<script>
import { ref } from "vue";
import { axiosApiInstance } from "@/utils/axios-api";
import { checkremote } from "@/utils/universal_functions";
import { spravURL, baseURL } from "@/utils/axios-api";
import { useDisplay } from "vuetify";
import GeneralInformationSize from "@/components/about_inspection/general_information/GeneralInformationSize.vue";

export default {
  components: { GeneralInformationSize },
  setup() {
    const { lgAndUp } = useDisplay();
    const userlinks = ref([]);
    const getfactsize = ref({ factsize: 0, date_created: new Date() });
    const getstatesize = ref({ statesize: 0, date_created: new Date() });
    const directionworks = ref([]);

    const infouser = () => {
      axiosApiInstance
        .get("api/accounts/getuser/?userlogin=9966-00-001")
        .then((res) => {
          userlinks.value = res.data;
        });
    };
    const getFactSize = () => {
      axiosApiInstance.get("api/about_inspection/getfactsize/").then((res) => {
        getfactsize.value = res.data;
      });
    };

    const getStateSize = () => {
      axiosApiInstance.get("api/about_inspection/getstatesize/").then((res) => {
        getstatesize.value = res.data;
      });
    };

    const getInspectionDirections = () => {
      axiosApiInstance
        .get("api/about_inspection/getinspectiondirections/")
        .then((res) => {
          directionworks.value = res.data;
        });
    };

    getInspectionDirections();
    getStateSize();
    getFactSize();

    infouser();

    return {
      userlinks,
      checkremote,
      directionworks,
      getstatesize,
      getfactsize,
      spravURL,
      baseURL,
      lgAndUp,

      date_now: new Date().toLocaleDateString("ru-RU"),
      caCuratorLink: ref(
        "https://www.nalog.gov.ru/rn77/about_fts/fts/structure_fts/ca_fns/9515034/"
      ),
    };
  },
};
</script>

<style></style>
