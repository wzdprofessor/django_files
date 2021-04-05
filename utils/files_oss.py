from django.core.files.storage import Storage
from django.conf import settings

import oss2

class Oss(Storage):

    # 这个是上传图片后阿里云返回的uri需要拼接下面这个url才可以访问，根据自己情况去写这步
    '''
    AccessKeyId = ''
    AccessKeySecret = ''
    endpoint = 'https://oss-cn-beijing.aliyuncs.com'
    OSS_BASE_URL = ''
    namespace = ''
    '''
    def __init__(self, base_url=None):
        auth = oss2.Auth(settings.AccessKeyId, settings.AccessKeySecret)
        endpoint = settings.endpoint
        buket_name = settings.buket_name
        self.bucket = oss2.Bucket(auth, endpoint, buket_name)  # 项目名称

        """初始化"""
        if base_url is None:
            base_url = settings.OSS_BASE_URL
        self.base_url = base_url

    def _open(self, name, mode='rb'):
        # 打开文件时使用
        pass

    def _save(self, name, content):
        print(name)
        print(self.base_url)
        # 保存文件时使用
        # name: 保存文件名字
        # content: 包含上传文件内容的File对象
        #文件名字要加上前缀
        file_name = self.base_url+name

        #指定存储的文件到test目录
        res = self.bucket.put_object('test/'+name, content)
        # 如果上传状态是200 代表成功 返回文件外网访问路径
        # 下面代码根据自己的需求写
        if res.status == 200:
            return file_name
        else:
            return False

    def exists(self, name):
        """Django判断文件名是否可用"""
        return False

    def url(self, name):
        """返回访问文件url路径"""
        return self.base_url + name
