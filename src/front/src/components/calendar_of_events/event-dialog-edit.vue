<template>
  <v-card>
    <v-card-title>
      <!-- <v-textarea
        v-model="dataToEdit.bigname"
        rows="1"
        placeholder="Название календаря"
      /> --> 
    
      <v-text-field v-model="dataToEdit.name" placeholder="Заголовок" />
    </v-card-title>
    <v-card-subtitle>
      <v-menu
        v-model="menudate"
        :close-on-content-click="false"
        :nudge-right="40"
        transition="scale-transition"
        offset-y
      >
        <template v-slot:activator="{ props }">
          <v-textarea
            v-model="dataToEdit.start"
            :value="formatComa(dataToEdit.start)"
            no-resize
            class="my-textarea"
            rows="1"
            hide-details
            style="width: 119px"
            variant="plain"
            density="compact"
            v-bind="props"
          >
         
            <template v-slot:prepend-inner>
              <v-icon
                v-bind="props"
                icon="mdi-calendar-today"
                color="cyan-darken-3"
                size="x-small"
              />
            </template>
          </v-textarea>
        </template>
        <v-locale-provider locale="ru">
          <v-date-picker
            v-model="dataToEdit.start"
            show-adjacent-months
            hide-header
            border
            no-time
            @update:modelValue="updateDateTime"
          />
        </v-locale-provider>
      </v-menu>
    </v-card-subtitle>
    <v-card-text class="pt-2">
      <!-- <v-textarea v-model="dataToEdit.description" placeholder="Описание события" /> -->
      <!-- <ckeditor
        :editor="editor"
        v-model="dataToEdit.description"
        :config="{
          placeholder: 'Описание события',
          language: 'ru',
        }"
      /> -->
      <!-- <ckeditor
        :editor="editor"
        v-model="dataToEdit.content"
        :config="{
          placeholder: 'Полное описание события',
          language: 'ru',
        }"
      /> -->
      {{dataToEdit}}
      <v-textarea
        v-model="dataToEdit.place"
        placeholder="Местопроведение события"
      />
      <!-- <v-btn @click="openDialog">
      добавить
      </v-btn> -->
      <!-- <event-dialog-edit-participant 
  :opendialog="showDialog"
  @update:opendialog="showDialog = $event"
/> -->
      <v-file-input
        label="File input w/ chips"
        chips
        multiple
        v-model="eventFiles"
      ></v-file-input>

      <strong>Время:</strong>

      <ul class="pl-5">
        <v-row>
          <v-col>
            <v-text-field
              label="Начало события"
              v-model="startTime"
              suffix="PST"
              type="time"
              @update:modelValue="updateDateTime"
            ></v-text-field>
          </v-col>
        </v-row>
      </ul>
    </v-card-text>
    <v-card-actions>
      <v-icon
        icon="mdi-check"
        color="green"
        class="pb-1"
        @click="confirmation"
      />
    </v-card-actions>
  </v-card>
</template>

<script>
import { formatComa } from "@/utils/universal_functions";
import { ref } from "vue";
import { axiosApiInstance } from "@/utils/axios-api";
import CKEditor from "@ckeditor/ckeditor5-vue";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import "@ckeditor/ckeditor5-build-classic/build/translations/ru";
import EventDialogEditParticipant from "./event-dialog-edit-participant.vue";
import eventDialogEdit from "@/components/calendar_of_events/event-dialog-edit.vue";

export default {
  props: {
    event: {
      type: Object,
      default: () => {},
    },
  },
  components: {
    // Use the <ckeditor> component in this view.
    ckeditor: CKEditor.component,
    EventDialogEditParticipant,
  },

  setup(props, { emit }) {
    const eventFiles = ref([]);
    const menudate = ref(false);
    const dataToEdit = ref({ ...props.event, description: "" });
    const showDialog = ref(false);

    const startTime = ref(
      `${dataToEdit.value.start.getHours()}:${String(
        dataToEdit.value.start.getMinutes()
      ).padStart(2, "0")}`
    );

    const updateDateTime = () => {
      if (startTime.value) {
        const timeParts = startTime.value.split(":");

        dataToEdit.value.start.setHours(parseInt(timeParts[0], 10));
        dataToEdit.value.start.setMinutes(parseInt(timeParts[1], 10));
      }
    };

    const confirmation = () => {

      const postFile = new FormData()

      postFile.append("file", eventFiles.value[0]);
      postFile.append("calendar", JSON.stringify(dataToEdit.value))
      postFile.append("participants", JSON.stringify(dataToEdit.value.bigname))

      
      axiosApiInstance
        .post(`api/calendar_of_events/calendarEvents/`, 
          // participants: dataToEdit.value.bigname,
          // calendar: dataToEdit.value,
          postFile
          
        
        
    //     {
    //   headers: {
    //     "Content-Type": "multipart/form-data"
    //   },
    // }
        )
        .then((data) => {
          emit("returnUpdateData");
        });
    };

    const openDialog = () => {
      showDialog.value = true;
    };

    return {
      editor: ClassicEditor,
      menudate,
      formatComa,
      startTime,
      updateDateTime,
      dataToEdit,
      confirmation,
      openDialog,
      showDialog,
      eventFiles,
    };
  },
};
</script>

<style></style>
