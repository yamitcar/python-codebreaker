
Feature:
  As a player
  I want to guess the secret code
  in order win

  AC:
    the number must have 4 digits
    the digits must be different
    i must be informed about matches and partial-matches
    i must be able to try again if fail
    i must be informed if i guess the secret code correctly

Scenario: the page must have a tittle
  Given i enter the player game with number "1234"
  Then i should see "Welcome to the jungle, try to guess the secret"

Scenario: i enter a 2 digit number
  Given i enter the player game with number "5321"
  When i guess with "21"
  Then i should see "Invalid number, the number must have 4 digits"

Scenario: i enter a 4 digit number
  Given i enter the player game with number "1234"
  When i guess with "7890"
  Then i should see "7890: 0M-0PM"