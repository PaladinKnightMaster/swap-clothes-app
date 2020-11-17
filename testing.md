
<h1 align="center">SWAP your clothes - Testing</h1>

 <a href="https://clothes-swap-app.herokuapp.com/"><img src="./static/graphics/SWAP-logo.png" width="25px" /></a> :point_left: Live website

<a href="https://github.com/LigaMoon/swap-clothes-app"><img src="./static/graphics/readme/githublogo.png" width="25px" /></a> :point_left: GitHub Repository

<a href="https://github.com/LigaMoon/swap-clothes-app/blob/main/README.md"> :scroll: </a>  :point_left:  README.md file
 


## Table of Contents

1. [Functionality](#functionality)

1. [Validators](#validators)
    - [HTML5](#html5)
    - [CSS](#css)
    - [JSHint](#jshint)
    - [JSHint](#jshint)
    - [PEP8](#pep8)

1. [Compatibility](#compatibility)

1. [Performance](#performance)

1. [User Stories](#user-stories)

1. [Known Bugs](#known-bugs)

1. [Future Testing](#future-testing)


## Functionality Testing
- #### Navigation Bar
    - When the logo 'SWAP' located in the middle of the navigation bar is clicked, it brings the user to the Home Page. This has been tested on desktop, tablet, and mobile views and from all pages.
    - All links in the navbar are working and have been tested.
    - The hamburger menu appears on screen sizes smaller than 992px. When clicked/tapped, it expands to reveal page links. These have been tested and are working as expected.
    - The navigation bar stays at the top of the page on all screen sizes.
    - The navigation links change depending on if the user is authorized or not, this has been tested.
        - Authorised user - Home, Items, My Profile, Add Item, Log Out
        - Unauthorised user - Home, Items, Register, Log In
    - The hover effect and active class work on all navigation links.
- #### Footer
    - Footer is always located at the bottom of the page regardless of the content amount. This was tested by removing all content from any given page.
    - When the social links are clicked, they open the relevant social media page in a new tab.
    - When the 'About' link is clicked, it opens a modal that overlays the existing content.
    - When the 'Go to Top' button is clicked, it brings the user to the top of the page.
- #### Buttons
    - When a button is hovered over in a >992px screen size, it increases in size and has a shadow applied creating a 3D movement effect.
    - Home Button 'Get Started' brings an authorized user to the 'Register' page and authorized user to the 'Items' page.
    - All buttons have been tested and they bring the user to correct pages as indicated in the name of the button
- #### Redirect
    - When a new user completes registration he/she is redirected to the 'Items' page.
    - When an existing user logs in, they are redirected to the 'My Profile' page.
    - When a user adds a new item they are redirected to the 'Items' page.
    - When a user edits an item, they are redirected to the 'Items' page.
    - When a user 'likes'/'unlikes' an item, they are redirected to the page they were on when they liked/unliked the item.
    - When a user deletes or flags an item they are redirected to the page they were on when they performed the action.
- #### Item Cards
    - 'Like' button is displayed according to the user's authorization level
        - Unauthorised user - button is gray and inactive
        - Authorised user - if the user is the creator of the item, the like button is gray and inactive. Otherwise, the user will see an empty heart if they haven't liked the item and a filled heart if they have liked the item.
    - 'more' button opens a hidden Card component with additional information.
    - The 'x' button on the revealed component, closes it.
    - The '?' in the revealed component brings the user to an external sizing website in a new tab.
    - Creator's username and profile image are displayed on the left side of the footer. If the user in session has matched with the creator, the creator's username is colored and clickable. When clicked on, it reveals creator's social icons that can be clicked and open their social pages in a new tab.
    - Pencil icon is displayed only to the creator of the item and opened the 'Edit Item' page when clicked on.
    - Delete button is displayed only to the creator of the item and to the 'Admin' user if they haven't liked an item (the logic being that if an admin likes an item, there shouldn't be a reason why it has to be deleted). When clicked this button displays a pop-up modal created in sweetalert asking the user to confirm whether they wish to delete the item. If it is confirmed, the pop-up lets the user know that the item has been deleted and redirects them to the page they were on. If the action is canceled, the pop-up is closed and no further action is taken.
    - Flag button is displayed to all authorized users. An empty flag is displayed if the item hasn't been flagged by anyone and a red flag is displayed when any user has flagged this item. Any user can flag an item, 

## Validators

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


## Known Bugs
- xxx

## Future Testing