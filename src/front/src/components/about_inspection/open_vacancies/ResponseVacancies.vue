<template>
  <div>
    <v-card-text class="text-center">
      <span class="text-h4">Откликнуться на вакансию</span>
    </v-card-text>
    <v-card-text class="d-flex flex-column pt-0">
      <v-form ref="form_vacancies"  @submit.prevent="submit">
        <v-row no-gutters class="justify-center">
          <v-col lg="8">
            <v-text-field
              v-model="form.fio"
              :counter="10"
              :rules="rules.fio"
              label="Фамилия, имя, отчество"
            />
            <v-row no-gutters class="gap">
              <v-col>
                <v-text-field
                  v-model="form.email"
                  :rules="rules.email"
                  label="E-mail или почта Lotus"
                />
              </v-col>
              <v-col>
                <v-text-field
                  v-model="form.tel"
                  :counter="7"
                  :rules="rules.tel"
                  label="Телефон"
                />
              </v-col>
            </v-row>
            <v-textarea
              v-model="form.text"
              no-resize
              rows="4"
              label="Сопроводительное письмо"
            />
            <v-file-input label="Резюме" hide-details v-model="file" />

            <v-btn block type="submit" class="mt-4 text-none" color="btn_text">
              Отправить
            </v-btn>
          </v-col>
        </v-row>
      </v-form>
    </v-card-text>
  </div>
</template>

<script>
import { ref } from "vue";
import { useAlertStore } from "@/store/useAlertStore";
import { clearAxios } from "@/utils/axios-api";

export default {
  props: {
    idVacations: {
      type: Number,
      default: -1,
    },
  },
  setup(props) {
    const form = ref({ fio: "", email: "", tel: "", text: "" });
    const feedalert = useAlertStore().alert;

    const req = (val) => {
      return !!val || "Поле обязательно";
    };

    const rules = {
      fio: [
        (val) => req(val),
        (val) =>
          val.match(/^[а-яА-ЯЁё ]+$/) !== null || "Имя должно содержать русские буквы",
      ],
      email: [(val) => req(val)],
      tel: [
        (val) => req(val),
        (val) => val.match(/^[[\d-]*\d[\d-]*$/) !== null || "Номер должен содержать цифры",
      ],
      text: "",
    };

    const file = ref(null);
    const form_vacancies = ref(null)

    const submit = () => {

      if(form_vacancies.value.isValid) {
        
     
      const postFile = new FormData();
      postFile.append(
        "data",
        JSON.stringify({ ...form.value, vacancy_id: props.idVacations })
      );
      if (file.value !== null) {

        postFile.append("file", file.value[0]);
      }

   
      clearAxios
        .post(`api/about_inspection/postresponsevacancy/`, postFile)
        .then((data) => {
          feedalert.alert = true;
          feedalert.text = data.data;
          feedalert.color = "teal-lighten-4";
          feedalert.ico = "mdi-email-outline";
        });
      }
    };

    return {
      form,
      file,
      rules,
      submit,
      form_vacancies
    };
  },
};
</script>
