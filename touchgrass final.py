# steam user ID: 76561198796244890

import selenium
import colorama
from colorama import Fore

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def timeplayed():
    """
    Function that detects time played and then determines what response is printed
    """

    driver = webdriver.Chrome()
    driver.get(f"https://steamladder.com/profile/{userID}/")

    totalplayed = driver.find_element(
        By.XPATH,
        "/html/body/div[2]/div[3]/div[4]/div/div[3]/div/table/tbody/tr[1]/td",
    ).text

    numHoursList = totalplayed.split(" ")

    trueTotal = numHoursList[0]

    # print("You have played a total of " + trueTotal + " hours on steam")

    if int(trueTotal) >= 10:
        print(
            "You have played a total of "
            + trueTotal
            + " hours across all your steam games. This is healthy"
        )
    elif int(trueTotal) >= 100:
        print(
            "You have played a total of "
            + trueTotal
            + " hours across all your steam games. You are spending to much time on steam. -100 Social credit. -100 minutes gaming time"
        )

    elif int(trueTotal) >= 200:
        print(
            "You have played a total of "
            + trueTotal
            + " hours across all your steam games. You need to seek immediate medical attention. It is advised you touch some grass"
        )
    else:
        print(
            "You have played a total of "
            + trueTotal
            + " hours across all your steam games. You need to seek immediate medical attention. It is advised you touch some grass"
        )


userID = input("[?]Enter a valid steam user ID: ")

length = len(userID)


if length == 17:
    print("Valid steam user ID")
    timeplayed()


else:
    print("Invalid Steam ID")
