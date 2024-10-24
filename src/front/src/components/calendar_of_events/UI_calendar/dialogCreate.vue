<template>
  <v-card min-height="436" class="pa-3">
    <v-card-title class="pr-0 pl-2 d-flex justify-space-between">
      {{ title }}
      <v-icon
        icon="mdi-close cursor-pointer"
        size="small"
        color="grey"
        @click="$emit('closeDialog')"
      />
    </v-card-title>
    <v-form ref="form_valid" @submit.prevent="transformation">
      <v-card-text class="d-flex px-3">
        <slot name="card_text"></slot>
      </v-card-text>
      <v-card-actions class="justify-end">
        <v-btn
          v-if="!newOrOld"
          icon="mdi-delete"
          variant="tonal"
          rounded
          size="36px"
          @click="$emit('delObject')"
        />
        <!-- <v-btn
          class="text-subtitle-1"
          elevation="0"
          width="150"
          @click="clearValidation"
          color="btn_gray"
          variant="flat"
          >резет</v-btn
        > -->
        <!-- <v-btn @click="clearFormValidation"></v-btn> -->
        <v-btn
          class="text-subtitle-1"
          elevation="0"
          width="150"
          @click="$emit('closeDialog')"
          color="btn_gray"
          variant="flat"
          >Отменить</v-btn
        >

        <v-btn
          class="text-subtitle-1 font-weight-regular"
          color="btn_text"
          variant="flat"
          elevation="0"
          width="150"
          type="transformation"
        >
          {{ newOrOld ? "Создать" : "Редактировать" }}
        </v-btn>
      </v-card-actions>
    </v-form>
  </v-card>
</template>

<script>
import { ref } from "vue";

export default {
  props: {
    title: {
      type: String,
      default: "",
    },

    newOrOld: {
      type: Boolean,
      default: false,
    },
  },

  setup(props, { emit }) {
    const form_valid = ref(null);

    const transformation = () => {
      emit("postData", form_valid.value.isValid);
    };

    const clearFormValidation = () => {

      if (!!form_valid.value) {
        form_valid.value.resetValidation();
      }
    };

    return {
      form_valid,
      transformation,

      clearFormValidation,
    };
  },
};
</script>

<style></style>
