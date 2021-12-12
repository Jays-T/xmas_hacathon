# The Hangry Elf

## Project: Code Institute December 2021 Hackathon: Happy Holidays

## Introduction

This website is the project for Code Institutes' December 2021 Hackathon created by John Traas, Claudia Lai, Marialena Livathinopoulou, David Paul Thompson and Adam Boley, collectively the team called The Newbies, since this is the first hackathon project undertaken by each member. 

The website is named The Hangry Elf, and is a combination advent calendar and recipe site. Each day of December is represented by a card item. When the card is clicked, it expands and displays a simple recipe for that day. An effort was made to source recipes from different countries and cultures, for the purposes of diversity, since the hackathon theme is not specifically Christmas, but the December holidays generally. Of particular note are the dishes traditionally made and eaten by Jews during Hannukah, since Hannukah 2021 falls partly in December. 

The recipes are held in a linked database. When a user creates an account, the recipes held behind each card are randomly generated from this database. As each day elapses, the recipe for that day unlocks. 

The theme of The Hangry Elf is that Santa's most important Elf, Jimmy, is prone to getting hangry (possessed of a famous temper when his belly starts rumbling...). 
To avoid this, Santa must ensure that Jimmy is fed a delicious dish every day so that all of the presents will be made in time, and that the sleigh is ready to go!

## UX

### User Stories

#### Site Owner goals

- The site owners must be able to access the back-end as superusers
- The site owners must be able to add, remove or update recipes

#### All visitor goals

- Visitors must be able to navigate the site easily and intuitively
- Visitors must be able to access the recipes and dishes by clicking on the recipe cards
- Users must be able to recognise the dates of the cards
- Users must be able to click on the card to display the dishes and recipes
- Users must be able to hover over a card so that they can easily understand what card they are going to click
- Users must be able to turn any music on or off with a clear button click

#### First time visitor goals

- First time visitors must be able to easily determine that the site is an Advent Calendar of holiday themed recipes
- First time visitors must be able to create a user account easily

#### Returning visitor goals

- Returning visitors must be able to easily log into the site
- Returning visitors, once logged in, must be able to see previously unlocked recipes


## Design

## Wireframes

The Wireframe.cc app was used to plan out the basic design and look of the project. We found it useful because David, the designated wireframe designer for the project, could share his screen during Slack calls and each call participant could draw on the wireframe to outline their ideas. The wireframe images are located in the wireframes folder in the .assets folder

Links to the wireframes are below:

[Landing page](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/wireframes/Homepage.png)

[Advent Calendar page](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/wireframes/GamePage.png)

[Unwrapping animation](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/wireframes/GameAnimation.png)

[Unwrapped recipe](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/wireframes/CardAction.png)

[Recipes page]()

## Features

## Technologies

The Hangry Elf was primarily created using the HTML, CSS and Python programming languages. Python was used because several of the team preferred Python over JavaScript. 
Platforms used:
- Github: Github was used to store the project files, and to allow each team member to be added as a contributor to the project. The Projects tab of the repository was used to note down initial ideas for the project, assign tasks and track progress.
- Gitpod: The Gitpod IDE was used to create and edit the project files, and could convientially be accessed directly from Github. Git version control proved useful as each member was working on different aspects of the site, and an informal goal of the team was to have each member both submit and approve a pull request from the main repository
- Bootstrap 5.0: Bootstrap was used to provide the initial project template.
- Django: Django was used as the technology framework, and provided the template for allowing the user to login to the site.
- Heroku: Heroku was used to deploy the project.
- Slack: Slack was used to coordinate the actions of the team, discuss ideas and share links. 
- Google Docs: The team created and shared a Google Doc to note down ideas and store recipe links.
- Font Awesome: Font Awesone was used for the site's icons.
- Google Fonts: Google Fonts was used for the site's font. The Mountains of Christmas font was used.
- Cloudinary: Used to host the site's static files.

## Testing

### Testing Site Owner Goals

#### The site owners must be able to access the back-end as superusers
- The Django framework allows the site owners to easily create superuser accounts in Gitpod and login to the site's back-end

#### The site owners must be able to add, remove or update recipes
- The Django framework and Postgres database allow easy addition, removal and modification of the recipes

### Testing All Visitor Goals

#### Visitors must be able to navigate the site easily and intuitively
- The site has clear links at the top of the pages

#### Visitors must be able to access the recipes and dishes by clicking on the recipe cards
- 

#### Users must be able to recognise the dates of the cards
- 

#### Users must be able to click on the card to display the dishes and recipes
- 

#### Users must be able to hover over a card so that they can easily understand what card they are going to click
- The cards on the Advent Calendar page have hover effects that cease when the mouse is removed from over the card

#### Users must be able to turn any music on or off with a clear button click
- The music is controlled by a standard control panel

### Testing First Time Visitor Goals

#### First time visitors must be able to easily determine that the site is an Advent Calendar of holiday themed recipes
- The snow effect, site name, and introduction should be clear enough to tell a first time user that the site contains holiday themed recipes in an advent calendar

#### First time visitors must be able to create a user account easily
- The main landing page has a register link that is prominent, and allows a first time user to easily register with the site

### Testing Returning Visitor Goals

#### - Returning visitors must be able to easily log into the site
- The main landing page has a login link that is prominent, and allows a returning user to login to the site easily

#### Returning visitors, once logged in, must be able to see previously unlocked recipes
- 

### Platform Testing - Desktop / Laptop

#### Google Chrome
- All tested and working correctly

#### Microsoft Edge
- 

#### Safari
-

#### Mozilla Firefox
-

## Deployment

The project was deployed using Heroku. The static files were hosted on Cloudinary. 

## Credits

### Resources

[The Snow Effect](https://www.youtube.com/watch?v=XSy7Yh83pWg&ab_channel=RajUpadhyay)
Author: [Raj Upadhyay](https://www.youtube.com/channel/UCLGMtGF18DZbzSbWLALB8tg)

Animations:
[W3Schools](https://www.w3schools.com/css/)
[MDN Web Docs](https://developer.mozilla.org/en-US/)


### Inspiration

The Winner of the Code Institute November 2021 Hackathon was agreed by all team members to have extensive documentation, and was used as a rough template for this project's documentation. 

### Recipe sources

- [BBC Good Food](https://www.bbcgoodfood.com/), for many of the Christmas-themed recipes used in the project

- [Tastes of Home](https://www.tasteofhome.com/)

- [Delish](https://www.delish.com/)

- [Once Upon a Chef](https://www.onceuponachef.com/)

### Media 

- Track name: A Christmas Dance
- Artist: Arthur Benson
- Retrieved from: [Epidemic Sound](https://www.epidemicsound.com/track/yRFwYp70k9/)

### Acknowledgements

- The Newbies:
  - [John Traas](https://github.com/Jays-T)

  - [Claudia Lai](https://github.com/ClaudiaLie)

  - [Marialena Livathinopoulou](https://github.com/Anelairam)

  - [David Paul Thompson](https://github.com/tomod24)

  - [Adam Boley](https://github.com/AdamBoley)



