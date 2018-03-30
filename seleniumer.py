#encoding:utf-8
#created time : 2018/3/30 20:34
#designed by zl

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
class Seleniumer(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_root_url(self,root_url):
        d = self.driver
        d.get(root_url)

        d.refresh()

        jSearchHeroDiv = d.find_element_by_id('jSearchHeroDiv')

        heroitems = jSearchHeroDiv.find_elements_by_tag_name("li")

        herolist=[]
        for item in heroitems:
            heronameitem = item.find_element_by_tag_name('a')
            heroname = heronameitem.get_attribute("title")
            heroinfo_url = heronameitem.get_attribute("href")
            img_url = heronameitem.find_elements_by_tag_name('img')[0].get_attribute("src")
            herodic = { 'heroinfo_url':heroinfo_url,'heroname':heroname,'img_url':img_url }
            #print(herodic)
            herolist.append(herodic)


        return herolist

    def get_hero_info(self,infourl):
        d = self.driver
        d.get(infourl)
        info = {}
        d.refresh()


        #皮肤
        time.sleep(5)


        #点击第二个皮肤小图
        d.find_element_by_css_selector(r'#skinNAV > li:nth-child(2) > a').click()

        #等待加载
        locator = (By.CSS_SELECTOR, r'#skinBG > li:nth-child(1)')

        WebDriverWait(d, 20).until(EC.presence_of_element_located(locator))

        # 查找显示皮肤大图的dom
        skinBG_item = d.find_element_by_css_selector('#skinBG')

        #查找全部大图li
        skinBG_li_items = skinBG_item.find_elements_by_tag_name('li')

        #查找缩略图的dom
        skinNAV_item = d.find_element_by_css_selector(r'#skinNAV')

        #查找全部缩略图的li
        skinNAV_li_items = skinNAV_item.find_elements_by_tag_name('li')
        skin_list = []
        for index in range(len(skinBG_li_items)):
            skinBG_li_item = skinBG_li_items[index]
            skin_name = skinBG_li_item.get_attribute('title')
            skinBG_url = skinBG_li_item.find_element_by_tag_name('img').get_attribute('src')

            skinNAV_li_item = skinNAV_li_items[index]
            skinNAV_url = skinNAV_li_item.find_element_by_tag_name('img').get_attribute('src')

            skin_dic = {'skin_name':skin_name,'skinBG_url':skinBG_url,'skinNAV':skinNAV_url}
            skin_list.append(skin_dic)
            print(skin_dic)


        #背景故事
        while 1:
            try:
                #点击背景故事中的更多按钮
                d.find_element_by_css_selector(r'#Gmore').click()
            except:
                print('没有点击更多')

            #获取背景故事
            background_story = d.find_element_by_css_selector(r'#DATAlore').text



            if background_story!= '':
                print('背景故事：' + background_story)
                break
            else:
                d.refresh()
                time.sleep(5)

        # 这个是你下拉多少像素
        d.execute_script("window.scrollBy(0,1000)")

        #技能
        # 等待加载
        locator = (By.CSS_SELECTOR, r'#DATAspellsNAV > li:nth-child(5)')

        WebDriverWait(d, 20).until(EC.presence_of_element_located(locator))

        skill_items = d.find_element_by_css_selector(r'#DATAspellsNAV').find_elements_by_tag_name('li')

        skill_info_list=[]

        for index in range(len(skill_items)):
            item = skill_items[index]

            #点击技能
            item.click()
            time.sleep(1)

            #获取技能小图
            skillNAV_url = item.find_element_by_tag_name('img').get_attribute('src')

            #获取技能名称
            skill_item = d.find_element_by_css_selector(r'#DATAspells')
            skillname = skill_item.find_element_by_tag_name('h5').text
            skillactive = skill_item.find_element_by_tag_name('em').text
            print("%s(%s),['skillNAV_url' %s]:" %(skillname,skillactive,skillNAV_url))

            #获取技能详情
            skill_tip = skill_item.find_element_by_class_name('skilltip').text
            skill_info_dict = {'skillNAV_url':skillNAV_url,'skillname':skillname,'skillactive':skillactive,'skill_tip':skill_tip}
            print(skill_tip)
            skill_info_list.append(skill_info_dict)

        hero_info_dict = {'skin_info':skin_list,'background_story':background_story,'skill':skill_info_list}

        print(hero_info_dict)

        return hero_info_dict