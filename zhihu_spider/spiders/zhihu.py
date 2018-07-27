# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/']
    def __init__(self,*args,**kwargs):
    	super(ZhihuSpider,self).__init__(*args,**kwargs)
    	self.xsrf = ''
    def start_request():
    	"""
    	从登录界面 获取xrsf
    	"""
    	return [Request(
    		"https://www.zhihu.com/#signin",
    		meta={'cookiejar':1},
    		callback=self.post_login
    	)]

    def post_login():
    	"""
    	模拟登录
    	解析登录界面，发送登陆表单
    	"""
    	self.xsrf = Selector(response).xpath(
    		'//input[@name="_xsrf"]/@value'
    		).extract()[0]
    	return [FormRequest(
    		'https://www.zhihu.com/login/email',
    		method = 'POST',
    		meta ={'cookiejar':response.meta['cookiejar']},
    		formdata={
    			'_xsrf':self.xsrf,
    			'email':"xxxxxxx",          #注意隐藏真实信息
    			'password':"xxxxx",         #测试登陆完成之后把真实信息改回来
    			'remember_me':'true'},      # 这个是干嘛的我也不知道，只是删了会
    			callback = self.after_login 
    		)]

    def parse(self, response):
        pass
