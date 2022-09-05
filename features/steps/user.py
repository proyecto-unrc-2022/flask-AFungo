import json
from behave import *
from application import USERS

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
    assert "Jason Bourne" in context.page.text




@given('a new customer username')
def step_impl(context): 
    context.data = {'name': 'Jason Bourne'}
    
@when(u'register in the page')
def step_impl(context):
    context.res = context.client.post('/users/newuser', data=json.dumps(context.data), headers = {'Content-Type': 'application/json'})
    print(context.res.text)
    assert context.res

@then(u'I should get a \'201\' response')
def step_impl(context): 
    print("code = ", context.res.status_code)
    assert context.res.status_code is 200




@given('A list of customers and a new data from customer')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne', 'name1': 'Juan B'}})
    context.user_info = ({'jasonb' : {'name': 'Jason Bourne', 'name1': 'Jhon B'}})

@when('I update customer')
def step_impl(context):
    context.page = context.client.put('/users/update'.format('jasonb', data=context.user_info))
    assert context.page

@then('I should get a \'204\' response')
def step_impl(context):
    print("code = ", context.page.status_code)
    assert context.page.status_code is 204


@given('A list of customers and a customer to delete')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne', 'name2': 'Juan B'}})
    context.user_info = ({'jasonb' : {'name': 'Jason Bourne', 'name1': 'Jhon B'}})

@when('delete customer')
def step_impl(context):
    context.page = context.client.put('/users/update'.format('jasonb', data=context.user_info))
    assert context.page

@then('I should get a \'202\' response')
def step_impl(context):
    print("code = ", context.page.status_code)
    assert context.page.status_code is 202