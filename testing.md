
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

1. [Bugs](#bugs)
    - [Identified Bugs](#identified-bugs)
    - [Existing Bugs](#existing-bugs)

1. [Future Testing](#future-testing)


## Functionality
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
- #### Matching
    - Users can like items by clicking on the 'like' button.
    - When the creator of the item likes the user's item, they match.
    - A flash message is displayed at the top of the page explaining that the user can now click on the creator's username to reveal their social media details.
    - The user can click on the social media icons which bring the user to the relevant social media platform opened in a new tab.
    - The user can see all the matched items on the 'My Profile' page under Matches.


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


### User Stories

- #### Common user stories
    1. I want to intuitively navigate through the site to browse the content.
        - The landing page takes the whole screen with one call-to-action button which brings the user to the 'Register' or 'Items' page.
        - The footer and the header remain the same throughout the site which provides consistency for the user to easily understand how the site works.
        - The header and the footer are kept in line with conventional styles which lets the user access the navigation without thinking.
        - The header is always visible at the top of the page and the user can find each page easily at any time.
        - The active website is indicated by different formatting.
        - All pages are displayed in the navigation bar as well as throughout the pages to provide the user with multiple points of navigation.
        - The style is kept the same throughout the page to allow the user to intuitively understand how to navigate the page.
    1. I want the experience of using this site to be interactive.
        - All cards have like/unlike buttons.
        - Flash message feedback is provided to the user.
        - Delete/Flag confirmation is displayed as a pop-up.
        - About modal is displayed as a pop-up.
        - Items are positioned on the 'My Profile' page in a carousel, allowing the user to click/drag/swipe.
        - Item category filter has animated checkboxes.
    1. I want to be able to view all clothing items.
        - User view all items on the 'Items' page.
        - If the user has filtered or searched, they can view all items by clicking 'reset' or 'Show All'.
        - User is given a link to the 'Items' page in the 'About' modal, on the 'Home' page under Hot Items, on the 'My Profile' page under Matches.
    1. I want to be able to sort all items by the most recent added.
        - On the 'Items' page, under 'Sort' there is a clickable calendar icon that sorts all items by the most recently added.
        - Icon changes color when hovered over.
        - By default, all items are sorted by the most recently added.
    1. I want to be able to sort all items by alphabetical and reverse alphabetical order.
        - On the 'Items' page, under 'Sort' there is a clickable A-Z icon that sorts all items in alphabetical order.
        - Icon changes color when hovered over.
    1. I want to be able to filter items by their categories.
        - On the 'Items' page, under 'Sort' there is a clickable Z-A icon that sorts all items in reversed alphabetical order.
        - Icon changes color when hovered over.
    1. I want to be able to search for a specific item.
        - On the 'Items' page, under 'Search' there is a text input field where user can enter their search keyword.
        - Users can search by either pressing the 'Enter' key or clicking on the search button.
    1. I want to be able to understand the purpose of the site.
        - Landing Page has a short description of what the site is.
        - 'About' modal in the footer provides a more detailed description of what the page is about.
        - On the Landing Page, under the call-to-action button, there is a '?' icon which opens the 'About' modal.
    1. I want to be able to contact the owner of the site.
        - Footer contains creators socials that can be used to contact the creator.
    1. I want the page to be responsive to all screen sizes.
        - Page has been extensively tested to ensure it is responsive and works in all screen sizes.
    1. I want to be able to navigate to the top of the page quickly, particularly in the mobile view.
        - Footer contains a 'Go to top' button which brings the user to the top of the page.

- #### As a first time visitor
    1. I want to be able to find the 'Register' page easily.
        - The 'Register' page is located and clearly labeled in the navigation bar.
        - If the user clicks on the 'Log In' page instead, they can fid the 'Register' page link under the login form.
        - The call-to-action button on the landing page redirects the user to the 'Register' page.
    1. I want to be able to register easily
        - Form on the 'Register' paged is responsive and easy to use.
        - Only 2 fields are required which allows the user to register quickly.
        - Real-time feedback is provided to the user in form of the color around the input field. This saves time for the user as they can see if the value entered is correct/incorrect before submitting the form.
    
- #### As a returning user
    1. I want to be able to navigate to the 'Login' page easily.
        - The 'Log In' page is located and clearly labeled in the navigation bar.
        - If the user clicks on the 'Register' page instead, they can find the 'Log In' page link under the login form.
        - The call-to-action button on the landing page redirects the user to the 'Register' page which has the 'Log In' page link. 
        - If the user Logs Out, they are redirected to the login page in case they want to Log in again.
    1. I want to be able to Log In quickly.
        - The login form only contains 2 fields.
    1. I want to add new items easily.
        - The 'Add Item' page is located in the navigation bar and clearly labeled.
        - If the user doesn't have any items added, there will be a call-to-action button displayed on the 'My Profile' page under My Items. This will bring the user to the 'Add Item' page.
        - Real-time feedback is provided to the user in form of the color around the input field. This saves time for the user as they can see if the value entered is correct/incorrect before submitting the form.
        - The form can be easily reset by clicking on the 'Rese' button.
        - The form is responsive and easy to use.
    1. I want to be able to edit and delete my items.
        - Each Item card displays an edit button to the creator of the item which brings the user to the 'Edit Item' page.
        - Item details are pre-filled in the form to allow the user to quickly change the relevant fields.
        - Users can cancel editing items by clicking the 'Cancel' button.
        - Each item displays a delete button to the creator of the item.
        - When the delete button is clicked, the user is prompted with a confirmation. This prevents the user from accidentally deleting an item (especially relevant on mobile sizes as it is easier to click/tap on the wrong button)
    1. I want to like items.
        - All items that have not been created by the user, has a like action button.
        - Like button is formatted depending if the user has liked an item.
        - Like functionality is provided throughout the whole site.
    1. I want to be able to flag inappropriate content.
        - All items display a flag button that is formatted depending if the item has already been flagged.
        - When clicked on the flag icon, the user will be prompted to confirm if they wish to flag this item as inappropriate.
        - The user cannot unflag an item. This is to facilitate the moderation of inappropriate content.
    1. I want to see the items that I have liked.
        - The user can sort items by their liked items on the 'Items' page by clicking the heart icon.
    1. I want to be able to update my profile.
        - The 'My Profile' page has an 'Edit Profile' button just under the profile details.
        - If the user hadn't selected what items they are looking for when registering, they will also see an 'Edit Profile; button under Suggestions on the 'My Profile' page.
        - The form is pr-filled with details already entered but the user when registering. This saves time and allows the user to update only relevant fields.
    1. I want to view all my added items.
        - The user can view all their added items on the 'My Profile' page under My Items.
    1. I want to view all items I have matched with.
        - The user can view all the items they have matched with on the 'My Profile' page under My Items.
    1. I want to see items that matched the categories that I'm looking for.
        - The user can view suggested items based on the categories they re looking for on the 'My Profile' page under Suggestions
    1. I want to be able to contact another user if I match to swap the items.
        - When a user likes an item from a creator that has liked the user's item, they match. The user can then click on the creator's username which will display their social media icons.
        - Matched username is colored and has a hover effect to indicate that it is clickable.
        - When the user has matched, flash messages lets them know that they can contact another user by clicking on their username.
    1. I want to be able to Log out.
        - The 'Log Out' button is located in the navigation bar and labeled clearly

- #### As an admin
    1. I want to be able to unflag an item if it's been flagged incorrectly.
        - Admin user has additional functionality to unflag items.
        - This is done by clicking the flagged items flag button.
    1. I want to be able to delete an item if it's inappropriate.
        - Admin has the additional functionality to delete items that haven't liked.
        - The delete icon is displayed on all unliked items.ms that haven't liked.
        - The delete icon is displayed on all unliked items.


## Bugs :beetle:
1. ### Identified bugs
    - Not retrieving information from MongoDB with an 'ERR_TOO_MANY_REDIRECTS' error.
        - This was caused due to some passwords being hashed and some that were added to the database before authentification.
        - This was fixed by deleting the first dummy accounts from the database/
    - Filtered item pagination not working when the user clicks on pages 2 and onwards
        - This was caused by the filter form trying to resubmit when the user clicks on pages 2 and onwards. Due to form/item filter not being filled in each time the user selects a new page, it would return 'No results found'
        - This was solved by changing the form method to `GET` instead of `POST` and using query strings alongside with `request.args.get`
    - Page breaking when the user likes a searched item
        - This happened as the user is redirected to the page they were on when they like an item and in this instance the 'search' page. Search functionality relies on the input string and as the user would be redirected to the same page, the search string would come back as None, breaking the page.
        - This was solved by changing the form method to `GET` instead of `POST` and using query strings alongside with `request.args.get`
    - On mobile, the dropdown options onclick does not fire when "clicked/tapped".
        - This is an identified bug within the materialize community as described in this [GitHub Post](https://github.com/Dogfalo/materialize/issues/6449)
        - The fix was implemented by manually adding a [select.js](https://github.com/LigaMoon/swap-clothes-app/blob/main/static/js/select.js) file with a fix coded into it as provided by this [solution by Dogfalo](https://github.com/Dogfalo/materialize/commit/c0da34049deec36efbd4681f73b3446e92918ca8)
2. ### Existing Bugs
    - No known existing bugs.


## Future Testing
- Automated testing using testing frameworks such as Jasmine will be implemented in future versions.