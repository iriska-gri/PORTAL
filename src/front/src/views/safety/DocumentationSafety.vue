<template>
  <v-row no-gutters class="h-100 gap">
    <v-col class="d-flex">
      <v-row no-gutters class="flex-column gap">
        <v-col lg="6" class="w100 d-flex flex-column">
          <v-card class="h-100 w-100 d-flex flex-column rounded-0">
            <v-card-title>
              <span class="text-h6 text-wrap"> Ответственность </span>
            </v-card-title>

            <v-row no-gutters class="h-0 overflow-auto flex-column flex-nowrap">
              <v-col
                class="flex-grow-0"
                v-for="(comm, key) in docSections.type_resp"
                :key="key"
              >
                <v-card-subtitle class="text-wrap">
                  <span class="text-subtitle-1 text-wrap">
                    {{ comm.resp.name }}
                  </span>
                </v-card-subtitle>

                <v-list :lines="false" density="compact" nav>
                  <v-row
                    no-gutters
                    v-for="file in comm.resp.get_resp_files"
                    :key="file.id"
                  >
                    <v-col>
                      <v-list-item
                        :active="filId == file.id"
                        color="primary"
                        density="compact"
                        @click="openPDF(file)">
                        <span class="text-body-2 text-wrap">
                          {{ get_name(decodeURI(file.file_name.replace(/\.[^/.]+$/, ""))) }}
                        </span>
                      </v-list-item>
                    </v-col>
                    <v-col class="flex-grow-0 align-self-center">
                      <v-icon
                        icon="mdi-file-download-outline"
                        @click="downloadItem(file)"
                    /></v-col>
                  </v-row>
                </v-list>
              </v-col>
            </v-row>
          </v-card>
        </v-col>

        <v-col class="w100 d-flex flex-column">
          <v-card class="h-100 w-100 d-flex flex-column pb-1 rounded-0">
            <v-card-title>
              <span class="text-h6 text-wrap"> Комиссии </span>
            </v-card-title>

            <v-row no-gutters class="h-0 overflow-auto flex-column flex-nowrap">
              <v-col
                class="flex-grow-0"
                v-for="(comm, key) in docSections.type_comm"
                :key="key">
                <v-card-subtitle class="text-wrap">
                  <span class="text-subtitle-1 text-wrap">
                    {{ comm.comm.name }}
                  </span>
                </v-card-subtitle>

                <v-list :lines="false" density="compact" nav>
                  <v-row
                    no-gutters
                    v-for="file in comm.comm.comitee_files"
                    :key="file.id">
                    <v-col>
                      <v-list-item
                        :active="filId == file.id"
                        color="primary"
                        density="compact"
                        @click="openPDF(file)"
                      >
                        <span class="text-body-2 text-wrap">
                          {{ get_name(decodeURI(file.file_name.replace(/\.[^/.]+$/, ""))) }}
                        </span>
                      </v-list-item></v-col
                    >
                    <v-col class="flex-grow-0 align-self-center">
                      <v-icon
                        icon="mdi-file-download-outline"
                        @click="downloadItem(file)"
                    /></v-col>
                  </v-row>
                </v-list>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-col>

    <v-col class="d-flex flex-column">
      <v-card class="flex-column h-100 d-flex rounded-0">
        <v-row no-gutters class="h-0 overflow-auto">
          <v-col class="d-flex flex-column "
          :class="!loading?'align-center align-self-center':''">
            <v-container v-if="loading">
              <v-progress-linear :rounded="5" indeterminate color="teal" />
            </v-container>
            <VuePdfEmbed              
              v-show="showFile"
              :source="pdfSource"
              width="720"
              @rendered="loading = false"
              @loading-failed="handlePdfError"/>
           <v-card-text v-show="!showFile" > 
            <span class="text-h5 text-grey">
              {{ err }}
            </span>
           </v-card-text>
          
          </v-col>
        </v-row>

        <v-divider />
        <v-card-actions v-show="showFile">
          <v-btn position="sticky" block @click="closeFile">Закрыть</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { ref, computed } from "vue";
import { axiosApiInstance, baseURL, spravURLBase } from "@/utils/axios-api";
import { saveAs } from "file-saver";
import VuePdfEmbed from "vue-pdf-embed";
import { get_name } from "@/utils/universal_functions";
export default {
  props: {
    docSections: {
      type: Object,
      default: () => {
        type_comm;
      },
    },
  },

  components: {
    VuePdfEmbed,
  },

  setup(props, { emit }) {
    const loading = ref(true);
    const burl = baseURL.slice(0, -1);
    const pdfSource = ref("");

    const showFile = ref(true);
    const filId = ref(null);
    const err = ref("Файл не выбран");

    const downloadItem = (file) => {
    
      let url = development.value ? burl + file.file_name : spravURLBase + `files/${file.typeoffile == 'comm' ? 'committee1_docs' : 'order_responsibility_docs'}/${file.parent}/${get_name(file.file_name)}`
  
      axiosApiInstance.get(url, { responseType: "blob" }).then((response) => {
        saveAs(response.data, get_name(decodeURI(file.file_name)));
      });
    };

    const openPDF = (file) => {     
      let source =development.value ? burl + file.file_name : spravURLBase + `files/${file.typeoffile == 'comm' ? 'committee1_docs' : 'order_responsibility_docs'}/${file.parent}/${get_name(file.file_name)}`
      if(source!=pdfSource.value){
        loading.value = true
        pdfSource.value = source
      }
      showFile.value = true;
      filId.value = file.id;
    };

    const development = computed({
      get() {
        return process.env.NODE_ENV == "development" ? true : false;
      }
    })



    const closeFile = () => {
      err.value = "Файл не выбран"
      showFile.value = false;
      filId.value = null;
    };

    const handlePdfError = (error) => {
      showFile.value=false
      err.value = "Файл не найден";
      loading.value = false;
    };

    const firstFile = () => {
 
      let files = []
      props.docSections.type_comm.forEach(el => {
        files.push(...el.comm.comitee_files)        
      });

      props.docSections.type_resp.forEach(el => {      
        files.push(...el.resp.get_resp_files)
      });
      pdfSource.value = 
        development.value ? burl + files[0].file_name : spravURLBase + `files/${files[0].typeoffile == 'comm' ? 'committee1_docs' : 'order_responsibility_docs'}/${files[0].parent}/${get_name(files[0].file_name)}`
      filId.value = files[0].id;
    };

    firstFile();

    return {
      downloadItem,
      openPDF,
      get_name,
      handlePdfError,
      loading,
      pdfSource,
      filId,
      burl,
      showFile,
      closeFile,
      err,
    };
  },
};

// http://10.252.44.33/accounting6/index.php?controller=OrderResponsibility&action=DownloadFile&fld_file=222&fld_order_responsibility=11
// http://10.252.44.33/accounting6/index.php?controller=Committee&action=DownloadFile&fld_file=412&fld_committee=29
// \\10.252.44.33\Webserver\data\htdocs\accounting6\files\committee1_docs\2
// \\10.252.44.33\Webserver\data\htdocs\accounting6\files\order_responsibility_docs\12
</script>

<style></style>
