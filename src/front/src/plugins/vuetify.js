
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import { VCalendar } from 'vuetify/labs/VCalendar'

import { createVuetify } from 'vuetify'
import { ru } from 'vuetify/locale'
import { VTimePicker } from 'vuetify/labs/VTimePicker'

export default createVuetify({
  
  locale: {
    messages: { ru, },
  },
  components: {
    VCalendar,
    VTimePicker,
  },
  theme: {
    defaultTheme: 'light'
  },
  theme: {
    themes: {
      light: {
        colors: {
          lampa: '#FFFFFF',
          primary: '#1867C0',
          secondary: '#5CBBF6',
          main_theme: "#f7f7f7",
          scrollbar: '#367F8A',
          cards: '#F5F5F5',
          text_grey: '#7A7A7A', //Цвет серого текста
          text_carous: '#242424',
          navigation: '#004D40', // Цвет текста и иконок в левом навигационном меню
          black_grey: '#3C3C3C', // Цвет для карусели с цифрами в работе 
          modal_btn: '#1E88E5', // Цвет для кнопок в модальных окнах
          grey: '#7A7A7A', // Цвет иконки для отображения количества посещений
          yellow: '#F9A825', // Цвет для звездочек в обратной связи
          more_details_btn: '#01579B', // Цвет для кнопки перехода "подробнее"
          loading_avatar: '#37474F', // Цвет поля прогрузки аватара пользователя
          bg_white: '#FFFFFF', // Цвет заднего фона для комментариев
          delete_btn: '#546E7A', // Цвет для кнопки удаления
          app_bar: '#004D40', // Цвет для навигационной (аппбар) панели
          black_and_white: '#FFFFFF',
          grey_white: '#FFFFFF', // Цвет для карточек
          insert_table: '#FAFAFA',
          btn_text: '#00897B', // фигма, текст кнопки с иконкой
          select_list: '#E0EAE8',
          btn_gray: '#E0E0E0'
        },
      },
      dark: {
        colors: {
          lampa: '#000000',
          primary: '#1867C0',
          secondary: '#5CBBF6',
          main_theme: "#101311",
          scrollbar: '#367F8A',
          cards: '#F5F5F5',
          text_grey: '#7A7A7A', //Цвет серого текста
          text_carous: '#242424',
          navigation: '#FDF5E6',
          black_grey: '#3C3C3C',
          modal_btn: '#1E88E5',
          grey: '#7A7A7A',
          yellow: '#F9A825',
          more_details_btn: '#01579B',
          loading_avatar: '#37474F',
          bg_white: '#FFFFFF',
          delete_btn: '#546E7A',
          app_bar: '#212121',
          black_and_white: '#101311',
          grey_white: '#212121',
          insert_table: '#323030',
          btn_text: '#00897B',
          select_list: '#E0EAE8',
          btn_gray: '#E0E0E0'
        },
    },
      options: {
        customProperties: true
    },
    },
  },
})
