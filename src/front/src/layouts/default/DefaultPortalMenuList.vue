<template>
  <div>
    <v-list nav density="compact" class="text-blue-grey-lighten-1">
      <div v-for="(list, key) in aMenuItem" :key="key">
        <div v-if="showProm(key)">
          <v-list-item
            v-for="x in list"
            :key="x"
            :title="x.name"
            :value="x.name"
            :href="x.link"
            :target="x.link ? '_blank' : ''"
            slim
          >
            <template v-slot:prepend>
              <v-icon :icon="x.ico" size="x_small" />
              <v-tooltip v-if="rail" activator="parent" location="top">
              </v-tooltip>
            </template>
          </v-list-item>
        </div>
      </div>
    </v-list>
  </div>
</template>

<script>
import { baseURL } from "@/utils/axios-api";
import { getDevelopment } from "@/utils/universal_functions";

export default {
  props: {
      rail: {
          type: Boolean,
          default: false
      },
  },

  setup() {
    const gittlink = () => {
      const link =
        baseURL == "http://127.0.0.1:8000/"
          ? "http://sulaco.nodered.ru:5223/COD2/PORTAL_COD2/projects"
          : "http://maestro.cod2.regions.tax.nalog.ru:3333/COD2/PORTAL_COD2/projects/22";
      return link;
    };
    const aMenuItem = {
      prom: [
        {
          name: "Панель администратора",
          ico: "mdi-wrench",
          link: baseURL + "admin",
        },
      ],
      my: [
        {
          name: "Gitt",
          ico: "mdi-github",
          link: gittlink(),
        },
        {
          name: "Swagger",
          ico: "mdi-puzzle",
          link: "http://127.0.0.1:8000/swagger/",
        },
      ],
    };

    const showProm = (data) => {
      let show = true;

      if (data == "my" && getDevelopment() == false) {
        show = false;
      }

      return show;
    };

    return {
      aMenuItem,
      getDevelopment,
      showProm,
    };
  },
};
</script>

<style></style>
