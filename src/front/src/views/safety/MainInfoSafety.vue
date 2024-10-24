<template>
  <v-row no-gutters class="h-100">
    <v-col cols="8" class="flex-column">
      <v-row no-gutters class="h-100 justify-center">
        <v-col
          lg="6"
          class="meheight"
          v-for="schema in formainpage"
          :key="schema.id"
        >
          <VuePdfEmbed
            v-if="schema.url.endsWith('.pdf')"
            :source="burl + schema.url"
            width="500"
            @click="openFirstPlan_opener(schema)"
          />
          <v-img
            v-else
            class="cursor-pointer"
            :src="burl + schema.url"
            @click="openFirstPlan_opener(schema)"
          >
          </v-img>
        </v-col>
      </v-row>
    </v-col>
    <v-col class="d-flex flex-column h-100">
      <v-row no-gutters class="h-0 overflow-auto">
        <v-col>
       
            <div class="text-h6 d-flex justify-center">Ответственность</div>
         
          <v-col class="v-col-auto">
            <div
              v-if="responsibility != undefined && responsibility.length > 0"
            >
              <v-expansion-panels variant="accordion">
                <v-expansion-panel v-for="item in responsibility">
                  <v-expansion-panel-title>
                    {{ item.resp.sphere_of_responsibility }}
                  </v-expansion-panel-title>
                  <v-expansion-panel-text>
                    <list-user
                      v-for="user in item.resp.employee"
                      :key="user"
                      :author="user"
                    >
                    </list-user>
                  </v-expansion-panel-text>
                </v-expansion-panel>
              </v-expansion-panels>
            </div>
            <div v-else>
              <div class="text-caption text-grey d-flex justify-center">
                Данные по ответственным отсутствуют
              </div>
            </div>
          </v-col>
          
            <div class="text-h6 d-flex justify-center">Комиссии</div>
         
          <v-col class="v-col-auto">
            <div v-if="commitee != undefined && commitee.length > 0">
              <v-expansion-panels variant="accordion">
                <v-expansion-panel v-for="item in commitee" :key="item">
                  <v-expansion-panel-title>
                    {{ item.comm.name }}
                  </v-expansion-panel-title>
                  <v-expansion-panel-text class="d-block">
                    <div v-if="item.comm.com_members.length > 0">
                      <list-user
                        class="text-subtitle-1"
                        v-for="user in item.comm.com_members"
                        :key="user"
                        :author="user"
                      >
                      </list-user>
                    </div>
                    <v-card-subtitle class="text-center" v-else
                      >Участников нет
                    </v-card-subtitle>
                  </v-expansion-panel-text>
                </v-expansion-panel>
              </v-expansion-panels>
            </div>
            <div v-else>
              <div class="text-caption text-grey d-flex justify-center">
                Данные по комиссиям отсутствуют
              </div>
            </div>
          </v-col>
        </v-col>
      </v-row>
    </v-col>
  </v-row>

  <v-dialog v-model="openFirstPlan" :width="900" height="100%">
    <v-row class="ma-0 overflow-auto h-0">
      <v-card class="h-100 w-100 pa-0">
        <v-card-actions class="d-flex justify-space-between">
          <v-btn
            density="compact"
            variant="text"
            icon="mdi-close"
            @click="openFirstPlan = false"
          >
          </v-btn>
          <v-btn
            class="d-flex align-center"
            icon="mdi-file-download-outline"
            color="green"
            @click="downloadFile(urlschema)"
          >
          </v-btn>
        </v-card-actions>

        <VuePdfEmbed
          v-if="urlschema.endsWith('.pdf')"
          :source="urlschema"
          width="500"
          @click="openFirstPlan = false"
        />
        <v-img
          v-else
          :src="urlschema"
          class="cursor-pointer"
          height="100%"
          width="100%"
          @click="openFirstPlan = false"
        >
        </v-img>
      </v-card>
    </v-row>
  </v-dialog>
</template>

<script setup>
import { baseURL, axiosApiInstance } from "@/utils/axios-api";
import { ref } from "vue";

import VuePdfEmbed from "vue-pdf-embed";
import { saveAs } from "file-saver";

defineProps({
  formainpage: Object,
  responsibility: Array,
  commitee: Array,
  require: true,
});

const downloadFile = (url, fileName) => {
  axiosApiInstance.get(url, { responseType: "blob" }).then((response) => {
    saveAs(response.data, fileName);
  });
};

const urlschema = ref(null);
const burl = baseURL.slice(0, -1);
const openFirstPlan = ref(false);

function openFirstPlan_opener(schema) {
  urlschema.value = burl + schema.url;
  openFirstPlan.value = true;
}
</script>

<style>
.meheight {
  max-height: 44vh;
}
</style>
