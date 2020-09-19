# -*- coding: utf-8 -*-
# @Time : 2020/7/21
# @Author : Angel
# @File : aliyunSmsSend.py

import sys
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient('这里填写你的阿里云的accessKeyId', '这里填写你的accessSecret', 'cn-hangzhou')

def smssend(phone,ip,internalIp,pcName,arch):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', "这里填写你的短信签名")
    request.add_query_param('TemplateCode', "这里填写你的短信模板")
    request.add_query_param('TemplateParam', "{\"device\":\""+ip+"\",\"code\":\""+internalIp+"\",\"num\":\""+pcName+"\",\"arch\":\""+arch+"\"}")

    response = client.do_action(request)
    # python2:  print(response)
    print(str(response))

if __name__ == '__main__':
    phones = sys.argv[1].split(",")
    externalip = str(sys.argv[2])
    internalip = str(sys.argv[3])
    pcname = str(sys.argv[4])
    arch = str(sys.argv[5])
    for phone in phones:
        print phone
        smssend(phone,externalip,internalip,pcname,arch)
