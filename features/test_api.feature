# Created by 邹艺明 at 2020/12/9
Feature: Task 2
  Using the API from Hong Kong Observatory,verify the status of the request response and
  extract the relative humidity (e,g, 60 - 85%) for the day after tomorrow.

  Scenario: Extract the relative humidity for the day after tomorrow from the API response
      Given get current time as <time>
      When I send get request to http://www.hko.gov.hk/json/DYN_DAT_MINDS_FND.json?<time>
      Then The status of the request should be 200
      And Print the relative humidity for the day after tomorrow




