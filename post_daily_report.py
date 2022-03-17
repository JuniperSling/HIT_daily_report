import requests
cookie = "JSESSIONID=ABCDEFGHIJKLMNHIJK"  # 在这里填写你的登陆Cookie

def get_token():
        url = "https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xs/getToken"
        head = {"Host": "xg.hit.edu.cn", "Origin": "https://xg.hit.edu.cn", "Accept-Encoding": "gzip, deflate, br",
                "Cookie": cookie, "Content-Length": "0", "Connection": "keep-alive",
                "Accept": "*/*", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/HuaWei-AnyOffice/2.6.1802.0010/cn.edu.hit.welink",
                "Referer": "https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsMrsbNew/edit", "Accept-Language": "zh-cn", "X-Requested-With": "XMLHttpRequest"}
        res = requests.post(url=url, headers=head)
        print("Token:" + res.text)
        return res.text

def post(token):
        url = "https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsMrsbNew/save"
        head = {"Host": "xg.hit.edu.cn", "Accept": "application/json, text/javascript, */*; q=0.01",
                "X-Requested-With": "XMLHttpRequest", "Accept-Language": "zh-cn",
                "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "https://xg.hit.edu.cn",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/HuaWei-AnyOffice/2.6.1802.0010/cn.edu.hit.welink",
                "Connection": "keep-alive", "Referer": "https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsMrsbNew/edit", "Content-Length": "1432",
                "Cookie": cookie}
        # 最大尝试次数5次
        for i in range(0, 5):
                rdata = {"info": "{\"model\":{\"gpsjd\":126.636165,\"gpswd\":45.744048,\"jzdz\":\"\",\"kzl1\":\"1\",\"kzl2\":\"\",\"kzl3\":\"\",\"kzl4\":\"\",\"kzl5\":\"\",\"kzl6\":\"黑龙江省\",\"kzl7\":\"哈尔滨市\",\"kzl8\":\"南岗区\",\"kzl9\":\"教化街11号\",\"kzl10\":\"黑龙江省哈尔滨市南岗区教化街11号\",\"kzl11\":\"\",\"kzl12\":\"\",\"kzl13\":\"0\",\"kzl14\":\"\",\"kzl15\":\"0\",\"kzl16\":\"\",\"kzl17\":\"1\",\"kzl18\":\"0;\",\"kzl19\":\"\",\"kzl20\":\"\",\"kzl21\":\"\",\"kzl22\":\"\",\"kzl23\":\"0\",\"kzl24\":\"0\",\"kzl25\":\"\",\"kzl26\":\"\",\"kzl27\":\"\",\"kzl28\":\"0\",\"kzl29\":\"\",\"kzl30\":\"\",\"kzl31\":\"\",\"kzl32\":\"2\",\"kzl33\":\"\",\"kzl34\":{},\"kzl38\":\"黑龙江省\",\"kzl39\":\"哈尔滨市\",\"kzl40\":\"南岗区\",\"kzl41\":\"0\",\"kzl42\":\"\"},\"token\": %s}" % token}
                res = requests.post(url=url, headers=head, data=rdata)
                if res.text.find("true") == 13:
                        return 1
                else:
                        token = get_token()
        return 0


if __name__ == '__main__':
        token = get_token()
        flag = post(token)
        if flag:
                print("上报成功！")
        else:
                print("上报失败！")
