# useAppStore
Хранилище для подсчета посещенных страниц пользователями 

#### Строка импорта:
```
import {useAppStore} from '@/store/app'
```

#### Переменная в setup:
```
const AppStore= useAppStore()
```
#### Переменная loading
Для вызова скелетов или обозначения загрузки сайта
const loading = ref(false)

#### Переменная countvisitor содержит ключи:

totalvisit - сколько страницу посетили с первой записи в базу данных
visittoday - сколько посещений было в течение сегодняшнего дня
uniqtoday - сколько уникальных пользователей песетило страницу
visitdate - дата перво записи, по умолчанию '2024-01-01'
