# Code Fellows 401n4 - Advanced Software Development in Python

## Lab 04: Garage Band with OOP

+ *Use Python classes to model a Band made up of different kinds of musicians.*
*Starts with Guitarist,Bassist, and Drummer. Makes use of a Musician base class to handle common functionality which particular kinds of musicians will inherit.*

### Feature Tasks and Requirements

+ **Band Tests**
  + A Band instance should have a name attribute which is a string.
  + A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
  + A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.
  + A Band instance should have appropriate __str__ and __repr__ methods.
  + A Band should have a class method to_list which returns a list of previously created Band instances

+ **Musician Subclass Tests**
  + Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
  + Each kind of Musician instance should have a get_instrument method that returns string.
  + Each kind of Musician instance should have a play_solo method that returns string.

### Deployed URLs

+ **Running Server:** N/A
+ **Running Clients:** N/A

### Pull Request

+ [madlib-cli/pull/1](URL 'https://github.com/micgreene/madlib-cli/pull/1')

### README

+ [README.md](URL 'https://github.com/micgreene/madlib-cli/blob/dev/README.md')