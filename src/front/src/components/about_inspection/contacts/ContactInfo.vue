<template>
  <v-row no-gutters class="h-100 gap">
    <v-col lg="5" md="12" sm="12" xs="12" class="flex-column d-flex">
      <v-card elevation="5" class="h-100" min-height="250">
        <l-map :zoom="14" :min-zoom="14" :center="markers[0].coordinate">
          <l-tile-layer :url="`${baseURL}media/Tiles/{z}/{x}/{y}.png`" />
          <l-marker
            v-for="marker in markers"
            :key="marker"
            :lat-lng="marker.coordinate"
            :icon="icon(marker.icon)"
          >
            <l-tooltip>
              <p>{{ marker.tooltip }}</p>
              <p style="max-width: 20%; min-width: 20%; word-wrap: break-word">
                {{ marker.tooltip_bus }}
              </p>
            </l-tooltip>
          </l-marker>
        </l-map>
      </v-card>
    </v-col>
    <v-col class="flex-column">
      <v-row no-gutters class="h-100 gap flex-column">
        <v-col lg="3" class="w100 flex-column">
          <v-card class="h-100 flex-column d-flex" elevation="5">
            <v-card-title
              class="d-flex justify-center bg-teal-lighten-5 text-teal-darken-4"
            >
              <v-row>
                <v-col lg="5" class="d-flex justify-center">Адрес</v-col>
                <v-col lg="6" class="d-flex justify-center">Время работы</v-col>
              </v-row>
            </v-card-title>
            <v-row class="d-flex justify-center align-center">
              <v-col lg="4">
                <v-card-text class="text-subtitle-1">
                  {{ address.building }}
                </v-card-text>
                <v-card-text class="text-subtitle-1">
                  {{ address.phone }}
                </v-card-text>
              </v-col>
              <v-col lg="7">
                <v-list>
                  <v-list-item v-for="work_time in work_times" :key="work_time">
                    <v-row>
                      <v-col
                        lg="6"
                        class="text-subtitle-1 d-flex justify-center align-center"
                        >{{ work_time.day }}</v-col
                      >
                      <v-col
                        lg="6"
                        class="text-subtitle-1 d-flex justify-center align-center"
                        >{{ work_time.time }}</v-col
                      >
                    </v-row>
                  </v-list-item>
                </v-list>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
        <v-col>
          <v-card class="h-100 flex-column d-flex" elevation="5">
            <v-card-title
              class="text-h6 d-flex justify-center bg-teal-lighten-5 text-teal-darken-4"
            >
              Способ проезда
            </v-card-title>
            <v-card-text class="text-subtitle-1">
              <v-list lines="three">
                <v-list-item
                  v-for="address_path in address_pathes"
                  :key="address_path"
                >
                  <strong>{{ address_path.title_path }}</strong
                  >{{ address_path.path }}
                </v-list-item>
              </v-list>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>
<script>
import { ref } from "vue";
import { baseURL } from "@/utils/axios-api";
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LMarker, LTooltip } from "@vue-leaflet/vue-leaflet";
import { L, icon } from "leaflet";

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LTooltip,
    L,
    icon,
  },
  setup() {
    const pathbuild = (icon) => {
      return `${baseURL}media/map_icons/${icon}.png`;
    };
    const icons = {
      icon_cod: {
        iconUrl: pathbuild(`fns`),
        iconSize: [30, 30],
        iconAnchor: [16, 40],
      },
      icon_metro: {
        iconUrl: pathbuild(`mos_metro`),
        iconSize: [30, 25],
        iconAnchor: [10, 20],
      },
      icon_mcd: {
        iconUrl: pathbuild(`mcd_d2`),
        iconSize: [32, 18],
        iconAnchor: [10, 20],
      },
      icon_bus: {
        iconUrl: pathbuild(`bus`),
        iconSize: [18, 18],
        iconAnchor: [1, 1],
      },
    };
    const markers = ref([
      {
        coordinate: [55.83451, 37.40848],
        icon: icons.icon_cod,
        tooltip: "МИ ФНС России по ЦОД №2",
        tooltip_bus: "",
      },
      {
        coordinate: [55.83309, 37.39933],
        icon: icons.icon_mcd,
        tooltip: 'МЦД D2: пл."Трикотажная"',
        tooltip_bus: "",
      },
      {
        coordinate: [55.82741, 37.43715],
        icon: icons.icon_metro,
        tooltip: 'Ст.метро: "Тушинская"',
        tooltip_bus: "",
      },
      {
        coordinate: [55.82705, 37.4411],
        icon: icons.icon_mcd,
        tooltip: 'МЦД D2: пл. "Тушинская"',
        tooltip_bus: "",
      },
      {
        coordinate: [55.8496, 37.43925],
        icon: icons.icon_metro,
        tooltip: 'Ст.метро: "Сходненская"',
        tooltip_bus: "",
      },
      {
        coordinate: [55.835274, 37.411052],
        icon: icons.icon_bus,
        tooltip: 'Остановка: "Налоговый городок"',
        tooltip_bus: "Автобусы:№368, №с377",
      },
      {
        coordinate: [55.833193, 37.400858],
        icon: icons.icon_bus,
        tooltip: 'Остановка:"МЦД Трикотажная"',
        tooltip_bus: "Автобусы: №26, №368, №с377, №с396",
      },
      {
        coordinate: [55.82524, 37.43575],
        icon: icons.icon_bus,
        tooltip: 'Остановка: "метро Тушинская", выход:5 ',
        tooltip_bus: "Автобусы: №400, №741, №741к, №856, №436, №575",
      },
      {
        coordinate: [55.8501, 37.43905],
        icon: icons.icon_bus,
        tooltip: 'Остановка: "метро Сходненская", выход:9',
        tooltip_bus: "Автобус: №368",
      },
      {
        coordinate: [55.83607, 37.40569],
        icon: icons.icon_bus,
        tooltip: 'Остановка "Храм Сергия Радонежского"',
        tooltip_bus: "Автобусы: №88, №488, №с377, №с396",
      },
      {
        coordinate: [55.83132, 37.4034],
        icon: icons.icon_bus,
        tooltip: 'Остановка "МЦД Трикотажная"',
        tooltip_bus: "Автобусы: №2, №210, №400Т, №741, №741к, №856, №436, №575",
      },
    ]);

    return {
      icons,
      markers,
      icon,

      address: {
        building: "125373, Москва, Походный проезд, двл.3, стр 1",
        phone: "Телефон: 8(495) 198-53-12",
      },
      address_pathes: [
        {
          title_path: "От станции МЦД «Трикотажная»,",
          path: 'на автобусе 368, до остановки "Налоговый городок" или пешком (10 минут) до территории Налоговго городка',
        },
        {
          title_path: "От станции метро «Сходненская», выход:9,",
          path: " 1-й вагон из центра, далее на автобусе № 368",
        },
        {
          title_path: "От станции МЦД «Тушинская»,",
          path: " проехать одну остановку до станции МЦД «Трикотажная» и далее на  автобусе 368 до остановки «Налоговый городок» или пешком(10 минут) до территории Налогового городка",
        },
        {
          title_path: "От станции метро «Тушинская», выход:5,",
          path: " последний вагон из центра, автобусы №2, №210, №400Т, №741, №741к, №856, №436, №575 до остановки «пл. Трикотажная» или от станции МЦД «Тушинская» проехать одну остановку до станции МЦД «Трикотажная» и далее на  автобусе 368 до остановки «Налоговый городок» или пешком(10 минут) до территории Налогового городка",
        },
        {
          title_path: "От остановки автобуса «Храм Сергия Радонежского»",
          path: " и далее пешком (10 минут) до территории Налоговго городка",
        },
      ],

      work_times: [
        { day: "Понедельник - Четверг", time: "09:00 - 18:00" },
        { day: "Пятница", time: "09:00 - 16:45" },
        { day: "Суббота - Воскресенье", time: "Выходной" },
      ],
      baseURL,
    };
  },
};
</script>
<style>
.leaflet-control-attribution {
  display: none;
}
</style>
