# Спецификация организации проекта Vue
Инструменты разработки
* Vscode
Инструмент проверки кода
* ESLint



## Спецификации разработки
### 1 Соглашения об именах для папок, файлов и компонентов
1. Для компонентов используем соглашение об именах (PascalCase), начинающееся с заглавных букв.
2. В дочерние компоненты, жестко привязанным к родителю, добавляем вперед название родительского компонента (РодительДочерний)
3. Для  не являющихся компонентами, используем  kebab-case, начинающиеся с строчных букв (если не получается обойтись одним словом).

### 2 Формат файла UTF-8

### 3 Требования к названиям: 

1. Стараемся избегать использования непонятного в названиях и используем  английские слова, передающие смысл. Пишем правильно (если что, онлайн-переводчик не сложно запустить)
2. Внутри методов допустимо использовать переменные, не несущие в своем названии смысла (arr, ob)  для перебора какого-то массива или объекта, но на коротких дистанциях. НЕ совсем правильно, но удобно.

3. Названия для переменных
    * Верблюжий регистр, начиная с типа данных в нижнем регистре
    * Тип числа начинается с n,
      - [x] строка - **s**,
      - [x]   логический - **b**,
      - [x]   объект - **o**,
      - [x]   массив - **a**.
        
        Например: nAge = 29, sName = "Jone".

###   4. Название функции
 * Верблюжий регистр, соглашение об именах первой буквы в нижнем регистре
 * По типу операции + объекту операции
 Типы операций следующие:
    - [x] add (добавить), 
    - [x] change/edit/set (изменить),
    - [x] del (удалить),
    - [x] get (получить),
    - [x] search/find/filter (поиск),
     - [x] load (загрузка)
    - [x] check (проверка),
    - [x] reset (сброс)

### 4. Спецификация структуры файла VUE:
1. Порядок оформления: 
  * template
  * script
  * style
2. PROPS должны быть подробно определены:
    
``` 
    props: {
      sStatus: {
       type: String,
       required: true,
       defaut:""
       }
       }
```
    
3. Характеристики функциональных элементов:
 * Элементы с несколькими атрибутами записываем в несколько строк, по одной строке для каждого атрибута. (чтобы облегчить чтение)
       
```
        <my-component
        :data="data"
        :class="name"
        @click="..."
        ....
        ...
        ...
        .........
        >   
```

        ! Если атрибутов немного и это не мешает чтению, допускается писать и в строку - 
### 5. Спецификация комментариев.  
Заполняем комментарий в следующих случаях:
* Инструкции по использованию компонентов и функций
* Описание важных/сложных функций функций 
* Больше комментариев - лучше для понимания.


### 6. Дополнительно
* Стараемся держать код в чистоте 
  - неиспользуемого быть не должно
  - не забываем проверять свой код на console.log перед отправкой на слияние веток
  - Экономим теги, будто их мало и редко выдают на отдел небольшими порциями.






    