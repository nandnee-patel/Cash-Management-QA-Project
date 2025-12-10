# Acceptance Criteria (Specification by Example)

---

## User Story 1: Login

### Scenario 1: Valid Login
Given I am a registered user  
When I enter a valid username and password  
And click Login  
Then I should land on the Dashboard page  

### Scenario 2: Invalid Login
Given I enter incorrect credentials  
When I click Login  
Then I should see an error message  
And access should be denied  

---

## User Story 2: Approve Payment

### Scenario: Approve a pending payment
Given a payment exists in "Pending" status  
When I click Approve  
Then the status changes to "Approved"  
And a confirmation message appears  

---

## User Story 3: View Account Balance
Given I am on the dashboard  
When I open "Account Summary"  
Then I should see my current balance displayed correctly  
