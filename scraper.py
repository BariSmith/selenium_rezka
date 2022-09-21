import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
path_driver = '/home/bari/PycharmProjects/t_rezka/chromedriver_linux'
driver = webdriver.Chrome(path_driver, options=chrome_options)
res = driver.get('https://rezka.ag/series/comedy/2040-kremnievaya-dolina-2014.html')

class Moviescrap():
    def parse(self, response):
        r = 1
        templist = []
        title = driver.find_element(By.XPATH,
                                    "/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[1]/h1").text

        driver.implicitly_wait(1)
        original_title = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[2]').text
        driver.implicitly_wait(1)
        imdb = driver.find_element(By.XPATH,
                               "/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[4]/div[2]/div/table/tbody/tr[1]/td[2]/span[1]/span").text
        driver.implicitly_wait(1)
        country = driver.find_element(By.XPATH,
                                  "/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[4]/div[2]/div/table/tbody/tr[5]/td[2]/a").text
        driver.implicitly_wait(1)
        duration = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[4]/div[2]/div/table/tbody/tr[10]/td[2]').text
        driver.implicitly_wait(1)
        description = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div[5]/div[2]').text


        scraped_dict = {
            'title': title,
            'original_title': original_title,
            'imdb': imdb,
            'country': country,
            'duration': duration,
            "description": description
            }
        templist.append(scraped_dict)
        df = pd.DataFrame(templist, columns=["title", "original_title", "imdb", "country", "duration", "description"])
        df.to_csv("Rezka.csv", index=False)


def main():
    try:
        driver.implicitly_wait(2)
        Moviescrap().parse(res)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    main()
