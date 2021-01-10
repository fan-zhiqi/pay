'''
登录请求的信息
'''
from setting import IP, HEADERS
from tools.logger import GetLogger
logger = GetLogger().get_logger()
class ApiLogin:
    def __init__(self):
        '''
        记录日志信息的时候，不用逗号拼接，推荐用format和%s
        '''
        logger.info('开始获取login的url地址:')
        self.url = IP + '/mtx/index.php?s=/index/user/login.html'
        logger.info('login的url地址是{}'.format(self.url))


    def login(self,session,data):
        '''
        对登录接口进行自动化测试
        :data  请求参数(post,get) 场景:1参数化  业务层传递     2验证这个功能,直接写死就可以了
        :return:
        '''
        # 发起请求
        logger.info('准备发起login的请求，请求的参数是{},header是{}'.format(data, HEADERS))
        resp_login=session.post(self.url,data=data,headers=HEADERS)
        logger.info('获取的响应值是%s'% resp_login)
        return resp_login



    def login_success(self,session):
        '''
        跟其他接口进行关联的，发起成功的登录请求
        :return:
        '''
        logger.info('准备发起成功的login的请求:')
        data = {'accounts': 'yaoyao','pwd':'yaoyao'}
        logger.info('成功的请求的data数据是{}'.format(data))
        resp_login = session.post(self.url, data=data, headers=HEADERS)
        logger.info('成功的请求的响应值是{}'.format(resp_login))
        return resp_login