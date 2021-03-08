import datetime
import hashlib
import base64
import json
import requests  # 发送http/https请求

"""
容联云短信业务

account sid: 8a216da877bef0fe0177f77e088b153b
auth token: beb969e265e44ed89c5839dff19841b2
appid: 8a216da877bef0fe0177f77e09591541
Base URL：https://app.cloopen.com:8883

Accept:application/json;
Content-Type:application/xml;charset=utf-8;
Content-Length:256; 
Authorization:

"""


class YunTongXin():
    base_url = 'https://app.cloopen.com:8883'
    def __init__(self, accountSid, accountToken, appId, templateId):
        self.accountSid = accountSid
        self.accountToken = accountToken
        self.appId = appId
        self.templateId = templateId

    # 1 构造url(基础url + 业务url )
    def get_request_url(self, sig):
        # /2013-12-26/Accounts/{accountSid}/SMS/{funcdes}?sig={SigParameter}
        self.url = self.base_url + '/2013-12-26/Accounts/%s/SMS/TemplateSMS?sig=%s' % (self.accountSid,sig)
        return self.url

        # 生成时间戳字符串
    def get_timestamp(self):
        now = datetime.datetime.now()
        now_str = now.strftime('%Y%m%d%H%M%S')
        return now_str

        # 生成sig
    def get_sig(self, timestamp):
        # 使用MD5加密（账户Id + 账户授权令牌 + 时间戳
        s = self.accountSid + self.accountToken + timestamp
        md5 = hashlib.md5()
        md5.update(s.encode())
        return md5.hexdigest().upper()

    # 2 请求包头
    def get_request_header(self, timestamp):
        s = self.accountSid + ":" + timestamp
        b_s = base64.b64encode(s.encode())
        b_s = b_s.decode()
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset=utf-8',
            'Authorization': b_s,
        }

    # 3 构造请求包body
    def get_request_body(self, phone, code):
        return {
            'to': phone,
            'appId': self.appId,
            'templateId': self.templateId,
            # code是验证码，3是有效期
            'datas': [code, '3']
        }

    # 4 发送请求
    def do_request(self, url, header, body):
        res = requests.post(url, headers=header, data=json.dumps(body))
        return res.text

    # 5 封装上述的四个步骤
    def run(self,phone,code):
        timestamp=self.get_timestamp()
        sig =self.get_sig(timestamp)

        # 1 url
        url=self.get_request_url(sig)
        # 2 header
        header =self.get_request_header(timestamp)
        # 3 body
        body=self.get_request_body(phone,code)
        # 4 send request
        res =self.do_request(url,header,body)
        return res



#测试代码
if __name__ == '__main__':
    aid='8a216da877bef0fe0177f77e088b153b'
    atoken='beb969e265e44ed89c5839dff19841b2'
    appid='8a216da877bef0fe0177f77e09591541'
    tid='1'

    x = YunTongXin(aid,atoken,appid,tid)

    res=x.run('15200536624','你好呀！李默默！')
    print(res)