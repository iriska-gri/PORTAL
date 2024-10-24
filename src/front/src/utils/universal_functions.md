# Универсальные функции
Содержит в себе часто использумые однотивные функции

> import {} from '@/utils/universal_functions'

#### formatComa - DD.MM.YYYY, formatDash - YYYY-MM-DD, formaComaTime - DD.MM.YYYY H:mm изменять формат времени

Принимает параметр date? в формате new Date()
Пример
> Tue Mar 12 2024 00:00:00 GMT+0300 (Москва, стандартное время)

#### checking_for_entry добавляет в массив уникальные данные 

Принимает параметры 
where - массив который нужно проверять
what - данные которые нужно добавлять

#### getfromserver использует соединение с токеном
path - url путь
reactive - переменная в которую передать данные
Пример 
> getfromserver("api/navigation/carousels/", carous)

#### getfromserverfree использует соединение без токена
path - url путь
reactive - переменная в которую передать данные

#### checkremote 
Проверка статуса проекта, если в разработке, использовать заглушку для фоторафии
Параметры:
filecheck- название картинки в БД
Пример - `${spravURL}${userlinks.login}.jpg`

import { spravURL } from '@/utils/axios-api'
userlinks.login - 9966-00-107

#### splitname возвращает фамилию с инициалами

Параметр принимает объект

 {"familyname": "Гришина",
 "name": "Ирина",
 "parentname": "Сергеевна",
 "id": 107,
 "login": "9966-00-107",
 "post": "Старший специалист 1 разряда",
 "department": "Отдел контроля технологических процессов" }
 Данный пример объекта содержит большее количество данных, главное чтобы были ключи **familyname**, **name**, **parentname**

#### pagecounter
Cчетчик для страницы

Записывает данные посещений на страницу

переменная router - предоставляет метаданные о странице, используя
import { useRouter } from 'vue-router'

accountStore - информация о пользователе из DictEmployee
appStore - данные о посещенных страницах

postdata - объект для записи информации о странице из бд  по умолчанию данные подгружаются из router и пользователе из стора

#### getDevelopment
Возвращает true если в разработке and false если на сервере запускается