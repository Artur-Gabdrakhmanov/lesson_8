from selene import have
from selene.support.shared import browser

from demoqa_tests.model.controls import dropdown, radio, checkboxes, datepicker
from demoqa_tests.utils import path_to_file


def open():
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.7)"')

def input_info(*, name, surname, email, mobile, address):
    browser.element('#firstName').type(name)
    browser.element('#lastName').type(surname)
    browser.element('#userEmail').type(email)
    browser.element('#userNumber').type(mobile)
    browser.element('#currentAddress').type(address)


def select_gender(gender):
    radio.select_by_value(browser.all('[name=gender]'), gender)


def select_birthday(*, month, year, day):
    browser.element('#dateOfBirthInput').click()
    datepicker.select_date(month, year, day)


def input_subject(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def select_hobbies(*texts):
    checkboxes.select(browser.all('[for^=hobbies-checkbox]'), *texts)


def upload_picture(path_to_picture):
    path_to_file.create_path('#uploadPicture', path_to_picture)


def select_state(value):
    dropdown.select('#state', by_text=value)


def select_city(value):
    dropdown.select('#city', by_text=value)


def submit():
    browser.element('#submit').press_enter()


def assert_of_registered_user(*args):
    browser.element('.table').all('td').even.should(have.texts(args))
