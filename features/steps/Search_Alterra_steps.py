from selenium import webdriver
from behave import *


@given('I go to Google.com')
def go_to_google(context):
    context.helperfunc.open('https://google.com')


@when('I type Alterra on Google search bar')
def type_to_seach_bar(context):
    context.helperfunc.find_by_name('q').send_keys('Alterra')


@when('I hit Google Search button')
def click_search_button(context):
    context.helperfunc.find_by_name('btnK').click()


@then('I should have information regarding "{title}"')
def search_result_google(context, title):
    context.helperfunc.title(title)

@given('I go to DuckDuckGo.com')
def go_to_google(context):
    context.helperfunc.open('https://duckduckgo.com')

@when('I type Alterra on DuckDuckGo search bar')
def type_to_seach_bar(context):
    context.helperfunc.find_by_id('search_form_input_homepage').send_keys('Alterra')

@when('I hit DuckDuckGo Search button')
def click_search_button_duck(context):
    context.helperfunc.find_by_id('search_button_homepage').click()