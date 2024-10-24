<template>
  <v-card>
    <v-card-title>
      <v-icon color="indigo-darken-3" class="pb-1">{{ event.icon }}</v-icon>

      <span class="pl-3"> {{ event.name }}</span>
    </v-card-title>
    <v-card-subtitle>
      <strong>{{ event.start && event.start.format("DD.MM.YYYY") }}</strong>
    </v-card-subtitle>
    <v-card-text class="pt-2">
      <p class="pb-3" v-html="formatText(event.content)" />
      <strong>Время:</strong>

      <ul class="pl-5">
        <li>
          Начало:
          {{ event.start && event.start.formatTime() }}
        </li>
        <li>
          Окончание:
          {{ event.end && event.end.formatTime() }}
        </li>
      </ul>
    </v-card-text>
  </v-card>
</template>

<script>
import { baseURL } from "@/utils/axios-api";
export default {
  props: {
    event: {
      type: Object,
      default: () => {},
    },
  },

  setup() {
    const formatText = (text) => {
      if (text !== null) {
        return text.replaceAll(
          'src="/media/uploads',
          `src="${baseURL}media/uploads`
        );
      } else {
        return "";
      }
    };
    return {
      formatText,
    };
  },
};
</script>

<style></style>
