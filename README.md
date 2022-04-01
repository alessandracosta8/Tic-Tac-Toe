# Tic Tac Toe game

[Deployed Game Link]

&nbsp;

## Table of Contents
---

- [UX](#ux)
    - [Website owners goals](#website-owners-goals)
    - [Users goals](#users-goals)
    - [Flow Chart](#flow-chart)
- [Features](#features)
    - [Game](#game)
    - [Future feature to implement](#future-feature-to-implement)
- [Technologies used](#tecnologies-used)
- [Libraries used](#libraries-used)
- [Testing and Validation](#testing-and-validation)
    - [PEP8](#pep8)
    - [Manual testing](#manual-testing)
    - [Compatibility](#compatibility)
    - [User stories testing](#user-stories-testing)
        - [Website owner](#website-owner)
        - [New visitor](#new-visitor)
        - [Returning visitor](#returning-visitor)
    - [Bugs](#bugs)
        - [From the Slack feedback request](#from-the-slack-feedback-request)
    - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)


&nbsp;

## UX
---

### Website owners goals
The goal of this program is to play a game of Tic Tac Toe against the computer.
Tic-tac-toe is a game in which two players take turns in drawing either an 'O' or an 'X' in one square of a grid consisting of nine squares. The winner is the first player to get three of the same symbols in a row, vertically, horizontally or diagonally.

&nbsp;

### User goals
The user can improve their skill at the game excercising with this program which puts them against the computer.
The user can navigate through the game with very easy commands and always available reference of the possible choices when making a move.

&nbsp;

### Flow Chart
![Flow Chart](assets/game_structure.jpeg)

&nbsp;


## Index

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

&nbsp;



## Credits
---

[Python Classmethods and Staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)

[12 Beginner Python Projects](https://www.youtube.com/watch?v=8ext9G7xspg&t=2189s)

[Tic Tac Toe definition - Collins Dictionary](https://www.collinsdictionary.com/dictionary/english/tic-tac-toe#:~:text=Tic%2Dtac%2Dtoe%20is%20a,same%20symbols%20in%20a%20row.)


&nbsp;


[Back to Table of contents](#table-of-contents)
