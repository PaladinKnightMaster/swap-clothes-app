
<h1 align="center">SWAP your clothes</h1>
<h1 align="center"><img src="./static/graphics/readme/amiresponsive.png" /></h1>

 <a href="https://clothes-swap-app.herokuapp.com/"><img src="./static/graphics/SWAP-logo.png" width="25px" /></a> :point_left: Live website

  <a href="https://github.com/LigaMoon/swap-clothes-app"><img src="./static/graphics/readme/githublogo.png" width="25px" /></a> :point_left: GitHub Repository
 
 ## About

This website is an alternative to thrifting, buying, and donating clothes by facilitating users to swap their pre-loved items. Not only is it great for the environment and allows users to connect with like-minded people, but it is cost-friendly too.

## Table of Contents

1. [User Experience (UX)](#user-experience)
    1. [User Stories](#user-stories)
    1. [Design](#design)
        - [Color sheme](#color-scheme)
        - [Typography](#typography)
        - [Imagery](#imagery)
        - [Wireframes](#wireframes)
        - [Mockups](#mockups)

[Features](#features)

[Technologies Used](#technologies-used)

[Testing](#testing)

[Deployment](#deployment)

[Known Bugs](#bugs)

[Credits](#credits)


## User Experience (UX)

### User Stories

- #### Common user stories
    1. I want to intuitively navigate through the site to browse the content.
    1. I want the experience of using this site to be interactive.
    1. I want to be able to view all clothing items.
    1. I want to be able to sort all items by the most recent added.
    1. I want to be able to sort all items by alphabetical and reverse alphabetical order.
    1. I want to be able to filter items by their categories.
    1. I want to be able to search for a specific item.
    1. I want to be able to understand the purpose of the site.
    1. I want to be able to contact the owner of the site.
    1. I want the page to be responsive on all screen sizes.
    1. I want to be able to navigate to the top of the page quickly, particularly in the mobile view.

- #### As a first time visitor
    1. I want to be able to find the 'Register' page easily.
    1. I want to be able to register easily
    
- #### As a returning user
    1. I want to be able to navigate to the 'Login' page easily.
    1. I want to be able to Log In quickly.
    1. I want to add new items easily.
    1. I want to be able to edit and delete my items.
    1. I want to like items.
    1. I want to be able to flag inappropriate content.
    1. I want to see the items that I have liked.
    1. I want to be able to update my profile.
    1. I want to view all my added items.
    1. I want to view all items I have matched with.
    1. I want to see items that matched the categories that I'm looking for.
    1. I want to be able to contact another user if I match to swap the items.
    1. I want to be able to Log out.

- #### As an admin
    1. I want to be able to unflag an item if it's been flagged incorrectly.
    1. I want to be able to delete an item if it's inapropriate.


### Design

- #### Color scheme
    - I wanted to create a fun/colorful but clean and simple (looking not coding) look to the site. I aimed to make swapping clothes and contributing to sustainable living - interesting and interactive. The inspiration for the colors came from [uiGradidents](https://uigradients.com/#SweetMorning) website, 'Sweet Morning' gradient. Colors used for this gradient and also as my accent colors are 'Fiery Rose' (#FF5F6D) and 'Mellow Apricot' (#FFC371). The primary accent color was 'Fiery Rose' as it provides more contrast against the white background - which is the dominant color of the website. The text color chosen was 'Davys Gray' (#585858) to create a softer look as opposed to opting to use black text, while still maintaining comfortable contrast between the background and the text. Finally, I used black as the main color for the Landing page to create an impactful first impression when a user first visits the site. The color palette was assembled using [coolors](https://coolors.co/ffc371-ff5f6d-ffffff-585858-000000) color palette generator.

        <img src="./static/graphics/readme/gradient.png" height="100px" />
        <img src="./static/graphics/readme/color-palette.png" height="50px" />

- #### Typography
    - The font used for this website is a sans serif type font 'Montserrat' with Sand Serif as a fallback font. I chose this font from [Google Fonts](https://fonts.google.com/specimen/Montserrat?query=Mont&preview.text=SWAP%20your%20clothes&preview.text_type=custom) website with the main aim to keep the text clean, clear, and easily readable. Since the website contains colorful accents and gradients, I opted to use only one font for the whole website with changing font weight and font style instead. 

        <img src="./static/graphics/readme/font-montserrat.png" height="50px" />


    - [Font awesome](https://fontawesome.com/) icons were used across pages to emphasize the meaning of the text it was placed alongside, allow the user to understand content faster, and add to the fun look of the site. 

- #### Imagery
    - Images
        - The primary reason for using images is for informative purposes. Images are displayed in item cards to allow users to visually engage with items added by other users and decide if they are interested in the item.
        - The secondary purpose of the images is aesthetic. The images displayed on cards are kept quite large and the same size while not being distorted. This attributes to the clean, organized look of the website. An image is also used as a hero image that takes the full screen to separate the page and not distract the user from the message on the landing page.
        - All images have been taken from [unspalsh](https://unsplash.com/) and minified using [tinyJPG](https://tinyjpg.co)

    - Graphics
        - Graphics are used for aesthetic and design purposes only. The legs on the landing page set the tone for the website and the colors tie in with the header gradient to create a sense of uniformity.
        - Graphics used were designed by [Pablo Stanley from Hhmaaans](https://www.humaaans.com/) and [Katerina Limpitsouni from unDraw](https://undraw.co/)

- #### Wireframes
    - Wireframes were created using Adobe Xd
    - Mobile Wireframes
        - [Unauthorised User](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/wireframes/wireframes-mobile-unauthorised.png) :point_left:
        - [Authorised User](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/wireframes/wireframes-mobile-authorised.png) :point_left:
        - [Admin](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/wireframes/wireframes-mobile-admin.png) :point_left:

         <img src="static/graphics/readme/wireframes/wireframes-mobile.png" height="400px"/>

    - Tablet Wireframes
        - [Unauthorised User](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/wireframes/wireframes-tablet-unauthorised.png) :point_left:
        - [Authorised User](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/wireframes/wireframes-tablet-authorised.png) :point_left:
        - [Admin](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/wireframes/wireframes-tablet-admin.png) :point_left:

         <img src="static/graphics/readme/wireframes/wireframes-tablet.png" height="400px"/>

    - Desktop Wireframes
        - [Unauthorised User](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/wireframes/wireframes-desktop-unauthorised.png) :point_left:
        - [Authorised User](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/wireframes/wireframes-desktop-authorised.png) :point_left:
        - [Admin](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/wireframes/wireframes-desktop-admin.png) :point_left:

         <img src="static/graphics/readme/wireframes/wireframes-desktop.png" height="400px"/>


- #### Mockups
    - Mockups were created using Adobe Xd
    - Mobile Mockups
        - [Unauthorised User](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/mockups/mockups-mobile-unauthorised.png) :point_left:
        - [Authorised User](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/mockups/mockups-mobile-authorised.png) :point_left:
        - [Admin](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/mockups/mockups-mobile-admin.png) :point_left:

         <img src="static/graphics/readme/mockups/mockups-mobile.png" height="400px"/>

    - Tablet Mockups
        - [Unauthorised User](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/mockups/mockups-tablet-unauthorised.png) :point_left:
        - [Authorised User](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/mockups/mockups-tablet-authorised.png) :point_left:
        - [Admin](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/mockups/mockups-tablet-admin.png) :point_left:

         <img src="static/graphics/readme/mockups/mockups-tablet.png" height="400px"/>

    - Desktop Mockups
        - [Unauthorised User](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/mockups/mockups-desktop-unauthorised.png) :point_left:
        - [Authorised User](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/mockups/mockups-desktop-authorised.png) :point_left:
        - [Admin](https://github.com/LigaMoon/swap-clothes-app/tree/main/static/graphics/readme/mockups/mockups-desktop-admin.png) :point_left:

         <img src="static/graphics/readme/mockups/mockups-desktop.png" height="400px"/>






## Features

### Existing Features

#### Common Features Across All Pages
- [x] **xxx** - xxx
    - xxx
    - xxx
- [x] **xxx**
    - xxx


### Specific to Pages
- [x] **xxx**
    - xxx


### Future Features
- [ ] xxx
        <img src="" />

- [ ] xxx



## Technologies Used

### Languages Used

- [xxx](xxx)


### Frameworks, Libraries and Programs Used
- [xxx](xxx) - xxx

<a name="#testing"></a>
## Testing

 ### Functionality Testing
- #### xxx
    - xxx
    - xxx

 

### HTML5 validator
- xxx - xxx - [Results](xxx)

### CSS3 validator - Pass


### JSHint validator
- xxx


### Usability Testing
- xxx

### Compatibility Testing
- Browser Compatibility

    | Screen size\Browser | Safari           | Opera            | Microsoft Edge   | Chrome           | Firefox          | Internet Explorer |
    | --------------------|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:-----------------:|
    | Mobile              |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| Not Tested        |
    | Tablet              |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| Not Tested        |
    | Laptop              |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| Not Tested        |
    | Desktop             |:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:|:heavy_check_mark:| Not Tested        |

- xxx

### Performance Testing
- xxx.
    - Home Page - [Results](xxx)
    - Constellations Page - [Results](xxx)
    - Zodiac Signs Page - [Results](xxx)
    - Calculator Page - [Results](xxx)

        <img src="" height="50px"/>


### Testing User Stories 
- #### xxx
    1. xxx
        - xxx
        - xxx
    1. xxx
        - xxx
        - xxx


<a name="deployment"></a>
## Deployment


<a name="bugs"></a>
## Known Bugs
- xxx



<a name="credits"></a>
## Credits

### Code :floppy_disk:
- xxx

### Content :book:

- xx


### Media :clapper:
- xx


### Acknowledgements

- xx



