from rest_framework.generics import ListAPIView
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from datetime import date, datetime, timedelta
from django.db.models import Sum, Q, Avg, F
from userauth.models import *
from feedback.models import *
from feedback.serializers import *


class Counter(ListAPIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        """Не используется"""
        return Response('Не используется')

    def post(self, request):
        """
        Представление получает информацию о ссылке на страницу, и производит создание
        или перезапись существующей страницы в таблицу, для того чтобы
        проследить на каких страницах был пользователь в конкретный день.
        {totalvisit: 10539, visittoday: 21, uniqtoday: 1, visitdate: '2023-12-21'}
        Мы получаем информацию о том сколько всего раз была посещена страница
        с момента первой записи в бд, сколько было сегодня людей и сколько уникальных, 
        """
        
        myfullPath = request.data['fullPath']

        if "?" in myfullPath:
            myfullPath= myfullPath.split("?")[0]

        page, create = Pages.objects.get_or_create(page=request.data['page'],
                                                   fullPath=myfullPath,
                                                   ico=request.data['ico'])

        if request.data['user__id'] is not None:
            watch, create = CountVisitor.objects.get_or_create(user = User(id = request.data['user__id']),
                                                               pages = page,
                                                               visitdate = date.today()
                                                               )
            
        watch.count += 1
        watch.save()

        datavisit = CountVisitor.objects.filter(pages = page.id).earliest('visitdate')
        
        res = {"totalvisit": CountVisitor.objects.filter(pages=page.id).aggregate(Sum('count'))['count__sum'],
            "visittoday":CountVisitor.objects.filter(visitdate=date.today(), pages=page.id).aggregate(Sum('count'))['count__sum'],
            "uniqtoday" : CountVisitor.objects.filter(visitdate=date.today(), pages=page.id).count(),
            "visitdate" : VisitdateSerializer(datavisit).data['visitdate']
        }
        
        return Response(res)
    
class SelectedLinksAPIView(ListAPIView):
    """Получаем массив объектов
    {pages__page: 'О портале', pages__fullPath: '/portal', pages__ico: 'mdi-information-variant', count__sum: 9827}
    Чтобы вывести на главной странице часто посещаемые страницы, ограничение 20 шт.
    """
    def get(self, request):
        user = User.objects.get(username=self.request.user)
        res = CountVisitor.objects.values('pages__page','pages__fullPath','pages__ico').filter(user_id=user).annotate(Sum('count')).exclude(pages__fullPath='/')
        sort = res.order_by('-count__sum')[:20]

        return Response(sort)
    
class DataForStatisticsAPIView(ListAPIView):
    """
    Принимает два параметра с фронта start=${}&end=${}
    Данные берет из фильтра и собираем всю необходимую информацию для отрисовки страницы.
    http://sulaco.nodered.ru:5223/COD2/PORTAL_COD2/issues/12 подробное описание с работой собранного объекта
    Возвращяет
    beforperiod - забирает данные за два периода назад для расчета удержания
    period - собирает информацию о пользователе, сколько раз и когда он посетил конкретную страницу
    staff - количество сотрудников на конец периода
    feedback - ключ для блока с обратной связью, он содержит:
        feed - берет все поля из модели с UserComment, и добавляет информацию об авторе
        criteria - среднее значение по критерию с иконкой и цветом
        data:
            score - оценки
                title - наименование
                all - за все время
                period - за период
            comment - комментарии
                '------'
        last_comment - дата последнего комментария
    """
    def get(self, request):

        data_start = datetime.strptime(request.GET.get("start"), "%Y-%m-%d").date()
        data_end = datetime.strptime(request.GET.get("end"), "%Y-%m-%d").date()
        data_rating = data_end + timedelta(days=1)
        beetween =  data_end - (data_start - timedelta(days=1))

        res = CountVisitor.objects.filter(visitdate__lt = request.GET.get("start"), visitdate__gte=data_start - beetween*2).distinct().values('visitdate','user__user_id')
        per = CountVisitor.objects.filter(Q(visitdate__lte = request.GET.get("end"), visitdate__gte =request.GET.get("start")) | Q(visitdate=date.today()))

        # Обратная связь
        feed = UserComment.objects.all()
        rating = RatingStatus.objects.values('crit__name', 'crit__ico', 'crit__color', 'rating').filter(usercom__time_create__range=[request.GET.get("start"), data_rating])

        d = feed.filter(time_create__range=[request.GET.get("start"), data_rating])
        return Response({
            'beforperiod': res,
            'period': PagesSerializer(per, many= True).data,
            'staff': DictEmployee.objects.filter(Q(deleteddate__isnull= True) | Q(deleteddate__gte = request.GET.get("end"))).count(),
            'feedback': {
                'feed': UserCommentSerializer(d, many=True).data,
                'criteria': list(rating.values('crit__name').annotate(ratings=Avg('rating'), name=F('crit__name'), ico=F('crit__ico'), color=F('crit__color')).values('ratings', 'name', 'ico', 'color')),
                'data': {
                    'score': {
                        'title': 'Поставлено оценок',
                        'all': feed.count(),
                        'period': feed.filter(time_create__range=[request.GET.get("start"), request.GET.get("end")]).count()
                    },
                    'comment': {
                        'title': 'Оставлено комментариев',
                        'all': feed.filter(~Q(comment='')).count(),
                        'period': feed.filter(Q(time_create__range=[request.GET.get("start"), request.GET.get("end")]) & ~Q(comment='')).count()
                    }
                },
                'last_comment': feed.values('time_create').filter(~Q(comment='')).latest('time_create'),            
            },
            
            })
       

       