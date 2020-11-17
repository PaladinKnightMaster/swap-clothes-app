
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
    - Flag button is displayed to all authorized users. An empty flag is displayed if the item hasn't been flagged by anyone and a red flag is displayed when any user has flagged this item. Any user can flag an item, when clicked this button displays a pop-up modal created in sweetalert asking the user to confirm whether they wish to flag the item. If it is confirmed, the pop-up lets the user know that the item has been flagged and redirects them to the page they were on. If the action is canceled, the pop-up is closed and no further action is taken.
    Only admin can unflag an item.
-  #### External links
    -  All external links were tested to make sure they open up the correct pages in new tabs
    - All social links in the footer and item cards bring the user to the relevant social pages that open in a new tab.
- #### Internal links
    - All internal links were tested to make sure that all pages are correctly connected 
    - Navigation links bring the user to the relevant pages.
    - Brand word located in the navigation bar always brings the user to the home page.
    - Links connecting the 'Register' page to the 'Log In' page and vice versa work and have been tested.
    - Links directed to the 'Items' page located in the navbar, on the 'Home' page under Hot Items, on the 'My Profile' page under My Items, in the 'About' modal, work as expected and bring the user to the 'Items' page.
- #### Home Page
    - Likes counter works as expected and increments/decrements by 1 when a user likes/unlikes the item.
    - Top 3 items are displayed - this has been tested by many test accounts liking/unliking numerous items.
- #### Items Page
    - Pagination
        - Only 9 items are displayed at a time - this has been tested by adding more than 9 items.
        - Total number of items is displayed alongside the page numbers.
        - Pagination works when an item is sorted, filtered, or searched
    - Category Filter
        - When categories are selected and the user clicks 'Apply', the relevant categories are displayed.
        - Selected categories are styled bolder and a checkbox is ticked.
        - Users can select additional categories to already existing ones without having to re-select the previous categories.
        - Pagination works when categories have been filtered.
        - When 'Show All' is clicked, the filter is removed and all items are displayed.
    - Sort functionality
        - Unauthorised users can sort items by the most recently added, alphabetical order, and reverse alphabetical order.
        - Authorised user can additionally sort items to only their liked items and flagged items
        - All buttons sort items accordingly 
        - Pagination works with all sorting options
    - Search functionality
        - User can search for an item by typing what they are looking for and this keyword will be searched through item headings and item short descriptions
        - When Enter is pressed after focusing on the search input component, it defaults as search function.
        - When the reset button is clicked, all items are displayed.
    - If there are no items to be displayed following filtering or searching, a message is displayed letting the user know.
- #### Register/Edit Profile Page
    - Username and Password are required and form will not submit unless they have been entered in the required format.
    - Under both of those fields a character counter and the required length are displayed.
    - When the '?' is hovered over/clicked on, it provides the user with additional information of what characters are allowed
    - Optional fields provide styled validation but are not required and the form can be submitted without filling them out.
    - If a Profile picture hasn't been selected, the user is given a generic image.
    - When the 'Register' button is clicked, it adds user data to the users and matches collections, and redirects the user to the 'Items' page
    - The form can be edited after registering from the 'My Profile' page and allows the user to edit all optional fields at any time.
    - When the 'Edit Profile' button is clicked, it updated user data in the user's collection and redirects the user to the 'My Profile' page and a flash message is displayed.
    - When the 'Cancel' button is clicked, the user is redirected to the 'My Profile' page.
- #### Log In Page
    - When correct credentials are entered, the user is logged in and redirected to the 'My Profile' page
    - When incorrect credentials are entered, a flash message is displayed letting the user know.
- #### Log Out
    - When 'Log Out' is clicked, the user is removed from the session cookie and logged out.
    - Flash message is displayed.
- #### MyProfile Page
    - When 'Edit Profile' is clicked, the 'Edit Profile' page is displayed which functions as described under 'Register/Edit Profile Page'
    - If the user has no items to display under the 'My Items', 'Matched' or 'Suggestions' sections, short instructions, and a call-to-action button are displayed. This brings the user to the relevant page to progress their account.
    - Item Carousel
        - Displays 3 items on large screen sizes, 2 on medium, and 1 on small.
        - Carousel has arrow icons on large screen sizes, when clicked, lets the user navigate the items in the carousel.
        - On large screen sizes, the user can drag items to navigate the carousel.
        - On medium and small screen sizes, the user can swipe left/right to navigate the items.
        - Circle icons are displayed at the bottom of each carousel, letting the user know how many slides/items there are. These are clickable and allow the user to navigate items.
- #### Add Item/Edit Item Pages
    - All fields, apart from the picture link, are required and validated accordingly.
    - Item Name, Short Description, and Long Description have character count displayed under the input field.
    - Category, From, Fit, and Used fields have dropdowns that are validated accordingly.
    - When 'Add Item' is clicked, the data is added to the items collection and the user is redirected to the 'Items' page.
    - When 'Reset' is clicked, the form is reset and all fields are cleared.
    - 'Edit Item' page is pre-filled with the item details.
    - When 'Edit Item' is clicked, the item data is updated in the items collection and the user is redirected to the 'Items' page.
    - When 'Cancel' is clicked, the user is redirected to the 'Items' page.

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