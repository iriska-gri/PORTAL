from django.shortcuts import render
from rest_framework.generics import ListAPIView
# Create your views here.
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from userauth.models import *
from general_vacation.models import *
from django.db.models import Q, Count
from userauth.models import *
from userauth.serializers import *
from datetime import date

class LinkAPIView(ListAPIView):
    """[
    Выстраивает список в меню, ссылки на внешние ресурсы и сортируетпо заданному приоритету
  {
    "id": 1,
    "name": "mdi",
    "link": "https://materialdesignicons.com/cdn/1.6.50-dev/",
    "imagecode": "mdi-panda",
    "order": 1
  }
]
    """
    permission_classes = (AllowAny,)
    serializer_class = LinkSerializer
   

    def get(self, request):
      
        queryset = Links.objects.all().order_by('order')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class GalleryAPIView(ListAPIView):
   


    def get(self, request):
        """ Метод гет не используется"""
        return Response('result')
    
    def post(self, request):
        """ 
        Представление позволяет получить информацию: author: об авторе новости, scores: количестве поставленных лайков и кем были поставлены, comment: хранит комментарии к посту, gallery: Прикрепленные изображения к новости

        {
        "id": 9,
        "show": false,
        "showComment": false,
        "author": {
            "familyname": "Гришина",
            "name": "Ирина",
            "parentname": "Сергеевна",
            "id": 107,
            "login": "9966-00-107",
            "post": "Старший специалист 1 разряда",
            "department": "Отдел контроля технологических процессов"
        },
        "scores": [
            {
                "score": false,
                "user": "9966-00-107"
            }
        ],
        "comment": [],
        "gallery": [],
        "title": "А что это",
        "text": "",
        "cdate": "2023-12-12T13:50:53+03:00",
        "link": "/media/newsimage/2023/12/12/glaza_cr.jpg"
        }
        """
        gal = ScoreGallery.objects.filter(author=self.request.user, gallery=request.data['image'])
        if gal.exists():
            gal.delete()
        else: {
            ScoreGallery.objects.create(author=self.request.user, like=1, gallery=Gallery.objects.get(id=request.data['image']))
        }
        result = ScoreGallerySerializer(ScoreGallery.objects.filter(gallery=request.data['image']), many=True).data
      
        return Response(result)



class NewsCrossroadAPIView(ListAPIView):

    def get(self, request):
        """Получает список новостей для отображения на главной странице в разрезе 10 последних записей, и на странице новостей с пагинацией"""
        if request.GET.__contains__('id'):
    
            newsqueryset = News.objects.filter(pk=int(request.GET.get('id')))
            countpage= 0
        else:
        
            newsqueryset = News.objects.all().filter(cdate__lte=datetime.now()).order_by('-cdate')
            countpage = newsqueryset.count()
            if request.GET.get("name") == "/":
             
                newsqueryset = newsqueryset[:10]
            else:
                pagesel = int(request.GET.get("page"))*int(request.GET.get("countpage"))
               
                newsqueryset =newsqueryset[pagesel:pagesel+int(request.GET.get("countpage"))] 

        
        result = NewsSerializer(newsqueryset, many=True).data
 
 
        return Response({"result":result, "countpage": countpage})
   
    def post(self, request):
            """Производит запись или обновление информации  по поставленному лайку в новости, либо создает коментарий к посту, либо удаляет запись комментария"""
            if 'scores' in request.data:
                upd, created =  ScoreNews.objects.get_or_create(news_id=request.data['news'], author=self.request.user)

                if created or (upd.score != request.data['scores']): 
                    upd.score = request.data['scores']
                else:
                    upd.score = None

                upd.cdate=datetime.now()
                upd.save()
            
                back = [{"score":y.score, "user":y.author.username} for y in ScoreNews.objects.filter(news_id=request.data['news'])]
                
            if 'text' in request.data:
                CommentNews.objects.create(news_id=request.data['news'], author=self.request.user, text=request.data['text'])
                back = {'news': request.data['news'], 'comment': ({"text":y.text, "cdate":y.cdate, "id": y.pk,
                                                                "author":model_to_dict(y.author.user)
                                                            } for y in CommentNews.objects.filter(news_id=request.data['news']))}
            if 'delid'  in request.data:
                CommentNews.objects.filter(pk=request.data['delid']).delete()
            
                back = {'news': request.data['news'], 'comment': ({"text":y.text, "cdate":y.cdate, "id": y.pk,
                                                                "author":model_to_dict(y.author.user)
                                                            } for y in CommentNews.objects.filter(news_id=request.data['news']))}

            return Response(back)
 
class CarouselsAPIView(ListAPIView):

    """  
    Выбирает Данные из модели Carousels, у которых стоит параметр публикации, дата начала публикации меньше
    или равна сегодняшнему дню и дата окончания больше или равна сегодняшнему дню, с сортировкой по приоритету,
    с добавлением информации по дням рождениям, которые будут в текущем месяце, но не меньше сегодняшнего дня.
    К дням рождения прибавлется рандомная картинка и рандомный текст
    {
        "title": "Новость прочее",
        "text": "",
        "link": "/media/newsimage/default.jpg",
        "senders": "senderimage/dr.jpg"
    }
    """
    permission_classes = (AllowAny,)
  
   

    def get(self, request):

        queryset = Carousels.objects.filter(published=True, cdate__lte=datetime.now(), enddate__gte=datetime.now()).order_by('sender__order') 
    
        result = CarouselsSerializer(queryset, many= True).data

        manbrd =  DictEmployee.objects.filter(birthdate__month=date.today().month, birthdate__day__gte=date.today().day).order_by('birthdate__day')
        dr_img = BaseSender.objects.update_or_create(name="День рождения", defaults={'name':"День рождения"})
        mess = ''
        if len(manbrd) > 0 :
            nowday= manbrd.filter(birthdate__day=date.today().day)
            brdimage = BirthdayImage.objects.order_by("?")[:len(nowday)+1]

            try:
                allbirthday = {
                    "title":'Дни рождения',
                    "text": "В этом месяце:\n"+"\n".join([f"{x.birthdate.strftime('%d')} - {x.fio}" for x in manbrd]),
                    "link": "/media/"+str(brdimage[0].img),
                    "published": 'true',
                    "sender": BaseSenderSerializer(dr_img).data,
                    }
          
                if len(nowday) > 0 :

                    brdtext = BirthdayText.objects.order_by("?")[:len(nowday)]

                    for k in nowday:
                
                        result.append({
                            "title":'Поздравляем:',
                            "text": f"{k.fio}!"+"\n"+ f"{brdtext[0].text}",
                            "link": "/media/"+str(brdimage[0].img),
                            "published": 'true',
                            "sender": BaseSenderSerializer(dr_img).data,
                            })
       

                result.append(allbirthday)
            except:
                mess = 'Добавьте открытку в панели администратора в Таблицу - "Открытки. Изображения". Либо текст поздравления в Таблицу - "Открытки. Тексты поздравлений"'

        return Response({"result": result, "mess": mess})

class ScreensaverAPIView(ListAPIView):
    """Получаем ссылку на картинку для экрана перед входом на сайт. Выбирает все записи с месяца и дня меньше и равного текущему  и окончание больше или равному текущему дню и месяцу. Год не учитывается. Выбирается одна рандомная запись"""
    def get(self, request):
        result=''
        # print(result, "--------------------------no foto screensaver")
        # try:
        # queryset = Screensaver.objects.all()
        # queryset = Screensaver.objects.filter(cdate__month__lte = date.today().month, cdate__day__lte = date.today().day,
        #                                     enddate__month__gte=date.today().month, enddate__day__gte=date.today().day).order_by('-cdate')
        queryset = Screensaver.objects.filter(cdate__month__lte = 6, cdate__day__lte = 3,
                                    enddate__month__gte=6, enddate__day__gte=3).order_by('-cdate')
        b = Screensaver.objects.values('cdate__month', 'cdate__day', 'enddate__month', 'enddate__day')
        # result = ScreensaverSerializer(queryset, many= True).data
        print(queryset,"--------------------------no foto screensaver")
        # queryset = queryset.filter(cdate=queryset[0].cdate).order_by("?")[:1]
        
        # result = ScreensaverSerializer(queryset, many= True).data
        
        # except Exception as e:
        #     print("no foto screensaver")
        #     print (e)

        return Response(result)