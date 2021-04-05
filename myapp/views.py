from django.shortcuts import render,HttpResponse
from .models import Test,OSS
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#django自带的上传文件路径
def test11(req):
    try:
        obj = Test.objects.filter(name='test1').first()
    except Exception as e:
        print(e)
    return render(req,'test.html',{'data':obj.files})

'''
文件上传分两种方式：
    A：如果不涉及到管理后台上传文件，则直接在视图中完成响应功能即可。
       1、接收用户上传的图片
       2、为图片改名，可以使用用户id+固定字符串作为图片文件名上传（user_img_01）
       3、将图片上传至oss，同时将图片url地址写入数据库中
       4、用户访问图片时，直接在视图中取出数据库中的url地址，拼接成真实地址返回
    
    B：涉及到管理后台上传图片：
        1、因为django admin中上传文件默认是存储到filesystem类中自定义的存储路径，如果想将文件上传至fastdfs、oss、七牛云
        则需要重写filesystem类中的_open和_save方法，url也要重写。
        2、还需要在url路由中定义图片的地址
       
'''
#使用阿里云的oss上传文件
@csrf_exempt
def oss(req):

    if req.method == 'GET':
        try:
            obj = Test.objects.filter(name='test3').first()
        except Exception as e:
            print(e)
        img_url = obj.files
        print(img_url)
        return render(req,'oss.html')


