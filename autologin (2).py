import requests
url = "http://172.17.0.2:801/eportal"
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip,deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    
    'Host':'172.17.0.2:801',
    'Referer':'http://172.17.0.2/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

data = {
     
    'c': 'ACSetting',
    'a': 'Login',
    'loginMethod': '1',
    'protocol': 'http:',
    'hostname': '172.17.0.2',
    
    'iTermType': '1',
   
    'wlanacname': 'ME60-1',
   
    'vlanid': '0',
    
    'ip': '172.18.17.23',
    'enAdvert': '0',
    'jsVersion': '2.4.3',
    'DDDDD': ',0,这里填写账号',   //0代表电脑端 1代表手机、ipad端
    'upass': '这里填写密码',
    'R1': '0',      //r1r2r3 应该是选择登录的渠道 校园网 移动联通电信 自己可以测试  0为校园网
    'R2': '0',
    'R3': '0',
    'R6': '0',
    'para': '00',
    '0MKKey': '123456',
   
 }


reditList = r.history

str_reditList=",".join(map(str,reditList))




if "<Response [302]>" in str_reditList:

    print("您已联网！")

input('源码简单！交流请联系QQ48846004！程序执行成功，按任意键退出：')





