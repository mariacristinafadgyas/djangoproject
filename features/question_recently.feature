Feature: Question was_published_recently

  Scenario: Question published within the last 24 hours
    Given a question published 30 minutes ago
    Then it should be considered published recently

  Scenario: Question published more than 1 day ago
    Given a question published 2 days ago
    Then it should not be considered published recently

  Scenario: Question published in the future
    Given a question published 1 hour from now
    Then it should not be considered published recently
