<template>
  <pattern-card
    :title="'Рейтинг посещаемости страниц портала'"
    :ico="'mdi-chart-bar'"
  >
    <template v-slot:filling>
      <v-data-table-virtual
        :headers="headers"
        :items="tabledata"
        height="400"
        class="mytable"
        item-value="name"
        @update:sortBy="customSort"
        v-model:sort-by="sortBy"
        density="compact"
      >
        <template v-slot:header.name>
          <v-switch
            :label="untot"
            false-value="уникальные"
            true-value="всего"
            hide-details
            v-model="untot"
            class="myleft ml-n4"
          />
        </template>
        <template v-slot:item.name="{ value }">
          <span class="font-weight-medium cursor-default text-grey-darken-3 myleft text-subtitle-2"
          >
            {{ value }}
          </span>
        </template>
        <template v-slot:item.now="{ value, item }">
          <span class="font-weight-medium text-subtitle-2">
            <v-tooltip v-if="value > 0" location="bottom">
              <template v-slot:activator="{ props }">
                <span
                  v-bind="props"
                  :class="
                    'untot' == 'уникальные'
                      ? getColorTooday1(value)
                      : getColorTooday2(value)
                  "
                  class="cursor-help font-weight-medium text-subtitle-1"
                >
                  {{ value }}
                </span>
              </template>
              <v-row no-gutters>
                <v-col>
                  <v-row no-gutters v-for="n in item.now.unic" :key="n">
                    <v-col>
                      {{ n }}
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-tooltip>
          </span>
        </template>
        <template v-slot:item.period="{ value, item }">
          <span class="font-weight-medium text-subtitle-2">
            <v-tooltip v-if="value > 0" location="bottom">
              <template v-slot:activator="{ props }">
                <span
                  v-bind="props"
                  :class="
                    'untot' == 'уникальные'
                      ? getColorPeriod1(value)
                      : getColorPeriod2(value)
                  "
                  class="cursor-help font-weight-medium text-subtitle-1"
                >
                  {{ value }}
                </span>
              </template>
              <v-row no-gutters>
                <v-col>
                  <v-row no-gutters v-for="n in item.period.unic" :key="n">
                    <v-col>
                      {{ n }}
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-tooltip>
          </span>
        </template>
      </v-data-table-virtual>
    </template>
  </pattern-card>
</template>

<script>
import { ref, watch } from "vue";
import PatternCard from "@/components/UI/aboutportal/pattern-card.vue";
import TooltipText from "@/components/UI/tooltip-text.vue";
import { splitname, formatDash } from "@/utils/universal_functions";

export default {
  components: { TooltipText, PatternCard },

  props: {
    pages_count: {
      type: Array,
      default: () => [],
    },
  },

  setup(props) {
    const sortBy = ref([
      {
        key: "now",
        order: "desc",
      },
    ]);

    const untot = ref("уникальные");
    let headers = ref([
      { title: "", align: "start", key: "name" },
      {
        title: "сегодня",
        align: "center",
        key: "now",
        value: (item) =>
          `${
            untot.value == "уникальные" ? item.now.unic.size : item.now.total
          }`,
      },
      {
        title: "за период",
        align: "center",
        key: "period",
        value: (item) =>
          `${
            untot.value == "уникальные"
              ? item.period.unic.size
              : item.period.total
          }`,
      },
    ]);

    const datas = () => {
      let data = [];
      props.pages_count.forEach((e) => {
        let ind = data.findIndex((el) => el.name == e.pages);
        if (ind == -1) {
          let ob = {
            name: e.pages,
            now: { unic: new Set(), total: 0 },
            period: { unic: new Set(), total: 0 },
          };
          if (e.visitdate == formatDash(new Date())) {
            ob.now.unic.add(splitname(e.user));
            ob.now.total = e.count;
          }
          ob.period.unic.add(splitname(e.user));
          ob.period.total = e.count;
          data.push(ob);
        } else {
          if (e.visitdate == formatDash(new Date())) {
            data[ind].now.unic.add(splitname(e.user));
            data[ind].now.total += e.count;
          }

          data[ind].period.unic.add(splitname(e.user));
          data[ind].period.total += e.count;
        }
      });

      return data;
    };

    const modelrating = ref(false);

    const getColorTooday1 = (pages) => {
      if (pages > 10) return "text-green";
      else if (pages > 5) return "text-orange";
      else return "text-red";
    };

    const getColorPeriod1 = (pages) => {
      if (pages > 30) return "text-green";
      else if (pages > 15) return "text-orange";
      else return "text-red";
    };

    const getColorTooday2 = (pages) => {
      if (pages > 50) return "text-green";
      else if (pages > 25) return "text-orange";
      else return "text-red";
    };

    const getColorPeriod2 = (pages) => {
      if (pages > 100) return "text-green";
      else if (pages > 50) return "text-orange";
      else return "text-red";
    };

    const getColorNow = (pages) => {
      if (pages > 10) return "text-green";
      else if (pages > 5) return "text-orange";
      else return "text-red";
    };

    const customSort = () => {
      let arr = tabledata.value;

      if (sortBy.value !== undefined && sortBy.value.length > 0) {
        let factor = sortBy.value[0].order == "desc" ? [-1, 1] : [1, -1];
        if (untot.value == "уникальные") {
          arr.sort((a, b) => {
            if (
              a[sortBy.value[0].key].unic.size >
              b[sortBy.value[0].key].unic.size
            )
              return factor[0];
            if (
              a[sortBy.value[0].key].unic.size <
              b[sortBy.value[0].key].unic.size
            )
              return factor[1];
            return 0;
          });
        } else {
          arr.sort((a, b) => {
            if (a[sortBy.value[0].key].total > b[sortBy.value[0].key].total)
              return factor[0];
            if (a[sortBy.value[0].key].total < b[sortBy.value[0].key].total)
              return factor[1];
            return 0;
          });
        }
      }
      tabledata.value = arr;
    };
    const tabledata = ref(datas());
    watch(
      () => props.pages_count,
      (newValue) => {
        if (newValue !== []) {
          tabledata.value = datas();
          customSort();
        }
      }
    );
    // tabledata.value=datas.value
    return {
      tabledata,
      sortBy,
      customSort,
      untot,
      modelrating,
      getColorTooday1,
      getColorPeriod1,
      getColorTooday2,
      getColorPeriod2,
      getColorNow,
      headers,
      datas,
    };
  },
};
</script>

<style>
.v-table {
  flex: 1 !important;
}

.mytable tr {
  font-size: 13px;
}
.mytable i {
  font-size: 10px;
}

.myleft {
  float: left;
}
</style>
