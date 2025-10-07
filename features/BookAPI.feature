# Created by Abdul-ur-Rehman at 10/07/2025

  Feature: Verify if books are adding and deleting using Library API

    Scenario: Verify AddBook API functionality
      Given the book details which needs to be added to library
      When we execute the AddBook Post API method
      Then book is successfully added