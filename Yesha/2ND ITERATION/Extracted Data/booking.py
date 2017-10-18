from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

#open csv file
file = open(os.path.expanduser(r"~/Desktop/Booking Reviews.csv"), "wb")
file.write(
    b"Review,Rating Date,Rating,Sentiment,Site  " + b"\n")


#extract booking and insert to database
def booking():
    browser = webdriver.Chrome()
    browser.get('https://www.booking.com/hotel/ph/taal-vista.en-gb.html#tab-reviews')

    try:
        WebDriverWait(browser, 50).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='review-policy__header-group']")))
    except TimeoutException:
        print("Timed out! Waiting for page to load")
        browser.quit()

    count = 0
    #for 11 reviews at first page
    range_num = 11
    time.sleep(10)
    while True:
        #######################################
        ###### EXTRACT DATA FROM BOOKING ######
        #######################################
        Review_element_neg = browser.find_elements_by_xpath("//*[@class='review_neg']")
        Review_element_pos = browser.find_elements_by_xpath("//*[@class='review_pos']")
        Rating_date_element = browser.find_elements_by_xpath("//*[@class='review_item_date']")
        Rating_element = browser.find_elements_by_xpath("//*[@class='review-score-badge']")

        Review = []
        Review2 = []
        Rating_date = []
        Rating = []

        for x in range(range_num):

            Review.append(Review_element_neg[x].text.replace(',', ' ').replace('눉', '').replace('"', '').replace('"', '').replace('"', '').replace('\n', ' ').strip())
            Rating.append(Rating_element[x].text.replace('.','').strip())
            Rating_date.append(Rating_date_element[x].text.replace('Reviewed', ' ').replace('NEW',' ').replace(',', ' ').strip())

            #print at cmd NEGATIVE
            print(Review[count] + " : " + Rating[count] + " : " + Rating_date[count] + " : " + "neg" + " : " + "booking")

            #write into csv file
            Record = Review[count] + "," + Rating_date[count] + "," + Rating[count] + "," + "neg" + "," + "booking"
            file.write(bytes(Record, encoding="ascii", errors='ignore') + b"\n")

            Review2.append(Review_element_pos[x].text.replace(',', ' ').replace('눇', '').replace('"', '').replace('"', '').replace('"', '').replace('\n', ' ').strip())

            #print at cmd POSITIVE
            print(Review2[count] + " : " + Rating[count] + " : " + Rating_date[count] + " : " + "pos" + " : " + "booking")

            #write into csv file
            Record = Review2[count] + "," + Rating_date[count] + "," + Rating[count] + "," + "pos" + "," + "booking"
            file.write(bytes(Record, encoding="ascii", errors='ignore')  + b"\n")

            count = count + 1

        count = 0
        range_num = 10
        link = browser.find_elements_by_xpath("//*[@data-selenium='reviews-next-page-link']")
        if link == False:
            break
        else:
            time.sleep(5)
            NextButton = browser.find_element_by_css_selector("a#review_next_page_link")
            NextButton.click()

            time.sleep(10)

if __name__ == "__main__":
  booking()
