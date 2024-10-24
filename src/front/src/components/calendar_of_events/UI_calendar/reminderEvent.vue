<template>
  <v-col class="flex-column d-flex">
    <v-row no-gutters class="map">
      <v-col lg="4">
        <v-autocomplete
          v-model="values"
          variant="outlined"
          :items="items"
          density="compact"
          disabled
          hide-details
        ></v-autocomplete>
      </v-col>
      <v-col class="flex-grow-0 px-2 pt-2">за</v-col>
      <v-col class="flex-grow-0 pr-2"
        ><v-text-field disabled min-width="55" density="compact" variant="outlined" hide-details
          >10</v-text-field
        ></v-col
      >
      <v-col lg=3>
        <v-autocomplete
          v-model="valuesTime"
          variant="outlined"
          :items="itemsTime"
          density="compact"
          disabled
          hide-details
        ></v-autocomplete>
      </v-col>
      <v-col class="flex-grow-0 pt-3 pl-3">
        <v-icon icon="mdi-close cursor-pointer"
        size="small"
        color="grey" disabled></v-icon>
      </v-col>
    </v-row>
  </v-col>
</template>

<script>
export default {
  setup() {
    const values = ["браузером"];
    const items = ["браузером", "bar", "fizz", "buzz"];

    const valuesTime = ["минут"];
    const itemsTime = ["часов", "минут", "fizz", "buzz"];
    return {
      values,
      items,
      valuesTime,
      itemsTime
    };
  },
};
</script>

<style></style>
