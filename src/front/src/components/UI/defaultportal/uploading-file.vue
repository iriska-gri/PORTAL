<template>
  <v-col>
    <v-file-input
      label="Файлы"
      chips
      multiple
      v-model="eventFiles"
      density="compact"
      variant="outlined"
      @click.stop=""
    >
    <template v-slot:selection="{ fileNames }">
      <template v-for="(fileName, index) in fileNames" :key="fileName">
        <v-chip
          v-if="index < 4"
          class="me-2"
          color="teal-darken-3"
          size="small"
          label
        >
          {{ fileName }}
        </v-chip>

        <span
          v-else-if="index === 4"
          class="text-overline text-grey-darken-3 mx-2"
        >
          +{{ files.length - 4 }} файла(ов)
        </span>
      </template>
    </template>
    </v-file-input>
  </v-col>
</template>

<script>
import { computed, ref } from "vue";
import { get_name } from "@/utils/universal_functions";
export default {
  props: {
    files: {
      type: Object,
      default: () => {},
    },
  },

  setup(props, { emit }) {

    const propsFiles = computed({
      get: () => props.files,
      set: (value) => emit("update:files", value),
    });

    const arrFiles = ref([]);

    const eventFiles = computed({
      get() {
        propsFiles.value.forEach((e) =>
            {
              
          arrFiles.value.push(
            dataURLtoFile(
              "data:text/plain;base64,aGVsbG8gd29ybGQ=",
              get_name(decodeURI(e.file))
            )
          )}
        );
        return arrFiles.value;
      },

      set(newValue) {
        let newFile = []
        arrFiles.value = [];
        if (newValue.length == 0) {
          arrFiles.value = [];
          propsFiles.value = [];
        } else {
          newValue.forEach((e) => {
            arrFiles.value.push(e)
            newFile.push(e)
        });
        }

        emit("postFiles", newFile);
      
       
      },
    });
    //

    function dataURLtoFile(dataurl, filename) {
      var arr = dataurl.split(","),
        mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]),
        n = bstr.length,
        u8arr = new Uint8Array(n);

      while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
      }

      return new File([u8arr], filename, { type: mime });
    }
    
  
    // const eventFiles = computed({
    //   get() {
    //     if (propsFiles.value.length > 0) {
    //       propsFiles.value.forEach((e) =>
    //         files.value.push(
    //           dataURLtoFile(
    //             "data:text/plain;base64,aGVsbG8gd29ybGQ=",
    //             get_name(decodeURI(e.file))
    //           )
    //         )
    //       );
    //       //   let file = dataURLtoFile(
    //       //     "data:text/plain;base64,aGVsbG8gd29ybGQ=",
    //       //     get_name(
    //       //   decodeURI(propsFiles.value.event.files[0].file)
    //       // )
    //       //   );

    //       //   files.value.push(file);
    //     }

    //     return files.value;
    //   },
    //   set(newValue) {
    //     // console.log(newValue,'file')
    //     newValue.forEach((e) => {
    //       if (!files.value.some((l) => l.name == e.name.split(" ").join("_"))) {
    //         files.value.push(e);
    //       }
    //     });
    //     if (newValue.length == 0) {
    //       files.value = [];
    //       propsFiles.value = [];
    //     }
    //   },
    // });
    return {
      eventFiles,
      arrFiles,
   
    };
  },
};
</script>

<style></style>
