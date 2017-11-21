import csv

data = csv.reader(open('C:/Users/Yesha/website/booking_reviews.csv'), delimiter=",")

def jan():
    Month = "Jan"
    Year = "2017"
    count_month = 0
    count = 0

    monthly = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    while True:
        for row in data:
            if row[2] == monthly[count]:
                if row[4] == "2017":
                    if row[6] == "pos":
                        count = count + 1
                        if count == 11:
                            break

        Sentiment = "pos"

        print(Month + " " + Year + " " + Sentiment + " " + str(count))

if __name__ == "__main__":
  jan()