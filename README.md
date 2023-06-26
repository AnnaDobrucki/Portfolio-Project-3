# Hangman
Welcome to the well known universal game of Hangman! Where getting a letter wrong can mean pain of death...
Using python as my main platform I have built this game using both Gitpod and Heroku for my [Code Insitute Tertiary Project.](https://codeinstitute.net/full-stack-software-development-diploma/)

![amIresponsive pics](./documentation/design_pics/amIresponsive_preview_pic.png "Responsivness Pic")

## Index

* [Project Goals](#project-goals) 
* [Features](#features)
* [Design](#design)
* [Testing](#testing)
* [Languages, Frameworks & Libraries](#languages-frameworks--libraries)
* [Deployment](#deployment)
* [Credits](#credits)


## Project Goals
When beginning to build this game I wanted to set out some straightforward goals to help with both building the code from the ground up, as well as things to aim for. I came up with the following:

* To validate players choices through out.
* To show a Leaderboard that remains up to date.
* Show the 5 top scores from Leaderboard.
* To show where and how a player went right or wrong.
* To create a sense of competition with other users, and creating a scoreboard function.
* Create direct dialouge to make the game straightforward for a user.

### How to Play Hangman 
For people who dont know, here's how you play Hangman:
* Enter your username 
* Read the rules - You have 6 attempts of guessing a random word. Fail to choose the correct letter, will result in a limb from your hangman being lost. 
* Look at how many spaces there are shown to you, each space represents a letter in the word.
* Guess a letter
* Win - You gussed the word correctly. +5 points
* Loose - You have chosen... poorley.
* See your name and score on the board -5 points

Using the above rules I built a flow chart to begin with to help me with what functions I needed to build and what order I should build them where possible. I used [lucidchart](https://www.lucidchart.com/pages/) to create the following:
![Lucidchart Flowchart](./documentation/features/flowchart_hangman.png "Flowchart")

### User Goals
- Create an ease of use for the player.
- Have a tricky, but not hard time playing the game, and keep it varied.
- Create a username, linked to the scoreboard for added personalisation, potentially for the hope of returning use.
- Give them clear feedback whilst playing the game. 

## Features 
Key Features within this project:

1. I made a scoreboard that adds a username and a point scoreing system to add to the competitiveness of this game. I hoped that the thrill of seeing your name pop up was reminicent of older arcade games, and might users come back to play again, and see who has the highest score.
![Scoreboard](./documentation/scoreboard_pics/scoreboard_pics.png "Scoreboard")

* (You can find the link to the scoreboard [HERE](https://docs.google.com/spreadsheets/d/1JdvTA2fKHEM3F4te9Y1SV8tsfhz-ruJAHCrfvIhJldQ/edit?usp=sharing) )

* Another addition after discussiong with my mentor, was to add in a showing of the scores to the game itself, so I added in a formula to Googlesheets to reconfigure/ orginise the scoreboard to show the top 5 scores to date. I used this article to help me with the formula. [HERE](https://www.lido.app/tutorials/google-sheets-auto-sort#sort) 
![Leaderboard](./documentation/scoreboard_pics/leaderboard_pic.png "Leaderboard")

2. I wanted the game to have a clearing function, so as to not crowd the terminal. I ended up also adding in a timed element to allow the user to read the terminal but not wipe the screen too quickly. 

3. After building the game and running through it a couple of times, I realised that playing a terminal based game can be quite dull with so much black and white space. I looked into how to create colours within the terminal to help elements pop out/ look interesting/ and align with my goal of ease of use. I imported Colorama which allowed me to achieve this.
![Colorama useage](./documentation/features/colorama_useage.png "Colorama usage")

4. The game constiently tells the user what words they have correctly guessed or what words the have already used. 
![Guessed correct](./documentation/features/show_correct_guesses.png "Guessed correct")


5. There is a "lives" counter that repeatedly tells the user how many guesses they have remaining. With, of course, the visual aid of "Hangman" loosing limbs every failed turn. In conjunction with a change of colour to aid visually for people with potential visual impairments. 
![Hangman Lives Lost](./documentation/features/hangman_lives_lost.png "Lives Lost Hangman drawing")

6. I have made sure that validation is required through out the game, ranging from Username through to letters being picked rather than numbers.
![Validate guessed letter](./documentation/features/validate_guessed_letter.png "validate guessed letter")

## Design 
Whilst desgin for this project was less creative than past projects in terms of web desgin. I still wanted to give the project something to make it not look just like writing in a terminal. Ways in which I achieved this were:
1. Using ASCII Art from [fsymbols](https://fsymbols.com/text-art/) I got the looks of the Hangman intro/WIN/LOOSE fonts to stand out and look impactful. 
![Lost Game Art](./documentation/design_pics/art_for_lost_game.png "Lost Game Art")


2. Creating the desgin for the loosing limbs hangman, to help the user visualise the Lives Lost, and keep track of how many tries they have left. As well as making them colourful for visual aids, not to mention more entertaining. However I also realised that because of my clearscreen() it meant that colours were essential, wihtout them it became harder to see the progession of lives lost. 

3. Using Colorama, after importing colours to help add definition for different lines of text. Helps to build tension for the user playing the game seeing colour progession. Found thanks to this helpful article [Colorama A Hidden Convenience](https://medium.com/analytics-vidhya/colorama-a-hidden-convinience-6fb22dc00835)

### Future Ideas
After building the application, there were a couple of ideas that in the future I would like to implement. 
* Creating a main menu to allow people to select 
* Making some difficulty settings, reducing the lives and making harder words to guess.
* Creating a "hint" option that allows the user a helping hand if they are struggling. 

## Testing

  ### All notes related to testing are found [here](documentation/testing.md).

## Languages, Frameworks & Libraries
* Python3

* Time, Random, OS were all used to help build functions like clear screen/ pick word.

* Gspread (Googlesheets) was used as the basis for my scoreboard to be regularly updated. 

* The Code Institute's template of Python3 with additional HTML/Javascript used to then be used in Heroku. 

* My repo on Github used for storing and pushing Git.

* Heroku - Within Heroku I used the packages of Python and Node.JS.

## Credits 
Through-out building I predominantly used my knowledge gained from [Code Institue's Diploma Course](https://codeinstitute.net/full-stack-software-development-diploma/). As well as multiple other sources:

 I went through many different sites to help me with building this app:
 * I was struggling to understand how to do Error handling and this page helped me with learning how to print Error Messages [w3school](https://www.w3schools.com/python/gloss_python_error_handling.asp)
 * Studying further into Booleans was helpful for itteraing through the current letters that had been guessed and checking againt the word itself. This article helped to break it down for me in a bitesized way [Real Python](https://realpython.com/python-in-operator/)
 * Here I learnt hot to import the os for clearing the screen, here [Clear screen article](https://www.codingninjas.com/codestudio/library/how-to-clear-a-screen-in-python)
 * As stated above the artwork used was used from here [fsymbols](https://fsymbols.com/text-art/)

 I was also inspired by these videos:

 * I also had a look at this video to help me with the "not" boolen for inverting truth [Inverting truth](https://www.youtube.com/watch?v=gbx04NJi5As)
 * I was also inspired by this video for the building of how to itterate through the guessed and correct amswers (spesifically the enumerate part) [Kite Python Video](https://www.youtube.com/watch?v=m4nEnsavl6w)



 After some sick leave I went back to revisit some basics and these challenges from [w3school](https://www.w3schools.com/python/exercise.asp?filename=exercise_ifelse1) were particularly helpful. 
 
