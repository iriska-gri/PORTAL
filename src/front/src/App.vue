<template>
  <router-view />
</template>

<script setup >
import {useAccountStore} from '@/store/AccountStore'
  const accountStore = useAccountStore()
  accountStore.setUser(accountStore.getuserFromStorage())
  
</script>
<style>


::-webkit-scrollbar {
    width: 1px;
    height: 6px;
}
/* Track */
::-webkit-scrollbar-track {
   
    -webkit-border-radius: 6px;
    border-radius: 6px;
}
/* Handle */
::-webkit-scrollbar-thumb {
    -webkit-border-radius: 6px;
    border-radius: 6px;
    background: rgb(var(--v-theme-scrollbar))
   
}
::-webkit-scrollbar-thumb:window-inactive {
    background: rgb(var(--v-theme-scrollbar)) 
}



.bggrad {
  background: linear-gradient(to top right, rgba(19,84,122,.8), rgba(128,208,199,.8));
}

.bgCard {
    /* #ffffff6b #ffffff8c*/
    background: #ffffff38 ;
}

.bgText {
    background:  #ffffffb0;
   line-height: 2.1rem!important;
 
}

.gap {
  gap: 5px;
}

.w100 {
    max-width: 100%!important
}

.bottom-alert {
  bottom: 10px;
    left: 40%;
}
</style>
