<template>
  <v-dialog
    v-model="menuAuthDialog"
    persistent
    width="400"
  >
    <template v-slot:activator="{ props }">
      <v-btn
        v-bind="props"
        append-icon="mdi-login"
        color="black_and_white"
      >
        <template v-slot:prepend>
          <v-icon color="black_and_white"></v-icon>
        </template>
          Войти
        <template v-slot:append>
          <v-icon color="black_and_white"/>
        </template>
      </v-btn>
    </template>
      
    <v-card @keyup.enter="logging">
      <v-card-title>
        <span class="text-h5">Вход в портал</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12" class="py-0">
              <v-text-field
                v-model="anon.username"
               
                label="Логин"
                variant="underlined"
                :error-messages="errorer('username')"
              />
            </v-col>
            <v-col cols="12" class="py-0">
              <v-text-field
          
                :type="eyeshow ? 'text' : 'password'"
                v-model="anon.password"
                label="Пароль"
                variant="underlined"
               
                :error-messages="errorer('password')"
                @click:append-inner="eyeshow= !eyeshow"
              >
              <template v-slot:append-inner>
                <v-icon size="x-small" :icon="eyeshow ? 'mdi-eye' : 'mdi-eye-off'" @click="eyeshow= !eyeshow">
                </v-icon>
              </template>

              </v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
      <v-spacer/>
        <v-btn
          color="modal_btn"
          variant="text"
          @click="menuAuthDialog = false"
        >
          Отмена
        </v-btn>
        <v-btn
          color="modal_btn"
          variant="text"
          @click="logging"
          
        >
          Войти

        </v-btn>
      </v-card-actions>

      <v-progress-linear location="bottom" v-show="AppStore.loading && !alert" absolute indeterminate></v-progress-linear>
    
    </v-card>
    <v-alert
                width = "400"
                position="fixed"
                class="bottom-alertauth bgerroralert"
             
                type="error"
                density="compact"
                title="Ошибка авторизации"
                :text="info"
                v-model="alert"
                
               
                closable
            >
            <template v-slot:prepend>
              <v-icon icon="mdi-alert-outline" class="pt-1"/>
            </template>
          </v-alert>
  </v-dialog>

  
</template>

<script>
import {useAccountStore} from '@/store/AccountStore'
import {useAppStore} from '@/store/app'
import { useVuelidate } from '@vuelidate/core'
import { required, helpers } from '@vuelidate/validators'
import { ref, reactive, computed, onMounted } from 'vue'

const req= helpers.withMessage('Обязательное поле', required)

export default {
  
  setup(props, context){
   
    const accountStore = useAccountStore()
    const AppStore= useAppStore()
    const menuAuthDialog = ref(false)
    const err = ref('')
    const alert = ref(false)
    const eyeshow = ref(false)
    

    const anon=reactive({
      username:"9966-00-",
      password:""
    })

    const rules = computed(()=> {
      return {
      username: { req, latin: helpers.withMessage(()=> 'Логин имееет вид "0000-00-000"', (value) => /(\d{4,4}[-]\d{2,2}[-]\d{3,3})+$/.test(value.toString()))}, // Matches state.firstName
      password: { req } // Matches state.lastName
      }
    }
    )

    const v$ = useVuelidate(rules, anon)
  
    const errorer = (field) => {
      let errors = v$.value[field].$error?v$.value[field].$errors[0].$message:''
      return errors
    }

    const logging=async()=>{
          if (!v$.value.$error) {
            
            try {
              await accountStore.logging(anon)
            }
            catch {
              AppStore.loading = false
              alert.value=true
             
              err.value = 'Ошибка авторизации'
         
           
            }
              
            
          }
          else {
            console.log(true);
          }
    }
 
    onMounted(() => {
      v$.value.$validate()
    })

    return {
      accountStore,
      AppStore,
      menuAuthDialog,
      anon,
      v$,
      logging,
      errorer,
      alert,
      err,
      eyeshow
    
    }
  }
}
</script>

<style>
.bottom-alertauth {
  top: 57vh;
    /* left: 38vw; */
}

.bottom-alertauth .v-alert-title {
font-size: 1.0rem;
}
/* , rgba(163, 5, 5, 0.8) */
.bgerroralert {
  background: linear-gradient(to top right, rgba(8, 4, 6, 0.8), rgba(90, 25, 50, 0.8), rgba(133, 5, 5, 0.8), rgba(192, 70, 70, 0.8));
}
</style>