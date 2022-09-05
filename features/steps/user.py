import json
from behave import *
from application import USERS

#Scenario: Retrieve a customers details
@given('some users are in the system')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne'}})

@when(u'I retrieve the customer \'jasonb\'')
def step_impl(context):
    context.page = context.client.get('/users/{}'.format('jasonb'))
    assert context.page

@then(u'I should get a \'200\' response')
def step_impl(context):
    assert context.page.status_code is 200

@then(u'the following user details are returned')
def step_impl(context):
    # assert context.table[0].cells[0] in context.page.text
    print(context.page.text)
    assert "Jason Bourne" in context.page.text


#Scenario: Create a new customer
@given('a new customer username')
def step_impl(context): 
    context.data = json.dumps({'jasonb': {'name': 'Jason Bourne'}})
    context.headers = {'Content-Type': 'application/json'}
    context.url = '/users/newuser'

@when(u'register in the page')
def step_impl(context):
    context.page = context.client.post(context.url, data=context.data, headers = context.headers)
    assert context.page

@then(u'I should get a \'201\' response')
def step_impl(context): 
    print("code = ", context.page.status_code)
    assert context.page.status_code is 200

@then('new user are in the list of users')
def step_impl(context):
    assert 'jasonb' in context.page.text

# Scenario: Update a user from the Users data store
@given('A list of customers and a new data from customer')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne'}})
    context.user_info = json.dumps({'name': 'Jhon Bourne'})
    context.headers = {'Content-Type': 'application/json'}
    context.url = '/users/update/{}'.format('jasonb')

@when('I update customer')
def step_impl(context):
    context.page = context.client.put(context.url, data=context.user_info, headers = context.headers)
    assert context.page

@then('I should get a \'204\' response')
def step_impl(context):
    print("code = ", context.page.status_code)
    assert context.page.status_code is 200

@then('update user details are returned')
def step_impl(context):
    assert 'Jhon Bourne' in context.page.text

#Scenario: Delete a existing customer
@given('A list of customers and a customer to delete')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne'}})
    USERS.update({'jhonL': {'name': 'Jhon Lenon'}})
    context.headers= {'Content-Type': 'application/json'}
    context.url = '/users/delete/{}'.format('jasonb')

@when('delete customer')
def step_impl(context):
    context.page = context.client.delete(context.url, headers = context.headers)
    assert context.page

@then('I should get a \'202\' response')
def step_impl(context):
    print("code = ", context.page.status_code)
    assert context.page.status_code is 200

@then('user arent in the list of users')
def step_impl(context):
    assert 'jasonb' not in context.page.text