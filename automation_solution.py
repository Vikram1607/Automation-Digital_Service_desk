from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from googletrans import Translator
import time
trans=Translator()
driver = webdriver.Firefox()
driver.get("http://cyber.freshservice.com")
time.sleep(3)
assert "cyber" in driver.title
#clicks sign_in button
elem = driver.find_element_by_xpath("//a[contains(@class,'portal-signin uppercase')]")
elem.click()
time.sleep(3)
#clicks login button
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/section/div[1]/a/button")
elem.click()
time.sleep(3)
#points the email_id textbox
elem = driver.find_element_by_xpath("//input[contains(@name,'email')]")
elem.clear()
#enters the mail id
elem.send_keys("m.vikram1607@gmail.com")
elem = driver.find_element_by_xpath("//input[contains(@type,'password')]")
elem.clear()
#enters the password
elem.send_keys("freshservice")
elem.send_keys(Keys.RETURN)
time.sleep(3)
i=1
while i>0:   
    time.sleep(5) 
    elem= driver.find_element_by_xpath("//a[@data-keybinding='g t']")
    elem.click()
    time.sleep(3)
    try:
        
        view=driver.find_element_by_class_name("list-noinfo")
        view.click()
        time.sleep(3)
        print("All tickets are closed")
    except:    
        #clicks the subject of the recently received ticket
        time.sleep(3)
        elem  = driver.find_element_by_class_name("ticket-info")
        elem.click()
        time.sleep(3)
        #finds the subject of the ticket
        elem = driver.find_element_by_xpath("//h2[contains(@class,'subject ')]")
        elem.click()
        #gets and prints the subject
        sub = elem.text
        print(sub)
        time.sleep(3)
        #Subject to be translated to english
        totrans=trans.translate(sub,dest='en')
        print("Translated-text --->"+totrans.text)
        #storing the source language in "SRCLAN"
        srclan=totrans.src
        #storing the translated text to "ENSUB"
        ensub=totrans.text
        time.sleep(3)
        #Redirected to Solution Categories page
        driver.get("https://cyber.freshservice.com/solution/categories")
        time.sleep(3)
        #Search the solutions available
        elem = driver.find_element_by_xpath("//input[contains(@class,'search')]")
        elem.send_keys(ensub)
        time.sleep(3)
        try:
            resfound = driver.find_element_by_xpath("//li[contains(.,'No results found')]")
            res=resfound.text
            time.sleep(3)
            if res=="No results found" :
                    #Clicks the ticket icon
                    elem = driver.find_element_by_xpath("//a[@data-keybinding='g t']")
                    elem.click()
                    time.sleep(3)
                    tick=driver.find_element_by_id("ids_")
                    tick.click()
                    time.sleep(3)
                    assto=driver.find_element_by_xpath("//button[@class='btn dialog2'][contains(.,'Assign to Agent')]")
                    assto.click()
                    time.sleep(3)
                    grpclk=driver.find_element_by_xpath("//a[@class='btn btn-primary'][contains(.,'Assign')]")
                    grpclk.click()
                    time.sleep(3)
        except:
            #clicks the searched content
            elem = driver.find_element_by_xpath("//a[@class='search-title']")
            elem.click()
            time.sleep(3)
            #clicks the edit button
            elem = driver.find_element_by_xpath("//a[@class='btn small'][contains(.,'Edit')]")
            elem.click()
            #selects the solution
            elem = driver.find_element_by_xpath("//div[@class='redactor_editor']")
            #Stores the solution in "SOL"
            sol=elem.text
            print("Required solution------>"+sol)
            #Translates to Native Language
            soltrans=trans.translate(sol,srclan)
            print("Translated-text --->" +soltrans.text)
            #Native Language in "SOLTRANSTXT"
            soltranstxt=soltrans.text
            #clicks the ticket button
            time.sleep(3)
            elem = driver.find_element_by_xpath("//a[@data-keybinding='g t']")
            elem.click()
            time.sleep(3)
            #clicks the mail 
            elem  = driver.find_element_by_class_name("ticket-info")
            elem.click()
            time.sleep(3)
            #clicks the reply button
            elem = driver.find_element_by_xpath("//a[contains(@class,'ficon-reply')]")
            elem.click()
            time.sleep(3)
            #points the search box
            elem = driver.find_element_by_xpath("//div[contains(@class,'redactor_editor')]")
            elem.clear()
            elem.send_keys(soltranstxt)
            time.sleep(3)
            #Reply Button
            elem  = driver.find_element_by_xpath("//*[@id='reply_dialog']")
            elem.click()
            time.sleep(3)
            #clicks the closed button 
            elem = driver.find_element_by_xpath("//a[contains(.,'Send and set as Closed')]")
            elem.click()
            time.sleep(3)
            #Dashboard
            elem = driver.find_element_by_xpath("//a[contains(@data-keybinding,'g d')]")
            elem.click()
            time.sleep(3)
            assert "No results found." not in driver.page_source
            time.sleep(3)
    i=i+1    
driver.close()