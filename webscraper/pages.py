from base import Page
from locators import *
from time import sleep
from datetime import date
from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.keys import Keys
from options import *

#clase desactivada ttcode
class LandingPage(Page):
    def go_to_main_page(self):
        #self.driver.find_element(*LandingPageLocators.ENGLISH).click()
        self.driver.find_element(*LandingPageLocators.SPANISH).click()


class MainPage(Page):
    print 'In Main Page'
    
    def enter_username(self, name):
        Page.wait_for_element(self, *MainPageLocators.USERNAME_INPUT)

        self.clear_username()
        self.driver.find_element(
            *MainPageLocators.USERNAME_INPUT).send_keys(name)
        print "username input" ,G , username, W
    
    def clear_username(self):
        self.driver.find_element(
            *MainPageLocators.USERNAME_INPUT).clear()
        print "clear pass input" ,G , 'OK', W

    def enter_password(self, name):
        Page.wait_for_element(self, *MainPageLocators.PASSWORD_INPUT)
        self.driver.execute_script(MainPageLocators.PASSWORD_INPUT_REVEAL)
        self.driver.find_element(*MainPageLocators.PASSWORD_INPUT).click()
        print "pass input" ,G , password, W


    def click_login(self):
        self.driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        print 'Login button send Click ', G, 'OK!', W

    #ttcode df close popop mensajes
    #def clicK_popmng(self):
       # print 'df cerrar msg'
        
    #ttcode df click desplegable user    
    def click_members_info_button(self):
        self.driver.find_element(*MainPageLocators.MEMBERS_INFO_BUTTON).click()
        print 'Info user button send Click ', G, 'OK!', W        
        
        
        
    def click_members_link(self):
        Page.wait_for_element(self, *MainPageLocators.MEMBERS_LINK)
        self.driver.find_element(*MainPageLocators.MEMBERS_LINK).click()
        print 'Link Member Click', G, 'OK!',W
        
        print P, (self.driver.current_url) , W
        
        
        
    def click_members_link_historial(self):
        
        self.driver.find_element(*MainPageLocators.MEMBERS_LINK_HISTORIAL).click()
        print 'Link Member Historial Click', G, 'OK!',W
        
        print P, (self.driver.current_url) , W        



    def login(self):
        self.enter_username(username)
        print 'username ', G , username , W
        sleep(2)
        self.enter_password(password)
        print 'password ', G , password , W
        sleep(2)
        self.click_login()
        print "Funcion clik Login", O, "....",W
        sleep(2)
        
        #ttcode add df memeber info button
        self.click_members_info_button()
        print "Funcion clik member info button", O, "....",W
        sleep(2)
        
        # df member link 
        Page.wait_for_element(self, *MainPageLocators.MEMBERS_LINK)
        self.click_members_link()
        #print MEMBERS_LINK
        print "Funcion clik Member Link" , G, "OK",W
        
        #
        self.click_members_link_historial()
        print 'click historial function'
 
    print 'End Main Page'        
        
        

class PopupWindow(Page):
    print 'In class popup page'
    
    def create_date_string(self, mon, day):
        date_string = self.get_date(mon, day)
        return self.format_date_string(date_string)

    def format_date_string(self, date_str):
        d = date_str.day
        m = date_str.month
        y = date_str.year

        d = self.prefix_zeroes(d)
        m = self.prefix_zeroes(m)

        return str(d) + "/" + str(m) + "/" + str(y)

    def prefix_zeroes(self, num):
        return num if num > 10 else "0" + str(num)

    def get_date(self, month, day):
        return date.today() + relativedelta(months=-month, days=-day)
    
    
    # df historial
    def get_bet_history(self):
        Page.wait_for_element(self, *PopUpWindowLocators.SHOW_MORE_BTN)
        self.click_show_more_until_no_more()

        sleep(2)

        Page.wait_for_element(self, *PopUpWindowLocators.BET_CONFIRMATION)
        bets = self.driver.find_elements(
            *PopUpWindowLocators.BET_CONFIRMATION_LINK)

        return self.get_bet_details(bets)

    def click_show_more_until_no_more(self):
        while(self.is_show_more_present()):
            try:
                Page.wait_for_element(self, *PopUpWindowLocators.SHOW_MORE_BTN)
                self.show_more()
            except Exception as e:
                print(e)
                break
            finally:
                pass

    def is_show_more_present(self):
        return self.driver.find_element(*PopUpWindowLocators
                                        .SHOW_MORE_BTN).is_displayed()

    def get_bet_details(self, bets):
        self.bets = []

        Page.wait_for_element(self, *PopUpWindowLocators.BET_CONFIRMATION)

        bet_confirmation = self.driver.find_elements(
            *PopUpWindowLocators.BET_CONFIRMATION)

        Page.wait_for_element(self, *PopUpWindowLocators.BET_RETURN)

        stakes = self.driver.find_elements(*PopUpWindowLocators.BET_STAKE)
        returns = self.driver.find_elements(
            *PopUpWindowLocators.BET_RETURN)

        for index, bet in enumerate(bets):

            try:
                self.bet_obj = {}

                self.bet_obj['bet_stake'] = stakes[index].text
                self.bet_obj['bet_return'] = returns[index].text

                bet.click()

                Page.wait_for_element(
                    self, *PopUpWindowLocators.BET_CONFIRMATION)
                Page.wait_for_element(self, *PopUpWindowLocators.BET_TYPE)
                sleep(1)

                self.bet_obj['bet_type'] = bet_confirmation[index].find_element(
                    *PopUpWindowLocators.BET_TYPE).text

                self.bet_obj['bet_event'] = bet_confirmation[index].find_element(
                    *PopUpWindowLocators.BET_EVENT).text

                self.bet_obj['bet_date'] = bet_confirmation[index].find_element(
                    *PopUpWindowLocators.BET_DATE).text

                self.bet_obj['bet_odds'] = bet_confirmation[index].find_element(
                    *PopUpWindowLocators.BET_ODDS).text

                self.bet_obj['bet_result'] = bet_confirmation[index].find_element(
                    *PopUpWindowLocators.BET_RESULT).text

                self.bet_obj['bet_id'] = bet_confirmation[index].find_element(
                    *PopUpWindowLocators.BET_ID).text
            except Exception as e:
                pass
            finally:
                pass

            self.bets.append(self.bet_obj)

            bet.click()

        return self.bets

    def get_list_of_bets(self):
        self.switch_to_bet_history_iframe()
        bets = self.driver.find_elements(*PopUpWindowLocators.BET_ITEMS)

        for bet in bets:
            self.driver.switch_to_window()
            bet.send_keys(Keys.ENTER)
            if(bet.is_displayed and bet.is_enabled):
                bet.click()
                Page.wait_for_element(
                    self, *PopUpWindowLocators.BET_CONFIRMATION)

    def switch_to_bet_history_iframe(self):
        self.driver.switch_to_frame(
            self.driver.find_element(By.ID, "historyV3Iframe"))

    def show_more(self):
        self.driver.find_element(*PopUpWindowLocators.SHOW_MORE_BTN).click()

    def get_bets_from_last_six_months(self):
        date_six_months_ago = self.create_date_string(6, 0)
        date_two_days_ago = self.create_date_string(0, 2)
     #  url ="https://members.bet365.es/members/services/host?Microsite=Members&MrsReq=True&DisplayMode=Desktop&prdid=1&lng=3&mh=2&ptqs=%2Fhe%2FAuthenticated%2FHistory%2FDisplay%2F%3Fsdate%3D02%2F01%2F2020%26edate%3D08%2F01%2F2020%26rt%3D3%26ht%3D4"
        url = "https://members.bet365.com/MEMBERS/History/SportsHistory/HistorySearch/?BetStatus=0&SearchScope=3&datefrom=" + \
            date_six_months_ago + "%2000:00:00&dateto=" + \
            date_two_days_ago + "%2023:59:59&platform=Desktop"
        url ="https://members.bet365.es/members/services/host?Microsite=Members&MrsReq=True&DisplayMode=Desktop&prdid=1&lng=3&mh=2&ptqs=%2Fhe%2FAuthenticated%2FHistory%2FDisplay%2F%3Fsdate%3D02%2F01%2F2020%26edate%3D08%2F01%2F2020%26rt%3D3%26ht%3D4"

        self.driver.get(url)
        return self.get_bet_history()
    
    print 'END class popup page'