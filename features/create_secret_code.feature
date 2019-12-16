
Feature:
  As a secret keeper
  I want to create a secret code
  in order to keep safe the secrets of the life

  AC:
    the page must have a tittle
    the digits must be different
    the number must be secret
    the number must have 4 digits

Scenario: the page must have a tittle
  Given i enter the game
  Then i should see "Welcome to code breaker"

Scenario: 1234 is a valid number
  Given I enter the game
  When i enter the number "1234"
  And i save the secret
  Then i should see "The secret was config correctly"

Scenario: 12 is an invalid number
  Given I enter the game
  When i enter the number "12"
  And i save the secret
  Then i should see "The secret was NOT config correctly"
