# HIT_daily_report
### request POST 实现

1. 需要python环境
2. 需要导入`requests`包
   ```bash
   pip intall requests
   ```
3. 请自行使用抓包工具获取登陆`Cookie`(我使用的iOS下的`Stream`软件)
4. 将你自己的Cookie填写在`report.py`文件第二行
5. 执行.py文件即可
   ```bash
   python post_daily_report.py
> 如果遇到返回“页面不存在”，请更换网络



### selenium 实现
> Selenium实现的代码参考校友代码，在此感谢[@eagleshield]https://gitee.com/eagleshield/selenium_daily_report

1. 需要python环境

2. 需要导入`selenium`包

   ```bash
   pip intall selenium
   ```

3. 需要和Chrome浏览器版本匹配的Chromedriver程序

4. 将自己的`学号密码`和`Chromedriver路径`填写在`selenium_daily_report.py`对应的位置中

5. 执行.py文件即可

   ```bash
   python selenium_daily_report.py
   ```

   

