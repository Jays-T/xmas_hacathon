![bannerimage](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/readme_img/readmebannerpn.png)

---
## Project: Code Institute December 2021 Hackathon: Happy Holidays

## Table of Content

<details><summary>Expand</summary>
<p>
 1. [Introduction](#introduction)
 2. 
</details>
 
### Introduction

This website is the project for Code Institutes' December 2021 Hackathon created by John Traas, Claudia Lai, Marialena Livathinopoulou, David Paul Thompson and Adam Boley, collectively the team called The Newbies, since this is the first hackathon project undertaken by each member. 

The website is named The Hangry Elf, and is a combination advent calendar and recipe site. Each day of December is represented by a card item. When the card is clicked, it expands and displays a simple recipe for that day. An effort was made to source recipes from different countries and cultures, for the purposes of diversity, since the hackathon theme is not specifically Christmas, but the December holidays generally. Of particular note are the dishes traditionally made and eaten by Jews during Hannukah, since Hannukah 2021 falls partly in December. 

The recipes are held in a linked database. When a user creates an account, the recipes held behind each card are randomly generated from this database. As each day elapses, the recipe for that day unlocks. 

The theme of The Hangry Elf is that Santa's most important Elf, Jimmy, is prone to getting hangry (possessed of a famous temper when his belly starts rumbling...). 
To avoid this, Santa must ensure that Jimmy is fed a delicious dish every day so that all of the presents will be made in time, and that the sleigh is ready to go!

---
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

#### Returning visitors must be able to easily log into the site
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

### Validation Testing
The following websites have been used to validate the code being used on the website. The original code has been tested to ensure the functionality of the website. This will detect any syntax errors if provided and ensure the website is functioning correctly for the developer and the users of the webpage. 
- JavaScript - https://jshint.com/
- HTML - https://validator.w3.org/
- CSS - https://jigsaw.w3.org/css-validator/
- Lighthouse - https://developers.google.com/web/tools/lighthouse/?utm_source=devtools

---
## User Stories Testing

### Manual testing
The use of manual testing ensures the results are correct and accurate at the time and can identify errors displayed which can be looked into further if necessary. From clicking items to completing full check outs on the website.  Provided below is a list of testing requirements to which will enable us to confirm the website is working to its full potential.  This will help confirm the site is working as required from the designing and creating aspect of the website development.
Testing Client Stories from UX Section
Manually testing was completed to ensure the website met the user/ user stories requirements. 
This would ensure testing the user stories we have covered the website requirements for the user the functionality, visual and usage responsiveness.
This would help to provide an indication to the level of the web site was working and if it completed all the requirements necessary
 

### Cross Browser Testing
The use of multiple web browsers allows us to check and test the functionality across different platforms and user interfaces.  The types of web browsers we used were web browsers and mobile devices. This will be due to the responsive testing required to ensure this works for all users.

Testing will ensure the website is suitable and the website has been thoroughly checked for any users. A list of actions required to be available for the website have been provided below.

- register details on the website and access a profile
- login and logout the website securely
- navigate the site easily and intuitively
- access the recipes and dishes by clicking on the recipe cards
- recognise the dates of the cards
- click on the card to display the dishes and recipes
- hover over a card so that they can easily understand what card they are going to click
- ability to mute or unmute the music
- ensure the square selected displays the card with all the information
- add a superuser

### Browser Testing

[Browser Testing Table 1](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/test/Test1.png)

[Browser Testing Table 2](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/test/Test2.png)

### Device Testing

To enable all device were tested and various device were explored tablets and mobiles were considered to test the game on. This would ensure this works on multiple devices.

[Mobile Testing Table 1](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/test/Test3.png)

[Mobile Testing Table 2](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/test/Test4.png)

### Lighthouse Audit

“Identify and fix common problems that affect your sites performance, accessibility, and user experience.”

Accessibility testing is key to checking the site functional and ensuring the site is running to its maximum performance. The lighthouse audit will provide accurate information from scanning the website and provide the finding of the website functioning. This can be selected by using the development tool and generating a report on a selected device

This can be mobile or desktop devices.

[Lighthouse Audit](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/lighthouse/LighthouseAudit.png)

Here are the results from the lighthouse audit on mobile devices.  Mobile devices show the responsiveness on the website and websites are based on the mobile responsiveness.

[Lighthouse Mobile First Result](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/lighthouse/LighthouseMobile.png)

The results for desktop lighthouse audit is as followed. As this is a early lighthouse review we want to see the improvements to the website when developing and improving the code on the website. This will be completed at the end of the website completion.

[Lighthouse Desktop First Result](https://github.com/Anelairam/xmas_hacathon/blob/main/.assets/lighthouse/LighthouseDesktop.png)

The website has been tested with the lighthouse function to provide the website functionality and performance score. As a result, some improvements were made to the desktop and mobile display on the website and the results have improved. The website presented has a clean feel for users and it’s not too difficult to navigate and use the website features.


### MobileLighthouse Audit Latest Result

 

### Desktop Lighthouse Audit Latest Result



### Lighthouse Audit

---
## Deployment

The project was deployed using Heroku. The static files were hosted on Cloudinary. 

---
## Credits

### Inspiration

The Winner of the Code Institute November 2021 Hackathon was agreed by all team members to have extensive documentation, and was used as a rough template for this project's documentation. 

### Resources

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
