<template>
  <div class="h-100">
    <v-list-item
      v-if="from_which == 'dialog-search'"
      class="pl-4 h-100 text-left pa-2"
      @click="open = true"
    >
      <template v-slot:prepend>
        <v-avatar
          color="grey-darken-3"
          :image="checkremote(`${spravURL}${author.login}.jpg`)"
        />
      </template>
      <v-list-item-title :class="style_item_title()">
        {{ author.fio }}
      </v-list-item-title>
      <v-list-item-subtitle :class="style_item_subtitle()">
        {{ author.post }}
      </v-list-item-subtitle>
    </v-list-item>

    <v-list-item
      v-if="from_which == 'top-user'"
      class="h-100 text-left pa-0 pl-0"
      @click="open = true"
    >
      <v-chip
        class="cursor-pointer pa-0"
        variant="text"
        label
        color="grey-darken-3"
        size="small"
      >
        <v-avatar
          color="grey-darken-3"
          :image="checkremote(`${spravURL}${author.login}.jpg`)"
          class="mr-2"
        />
        <span class="font-weight-medium text-grey-darken-3 myleft text-caption">
          {{ splitname(author) }}
        </span>
      </v-chip>
    </v-list-item>

    <v-img
      v-if="from_which == 'top_comment'"
      @click="open = true"
      cover
      class="cursor-pointer"
      :src="checkremote(`${spravURL}${author.login}.jpg`)"
    />

    <info-user-card
      :author="author"
      :opendialog="open"
      @update:opendialog="open = $event"
    />
  </div>
</template>

<script>
import { ref } from "vue";
import { checkremote } from "@/utils/universal_functions";
import { spravURL } from "@/utils/axios-api";
import { splitname } from "@/utils/universal_functions";

export default {
  name: "list-user",
  props: {
    author: {
      type: Object,
      default: {},
    },

    from_which: {
      type: String,
      default: "dialog-search",
    },
  },
  setup(props) {
    const open = ref(false);

    const style_item_title = () => {
      if (props.from_which == "top-user") {
        return "text-body-1 font-weight-medium";
      } else return "text-body-1 font-weight-medium pt-2";
    };

    const style_item_subtitle = () => {
      if (props.from_which == "top-user") {
        return "text-caption";
      } else return "pb-2";
    };

    return {
      open,
      checkremote,
      spravURL,
      style_item_title,
      style_item_subtitle,
      splitname,
    };
  },
};
</script>

<style></style>
