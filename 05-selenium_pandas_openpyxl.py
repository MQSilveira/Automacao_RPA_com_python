from selenium import webdriver as opcSelenium
from selenium.webdriver.common.by import By

# Seleciona o navegador 
chrome = opcSelenium.Chrome()

chrome.get('https://www.google.com/')


