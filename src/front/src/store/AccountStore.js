// Utilities
import { defineStore } from "pinia";
import { ref, watch, computed } from "vue";
import { clearAxios, spravURL } from "@/utils/axios-api";
import VueJwtDecode from "vue-jwt-decode";
import { checkremote } from "@/utils/universal_functions";
import { useAppStore } from "@/store/app.js";

export const useAccountStore = defineStore("AccountStore", () => {
  const AppStore = useAppStore();
  const user = ref(getuserFromStorage());






  const settingsStorage = computed({
    get() {
      if (Object.keys(user.value).length==0){
        getuserFromStorage()
      }
      return JSON.parse(localStorage.getItem(user.value.is_idEmployee));
    },
  });

  const defaultSettings = {
    calendar: [],
  };

  function get_setting(key) {
    console.log(settingsStorage.value);
    return settingsStorage.value === null? defaultSettings[key]: settingsStorage.value[key];
  }
  
  const cod2user = ref(false);
  const calendar = ref(get_setting("calendar")
  );
  console.log(calendar.value, 'calval');

  const setUser = (value) => {
    value.photo = checkremote(`${spravURL}${value.login}.jpg`);
    user.value = value;
  };

  //
  // геттер бывший
  // const getUser=computed(()=> uyser.value)
  function getuserFromStorage(){
    try{
    let u = VueJwtDecode.decode(localStorage.getItem("refresh"));
    u.user.photo = checkremote(`${spravURL}${u.user.login}.jpg`);   
    return u.user;
    }catch{
    return {}}
  }
  const logging = async (anon) => {
    AppStore.loading = true;
    const result = await clearAxios.post("api/accounts/token/", anon);
   
    localStorage.setItem("access", result.data.access);
    localStorage.setItem("refresh", result.data.refresh);
    user.value=getuserFromStorage()
   
    if (settingsStorage.value === null) {
      settingsUp(defaultSettings)
    }
  
    AppStore.loading = false;
  };

 

  const logout = () => {
    user.value = {};
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    
  };
  watch(
    user,
    (newValue, oldValue) => {
      cod2user.value =
        "login" in newValue && newValue.login.startsWith("9966-")
          ? true
          : false;
    },
    { deep: true }
  );

 function settingsUp(newSet) {

    localStorage.setItem(user.value.is_idEmployee, JSON.stringify(newSet)
      
    );
   
  }



  watch(() => calendar.value, (newValue) => {
    
    let settings = JSON.parse(localStorage.getItem(user.value.is_idEmployee))
    settings.calendar = newValue

    settingsUp(settings)
   
  }, {deep: true})

  return { user, setUser, cod2user, logging, logout, calendar,getuserFromStorage };
});
