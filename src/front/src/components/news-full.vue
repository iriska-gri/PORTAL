<template>
  <div
    v-if="Object.keys(newsFull).length > 0"
    class="d-flex flex-column flex-fill"
  >
    <v-row class="d-flex flex-row ma-0">
      <v-col class="flex-column d-flex">
        <v-row class="flex-grow-0">
          <v-col class="pb-0 pr-0">
            <v-card height="350px" class="rounded-b-0">
              <v-card-title class="pt-0 pb-1 flex-column d-flex">
                <v-row>
                  <v-col lg="9" class="pt-4">
                    {{ newsFull.title }}
                  </v-col>
                  <v-col
                    class="pa-0 pr-3 pt-1 flex-grow-1 d-flex flex-column flex-wrap"
                  >
                    <v-switch
                      v-model="gallery"
                      class="align-self-end comgal"
                      hide-details
                    >
                      <template v-slot:prepend>
                        <v-tooltip location="top">
                          <template v-slot:activator="{ props }">
                            <v-icon
                              v-bind="props"
                              icon="mdi-message-text-outline"
                              color="pink-darken-4"
                            />
                            <span class="pl-3">
                              {{ newsFull.comment.length }}
                            </span>
                          </template>
                          <span> Чат </span>
                        </v-tooltip>
                      </template>
                      <template v-slot:append>
                        <v-tooltip location="top">
                          <template v-slot:activator="{ props }">
                            <v-icon
                              v-bind="props"
                              :icon="'mdi-image'"
                              color="teal-darken-2"
                            />
                            <span class="pl-3">
                              {{ newsFull.gallery.length }}
                            </span>
                          </template>
                          <span> Галерея </span>
                        </v-tooltip>
                      </template>
                    </v-switch>
                  </v-col>
                </v-row>
              </v-card-title>

              <!--  -->
              <v-img
                :src="`${burl}${newsFull.link}`"
                height="450px"
                width="96%"
                class="mx-auto"
                cover
                @click="openOneImg(newsFull.link)"
              />
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="pt-0 pr-0">
            <v-card class="rounded-t-0 flex-column d-flex h-100">
              <v-list-item class="w-100">
                <template v-slot:prepend>
                  <ico-user :author="newsFull.author" />
                </template>
                <template v-slot:append>
                  <div class="justify-self-end">
                    <v-icon
                      class="me-1"
                      :icon="
                        newsFull.scores.filter(
                          (e) =>
                            e.user == accountStore.user.login && e.score == true
                        ).length > 0
                          ? 'mdi-thumb-up'
                          : 'mdi-thumb-up-outline'
                      "
                      @click="toggleIncrementLike(newsFull.id, true)"
                    />
                    <span class="subheading me-2">
                      {{
                        newsFull.scores.filter((e) => e.score == true).length
                      }}
                    </span>
                    <span class="me-1"> · </span>

                    <v-icon
                      class="me-1"
                      :icon="
                        newsFull.scores.filter(
                          (e) =>
                            e.user == accountStore.user.login &&
                            e.score == false
                        ).length > 0
                          ? 'mdi-thumb-down'
                          : 'mdi-thumb-down-outline'
                      "
                      @click="toggleIncrementLike(newsFull.id, false)"
                    />
                    <span class="subheading me-2">
                      {{
                        newsFull.scores.filter((e) => e.score == false).length
                      }}
                    </span>
                  </div>
                </template>
              </v-list-item>
              <v-divider />
              <v-row class="ma-0 my-3 overflow-auto h-0">
                <v-col class="pa-0">
                  <v-card-text class="pt-0">
                    <div
                      v-if="newsFull.text"
                      v-html="formatText(newsFull.text)"
                    ></div>
                    <div v-else>
                      <v-row>
                        <v-col
                          class="text-h6 text-grey text-center align-self-center text--lighten-1 font-weight-light"
                        >
                          Без описания
                        </v-col>
                      </v-row>
                    </div>
                  </v-card-text>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
      <v-col class="flex-column d-flex">
        <v-row class="d-flex flex-column" v-if="gallery">
          <v-col class="d-flex flex-column">
            <v-card
              class="h-100 flex-column pa-3 d-flex overflow-auto overflow-x-hidden"
            >
              <div class="flex-column d-flex ma-3">
                <v-row
                  style="height: 250px"
                  class="justify-space-between"
                  v-if="newsFull.gallery.length > 0"
                >
                  <v-col
                    v-for="e in newsFull.gallery"
                    :key="e"
                    :lg="
                      Math.floor(
                        Math.random() * (Math.floor(5) - Math.ceil(3)) +
                          Math.ceil(2)
                      )
                    "
                    class="flex-column d-flex pa-0 pb-3"
                  >
                    <div class="h-100 w-100 flex-column d-flex">
                      <v-row>
                        <v-col class="d-flex">
                          <v-img
                            cover
                            class="cursor-pointer"
                            :src="`${burl}${e.img}`"
                            @click="openImg(e.id)"
                          />
                        </v-col>
                      </v-row>
                      <v-row class="flex-grow-0 mt-0 align-self-center">
                        <v-col class="pa-0 flex-grow-0">
                          <v-btn
                            density="compact"
                            variant="text"
                            size="small"
                            :color="heartIcoAll(e) ? 'red' : 'black'"
                            :icon="
                              heartIcoAll(e) ? 'mdi-heart' : 'mdi-heart-outline'
                            "
                            @click="toggleLikeAll(e.id)"
                          />
                        </v-col>
                        <v-col class="pa-0 pl-1">
                          {{ e.likes.length }}
                        </v-col>
                      </v-row>
                    </div>
                  </v-col>
                </v-row>
                <v-row v-else>
                  <v-col
                    class="text-h6 text-grey text-center align-self-center text--lighten-1 font-weight-light"
                  >
                    У новости нет фотографий
                  </v-col>
                </v-row>
              </div>
            </v-card>
          </v-col>
        </v-row>

        <v-row v-else>
          <v-col class="">
            <v-card class="h-100 flex-column d-flex">
              <v-row
                class="ma-0 my-3 overflow-auto h-0"
                v-if="newsFull.comment.length > 0"
              >
                <v-col class="pa-0">
                  <v-card-text class="pt-0">
                    <div
                      v-for="(y, key) in newsFull.comment"
                      :key="key"
                      class="d-flex flex-column pa-3"
                    >
                      <v-row
                        class="justify-space-between ma-0 align-center bgchat mr-7"
                        :class="
                          accountStore.user.login == y.author.login
                            ? 'bgchatnot'
                            : 'bgchat'
                        "
                      >
                        <v-col class="flex-grow-1 text-subtitle-2 pl-2 pa-0">
                          {{
                            accountStore.user.login == y.author.login
                              ? ""
                              : splitname(y.author)
                          }}
                        </v-col>
                        <v-col class="pa-0 text-center text-subtitle-2">
                          {{ dateformat(y.cdate) }}
                        </v-col>
                        <v-col class="pa-0 text-end text-subtitle-2">
                          {{
                            accountStore.user.login != y.author.login
                              ? ""
                              : splitname(y.author)
                          }}
                        </v-col>
                      </v-row>

                      <div class="text-subtitle-2"></div>
                      <v-row>
                        <v-col class="pr-0">
                          <v-alert
                            color="bg_white"
                            rounded="0"
                            :border="
                              accountStore.user.login == y.author.login
                                ? 'end'
                                : 'start'
                            "
                            :border-color="
                              accountStore.user.login == y.author.login
                                ? 'success'
                                : 'deep-purple accent-4'
                            "
                            elevation="0"
                          >
                            {{ y.text }}
                          </v-alert>
                        </v-col>
                        <v-col
                          class="flex-grow-0 d-flex pa-0 align-center"
                          :class="
                            accountStore.user.login == y.author.login
                              ? 'pa-0'
                              : 'pa-5'
                          "
                        >
                          <v-btn
                            v-if="accountStore.user.login == y.author.login"
                            variant="text"
                            size="small"
                            icon="mdi-delete"
                            color="delete_btn"
                            @click="deletComment(y.id, newsFull.id)"
                          />
                        </v-col>
                      </v-row>
                    </div>
                  </v-card-text>
                </v-col>
              </v-row>
              <v-row v-else>
                <v-col
                  class="text-h6 text-grey text-center align-self-center text--lighten-1 font-weight-light"
                >
                  Оставьте первый комментарий
                </v-col>
              </v-row>
              <v-divider />
              <v-row class="flex-grow-0 ma-1">
                <v-col>
                  <!-- <v-text-field
          v-model="textcomment"
          clearable

          hide-details
          class="ma-0"
          label="Комментарий"
          rows="1"
          no-resize
        /> -->
                  <v-textarea
                    label="Комментарий"
                    no-resize
                    variant="underlined"
                    rows="1"
                    row-height="25"
                    shaped
                    @keyup.enter.exact="addComment(newsFull.id)"
                    hide-details
                    v-model="textcomment"
                  />
                </v-col>
                <v-col class="flex-grow-0 pl-0 py-0 align-self-center">
                  <v-btn
                    variant="text"
                    density="compact"
                    icon="mdi-google-play"
                    color="teal-darken-4"
                    :disabled="textcomment == ''"
                    @click="addComment(newsFull.id)"
                  />
                </v-col>
              </v-row>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <v-dialog
      v-model="dialogfoto"
      width="w-100"
      height="900"
      class="flex-column"
    >
      <v-card class="pa-4 h-100 flex-column d-flex">
        <v-row class="flex-grow-0 justify-end">
          <v-col class="pa-0 flex-grow-0">
            <v-btn
              density="compact"
              variant="text"
              icon="mdi-close"
              @click="dialogfoto = false"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col class="flex-grow-0 align-self-center">
            <v-btn
              :disabled="newsFull.gallery.length == 1"
              density="compact"
              variant="text"
              icon="mdi-chevron-left"
              @click="
                indximg != 0
                  ? (indximg -= 1)
                  : (indximg = newsFull.gallery.length - 1)
              "
            />
          </v-col>
          <v-col class="flex-column h_cards pa-0">
            <v-img class="d-flex" :src="`${burl}${galleryimges.img}`" />
          </v-col>
          <v-col class="d-flex flex-column flex-grow-0">
            <v-row>
              <v-col class="flex-column d-flex align-end align-self-center">
                <v-btn
                  :disabled="newsFull.gallery.length == 1"
                  density="compact"
                  variant="text"
                  icon="mdi-chevron-right"
                  @click="
                    indximg != newsFull.gallery.length - 1
                      ? (indximg += 1)
                      : (indximg = 0)
                  "
                />
              </v-col>
            </v-row>
          </v-col>
        </v-row>
        <v-row class="flex-grow-1 align-self-center d-flex placeIt">
          <v-col class="pa-0">
            <v-btn
              density="compact"
              variant="text"
              :color="heartIco() ? 'red' : 'black'"
              :icon="heartIco() ? 'mdi-heart' : 'mdi-heart-outline'"
              @click="toggleLike(galleryimges.id)"
            />
          </v-col>
          <v-col class="pa-0 text-overline">
            {{ galleryimges.likes.length }}
          </v-col>
        </v-row>
      </v-card>
    </v-dialog>

    <v-dialog
      v-model="dialogfotoOne"
      width="w-100"
      height="900"
      class="flex-column"
    >
      <v-card class="pa-4 h-100 flex-column d-flex">
        <v-row class="flex-grow-0 justify-end">
          <v-col class="pa-0 flex-grow-0">
            <v-btn
              density="compact"
              variant="text"
              icon="mdi-close"
              @click="dialogfotoOne = false"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col class="flex-column h_cards pa-0">
            <v-img class="d-flex" :src="`${burl}${galleryimges}`" />
          </v-col>
        </v-row>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { useRoute } from "vue-router";
import { axiosApiInstance } from "@/utils/axios-api";
import { ref, watch } from "vue";
import { baseURL } from "@/utils/axios-api";
import { checkremote } from "@/utils/universal_functions";
import { spravURL } from "@/utils/axios-api";
import { useAccountStore } from "@/store/AccountStore";
import { format } from "date-fns";
import icoUser from "@/components/UI/fiousercard/icoUser.vue";

const accountStore = useAccountStore();

export default {
  components: { icoUser },

  setup() {
    const textcomment = ref("");
    const route = useRoute();
    const newsFull = ref([]);
    const gallery = ref(false);

    const burl = baseURL.slice(0, -1);

    const loadNews = () => {
      axiosApiInstance
        .get(`api/navigation/newscrossroad/?id=${route.query.id}`)
        .then((result) => {
          newsFull.value = result.data.result[0];

          if (newsFull.value.gallery.length > 0) {
            gallery.value = true;
          }
        });
    };

    loadNews();

    const splitname = (name) => {
      return (
        name.familyname + " " + name.name[0] + "." + name.parentname[0] + "."
      );
    };

    const formatText = (text) => {
      return text.replaceAll(
        'src="/media/uploads',
        `src="${baseURL}media/uploads`
      );
    };

    const dateformat = (datas) => {
      return format(new Date(datas), "dd.MM.yyyy HH:mm");
    };

    const addComment = (idnew) => {
      axiosApiInstance
        .post(`api/navigation/newscrossroad/`, {
          news: idnew,
          text: textcomment.value,
        })
        .then((result) => {
          newsFull.value.comment = result.data.comment;
        });
      textcomment.value = "";
    };

    const deletComment = (id, news) => {
      axiosApiInstance
        .post(`api/navigation/newscrossroad/`, { delid: id, news: news })
        .then((result) => {
          newsFull.value.comment = result.data.comment;
        });
    };

    const heartIcoAll = (image) => {
      return (
        image.likes.filter((e) => e.user == accountStore.user.login).length == 1
      );
    };

    // ------------------------------ Галерея
    const galleryimges = ref([]);
    const dialogfoto = ref(false);
    const dialogfotoOne = ref(false);
    const indximg = ref("");

    const openImg = (idimg) => {
      dialogfoto.value = true;
      indximg.value = newsFull.value.gallery.findIndex((e) => e.id == idimg);
    };

    const openOneImg = (idimg) => {
      dialogfotoOne.value = true;
      galleryimges.value = idimg;
    };

    watch(
      () => indximg,
      (newValue, oldValue) => {
        if (newValue) {
          galleryimges.value = newsFull.value.gallery[newValue.value];
        }
      },
      { deep: true }
    );

    // Лайки на фотографии

    const toggleLike = (idimage) => {
      axiosApiInstance
        .post(`api/navigation/gallery/`, { image: idimage })
        .then((result) => {
          galleryimges.value.likes = result.data;
        });
    };

    const toggleLikeAll = (idimage) => {
      axiosApiInstance
        .post(`api/navigation/gallery/`, { image: idimage })
        .then((result) => {
          newsFull.value.gallery.filter((e) => e.id == idimage)[0].likes =
            result.data;
        });
    };
    const heartIco = () => {
      return (
        galleryimges.value.likes.filter(
          (e) => e.user == accountStore.user.login
        ).length == 1
      );
    };

    const toggleIncrementLike = (news, scores) => {
      axiosApiInstance
        .post(`api/navigation/newscrossroad/`, { news: news, scores: scores })
        .then((result) => {
          newsFull.value.scores = result.data;
        });
    };

    return {
      route,
      newsFull,
      gallery,
      burl,
      checkremote,
      spravURL,
      splitname,
      accountStore,
      formatText,
      dateformat,
      textcomment,
      addComment,
      deletComment,
      heartIcoAll,
      heartIco,
      toggleLikeAll,
      toggleLike,
      openImg,
      dialogfoto,
      galleryimges,
      indximg,
      toggleIncrementLike,
      openOneImg,
      dialogfotoOne,
    };
  },
};
</script>

<style>
.comgal .v-switch__thumb {
  color: white !important;
}

.h_cards {
  height: 86vh;
}
</style>
