# alertDefault

Компонент для отображения информации о выполненном действии/оповещении/предупреждения

Импорт глобальный, прописан в src/front/src/components/UI/index.js

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
