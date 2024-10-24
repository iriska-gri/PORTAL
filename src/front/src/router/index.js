// Composables
import { createRouter, createWebHistory } from "vue-router";
import { useAccountStore } from "@/store/AccountStore";

const routes = [
  {
    path: "/",
    component: () => import("@/layouts/default/DefaultPortal.vue"),
    meta: {
      title: "Вход",
    },

    children: [
      {
        path: "/",
        name: "HomePage",
        component: () => import("@/views/HomePage.vue"),
        meta: {
          title: "Портал МИ ФНС России по ЦОД №2",
          ico: "mdi-arrow-top-right",
        },
      },

      {
        path: "/okib",
        name: "OKiBPage",
        component: () => import("@/views/nested_view/o_OKiB.vue"),
        meta: {
          title: "Отдел кадров и безопасности",
          ico: "mdi-comment-account-outline",
        },
      },
      {
        path: "/providing",
        name: "ProvidingActivitiesPage",
        component: () => import("@/views/ProvidingActivitiesPage.vue"),
        meta: {
          title: "Обеспечивающая деятельность",
          ico: "mdi-bulletin-board",
        },
      },
      {
        path: "/faq",
        name: "FAQPage",
        component: () => import("@/views/FAQPage.vue"),
        meta: {
          title: "Часто задаваемые вопросы",
          ico: "mdi-comment-question-outline",
        },
      },
      {
        path: "/feedback",
        name: "FeedbackPage",
        component: () => import("@/views/FeedbackPage.vue"),
        meta: {
          title: "Обратная связь",
          ico: "mdi-thumb-up-outline",
        },
      },
      {
        path: "/labor",
        name: "LaborProtection",
        component: () => import("@/views/LaborProtection.vue"),
        meta: {
          title: "Охрана труда",
          ico: "mdi-pharmacy",
        },
      },
      {
        path: "/securyty",
        name: "SecurityPage",
        component: () => import("@/views/SecurityPage.vue"),
        meta: {
          title: "Безопасность",
          ico: "mdi-security",
        },
      },
      {
        path: "/safety/:chapter",
        component: () => import("@/views/safety/ChaptersSafety.vue"),
        meta: {
          title: "Разделы безопасности",
          ico: "mdi-fire-extinguisher",
        },
      },
      {
        path: "/inspection",
        name: "AboutInspectionPage",
        component: () => import("@/views/AboutInspectionPage.vue"),
        meta: {
          title: "Об инспекции",
          ico: "mdi-city",
        },
      },
      {
        path: "/portal",
        name: "AboutPortalPage",
        component: () => import("@/views/AboutPortalPage.vue"),
        meta: {
          title: "О портале",
          ico: "mdi-information-variant",
          requiresAuth: true,
        },
      },
      {
        path: "/news",
        name: "AboutNewsPage",
        component: () => import("@/views/NewsPage.vue"),
        meta: {
          title: "Лента новостей",
          ico: "mdi-newspaper",
        },
      },
      {
        path: "/newsfull",
        name: "FullNewsPage",
        component: () => import("@/components/news-full.vue"),
        meta: {
          title: "Одна новость",
          ico: "mdi-newspaper",
        },
      },

      {
        path: "/fnshol",
        name: "FnsHol.vue",
        component: () => import("@/views/FnsHol.vue"),
        meta: {
          title: "К празднику",
          ico: "mdi-city",
        },
      },
      {
        path: "/ical",
        name: "Calendar",
        component: () =>
          import("@/components/calendar_of_events/BigCalendar.vue"),
        meta: {
          title: "Календарь",
          ico: "mdi-account",
        },
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});


function isSuperuser() {
  const accountStore = useAccountStore();

  if (accountStore.user.is_superuser === false) {
    return true;
  } else {
    return false;
  }
}

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && isSuperuser()) {
    document.title = to.meta.title;
    next("/");
  } else {
    document.title = to.meta.title;
    next();
  }
});

export default router;
