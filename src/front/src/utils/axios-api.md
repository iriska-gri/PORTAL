# Axios-api
Файл хранения настроек соединения с бэком и связанных с ними переменных
## Осуществленик запросов на бэк.
Пример использования защищенного запроса:
### GET
```
axiosApiInstance.get('api/')
            .then(data => {            


            })

```
### POST
```
 axiosApiInstance.post(`api/`, data).then(result => { 
                
            })

```

### Открытое соединение
Только определенные страницы. Для авторизации.
clearAxios

#### Строка импорта:
```
import { clearAxios } from '@/utils/axios-api'
```

### Соединение с использованием Токена
Используется для всех запросов
axiosApiInstance

#### Строка импорта:

```
import { axiosApiInstance } from '@/utils/axios-api'

```


### Соединение по Вебсокету
Используется для непрерывных соединений WS 

#### Строка импорта 
```
import { baseWS } from '@/utils/axios-api'
```
#### Пример использования:
```
const connect = new WebSocket(baseWS+"ws/watcher/?token="+localStorage.access)
```

## Переменные

### spravURL
URL хранения фотографий сотрудников в справочнике


### baseURL
Настраиваемый URL Соединения с сервером для Axios


### baseWS

Смотри "Соединение по вебсокету" выше
