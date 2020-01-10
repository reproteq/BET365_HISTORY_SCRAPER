### requerimets  pip install python-dateutil

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from pages import *
from options import *
import json
import io
import os
global now_dir

now_dir = os.getcwd() # get directorio actual

def main():
    logo = ban()
    print 'Cargando interface Selenium' , G ,'Ok!', W
    print 'Cargando GeckoDriver Firefox ' , G ,'Ok!', W
    binary = FirefoxBinary()
    driver = webdriver.Firefox(firefox_binary=binary)

    driver.set_window_position(800, 100)
    driver.set_window_size(800, 800)

    #driver.get("https://www.bet365.com/?lng=1&cb=10326429708#/HO/")
    driver.get("https://www.bet365.es/#/HO/")
    
    #comento esta funcion
    #landing_page = LandingPage(driver)
    #landing_page.go_to_main_page()

    main_page = MainPage(driver)
    
    print 'Funcion Login ' , O ,'Run Python Script ...', G, 'OK!',W
    main_page.login()

    #driver.get("https://members.bet365.com/MEMBERS/History/SportsHistory/HistorySearch/?BetStatus=0&SearchScope=2&platform=Desktop")
    driver.get("https://members.bet365.es/members/services/host?Microsite=Members&MrsReq=True&DisplayMode=Desktop&prdid=1&lng=3&mh=2&ptqs=%2Fhe%2FAuthenticated%2F%3Fmh%3D1%26prdid%3D1%26pid%3D8020%26cnt%3DSports%252fHome%26isb%3D0%26hostedBy%3DMEMBERS_HOST")
    
    popup_window = PopupWindow(driver)


    bets_last_two_days = popup_window.get_bet_history()

    bets_last_six_months = popup_window.get_bets_from_last_six_months()

    all_bets_from_last_six_months = bets_last_two_days + bets_last_six_months

    output = {
        'bets': []
    }

    output['bets'] = all_bets_from_last_six_months
    print 'Guardando Json', G , 'Ok!', W
    with io.open('bets.json', 'w', encoding="utf-8") as f:
        f.write(unicode(json.dumps(output, ensure_ascii=False)))


if __name__ == '__main__':
    main()
