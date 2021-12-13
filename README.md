![bannerimage](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/readme_img/readmebannerpn.png)

---
## Project: Code Institute December 2021 Hackathon: Happy Holidays

## Table of Contents

<details>
<summary>
  Expand
</summary>
  
  * [Introduction](#introduction)
  * [User Experience (UX)](#user-experience-(ux))
    * [User Stories](#user-stories)
      * [Site Owner Goals](#site-owner-goals)
      * [All Visitor Goals](#all-visitor-goals)
      * [First Time Visitor Goals](#first-time-visitor-goals)
      * [Returning Visitor Goals](#returning-visitor-goals)
  * [Design](#design)
  * [Wireframes](#wireframes)
  * [Features](#features)
  * [Technologies](#technologies)
  * [Testing](#testing)
    * [Testing Site Owner Goals](#testing-site-owner-goals)
    * [Testing All Visitor Goals](#testing-all-visitor-goals)
    * [Testing First Time Visitor Goals](#testing-all-visitor-goals)
    * [Testing Returning Visitor Goals](#testing-returning-visitor-goals)
    * [Validation Testing](#validation-testing)
    * [Manual Testing](#manual-testing)
    * [Cross Browser Testing](#cross-browser-testing)
    * [Browser Testing](#browser-testing)
    * [Device Testing](#device-testing)
    * [Lighthouse Audit](#lighthouse-audit)
  * [Deployment](#deployment)
  * [Credits](#credits)
    * [Inspiration](#inspiration)
    * [Resources](#resources)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)
    
</details>
 
### Introduction

This website is the project for Code Institutes' December 2021 Hackathon created by John Traas, Claudia Lai, Marialena Livathinopoulou, David Paul Thompson and Adam Boley, collectively the team called The Newbies, since this is the first hackathon project undertaken by each member. 

The website is named The Hangry Elf, and is a combination advent calendar and recipe site. Each day of December is represented by a card item. When the card is clicked, it expands and displays a simple recipe for that day. An effort was made to source recipes from different countries and cultures, for the purposes of diversity, since the hackathon theme is not specifically Christmas, but the December holidays generally. Of particular note are the dishes traditionally made and eaten by Jews during Hannukah, since Hannukah 2021 falls partly in December. 

The recipes are held in a linked database. When a user creates an account, the recipes held behind each card are randomly generated from this database. As each day elapses, the recipe for that day unlocks. 

The theme of The Hangry Elf is that Santa's most important Elf, Jimmy, is prone to getting hangry (possessed of a famous temper when his belly starts rumbling...). 
To avoid this, Santa must ensure that Jimmy is fed a delicious dish every day so that all of the presents will be made in time, and that the sleigh is ready to go!

---
## User Experience

### User Stories

#### Site Owner goals

- The site owners must be able to access the back-end as superusers
- The site owners must be able to add, remove or update recipes

#### All visitor goals

- Visitors must be able to navigate the site easily and intuitively
- Visitors must be able to access the recipes and dishes by clicking on the recipe cards
- Users must be able to recognise the dates of the cards
- Users must be able to hover over a card so that they can easily understand what card they are going to click
- Users must be able to turn any music on or off with a clear button click

#### First time visitor goals

- First time visitors must be able to easily determine that the site is an Advent Calendar of holiday themed recipes
- First time visitors must be able to create a user account easily

#### Returning visitor goals

- Returning visitors must be able to easily log into the site
- Returning visitors, once logged in, must be able to see previously unlocked recipes

---
## Design

Database planning and mapping out was done using <a href="https://dbdiagram.io/">Db Diagram</a>: 

![image](https://user-images.githubusercontent.com/59046774/145722188-b6dbe9cc-257d-421e-b6d0-d68092e83e1f.png)

---
## Wireframes

The Wireframe.cc app was used to plan out the basic design and look of the project. We found it useful because David, the designated wireframe designer for the project, could share his screen during Slack calls and each call participant could draw on the wireframe to outline their ideas. The wireframe images are located in the wireframes folder in the .assets folder

Links to the wireframes are below:

[Landing page](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/wireframes/Homepage.png)

[Advent Calendar page](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/wireframes/GamePage.png)

[Unwrapping animation](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/wireframes/GameAnimation.png)

[Unwrapped recipe](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/wireframes/CardAction.png)

[Login page](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/wireframes/LogIn.png)

[Sign Up page](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/wireframes/SignUp.png)

[Recipe](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/wireframes/Recipe.png)

---
## Features

### Technologies

The Hangry Elf was primarily created using the HTML, CSS and Python programming languages. 
Python was used because several of the team preferred Python over JavaScript. 
Platforms used:
- [Github](https://github.com/): Github was used to store the project files, and to allow each team member to be added as a contributor to the project. The Projects tab of the repository was used to note down initial ideas for the project, assign tasks and track progress.
- [Gitpod](https://www.gitpod.io/): The Gitpod IDE was used to create and edit the project files, and could convientially be accessed directly from Github. Git version control proved useful as each member was working on different aspects of the site, and an informal goal of the team was to have each member both submit and approve a pull request from the main repository
- [Bootstrap 5.0](https://getbootstrap.com/docs/5.0/getting-started/introduction/): Bootstrap was used to provide the initial project template.
- [Django](https://docs.djangoproject.com/en/4.0/): Django was used as the technology framework, and provided the template for allowing the user to login to the site.
- [Heroku](https://www.heroku.com/): Heroku was used to deploy the project.
- [Slack](https://slack.com/): Slack was used to coordinate the actions of the team, discuss ideas and share links. 
- [Google Docs](https://www.google.com/docs/about/): The team created and shared a Google Doc to note down ideas and store recipe links.
- [Font Awesome](https://fontawesome.com/): Font Awesone was used for the site's icons.
- [Google Fonts](https://fonts.google.com/): Google Fonts was used for the site's font. The Mountains of Christmas font was used.
- [Cloudinary](https://cloudinary.com/): Used to host the site's static files.

---
## Testing

### Manual testing

The Hangry Elf was manually tested throughout its development to ensure that each of the [user stories](#user-stories) was fulfilled. The user stories are noted below, along with the results of the testing.

### Testing Site Owner Goals

#### The site owners must be able to access the back-end as superusers
- The Django framework allows the site owners to easily create superuser accounts in Gitpod and login to the site's back-end

#### The site owners must be able to add, remove or update recipes
- The Django framework and Postgres database allow easy addition, removal and modification of the recipes

### Testing All Visitor Goals

#### Visitors must be able to navigate the site easily and intuitively
- The site has clear links at the top of the pages

#### Visitors must be able to access the recipes and dishes by clicking on the recipe cards
- Each card contains an "unlock" button to access the recipes

#### Users must be able to recognise the dates of the cards
- The date is displayed on the card

#### Users must be able to hover over a card so that they can easily understand what card they are going to click
- The cards on the Advent Calendar page have hover effects that cease when the mouse is removed from over the card

#### Users must be able to turn any music on or off with a clear button click
- The music is controlled by a standard control panel in the header with clear, intuitive buttons. 

### Testing First Time Visitor Goals

#### First time visitors must be able to easily determine that the site is an Advent Calendar of holiday themed recipes
- The snow effect, site name, and introduction should be clear enough to tell a first time user that the site contains holiday themed recipes in an advent calendar

#### First time visitors must be able to create a user account easily
- The main landing page has a register link that is prominent, and allows a first time user to easily register with the site

### Testing Returning Visitor Goals

#### Returning visitors must be able to easily log into the site
- The main landing page has a log-in link that is displayed prominently in the header, and allows a returning user to log-in to the site easily

#### Returning visitors, once logged in, must be able to see previously unlocked recipes
- On the advent calendar page, a logged-in returning user can see their progress through the advent calendar as previously unlocked recipes are marked by a green checkmark

### Validation Testing
The following websites have been used to validate the code being used on the website. The original code has been tested to ensure the functionality of the website. This will detect any syntax errors if provided and ensure the website is functioning correctly for the developer and the users of the webpage. 
- JavaScript - https://jshint.com/
  - None

- HTML - https://validator.w3.org/
  - 1 errors and 1 warning were noted, but left uncorrected due to preserve the integrity and function of the website

- CSS - https://jigsaw.w3.org/css-validator/
  - No errors found

- Lighthouse - https://developers.google.com/web/tools/lighthouse/?utm_source=devtools

---

### Cross Browser Testing

The Chrome Dev Tools were used to ensure that the Hangry Elf was responsive when viewed on desktop browsers. The most common desktop and laptop browsers - Google Chrome, Microsoft Edge, Safari and Mozilla Firefox - were used to view the site to ensure that all users could use the site unimpeded. The functions that must work regardless of browser are below:

- Register details on the website and access a profile
- Login and logout the website securely
- Navigate the site easily and intuitively
- Access the recipes and dishes by clicking on the recipe cards
- Recognise the dates of the cards
- Click on the card to display the dishes and recipes
- Hover over a card so that they can easily understand what card they are going to click
- Ability to mute or unmute the music
- Ensure the square selected displays the card with all the information
- Add a superuser

### Browser Testing

Below are the browser testing tables. Table 1 is for Google Chrome and Firefox. Table 2 is for Microsoft Edge and Safari

[Browser Testing Table 1](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/test/Test1.png)

[Browser Testing Table 2](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/test/Test2.png)

### Device Testing

Below are the mobile device testing tables. Table 1 is for the iPad Pro and the Google Pixel 2. Table 2 is for the Huawei P20 Pro and Samsung Galaxy Pro

[Mobile Testing Table 1](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/test/Test3.png)

[Mobile Testing Table 2](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/test/Test4.png)

### Lighthouse Audit

“Identify and fix common problems that affect your sites' performance, accessibility, and user experience.”

Accessibility testing is key to checking that the site is functional, and ensuring that the site is running at maximum performance. The Lighthouse audit provides accurate information from scanning the website and providing a finding of the website's functionality. The Lighthouse tests can be run by opening the Chrome Dev Tools (F12 or right-click, then Inspect), and then generating a report for either desktop or mobile devices.

[Lighthouse Audit](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/lighthouse/LighthouseAudit.png)

Below is the result from the Lighthouse audit for mobile devices. The audit shows that the site initially had excellent performance on mobile devices.

[Lighthouse Mobile First Result](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/lighthouse/LighthouseMobile.png)

Below is the result from the Lighthouse audit for desktop devices. The audit shows that the site initially had good but not excellent performance on desktop devices.

[Lighthouse Desktop First Result](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/lighthouse/LighthouseDesktop.png)

As a result of these audits, some improvements were made to the desktop and mobile display on the website. The website has a clean feel for users, and is easy for users to both navigate and use the features of the website.


### Mobile Lighthouse Audit Final Result

Below is the result from the final Lighthouse audit for mobile devices. The audit shows that the final iteration ofthe website of has excellent performance on mobile devices

[Lighthouse Mobile Final Result](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/lighthouse/LighthouseMobileFinal.png)

### Desktop Lighthouse Audit Final Result

Below is the result from the final Lighthouse audit for desktops devices. The audit shows that the final iteration ofthe website of has excellent performance on desktop devices

[Lighthouse Desktop Final Result](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/lighthouse/LighthouseDesktopFinal.png)

---
## Deployment

The project was deployed using Heroku. The static files were hosted on Cloudinary. 

---
## Credits

### Inspiration

The Winner of the Code Institute November 2021 Hackathon was agreed by all team members to have extensive documentation, and was used as a rough template for this project's documentation. 

### Recipes

- [BBC Good Food](https://www.bbcgoodfood.com/), for many of the Christmas-themed recipes used in the project

- [Tastes of Home](https://www.tasteofhome.com/), for the traditional Jewish dishes

- [Delish](https://www.delish.com/)

- [Once Upon a Chef](https://www.onceuponachef.com/)

### Media 

* Audio
  - Track name: A Christmas Dance
  - Artist: Arthur Benson
  - Retrieved from: [Epidemic Sound](https://www.epidemicsound.com/track/yRFwYp70k9/)

* Images
  - [Adobe Stock Images](https://stock.adobe.com/)
  - [Clip Art Max](https://www.clipartmax.com/)
    - * Toast images
    - * Custom 404 error pages

### Acknowledgements

- The Newbies:
  - [John Traas](https://github.com/Jays-T)

  - [Claudia Lai](https://github.com/ClaudiaLie)

  - [Marialena Livathinopoulou](https://github.com/Anelairam)

  - [David Paul Thompson](https://github.com/tomod24)

  - [Adam Boley](https://github.com/AdamBoley) (and his cat)
