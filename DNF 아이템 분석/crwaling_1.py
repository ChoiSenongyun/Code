import numpy as np
import pprint
from selenium import webdriver
import time

pp=pprint.PrettyPrinter(indent=4)

user_list=[]
driver = webdriver.Chrome("./chromedriver")
for i in range(500):
    print(i)
    driver.get("https://dundam.xyz/damage_ranking?page="+str(i+1)+"&type=7&job=%E7%9C%9E%20%EB%B9%99%EA%B2%B0%EC"
                                                                  "%82%AC&baseJob=%EB%A7%88%EB%B2%95%EC%82%AC(%EB%82"
                                                                  "%A8)&weaponType=%EC%A0%84%EC%B2%B4&weaponDetail=%"
                                                                  "EC%A0%84%EC%B2%B4")
    time.sleep(1)
    for j in range(10):
        name=driver.find_element_by_xpath('//*[@id="ranking"]/div[2]/div[5]/div[2]/div[2]/div['+str(j+1)+']/div[2]/span[2]')
        server=driver.find_element_by_xpath('//*[@id="ranking"]/div[2]/div[5]/div[2]/div[2]/div['+str(j+1)+']/div[2]/div/div[2]/div/span')
        damage=driver.find_element_by_xpath('//*[@id="ranking"]/div[2]/div[5]/div[2]/div[2]/div['+str(j+1)+']/div[3]/span[2]')
        user_list.append([str(name.text),str(server.text),str(damage.text).replace(",","")])
user_list=np.array(user_list)
np.savetxt('userlist.csv', user_list,delimiter=",",fmt="%s")