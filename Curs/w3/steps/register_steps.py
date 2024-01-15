from behave import *


@given('I am on the Register Page')
def step_impl(context):
    context.register_page.navigate_to_register_page()


@when('I select the male radio button')
def step_impl(context):
    context.register_page.click_male_radio_button()


@when('I set first name as "{text}"')
def step_impl(context, text):
    context.register_page.set_first_name(text)


@when('I set last name as "{text}"')
def step_impl(context, text):
    context.register_page.set_last_name(text)


@when('I set a new email')
def step_impl(context):
    context.register_page.set_random_email()


@when('I set company name as "{text}"')
def step_impl(context, text):
    context.register_page.set_company_name(text)


@when('I select day "{text}"')
def step_impl(context, text):
    context.register_page.select_day_of_birth(text)


@when('I select month "{text}"')
def step_impl(context, text):
    context.register_page.select_month_of_birth(text)


@when('I select year "{text}"')
def step_impl(context, text):
    context.register_page.select_year_of_birth(text)


@when('I click the newsletter checkbox')
def step_impl(context):
    context.register_page.check_newsletter_checkbox()


@when('I set password as {text}')
def step_impl(context, text):
    context.register_page.set_password(text)


@when('I set confirm password as {text}')
def step_impl(context, text):
    context.register_page.set_password_confirm(text)


@when('I click on register button')
def step_impl(context):
    context.register_page.click_register_button()


@then('Success message is displayed')
def step_impl(context):
    assert context.register_page.is_success_message_displayed()
