<template>
  <v-row no-gutters class="h-100 gap">
    <v-col class="flex-grow-0 d-flex d-sm-none d-lg-none d-xl-flex">
      <v-row no-gutters class="flex-column">
        <v-col lg="4">
          <span class="vertext text-button my-1 pb-8">Руководство</span>
        </v-col>
        <v-col>
          <span class="vertext text-button my-1 pb-13"
            >Структурные подразделения</span
          >
        </v-col>
      </v-row>
    </v-col>

    <v-col class="d-flex">
      <v-row no-gutters :class="smAndDown ? ' flex-column' : ''">
        <v-col
          :md="mdAndDown ? '12' : ''"
          :lg="lgAndDown ? 6 : ''"
          class="w100 flex-column d-flex"
          v-for="structure in structures"
          :key="structure.id"
        >
          <v-row no-gutters class="flex-grow-0">
            <v-col class="flex-column d-flex">
              <v-row no-gutters class="mb-2 mt-1 justify-center d-flex mx-1">
                <v-card class="flex-column d-flex flex-grow-1" :elevation="10">
                  <v-card-text class="pa-0">
                    <v-col lg="12" class="pa-0">
                      <v-row no-gutters>
                        <v-col
                          class="d-flex py-3 justify-center align-center font-weight-medium text-uppercase"
                        >
                          {{ structure.post }}
                       
                        </v-col>
                      </v-row>
                    </v-col>
                    <v-row no-gutters>
                      <v-col lg="4" class="pa-1 heightfoto">
                    
                        <list-user :author="structure" :from_which="'top_comment'" />
                        <!-- <v-img
                          class="h-100"
                          :src="
                            checkremote(`${spravURL}${structure.login}.jpg`)
                          "
                          cover
                        /> -->
                      </v-col>
                      <v-col
                        class="text-center align-self-center font-weight-medium"
                      >
                        {{ structure.fio }}
                      </v-col>
                    </v-row>
                  </v-card-text>
                </v-card>
              </v-row>
            </v-col>
            <!-- :class="mdAndDown ? 'flex-column gap' : ''" -->
          </v-row>

          <v-row no-gutters :class="lgAndDown ? '' : 'gap  h-0  overflow-auto'">
            <v-col lg="12">
              <v-row
                no-gutters
                class="gap mb-1"
                v-for="boss in structure.deps"
                :key="boss.id"
              >
                <v-col class="d-flex flex-column">
                  <v-card
                    class="flex-column d-flex flex-grow-1 mx-1"
                    :elevation="5"
                  >
                    <v-card-text class="pa-1 pt-3 px-3 flex-column">
                      <v-col lg="12" class="minh pa-0">
                        <v-row no-gutters>
                          <v-col
                            class="text-wrap text-center text-body-2 font-weight-medium text-uppercase"
                          >
                            {{ boss.name }}
                          </v-col>
                          <v-col class="flex-grow-0">
                            <v-tooltip location="top">
                              <template v-slot:activator="{ props }">
                                <span v-bind="props">
                                  <v-icon
                                    size="large"
                                    color="green"
                                    icon="mdi-arrow-top-right"
                                  />
                                </span>
                              </template>
                              <v-row>
                                <v-col> Перейти на страницу отдела </v-col>
                              </v-row>
                            </v-tooltip>
                          </v-col>
                        </v-row>
                      </v-col>
                      <v-row no-gutters>
                        <list-user :author="boss.chief_deps" />
                      </v-row>
                    </v-card-text>
                  </v-card>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
import { ref } from "vue";
import { spravURL } from "@/utils/axios-api";
import { checkremote } from "@/utils/universal_functions";
import { axiosApiInstance } from "@/utils/axios-api";
import StructureInspectionRow from "./StructureInspectionRow.vue";
import { useDisplay } from "vuetify";

export default {
  components: { StructureInspectionRow },
  setup() {
    const structures = ref([]);
    const { smAndDown, mdAndDown, lgAndDown } = useDisplay();

    const getStructure = () => {
      axiosApiInstance.get("api/about_inspection/getstructure/").then((res) => {
        structures.value = res.data;
      });
    };

    getStructure();
    return {
      structures,
      checkremote,
      spravURL,
      mdAndDown,
      lgAndDown,
      smAndDown,
    };
  },
};
</script>

<style>
.vertext {
  writing-mode: vertical-rl;
  transform: rotate(180deg);
}

.deps-title {
  height: 90px;
}

.rotate-text {
  transform: rotate(-90deg);
}

.minh {
  min-height: 43px;
}

.heightfoto {
  max-height: 140px;
  min-height: 140px;
}

/* .width-subdeps {
  width: 350px;
} */
</style>
