import csv

from mainapp.parsing.pars import Parser

# data.data_lenta('https://lenta.ru/rss/news')
# data.data_rbc('http://static.feed.rbc.ru/rbc/logical/footer/news.rss')
# data.data_cnews('https://www.cnews.ru/inc/rss/news.xml')
# # #######data.data_turizm('https://www.turizm.ru/news/rss/yandex/')
# data.data_3dnews('http://3dnews.ru/news/rss/')

def csv_write():
    data = Parser()
    with open("../recommendations/data.csv", "w", encoding='utf-8-sig') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(
            (
                "title",
                "description",
                "url"
            )
        )
    data_csv = data.data_lenta('https://lenta.ru/rss/news')
    for key, value in data_csv.items():
        print(key, value)
        list_data = [key, value[1], value[0]]

        with open("../recommendations/data.csv", "a", newline="", encoding='utf-8-sig') as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(
                (
                    #f"{key},{value[1]}",
                    list_data
                )
            )
    data_csv = data.data_cnews('https://www.cnews.ru/inc/rss/news.xml')
    for key, value in data_csv.items():
        print(key, value)
        list_data = [key, value[1], value[0]]

        with open("../recommendations/data.csv", "a", newline="", encoding='utf-8-sig') as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(
                (
                    list_data
                )
            )

csv_write()