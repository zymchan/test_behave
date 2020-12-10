# Created by 邹艺明 at 2020/12/9
@android
Feature: Task 1

  Scenario: Check tomorrow weather forecast from 9-day forecast screen
     Given When we are at the home page
      When We click the menu icon
       And We click the 9-day forecast
      Then We can check tomorrow weather forecast
