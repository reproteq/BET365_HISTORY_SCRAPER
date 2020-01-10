from selenium.webdriver.common.by import By
from options import *

class LandingPageLocators(object):
    #ENGLISH = (By.LINK_TEXT, "English")
    SPANISH = (By.LINK_TEXT, "Spanish")

class MainPageLocators(object):
    USERNAME_INPUT = (
        By.XPATH, "//div[contains(@class, 'hm-Login_UserNameWrapper')]/input")
    PASSWORD_INPUT = (
        By.XPATH, "//div[contains(@class, 'hm-Login_PasswordWrapper')]/input")
    LOGIN_BUTTON = (By.CLASS_NAME, "hm-Login_LoginBtn")
    
    
    #PASSWORD_INPUT_REVEAL = "document.getElementsByClassName('hm-Login_InputField')[2].value = '';"
    PASSWORD_INPUT_REVEAL = "document.getElementsByClassName('hm-Login_InputField')[2].value = '"+ password +"';"
    
    #MEMBERS_LINK = (By.CLASS_NAME, "hm-MembersInfo_UserLink")
    # class="hm-MembersInfoButton_AccountIcon " button user
    # class="hm-MembersInfoContainer Hidden "
    # class="hm-MembersInfoGeneral_Link "  Historial
    
    
    #ttcode add locator class buton member
    MEMBERS_INFO_BUTTON = (By.CLASS_NAME, "hm-MembersInfoButton_AccountIcon")
    print 'user button press ok'
    
    
   # MEMBERS_LINK = "document.getElementsByClassName('MembersInfoGeneral_Link')[3].value = 'Historial';"
    #print 'member link ok'     
    
    MEMBERS_LINK = (By.CLASS_NAME, "hm-MembersInfoGeneral_Link")
    print 'member link ok'    
    
    # class="members-menuItem_Link selected_MenuItem_TextColor members-menuItem_HighlightedLink"
    MEMBERS_LINK_HISTORIAL ="document.getElementsByClassName('MembersInfoGeneral_Link')[3].value = 'Historial';"
    #MEMBERS_LINK_HISTORIAL = (By.CLASS_NAME, "members-menuItem_Link")
    print 'member link historial ok'    
    print MEMBERS_LINK_HISTORIAL
        
    

class PopUpWindowLocators(object):
    print 'PopUP '
    HISTORY = (By.ID, "TopMenuNew_lnk15")
    BETTYPE_DROPDOWN = (
        By.ID, 'ctl00_main_SportsHistorySearchControl_ddlHistType')
    SETTLED_BETS = "Settled Sports Bets"

    BET_CONFIRMATION_LINK = (
        By.CLASS_NAME, "bet-summary-bet-confirmation-stake")
    BET_CONFIRMATION = (By.CLASS_NAME, "bet-confirmation")
    BET_SUMMARY_BODY_ROW = (By.CLASS_NAME, "bet-summary-body-row")
    BET_TYPE = (By.CLASS_NAME, "bet-confirmation-table-body-selections")
    BET_EVENT = (By.CLASS_NAME, "bet-confirmation-table-body-event")
    BET_DATE = (By.CLASS_NAME, "bet-confirmation-table-body-eventdate")
    BET_ODDS = (By.CLASS_NAME, "bet-confirmation-table-body-odds")
    BET_RESULT = (By.CLASS_NAME, "bet-confirmation-table-body-result")
    BET_ID = (By.CLASS_NAME, "bet-confirmation-details-ref")
    BET_STAKE = (By.CLASS_NAME, "bet-summary-total-stake")
    BET_RETURN = (By.CLASS_NAME, "bet-summary-return")

    FROM_RADIOBUTTON = (
        By.ID, 'ctl00_main_SportsHistorySearchControl_dateSearchControl_rdbFrom')
    DATE_FROM_INPUT = (
        By.ID, 'ctl00_main_SportsHistorySearchControl_dateSearchControl_txtFromDate')
    SEARCH_HISTORY_BUTTON = (
        By.ID, 'ctl00_main_SportsHistorySearchControl_dateSearchControl_lkGo')
    BET_ITEMS = (By.CLASS_NAME, 'bet-summary-bet-confirmation-link')
    BET_DETAILS = (
        By.CLASS_NAME, 'bet-confirmation-details')
    BET_RESULT = (
        By.CLASS_NAME, 'bet-confirmation-table-body-result')
    BET_CONFIRMATION_TABLE = (By.CLASS_NAME, 'bet-confirmation-table')
    SHOW_MORE_BTN = (By.ID, 'bet365-show-more-button')
