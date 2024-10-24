# Календарь событий

Пример объекта
```
const events = ref([
    {
      start: '2024-04-15 14:00',
      end: '2024-04-25 18:00',
      title: 'Need to go shopping',
      icon: 'shopping_cart', // Custom attribute.
      content: 'Click to see my shopping list',
      contentFull: 'My shopping list is rather long:<br><ul><li>Avocados</li><li>Tomatoes</li><li>Potatoes</li><li>Mangoes</li></ul>', // Custom attribute.
      class: 'leisure',
      repeat: {
        every: 'week', // You can repeat on multiple days of the week.
        until: '2024-05-30' // Don't need a time here as it will take the same as original event date.
      }
    },
    {
      start: '2024-04-15 10:00',
      end: '2024-04-25 15:00',
      title: 'Golf with John',
      icon: 'golf_course', // Custom attribute.
      content: 'Do I need to tell how many holes?',
      contentFull: 'Okay.<br>It will be a 18 hole golf course.', // Custom attribute.
      class: 'sport'
    }
    ])

```

Повторяющиеся события
Когда это будет готово, вот как это будет работать.
Вы можете повторить событие:
Каждый день - предоставляя свойство every: "день".
Каждую неделю - предоставляя каждую: "неделю" свойство.
Каждый месяц - путем предоставления каждого: свойства "месяц".
Каждый год - путем предоставления каждого: "годового" объекта недвижимости.
Для каждого конкретного дня недели - путем предоставления массива дней недели, содержащего номера дней недели (от 1 до 7 для воскресенья).
Каждые x дней - путем предоставления свойства every: x, где x является целым числом.
Навсегда; Или до истечения срока действия, если вы предоставляете свойство until: {String | Date}.
Будь то однодневный, многодневный, фоновый, на весь день, со временем или вне времени.

repeat: {
    weekdays: [1, 3], // You can repeat on multiple days of the week.
    until: '2020-11-30' // Don't need a time here as it will take the same as original event date.
  }

repeat: {
    weekdays: [5] // If original event day is not in these days, original event will still show up.
    // Without `until` property, it will go on forever.
  }

repeat: {
    every: 'week',
    until: new Date('2019/06/01') // You can also use a Javascript Date.
  }

repeat: {
    every: 14,
    until: '2019-01-20'
  }

repeat: {
    every: 'month',
    until: '2019-12-26'
  }

repeat: {
    every: 'year'
  }