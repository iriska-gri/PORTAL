<template>
  <v-snackbar
    :timeout="3000"
    v-model="feedalert.alert"
    :color="feedalert.color"
    :icon="feedalert.ico"

  >
    <v-icon :icon="feedalert.ico" />
<span class="pl-2 text-body-2">
    {{ feedalert.text }}
</span>

  </v-snackbar>

</template>

<script>
import { watch } from "vue";
import { useAlertStore } from "@/store/useAlertStore";

export default {
  name: "AlertDefault",
  setup() {
    const feedalert = useAlertStore().alert;

    watch(
      () => feedalert,
      () => {
        setTimeout(function () {
          feedalert.text = "";
          feedalert.ico = "";
          feedalert.color = "";
          feedalert.alert = false;
        }, 8000);
      },
      { deep: true }
    );

    return {
      feedalert,
    };
  },
};
</script>

<style></style>
