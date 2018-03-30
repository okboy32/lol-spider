#encoding:utf-8
#created time : 2018/3/30 20:33
#designed by zl

import seleniumer,htmloutputer,urlmanager

class LolSpider():
    def __init__(self):
        print('init html lolspider')
        self.seleniumer = seleniumer.Seleniumer()
        self.urlManager = urlmanager.UrlManager()
        self.htmlOutputer = htmloutputer.HtmlOutputer()

    def craw(self,root_url):
        #获取英雄url列表
        herolist = self.seleniumer.open_root_url(root_url)
        self.urlManager.seturl(herolist)
        f = open('counter.txt', 'r')
        count = int(f.read()) #当前在抓取的几个
        if count != 0:

            self.urlManager.reseturl(count)

        f.close()
        while self.urlManager.is_have_data():
            count += 1

            #获取一个英雄 详细信息的 url
            data = self.urlManager.geturl()
            heroname = data['heroname']
            print('%d. %s' % (count, data['heroname']))


            #获取英雄信息
            info = self.seleniumer.get_hero_info(data['heroinfo_url'])

            if self.htmlOutputer.output(info,heroname):
                print('图片下载完成 [ %s ] '% ( heroname, ))

            #counter
            f = open('counter.txt','w')
            print(count)
            f.write(str(count))
            f.close()

if __name__ == '__main__':
    root_url = 'http://lol.qq.com/web201310/info-heros.shtml'
    lolspider = LolSpider()
    lolspider.craw(root_url)