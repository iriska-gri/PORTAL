<template>
  <div class="align-center d-flex flex-column py-1">
    <v-btn variant="text" v-for="x in onlineuser" :key="x" height="50">
      <v-avatar size="36px">
        <v-img :src="checkremote(`${spravURL}${x}.jpg`)" @click="whatuser(x)" />
      </v-avatar>
    </v-btn>
    <info-user-card 
      :author="author"
      :opendialog="open"
      @update:opendialog="open = $event"
    />
  </div>
</template>

<script>
import { ref, watch } from "vue";
import { baseWS } from "@/utils/axios-api";
import { useAccountStore } from "@/store/AccountStore";
import { spravURL } from "@/utils/axios-api";
import { checkremote } from "@/utils/universal_functions";
import { axiosApiInstance } from "@/utils/axios-api";

export default {
  setup() {
    const author = ref({});
    const open = ref(false);
    const wsfuncs = {
      onliner: function (data) {
        let newset = new Set(data);
        let arr = Array.from(newset);

        arr.splice(
          arr.findIndex((e) => e == accountStore.user.login),
          1
        );
        onlineuser.value = arr;
      },
    };
    const accountStore = useAccountStore();
    let onlineuser = ref([]);

    const connect = new WebSocket(
      baseWS + "ws/watcher/?token=" + localStorage.access
    );
    const whatuser = (x) => {
      open.value = true;
      axiosApiInstance
        .get(`api/accounts/getuser/?userlogin=${x}`)
        .then((data) => {
          author.value = {
            department: data.data.department,
            fio: data.data.fio,
            post: data.data.post,
            email: data.data.email,
            tel: data.data.tel,
            room: data.data.room,
            login: data.data.login,
          };
        });
    };

    connect.onmessage = (e) => {
      let data = JSON.parse(e.data);

      wsfuncs[data["message"]["action"]](data.message.data);
    };

    watch(
      () => accountStore.cod2user,
      function () {
        if (!accountStore.cod2user.value) {
          connect.close();
        }
      }
    );

    return {
      author,
      open,
      onlineuser,
      checkremote,
      spravURL,
      whatuser,
      accountStore,
    };
  },
};
</script>

<style></style>
