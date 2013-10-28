#coding=utf-8
import sys, os, time, re
import urllib, urllib2, cookielib

class LoginDouBan:
    
    def __init__(self, email, pwd):
        
        self._login_url = 'http://www.douban.com/accounts/login'
        self._email = email
        self._pwd = pwd
        self._reg_imgurl = '<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>'
        self._reg_hid_val = '<input type="hidden" name="captcha-id" value="(.+?)"/>'
        
        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(self.opener)
        self.douban_url = "http://www.douban.com/"
    
    def login_params(self, vcode, catcha_id):
        params = {"form_email":self._email,"form_password":self._pwd,"source":"index_nav",
                  "captcha-solution" : vcode, "captcha-id" : catcha_id, "user_login" : "login"}
        return params
    
    def reg_imgurl(self):
        return self._reg_imgurl
    
    def reg_hidval(self):
        return self._reg_hid_val
    
    def login_url(self):
        return self._login_url

    def validate_image(self, url):
        reg_iu = self.reg_imgurl()
        html = self.opener.open(url).read()
        imgurl_match = re.search(reg_iu, html)
        if imgurl_match:
            url = imgurl_match.group(1)
            urllib.urlretrieve(url, 'v_pic.jpg') #download the validate pic
        return html
        
    def login(self):
        rh = self.reg_hidval()
        lurl = self.login_url()
        
        html = self.validate_image(lurl)
        captcha_match = re.search(rh, html)
        vcode = raw_input('put the validate code : '.encode('utf-8'))
        lp = self.login_params(vcode, captcha_match.group(1))
        response = urllib2.urlopen(lurl, urllib.urlencode(lp))
        
        if response.geturl() == self.douban_url:
            f = open("login.html", "w")
            f.write(response.read())
            f.close()
            print 'ok'
            
    def contact_list(self):
        response = urllib2.urlopen("http://www.douban.com/contacts/list")
        fobj = open("contactlist.html", "w")
        fobj.write(response.read())
        fobj.close()

def test_attribute(ldb):
    print ldb.reg_imgurl()
    print ldb.reg_hidval()
    print ldb.login_url()
    ldb.login()
    ldb.contact_list()

if __name__ == '__main__':
    e = ""
    p = ""
    ldb = LoginDouBan(e,p)
    test_attribute(ldb) 
    
    
