#django_files
django站点管理，使用admin上传文件，包括本地默认模式、分布式fastdfs和阿里云的oss

##如何使用
  1、拉取代码后，直接运行测试
  python manage.py runserver
  
  2、测试时打开站点管理
  http:127.0.0.1:8000/admin
  默认账户：admin
  密码：123456
  或者你可以重新创建管理员账户
  
  3、文件重写了两个类，一个是fasdfs和oss，两者都需要继承django的Storage
    其中FastDFS需要修改client.conf中的ip地址
    oss的需要在配置文件中填写自己的appid和appsecret……等等
 ##更新   
