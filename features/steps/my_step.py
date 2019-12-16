from app import *
from behave import *
from splinter import Browser
from expects import expect, equal, match

browser = Browser('flask', app=app)

@given(u'i enter the game')
def step_impl(context):
    browser.visit('http://localhost:5000')
    browser.find_by_tag("a").first.click() #it happens whit headless mode

@then(u'i should see "{text}"')
@given(u'i should see "{text}"')
def step_impl(context, text):
    expect(browser.html).to(match(text))
    #browser.quit() #with headless is not necessary

@when(u'i enter the number "{number}"')
def step_impl(context, number):
    browser.fill('secret_code', number)

@when(u'i save the secret')
def step_impl(context):
    browser.find_by_css('.save').first.click()

@given(u'i enter the player game with number "{number}"')
def step_impl(context, number):
    context.execute_steps(u"""
        given i enter the game
         when i enter the number "{number}"
         when i save the secret
    """.format(number=number))

@when(u'i guess with "{number}"')
@given(u'i guess with "{number}"')
def step_impl(context, number):
    browser.fill('your_guess', number)
    browser.find_by_css('.guess').first.click()

# splinter examples:
# browser.fill('q', 'splinter - python')
# button = browser.find_by_css('.lsb').first
# button.first.click()
# browser.is_text_present('http://splinter.cobrateam.info')