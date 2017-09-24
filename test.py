#!/usr/bin/python

from selenium import webdriver


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://stxnext.com/")
