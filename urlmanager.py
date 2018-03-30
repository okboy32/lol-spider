#encoding:utf-8
#created time : 2018/3/30 20:34
#designed by zl

class UrlManager(object):

    def __init__(self):
        self.hero_data = []
        self.imgurl = []

    def seturl(self, herolist):
        if len(herolist) == 0:
            return
        else:
            self.hero_data += herolist

    def is_have_data(self):
        return len(self.hero_data)

    def geturl(self):
        return self.hero_data.pop()

    def setimgurl(self, info):
        pass


    def reseturl(self, count):
        self.hero_data = self.hero_data[:-count]
