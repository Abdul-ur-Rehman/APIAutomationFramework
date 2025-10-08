# Created by Abdul-ur-Rehman at 10/07/2025

  Feature: Verify if books are adding and deleting using Library API

    Scenario: Verify AddBook API functionality
      Given the book details which needs to be added to library
      When we execute the AddBook Post API method
      Then book is successfully added

    Scenario: Verify AddBook API functionality with hard coded data
      Given the hard coded book details which needs to be added to library
      When we execute the AddBook Post API method
      Then book is successfully added

    Scenario Outline: Verify AddBook API functionality with parameteratization
      Given the book details with <isbn> and <aisle>
      When we execute the AddBook Post API method
      Then book is successfully added
      Examples:
        | isbn | aisle |
        | abc  | 1234  |
        | mnp  | 1234  |
        | jkl  | 1234  |
        | xyz  | 1234  |
