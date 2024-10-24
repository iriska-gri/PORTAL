<template>
  <div>
    <v-card class="bg-white pa-1 px-0" width="550">
      <v-card
        class="mx-auto overflow-auto mx-0 px-0"
        width="550"
        height="600"
        flat
      >
        <v-card-title class="fixed-bar bg-white">
          <v-row class="bggrad">
            <v-col class="text-center text-black_and_white">
              {{ namepos }}
            </v-col>
          </v-row>
          <v-row>
            <v-col class="pa-0 mb-1">
              <v-divider class="" />
              <v-text-field
                v-model="searchname"
                clearable
                prepend-inner-icon="mdi-magnify"
                hide-details
                class="ma-0"
                label="Поиск"
                rows="1"
                no-resize
              />
            </v-col>
          </v-row>
        </v-card-title>

        <div v-for="(x, key) in result" :key="key" class="px-3 ddd">
          <v-list class="py-0">
            <v-list-subheader>{{ key }} </v-list-subheader>
          </v-list>
          <div v-for="item in x" :key="item">
            <list-user :author="item" />
            <!-- <vcard-user :author = item     /> -->
          </div>
        </div>
      </v-card>
      <v-divider class="" />
      <v-card-actions class="pb-0" style="place-content: end">
        <v-btn color="more_details_btn" variant="text" @click="onSubmit">
          Закрыть
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import { ref, onMounted, computed } from "vue";
import { checkremote } from "@/utils/universal_functions";
import { spravURL } from "@/utils/axios-api";
import { axiosApiInstance } from "@/utils/axios-api";
import VcardUser from "@/components/UI/fiousercard/vcardUser.vue";

export default {
  components: {
    VcardUser,
  },

  props: {
    idpos: {
      type: Number,
      default: "",
    },
    namepos: {
      type: String,
      default: "",
    },
  },

  setup(props, { emit }) {
    const t_dailyRound = ref({});
    // const result = ref({})
    const iduser = ref("");
    const searchname = ref("");

    const onSubmit = () => {
      emit("searchClose");
    };

    onMounted(() => {
      axiosApiInstance
        .get(`api/general_vacation/dailyload/?id=${props.idpos}`)
        .then((data) => {
          t_dailyRound.value = data.data.daily;
        });
    });

    const getcard = async (idus) => {
      iduser.value = idus;
    };

    const result = computed({
      get() {
        let ob = {};
        Object.keys(t_dailyRound.value).map((el1) => {
          let myarr = t_dailyRound.value[el1].filter((el) =>
            el.fio.toLowerCase().includes(searchname.value.toLowerCase())
          );

          if (myarr.length > 0) {
            ob[el1] = myarr;
          }
        });
        return ob;
      },
    });

    return {
      onSubmit,
      checkremote,
      searchname,
      spravURL,
      t_dailyRound,
      result,

      getcard,
      iduser,
    };
  },
};
</script>

<style></style>
