import setting
from setting import IP, HEADERS


class ApiOrder:
    def __init__(self):
        self.url = IP + '/mtx/index.php?s=/index/buy/add.html'


    def order(self,session):
        '''
        发起下订单的请求
        :param session:
        :return:
        '''
        data = {
            'goods_id': 1,
            'stock': 1,
            'buy_type': 'goods',
            'address_id': 1290,
            'payment_id': 1,
            'spec': '',

        }
        resp_order = session.post(self.url,data=data,headers=HEADERS)

        # 产生数据->并把数据放到setting当中(注意)
        setting.JUMP_URL = resp_order.json().get('data').get('jump_url')
        return resp_order
