# useMainmenuStore
Хранилище для выстраивания списка в меню, содержащие ссылки на внешние ресурсы

#### Строка импорта:
```
import { useMainmenuStore } from '@/store/MainmenuStore'

```

#### Переменная в setup:
```
const mainmenuStore = useMainmenuStore()
```

#### Переменная portallinks:
Массив с объектами содержащие данные по странице
пример
> {id: 1, name: 'mdi', link: 'https://materialdesignicons.com/cdn/1.6.50-dev/', imagecode: 'mdi-panda', order: 1}