<template>
  <v-dialog v-model="mydialog" max-width="700">
    <v-card
    :loading="isUpdating"
    class="mx-auto"
    color="blue-grey-darken-1"
    max-width="420"
  >
    <template v-slot:loader="{ isActive }">
      <v-progress-linear
        :active="isActive"
        color="green-lighten-3"
        height="4"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-img
      height="200"
      src="https://cdn.vuetifyjs.com/images/cards/dark-beach.jpg"
      cover
    >
      <v-row class="pa-3">
        <v-col cols="12">
          <v-menu
            location="bottom start"
            origin="overlap"
            transition="slide-y-transition"
          >
            <template v-slot:activator="{ props }">
              <v-btn
                v-bind="props"
                density="comfortable"
                icon="mdi-dots-vertical"
                variant="tonal"
              ></v-btn>
            </template>

            <v-list :lines="false">
              <v-list-item
                title="Update"
                @click="isUpdating = true"
              ></v-list-item>
            </v-list>
          </v-menu>
        </v-col>

        <v-row>
          <v-col class="text-center">
            <h3 class="text-h5">{{ name }}</h3>

            <span class="text-grey-lighten-1">{{ title }}</span>
          </v-col>
        </v-row>
      </v-row>
    </v-img>

    <v-form>
      <v-container>
        <v-row dense>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="name"
              :disabled="isUpdating"
              color="blue-grey-lighten-2"
              label="Name"
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field
              v-model="title"
              :disabled="isUpdating"
              color="blue-grey-lighten-2"
              label="Title"
            ></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-autocomplete
              v-model="friends"
              :disabled="isUpdating"
              :items="people"
              color="blue-grey-lighten-2"
              item-title="name"
              item-value="name"
              label="Select"
              chips
              closable-chips
              multiple
            >
              <template v-slot:chip="{ props, item }">
                <v-chip
                  v-bind="props"
                  :prepend-avatar="item.raw.avatar"
                  :text="item.raw.name"
                ></v-chip>
              </template>

              <template v-slot:item="{ props, item }">
                <v-list-item
                  v-bind="props"
                  :prepend-avatar="item.raw.avatar"
                  :subtitle="item.raw.group"
                  :title="item.raw.name"
                ></v-list-item>
              </template>
            </v-autocomplete>
          </v-col>
        </v-row>
      </v-container>
    </v-form>

    <v-divider></v-divider>

    <v-card-actions>
      <v-switch
        v-model="autoUpdate"
        :disabled="isUpdating"
        class="mt-0 ms-2"
        color="green-lighten-2"
        density="compact"
        label="Auto Update"
        hide-details
      ></v-switch>

      <v-spacer></v-spacer>

      <v-btn
        :disabled="autoUpdate"
        :loading="isUpdating"
        :variant="isUpdating ? 'tonal' : undefined"
        color="blue-grey-lighten-3"
        prepend-icon="mdi-update"
        @click="isUpdating = true"
      >
        Update Now
      </v-btn>
    </v-card-actions>
  </v-card>
  </v-dialog>
</template>

<script>
import { ref, computed } from "vue";

export default {
  props: {
    opendialog: {
      type: Boolean,
      default: false,
    },
  },
  setup(props, { emit }) {


    const mydialog = computed({
      get: () => props.opendialog,
      set: (value) => emit("update:opendialog", value),
    });



     
      const    people= [
          // TODO: https://github.com/vuetifyjs/vuetify/issues/15721
          // { header: 'Group 1' },
          { name: 'Sandra Adams', group: 'Group 1', avatar: srcs[1] },
          { name: 'Ali Connors', group: 'Group 1', avatar: srcs[2] },
          { name: 'Trevor Hansen', group: 'Group 1', avatar: srcs[3] },
          { name: 'Tucker Smith', group: 'Group 1', avatar: srcs[2] },
          // { divider: true },
          // { header: 'Group 2' },
          { name: 'Britta Holt', group: 'Group 2', avatar: srcs[4] },
          { name: 'Jane Smith ', group: 'Group 2', avatar: srcs[5] },
          { name: 'John Smith', group: 'Group 2', avatar: srcs[1] },
          { name: 'Sandra Williams', group: 'Group 2', avatar: srcs[3] },
        ]

    return {
      mydialog,
    };
  },
};
</script>

<style></style>
