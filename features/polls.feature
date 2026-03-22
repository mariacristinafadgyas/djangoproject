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

Feature: Polls Application User Journey

  Scenario: Viewing the polls index page
    Given a question "Past question?" published 35 days ago
    And a question "Future question?" to be published in 30 days
    And a question "Recent question?" published 1 hour ago
    When I visit the polls index page
    Then I should see the text "Recent question?"
    And I should not see the text "Past question?"
    And I should not see the text "Future question?"

  Scenario: Viewing an empty polls index page
    Given there are no questions in the system
    When I visit the polls index page
    Then I should see the text "No polls are available."
