# H1 Для отрисовки карточки, необходимы поля от пользователя

department
fio
post
email
tel
room
login

Использовать серриализатор InfoUserCardSerializer из userauth для сбора

Пример
```
class PagesSerializer(serializers.ModelSerializer):
      user = serializers.SerializerMethodField('get_user')
      pages = serializers.CharField(source='pages.page')
      fullPath = serializers.CharField(source='pages.fullPath')
      ico = serializers.CharField(source='pages.ico')

      class Meta:
            model = CountVisitor
            fields = ['user', 'pages', 'fullPath', 'ico', 'visitdate', 'count']

      def get_user(self, obj):

            return InfoUserCardSerializer(obj.user.user).data
```
`
        const basicInformation = () => [
            {title: 'Отдел:', info: department},
            {title: 'ФИО:', info: fio},
            {title: 'Должность:', info: post},
        ]

        const subInformation = () => [
            {title: 'E-mail: ', info: email},
            {title: 'Телефон: ', info: tel},
            {title: 'Комната: ', info: room},
            {title: 'Логин: ', info: login},
        ]
`
