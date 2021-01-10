import setting

class ApiPay:
    def __init__(self):
        self.url = setting.JUMP_URL

    def pay(self,session):
        # 对302接口禁止重定向 allow_redirects=False
        resp = session.get(self.url,allow_redirects=False)
        # 提取响应头中的location,对location后面的地址发起请求，
        # 然后获取响应，以便testcase中做断言
        resp_pay = session.get(resp.headers['location'])
        return resp_pay
