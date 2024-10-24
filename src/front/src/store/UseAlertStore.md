# useAlertStore
Хранилище для компонента
src/layouts/default/alertDefault.vue

#### Строка импорта:
```
import { useAlertStore } from '@/store/useAlertStore'

```

#### Переменная в setup:
```
const feedalert = useAlertStore().alert
```

#### Переменная alert содержит ключи:
|Ключ|Тип|Значение по умолчанию|Описание|
|-|--------|--------|--------|
|alert|boolean|false|Запуск/скрытие отоборажения на экране|
|text|string|''|Тект, который будет отображаться в алерте|
|ico|string|'mdi-plus'|Замена иконки, отображаемой слева от текста|
|color|string|''|Замена цвета|
