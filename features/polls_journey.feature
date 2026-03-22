Feature: Polls Application User Journey

  Scenario: Viewing the polls index page
    Given a question "Past question?" published 35 days ago
    And a question "Future question?" to be published in 30 days
    And a question "Recent question?" published 1 hour ago
    When I visit the polls index page
    Then I should see the text "Recent question?"
    And I should see the text "Past question?"
    And I should not see the text "Future question?"

  Scenario: Viewing an empty polls index page
    Given there are no questions in the system
    When I visit the polls index page
    Then I should see the text "No polls are available!"
