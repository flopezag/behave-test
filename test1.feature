# Created by fernandolopez at 18.05.21
Feature: Test tutorial 101. Getting Started

  This is the feature file of the FIWARE Step by Step tutorial for NGSI-v2
  url: https://fiware-tutorials.readthedocs.io/en/latest/getting-started/index.html
  docker-compose: https://raw.githubusercontent.com/FIWARE/tutorials.Getting-Started/master/docker-compose.yml
  environment: https://raw.githubusercontent.com/FIWARE/tutorials.Getting-Started/master/.env

  Scenario: POST request example
    Given I Set POST posts api endpoint
    When I Set HEADER param request content type as "application/json."
    And Set request Body
    And Send a POST HTTP request
    Then I receive valid HTTP response code 201
    And Response BODY "POST" is non-empty.


  Scenario: GET request example
    Given I Set GET posts api endpoint ""
    When I Set HEADER param request content type as "application/json."
    And Send GET HTTP request
    Then I receive valid HTTP response code 200 for "GET."
    And Response BODY "GET" is non-empty


  Scenario: UPDATE request example
    Given I Set PUT posts api endpoint for ""
    When I Set Update request Body
    And Send PUT HTTP request
    Then I receive valid HTTP response code 200 for "PUT."
    And Response BODY "PUT" is non-empty


  Scenario: DELETE request example
    Given I Set DELETE posts api endpoint for ""
    When I Send DELETE HTTP request
    Then I receive valid HTTP response code 200 for "DELETE."