<template>
  <v-row no-gutters class="h-100 gap" v-if="vacancy.length > 0">
    <v-col lg="4" class="flex-column d-flex">
      <v-card class="h-100 pa-1 d-flex flex-column rounded-0">
        <v-card-title
          class="d-flex justify-center bg-teal-lighten-5 text-teal-darken-4"
        >
          Вакансии
        </v-card-title>
        <v-row no-gutters class="h-0 gap overflow-auto">
          <v-col>
            <v-card class="mx-auto h-100">
              <v-list density="compact" class="px-0">
                <v-list-item
                  v-for="vac in vacancy"
                  :key="vac.id"
                  :value="vac"
                  class="border-b-sm"
                  active-class="custom-active"
                  color="teal-darken-3"
                  @click="getIndVacation(vac.id)"
                >
                  <v-card class="rounded-0 bg-transparent">
                    <v-card-title class="text-wrap">
                      {{ vac.name }}
                    </v-card-title>
                    <v-card-text class="pb-2">
                      <v-row no-gutters class="gap">
                        <v-col>{{ vac.department.name }}</v-col>
                        <v-col
                          class="flex-grow-0 text-subtitle-1 text-btn_text"
                        >
                          Подробнее
                        </v-col>
                        <v-col class="flex-grow-0 align-self-center pl-2">
                          <v-icon
                            icon="mdi-arrow-right"
                            color="btn_text"
                            size="small"
                          />
                        </v-col>
                      </v-row>
                    </v-card-text>
                  </v-card>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
    <v-col class="flex-column d-flex">
      <v-card class="h-100 pa-1 d-flex flex-column rounded-0">
        <v-card-title
          class="d-flex justify-center bg-teal-lighten-5 text-teal-darken-4"
        >
          Описание
        </v-card-title>
        <v-row
          no-gutters
          class="h-0 gap overflow-auto"
          id="goto-container-example"
        >
          <v-col>
            <v-card
              class="rounded-0 h-100"
              v-if="vacancyDescription.name != ''"
            >
              <v-card-title class="mt-4">
                <span class="text-h4 text-wrap">
                  {{ vacancyDescription.name }}
                </span>
              </v-card-title>

              <v-card-title class="pt-0">
                <span class="text-h5">
                  {{ vacancyDescription.department.name }}
                </span>
              </v-card-title>
              <v-card-title>
                <v-btn
                  type="submit"
                  class="text-subtitle-1 font-weight-light"
                  color="btn_text"
                  elevation="1"
                  @click="
                    goTo('#response', { container: '#goto-container-example' })
                  "
                >
                  Откликнуться
                </v-btn>
              </v-card-title>
              <v-card-title class="pt-6">
                <span class="text-h6">
                  Направление деятельности подразделения
                </span>
              </v-card-title>
              <v-card-text class="mx-5 my-1">
                <ul>
                  <li
                    class="py-1"
                    v-for="directionTitle in vacancyDescription.department
                      .department_directions"
                    :key="directionTitle"
                  >
                    {{ directionTitle.direction_title }}
                  </li>
                </ul>
              </v-card-text>
              <v-card-title>
                <span class="text-h6">
                  Функционал и должностные обязанности
                </span>
              </v-card-title>
              <v-card-text class="mx-5 my-0 ckeditor_ul">
                <div class="py-1" v-html="vacancyDescription.functional"></div>
              </v-card-text>
              <v-card-title>
                <span class="text-h6"> Базовые требования к соискателю </span>
              </v-card-title>
              <v-card-text class="mx-5 my-0 ckeditor_ul">
                <!-- {{vacancyDescription}} -->
                <div class="py-1" v-html="vacancyDescription.requirements"></div>
              </v-card-text>
              <v-divider />
              <response-vacancies id="response" :idVacations=vacancySelect />
            </v-card>

            <v-card
              class="h-100 pa-1 d-flex align-center justify-center text-center"
              v-else
            >
              <v-card-subtitle>
                <v-icon
                  icon="mdi-format-list-bulleted"
                  color="grey"
                  size="x-large"
                />
                <br />
                <span class="text-h5 text-grey"
                  >Для подробного описания вакансии <br />
                  выберите её из списка слева</span
                >
              </v-card-subtitle>
            </v-card>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
  </v-row>
  <v-row no-gutters class="h-100 gap" v-else>
    <v-col class="flex-column d-flex">
      <v-card class="h-100 pa-1 d-flex align-center justify-center text-center">
        <v-card-subtitle>
          <v-icon icon="mdi-credit-card-off" size="x-large" color="grey" />
          <br />
          <span class="text-h5 text-grey"
            >Сейчас вакансий нет, <br />
            загляните позжет</span
          >
        </v-card-subtitle>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { ref } from "vue";
import { useGoTo } from "vuetify";
import { clearAxios } from "@/utils/axios-api";
import { baseURL } from "@/utils/axios-api";
import ResponseVacancies from "@/components/about_inspection/open_vacancies/ResponseVacancies.vue";

export default {
  components: { ResponseVacancies },
  setup() {
    const goTo = useGoTo();
    let vacancyDescription = ref({ name: "", department: { name: "" } });
    let vacancySelect = ref(-1);

    let vacancy = ref({});

    const getVacancies = () => {
      clearAxios.get(`api/about_inspection/getvacancy/`).then((data) => {
        vacancy.value = data.data;
        vacancyDescription.value = vacancy.value[0];
        vacancySelect.value = vacancy.value[0].id
      });
    };

    const formatText = (text) => {
      return text.replaceAll(
        'src="/media/uploads',
        `src="${baseURL}media/uploads`
      );
    };

    const getIndVacation = (ind) => {
      if (vacancySelect.value != ind) {
        vacancySelect.value = ind;
        vacancyDescription.value = vacancy.value.find((el) => el.id == ind);
      } else {
        vacancySelect.value = -1;
        vacancyDescription.value = { name: "", department: { name: "" } };
      }
    };

    getVacancies();

    return {
      vacancy,
      formatText,
      vacancyDescription,
      getIndVacation,
      vacancySelect,
      goTo,
    };
  },
};
</script>

<style>
.ckeditor_ul ul li {
  padding-top: 8px;
}

.custom-active .v-card-title {
  color: #001e19;
}

.custom-active .v-card-text {
  color: black;
}
</style>
