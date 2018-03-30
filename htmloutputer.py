#encoding:utf-8
#created time : 2018/3/29 20:34
#designed by zl

from urllib import request
import os


class HtmlOutputer(object):
    def __init__(self):
        print('init html outputer')


    def output(self, info,name):
        path = r'./lol/ %s' % name

        #download 皮肤图片
        for skin_dic in info['skin_info']:
            skin_name = skin_dic['skin_name']
            skinNAV =  skin_dic['skinNAV']
            skinBG_url = skin_dic['skinBG_url']

            self.img_download(path, skinNAV, skin_name + '_Nav.jpg')
            self.img_download(path, skinBG_url, skin_name + '_BG.jpg', )

        #download
        index = 0
        for skill_dic in info['skill']:
            skill_name = skill_dic['skillname']
            skill_active = skill_dic['skillactive']
            skill_tip = skill_dic['skill_tip']
            skillNAV_url = skill_dic['skillNAV_url']

            self.img_download(path,skillNAV_url,'%d.' % index + skill_name + '.png')

            line_num = len(skill_tip) // 20

            str = skill_tip
            skill_tip = ''
            for line in range(line_num):
                skill_tip = skill_tip + str[line * 20 :(line + 1) * 20] + '\n'

            data = skill_name + " " + skill_active + '\n' + skill_tip
            self.write2txt('%d.' % index + skill_name + '.txt',path,data)
            index += 1

        story = info['background_story']
        self.write2txt(name + '.txt',path,story)

    def img_download(self,path,url,name):
        if not os.path.exists(path):
            os.makedirs(path)
        try:
            request.urlretrieve(url,path + r'/'+ name)
        except :
            f = open('error-log.txt','w')
            f.write(r'404 - [%s]' %(url))

    def write2txt(self,name,path,data):
        if not os.path.exists(path):
            os.makedirs(path)
        try:
            f = open(path + r'/' +name,'a')
            f.write(data)
            f.close()
        except :
            f = open('error-log.txt','w')
            f.write(r'write false [ %s - %s ]' %(name,data))
            f.close()