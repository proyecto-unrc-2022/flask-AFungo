Feature: Handle storing, retrieving and deleting customer details # test/features/user.feature:1

  Scenario: Retrieve a customers details
    Given some users are in the system
    When I retrieve the customer 'jasonb'
    Then I should get a '200' response
    And the following user details are returned:
      | name        |
      | Jason Borne |

  Scenario: Create a new customer
    Given a new customer username
    When register in the page
    Then I should get a '201' response


  Scenario: Update a user from the Users data store
    Given A list of customers and a new data from customer
    When I update customer
    Then I should get a '204' response


  Scenario: Delete a existing customer
    Given A list of customers and a customer to delete
    When delete customer
    Then I should get a '202' response