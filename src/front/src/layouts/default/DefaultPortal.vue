<template>
  <v-app>
    <v-app-bar
      :elevation="accountStore.cod2user ? 2 : 0"
      density="compact"
      color="app_bar"
      class="pl-4"
    >
      <v-icon
        v-if="accountStore.cod2user"
        class="px-3"
        size="20"
        color="black_and_white"
        :icon="rail ? 'mdi-chevron-right' : 'mdi-chevron-left'"
        @click="rail = !rail"
      />

      <v-card
        v-if="accountStore.cod2user"
        class="bg-transparent py"
        color="black_and_white"
        density="compact"
        :prepend-avatar="imageSrc"
        title="Портал МИ ФНС России по ЦОД № 2"
        variant="text"
        :to="'/'"
      />
      <template v-slot:image>
        <v-img class="bggrad" />
      </template>
      <template v-slot:append>
        <template v-if="accountStore.cod2user">
          <vcard-user :author="accountStore.user" />
    
          <v-tooltip location="bottom">
            <template v-slot:activator="{ props }">
              <v-btn
                color="black_and_white"
                v-bind="props"
                dark
                to="/faq"
                icon="mdi-comment-question-outline"
              />
            </template>
            <span>F.A.Q.</span>
          </v-tooltip>

          <v-dialog v-model="LikeDialog" persistent width="800">
            <template v-slot:activator="{ props }">
              <v-btn
                color="black_and_white"
                v-bind="props"
                dark
                icon="mdi-thumb-up-outline"
              >
                <v-icon></v-icon>
                <v-tooltip activator="parent" location="bottom"
                  >Обратная связь</v-tooltip
                >
              </v-btn>
            </template>

            <Card-like :LikeDialog="LikeDialog" @menusClose="closeinfo()" />
          </v-dialog>

          <v-tooltip location="bottom">
            <template v-slot:activator="{ props }">
              <v-btn icon @click="toggleTheme">
                <v-icon v-bind="props" class="mr-1" color="lampa">
                  mdi-lightbulb-outline
                </v-icon>
              </v-btn>
            </template>
            <span> Сменить тему</span>
          </v-tooltip>

          <v-card v-show="message" class="" width="50">{{ name }}</v-card>

          <v-tooltip location="bottom">
            <template v-slot:activator="{ props }">
              <v-btn
                color="black_and_white"
                icon="mdi-account-multiple-outline"
                @click="drawer_right = !drawer_right"
                v-bind="props"
              />
            </template>
            <span>
              {{
                drawer_right == true
                  ? "Скрыть пользователей"
                  : "Показать пользователей"
              }}
            </span>
          </v-tooltip>
          <v-tooltip location="bottom">
            <template v-slot:activator="{ props }">
              <v-btn
                color="black_and_white"
                icon="mdi-logout"
                @click="accountStore.logout"
                v-bind="props"
              />
            </template>
            <span> Выход </span>
          </v-tooltip>
        </template>

        <template v-else>
          <v-row justify="center">
            <Auth-form @challengealert="alert = true" />
          </v-row>
        </template>
      </template>
    </v-app-bar>
    <v-navigation-drawer
      v-if="accountStore.cod2user"
      :width="245"
      :rail="rail"
      permanent
      v-model="drawer"
    >
      <v-row class="my-0 h-100">
        <v-col class="flex-column d-flex">
          <v-row
            ><v-col>
              <v-list nav density="compact">
                <template v-for="(x, key) in navigations">
                  <!-- v-if="!('submenu' in x) || (x.path== '/portal' && accountStore.user.is_staff)" -->
                  <v-list-item
                    v-if="
                      (x.path == '/portal'
                        ? accountStore.user.is_superuser
                        : true) && !('submenu' in x)
                    "
                    :key="x.key"
                    :title="x.name"
                    :value="x.name"
                    :href="x.link"
                    :disabled="x.path == ''"
                    :to="x.path"
                    :target="x.link ? '_blank' : ''"
                    color="navigation"
                  >
            
                    <!-- Чтобы сделать неактивным раздел безопасность, не забыть прописать путь до него в disabled для показа -->
                    <template v-slot:prepend>
                      <v-icon :icon="x.ico" />
                      <v-tooltip v-if="rail" activator="parent" location="top">
                        {{ x.name }}
                      </v-tooltip>
                    </template>
                  </v-list-item>

                  <v-list-group
                    v-if="x.path != '/portal' && 'submenu' in x"
                    :class="rail ? 'railmenu' : ''"
                    :key="key"
                    :value="x.name"
                  >
                    <template v-slot:activator="{ props }">
                      <v-list-item
                        v-bind="props"
                        :title="x.name"
                        :prepend-icon="x.ico"
                        color="navigation"
                      >
                        <v-tooltip
                          v-if="rail"
                          activator="parent"
                          location="top"
                        >
                          {{ x.name }}
                        </v-tooltip>
                      </v-list-item>
                    </template>
                    <v-list-item
                      v-for="(child, k) in x.submenu"
                      color="navigation"
                      :href="child.link"
                      :key="k"
                      :value="child.name"
                      :title="!rail ? child.name : menuTruncated(child.name)"
                      :to="child.path"
                      :target="child.link ? '_blank' : ''"
                    >
                      <v-tooltip v-if="rail" activator="parent" location="top">
                        {{ child.name }}
                      </v-tooltip>
                    </v-list-item>
                  </v-list-group>
                </template>
              </v-list>

              <v-list nav density="compact">
                <v-list-item
                  v-for="x of mainmenuStore.portallinks"
                  :key="x.name"
                  :title="x.name"
                  :value="x.name"
                  :href="x.link"
                  color="app_bar"
                  :target="x.link ? '_blank' : ''"
                >
                  <template v-slot:prepend>
                    <v-icon :icon="x.imagecode" />
                    <v-tooltip v-if="rail" activator="parent" location="top">
                      {{ x.name }}
                    </v-tooltip>
                  </template>
                </v-list-item>
              </v-list>
            </v-col>
          </v-row>

          <v-row class="flex-grow-0" v-if="accountStore.user.is_staff">
            <v-col>
              <default-portal-menu-list :rail="rail" />
              <!-- <v-list nav density="compact" active-class="noneoutline">
                <default-portal-menu-list :aMenuItem="supperuser"/>
                <div v-if="getDevelopment()">
                 
                  <default-portal-menu-list :aMenuItem="oRasrab"/>
                </div>
                    


              </v-list> -->
            </v-col>
          </v-row>
          <v-row no-gutters class="flex-grow-0">
            <v-col>
              <page-counter :rail="rail" />
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-navigation-drawer>

    <v-main v-if="accountStore.cod2user" class="d-flex bg-main_theme">
      <router-view />

      <alert-default />
    </v-main>
    <v-main v-else class="d-flex align-center text-h3 bg-teal-lighten-2">
      <v-card
        class="h-100 w-100 d-flex justify-center rounded-0 flex-column"
        :image="`${burl}${scrimg}`"
      >
        <v-card-text
          class="justify-center bgCard h-100 ma-3 d-flex flex-column"
        >
          <v-row class="bgText flex-grow-0">
            <v-col class="text-center textcolor font-weight-black text-h3 pb-0">
              Добро пожаловать на портал МИ ФНС России по ЦОД № 2
            </v-col>
          </v-row>
          <v-row class="bgText flex-grow-0">
            <v-col class="text-subtitle-1 text-center textcolor pt-0">
              Авторизуйтесь для получения доступа к контенту портала
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>

      <alert-default />
    </v-main>
    <v-navigation-drawer
      v-if="accountStore.cod2user"
      v-model="drawer_right"
      rail
      permanent
      location="right"
      @click="rail = false"
    >
      <Online-users />
    </v-navigation-drawer>
  </v-app>
</template>

<script>
import { ref, computed } from "vue";
import uf from "@/utils/universal_functions";
import { useAccountStore } from "@/store/AccountStore";
import { useMainmenuStore } from "@/store/MainmenuStore";
import { useTheme } from "vuetify";
import AuthForm from "@/components/UI/Auth-form.vue";
import OnlineUsers from "@/components/UI/fiousercard/onlineUsers.vue";
import CardLike from "@/components/cardLike.vue";
import { axiosApiInstance, clearAxios } from "@/utils/axios-api";

import { baseURL } from "@/utils/axios-api";
import VcardUser from "@/components/UI/fiousercard/vcardUser.vue";
import PageCounter from "@/components/UI/defaultportal/page-counter.vue";
import DefaultPortalMenuList from "@/layouts/default/DefaultPortalMenuList.vue";
import { getDevelopment } from "@/utils/universal_functions";
import { useDisplay } from "vuetify";

export default {
  components: {
    AuthForm,
    OnlineUsers,
    CardLike,
    VcardUser,
    PageCounter,
    DefaultPortalMenuList,
  },

  mixins: [uf],

  setup() {
    const { name } = useDisplay();
    const theme = useTheme();
    const mainmenuStore = useMainmenuStore();
    const accountStore = useAccountStore();
    const drawer = ref(true);
    const drawer_right = ref(true);

    const LikeDialog = ref(false);
    const rail = ref(false);
    const showTooltip = ref(false);
    const alert = ref(false);
    const burl = baseURL.slice(0, -1);
    const scrimg = ref([]);

    const message = computed({
      get: () => {
        return process.env.NODE_ENV == "development" ? true : false;
      },
    });

    const screenimg = () => {
      if (!accountStore.cod2user) {
     
        clearAxios.get(`api/navigation/screensaver/`).then((data) => {
          console.log(data, 'saver--')
          // scrimg.value = data.data[0].img;
        });
      }
    };

    screenimg();

    const menuTruncated = (menus) => {
      return menus.slice(0, 2).toUpperCase();
    };

    const toggleTheme = () => {
      theme.global.name.value = theme.global.current.value.dark
        ? "light"
        : "dark";
    };

    mainmenuStore.loadlinks();

    const gittlink = () => {
      const link =
        baseURL == "http://127.0.0.1:8000/"
          ? "http://sulaco.nodered.ru:5223/COD2/PORTAL_COD2/projects"
          : "http://maestro.cod2.regions.tax.nalog.ru:3333/COD2/PORTAL_COD2/projects/22";
      return link;
    };

    // 'https://materialdesignicons.com/cdn/1.6.50-dev/'

    const oRasrab = [
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
    ];

    // ]

    const navigations = ref([
      {
        name: "Новости",
        ico: "mdi-newspaper",
        path: "/news",
      },
      {
        name: "Структура",
        ico: "mdi-source-branch",
        submenu: [
          {
            name: "ОКиБ",
            path: "/okib",
          },
        ],
      },
      {
        name: "Сотрудники",
        ico: "mdi-account-multiple-outline",
        submenu: [
          {
            name: "Справочник",
            link: "http://10.252.44.33/accounting6/members.php",
          },
          //     {
          //   name: 'О пользователе',
          //   ico: 'mdi-account',
          //   path: "/userinfo"
          // },
        ],
      },
      // {
      //   name: "Деятельность",
      //   ico: "mdi-bulletin-board",
      //   submenu: [
      //     {
      //       name: "Обеспечивающая",
      //       path: "/providing",
      //     },
      //   ],
      // },

      {
        name: "Календарь",
        ico: "mdi-calendar",
        path: "/ical",
      },

      {
        name: "Об инспекции",
        ico: "mdi-city",
        path: "/inspection",
      },

      {
        name: "О портале",
        ico: "mdi-information-variant",
        path: "/portal",
      },

      // {
      //   name: 'К празднику',
      //   ico: 'mdi-cake-variant',
      //   path: "/fnshol"
      // }
    ]);

    const imageSrc = computed(() => {
      return new URL(`@/assets/FNS-logo-xs.png`, import.meta.url).href;
    });

    const closeinfo = () => {
      LikeDialog.value = false;
      // feedalert.value=true
    };

    const getSafetyChapter = () => {
      axiosApiInstance.get("api/safety/gettypes/").then((response) => {
        response.data.forEach((item) => {
          if (!item.path.startsWith("/")) {
            item.path = "/" + item.path;
          }
          item.path = "/safety" + item.path;
        });

        if (response.data.length > 0) {
          let safetyMenu = {
            name: "Безопасность",
            ico: "mdi-security",
            submenu: response.data,
          };
          navigations.value.splice(4, 0, safetyMenu);
        }
      });
    };

    getSafetyChapter();

    return {
      theme,
      mainmenuStore,
      accountStore,
      drawer,
      drawer_right,
      toggleTheme,
      navigations,
      imageSrc,
      LikeDialog,
      scrimg,
      oRasrab,
      rail,
      showTooltip,
      menuTruncated,
      // feedalert,
      alert,
      burl,
      name,
      closeinfo,
      baseURL,
      getDevelopment,
      message,
    };
  },
};
</script>
<style lang="scss">
.mystat {
  position: fixed;
  right: 10px;
  bottom: 10px;
  z-index: 1005;
}

.btnNav .v-navigation-drawer__content {
  display: flex;
  align-items: center;
}

.railmenu .v-list-group__items .v-list-item {
  padding-inline-start: 11px !important;
}

.textcolor {
  color: #2f535e;
}

#tr-popup {
  display: none;
}
</style>
