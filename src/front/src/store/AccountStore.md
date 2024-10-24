# useAccountStore
Хранилище для хранения информации о пользователе

#### Строка импорта:
```
import {useAccountStore} from '@/store/AccountStore'

```

#### Переменная в setup:
```
const accountStore = useAccountStore()
```

#### Переменная AppStore
Использует переменную loading из import {useAppStore} from '@/store/app.js'. loading- Для вызова скелетов или обозначения загрузки сайта

#### Переменная user
Объект, который содержит всю информацию по пользователю, находящейся в таблице DictEmployee

>birthdate: "1991-03-19 00:00:00"
datebegin: null
dateend: null
deleted: 0
deleteddate: null
department: "Отдел контроля технологических процессов"
email: "i.grishina.r9966@tax.gov.ru"
familyname: "Гришина"
fio: "Гришина Ирина Сергеевна"
id: 22
id_dict_department: 4
id_dict_position: 4
iptel: "-"
is_active: true
is_changed: 0
is_curator: 0
is_responsible: 0
is_staff: true
login: "9966-00-107"
name: "Ирина"
parentname: "Сергеевна"
password: null
photo: "https://pixelbox.ru/wp-content/uploads/2021/11/avatar-whatsapp-pixelbox.ru-36.jpg"
post: "Старший специалист 1 разряда"
room: "8.12"
tel: "-"
workstatus: null
workstatus2: "True"

#### Переменная cod2user
boolean значение, показывает принадлоежность пользователя к инспекции, или позицианирует как гость

#### Функция setUser 
Принимает параметр value (данные о пользователе, где выполняет функцию замены изображения photo, на фотографию сотрудника) и присвает новое значение в переменную user

#### Функция logging
При входе на сайт, получение токена иполучение информации по пользователю

#### Функция logging
При входе на сайт, получение токена иполучение информации по пользователю

#### Функция logout
Удаление данных из локального хранища о пользователе

#### watch следить за статусом пользователя
Меняет информацию о cod2user
