# pythonic-garage-band

**Author**: Raven Delaney
**Version**: 1.1.0

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for a Code Fellows 401 class. (i.e. What's your problem domain?) -->
Intro to classes using the idea of a band and inheritance from other classes

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
Using VS code, command line, and Python 3, you build out your classes.
A band inherits musician classes and each musician is given different actions

## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. This is also an area which you can include any visuals; flow charts, example usage gifs, screen captures, etc.-->
Necessary tools - Command line,  Python 3, VS code
Steps to run it - once you have the files on your local machine, get into the folder and get into a shell environment
    Once in the shell you can call the functions to get the musicians, their solos, etc. returned

## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->
Musician super class - holds repr and string methods for each musician in the band - will return the instrument and playing a solo
Band class - imports band members from musician class and return band name and members of band
Vocals/Guitar/Bassist/Drums class - creates each instance of a musician

## Change Log

<!-- Use this are to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:
01-01-2001 4:59pm - Added functionality to add and delete some things.
-->
12/04/2019 2:45pm - repository setup, starting readme
01/06/2020 4:00pm - Added to readme, working on tests
