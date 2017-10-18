from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

#open csv file
file = open(os.path.expanduser(r"~/Desktop/Agoda Reviews.csv"), "wb")
file.write(
    b"Review,Rating Date,Rating  " + b"\n")

#extract agoda and insert to database
def agoda():
    browser = webdriver.Chrome()
    browser.get('https://www.agoda.com/taal-vista-hotel/hotel/tagaytay-ph.html#REVIEWS')

    time.sleep(20)

    count = 0
    while True:
        #######################################
        ####### EXTRACT DATA FROM AGODA #######
        #######################################
        helpcountarray = ""

        for profile in browser.find_elements_by_xpath("//*[@data-type='comment']"):
            image = profile.text.replace("\n", "|||||").strip()
            if image.find("helpful vote") > 0:
                counter = image.split("helpful vote", 1)[0].split("|", 1)[1][-4:].replace("|", "").strip()
                if len(helpcountarray) == 0:
                    helpcountarray = [counter]
                else:
                    helpcountarray.append(counter)
            elif image.find("helpful vote") < 0:
                if len(helpcountarray) == 0:
                    helpcountarray = ["0"]
                else:
                    helpcountarray.append("0")

        Review_element = browser.find_elements_by_xpath("//*[@data-type='comment']")
        Rating_date_element = browser.find_elements_by_xpath("//*[@class='Review-statusBar-date ']")
        Rating_element = browser.find_elements_by_xpath("//*[@class='Review-comment-score']")

        Review = []
        Rating_date = []
        Rating = []

        for x in range(0, len(helpcountarray)):
            Review.append(Review_element[x].text.replace(',', ' ').replace('"', '').replace('"', '').replace('"', '').replace('\n', ' ').strip())
            Rating.append(Rating_element[x].text.replace('.','').strip())
            Rating_date.append(Rating_date_element[x].text.replace('Reviewed', ' ').replace('NEW',' ').replace(',', ' ').strip())

            #print at cmd
            print(Review[count] + Rating[count] + Rating_date[count])

            #write into csv file
            Record = Review[count] + "," + Rating_date[count] + "," + Rating[count]
            file.write(bytes(Record, encoding="ascii", errors='ignore')  + b"\n")

            count = count + 1

        count = 0
        link = browser.find_elements_by_xpath("//*[@class='Review-paginator-number ']")
        if link == "148":
            break
        else:

            time.sleep(20)
            NextButton = browser.find_element_by_xpath("//*[@class='ficon ficon-24 ficon-carrouselarrow-right']")
            NextButton.click()

            time.sleep(20)

if __name__ == "__main__":
  agoda()
