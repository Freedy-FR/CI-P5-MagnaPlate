# MagnaPlate - Introduction

Welcome to the code repository for the "Magnaplate" E-commerce Store; a platform that not only showcases the magnetic poster products but also enables customers to purchase them online.

This project is highly relevant as the trend of online shopping continues to grow, with people increasingly looking to buy all sorts of items online, including unique and customizable decor items like magnetic posters. The website’s flexible design makes it suitable for any e-commerce business that requires customers to make purchases using a credit card before receiving the products.
<br>

[Live Project Here](https://magnaplate-3f8ee7baac73.herokuapp.com/)

<p align="center"><img src="assets/readme/amiresponsive/amiresponsive.webp" alt="MagnaPlate webpage on multiple devices"></p>

README Table Content

- [MagnaPlate - Introduction](#)
  - [User Experience - UX](#user-experience---ux)
    - [User Stories](#user-stories)
    - [Agile Methodology](#agile-methodology)
    - [The Scope](#the-scope)
      - [Main Site Goals](#main-site-goals)
  - [Design](#design)
    - [Colours](#colours)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Carousel](#carousel)
    - [Wireframes](#wireframes)
  - [Database Diagram](#database-diagram)
  - [Features](#features)
    - [Landing Page](#landing-page)
    - [Home Page - Images Carousel](#home-page---images-carousel)
    - [Home Page - Selected Products](#home-page---selected-products)
    - [Home Page - Image Banner](#home-page---image-banner)
    - [Home Page - Customers Reviews Carousel](#home-page---customers-reviews-carousel)
    - [Products Page](#products-page)
    - [Products Details](#products-details)
    - [Products Details - Features](#products-details---features)
    - [Products Details - Products on Sale](#products-details---products-on-sale)
    - [Products Shopping cart](#products-shopping-cart)
    - [Products Shopping cart - Products Coming Soon](#products-shopping-cart---products-coming-soon)
    - [Products Checkout](#products-checkout)
    - [Products Checkout - Success](#products-checkout---success)
    - [Products Management](#products-management)
    - [Profile Page](#profile-page)
      - [Service Reviews Page](#service-reviews-page)
      - [Add/Edit Service Review Page](#addedit-service-review-page)
    - [Signup Page](#signup-page)
    - [Signup Page - Verify Email](#signup-page---verify-email)
    - [Signup Page - Confirm Email](#signup-page---confirm-email)
    - [Login Page](#login-page)
    - [Logout Page](#logout-page)
    - [Reset Password Page](#reset-password-page)
    - [Change Password Page](#change-password-page)
    - [Navbar](#navbar)
    - [Footer](#footer)
    - [Page 404 - Page Not Found](#page-404---page-not-found)
  - [Messages and Interaction with Users](#messages-and-interaction-with-users)
    - [Sign up 1](#sign-up-1)
    - [Sign up 2](#sign-up-2)
    - [Login](#login)
    - [Logout](#logout)
    - [Profile Update](#profile-update)
    - [Service Review - Add Review](#service-review---add-review)
    - [Service Review - Update Review 1](#service-review---update-review-1)
    - [Service Review - Update Review 2](#service-review---update-review-2)
    - [Service Review - Delete Review 1](#service-review---delete-review-1)
    - [Service Review - Delete Review 2](#service-review---delete-review-2)
    - [Service Review - Delete Review 3](#service-review---delete-review-3)
    - [Add Product](#add-product)
    - [Edit Product 1](#edit-product-1)
    - [Edit Product 2](#edit-product-2)
    - [Edit Product 3](#edit-product-3)
    - [Delete Product 1](#delete-product-1)
    - [Delete Product 2](#delete-product-2)
    - [Delete Product 3](#delete-product-3)
    - [Add Product to cart](#add-product-to-cart)
    - [Update cart](#update-cart)
    - [Remove Product from cart](#remove-product-from-cart)
    - [Purchase Success](#purchase-success)
    - [Purchase Success - Confirmation Email](#purchase-success---confirmation-email)
  - [Admin Panel / Superuser](#admin-panel--superuser)
  - [Marketing and Social Media](#marketing-and-social-media)
    - [Statista - Facebook Users](#statista---facebook-users)
    - [MagnaPlate - Facebook Page](#facebook-page)
    - [Meta Pixel - Tracking Audience](#meta-pixel---tracking-audience)
    - [Mailchimp Subscription Service](#mailchimp-subscription-service)
  - [Privacy Policy](#privacy-policy)
  - [Search Engine Optimization](#search-engine-optimization)
    - [sitemap.xml](#sitemapxml)
    - [robots.txt](#robotstxt)
    - [Sitemap Google Registration](#sitemap-google-registration)
  - [AWS Setup Process](#aws-setup-process)
    - [AWS S3 Bucket](#aws-s3-bucket)
    - [IAM Set Up](#iam-set-up)
    - [Connecting AWS to the Project](#connecting-aws-to-the-project)
  - [Stripe Payments](#stripe-payments)
    - [Payments](#payments)
    - [Webhooks](#webhooks)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Django Packages](#django-packages)
    - [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
    - [Testing](#testing)
  - [Creating the Django app](#creating-the-django-app)
  - [Deployment of This Project](#deployment-of-this-project)
  - [Final Deployment](#final-deployment)
  - [Forking This Project](#forking-this-project)
  - [Cloning This Project](#cloning-this-project)
  - [Credits](#credits)
    - [Content](#content)
    - [Information Sources / Resources](#information-sources--resources)
  - [Special Thanks](#special-thanks)

## User Experience - UX

### User Stories

#### As a Site User
| id  |  Content | Label |
| ------ | ------ | ------ |
| [2](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/2) | As a Site User, I can view top navigation for easy access to website main functions. | Must Have |
| [3](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/3) | As a Site User, I can view the main navigation for easy access to products and deals. | Must Have |
| [4](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/4) | As a Site User, I can register, log in, and log out to access the main features of the website. | Must Have |
| [5](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/5) | As a Site User, I can use a search system for easy access to specific products and deals. | Must Have |
| [6](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/6) | As a Site User, I can view a carousel of images on the main page to see the main deals and collections. | Should Have |
| [7](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/7) | As a Site User, I can view detailed product information, images, and options to buy or add to favorites. | Must Have |
| [8](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/8) | As a Site User, I can add products to a favorites page for easy access to my favorite products. | Must Have |
| [9](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/9) | As a Site User, I can add products to the shopping cart, view purchase details, and complete the purchase. | Must Have |
| [10](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/10) | As a Site User, I can sign up for a newsletter to receive email updates about new products. | Should Have |
| [11](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/11) | As a Site User, I can access my account profile page to manage personal information and preferences. | Must Have |
| [12](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/12) | As a Site User, I can access the order management page to review and manage previous orders. | Must Have |
| [13](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/13) | As a Site User, I can add products to the cart, preparing for purchase. | Must Have |
| [14](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/14) | As a Site User, I can edit the contents of their shopping cart, including updating quantities. | Must Have |
| [15](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/15) | As a Site User, I can remove items from their shopping cart. | Must Have |
| [16](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/16) | As a Site User, I can view a paginated list of products to easily select a product for viewing. | Must Have |
| [17](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/17) | As a Site User, I can switch between dark and light themes for optimal viewing in different lighting environments. | Could Have |
| [18](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/18) | As a Site User, I can see site notifications to receive feedback on my actions. | Should Have |
| [19](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/19) | As a Site User, I have the option to leave product reviews and ratings. | Could Have |
| [24](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/24) | As a Site User, I can view a footer for easy access to website functions. | Must Have |
| [25](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/25) | As a Site User, I can use a sorting system for easy access to specific products and deals. | Must Have |
| [30](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/30) | As a Site User, I can access the Carousel management page to review and manage the images and text on the carousel. | Should Have |
| [31](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/31) | As a Site User, I can see a list of all creators and click on them to see more details and their related products. | Must Have |
| [32](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/32) | As a Site User, I want the project's style to be consistent across all pages and components, so that the user experience is seamless and professional. | Should Have |

#### As a Site Admin
| id  |  Content | Label |
| ------ | ------ | ------ |
| [20](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/20) | As a Site Admin, I can process payments using the Stripe gateway. | Must Have |
| [21](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/21) | As a Site Admin, I can add new products to the website's database. | Must Have |
| [22](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/22) | As a Site Admin, I can delete products from the website's database. | Must Have |
| [23](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/23) | As a Site Admin, I can edit and update product information in the website's database. | Must Have |
| [26](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/26) | As a Site Admin, I can add, remove or edit collections to the website's database. | Must Have |
| [28](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/28) | As a Site Admin, I can add, remove or edit creators to the website's database. | Must Have |
| [29](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/29) | As a Site Admin, I can add, remove or edit categories to the website's database. | Must Have |
| [40](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/40) | As a Site Admin, I can manage product collections. | Must Have |
| [41](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/41) | As a Site Admin, I can edit products in the database. | Must Have |
| [42](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/42) | As a Site Admin, I can delete products from the database. | Must Have |
| [43](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/43) | As a Site Admin, I can add products to the database. | Must Have |
| [44](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/44) | As a Site Admin, I can process payments using Stripe. | Must Have |

#### As a Developer
| id  |  Content | Label |
| ------ | ------ | ------ |
| [33](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/33) | As a Developer, I want the codebase to follow consistent coding standards, so that it is easy to maintain, understand, and collaborate on. | Must Have |
| [34](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/34) | As a Developer,I want to implement SEO best practices on our website,so that the website ranks higher in search engine results and attracts more organic traffic. | Must Have |
| [35](https://github.com/Freedy-FR/CI-P5-MagnaPlate/issues/35) | As a Developer, I want a comprehensive documentation system so that it is easy to understand, maintain, and collaborate on the codebase. | Documentation Implementation |


### Agile Methodology

The agile planning approach was employed in the development of this site, wherein each user feature was broken down into individual user stories, each accompanied by specific acceptance criteria. These criteria were then translated into tasks, serving as markers of completion for the respective user stories.

To enhance functionality, interconnected user stories that contributed to specific site features were grouped into broader Epics. User stories were categorized as Must Have, Should Have, or Could Have, aiding in prioritization during the implementation process.

As the site evolved, tasks were refined or adapted based on changing user needs and a more mature understanding of project requirements. GitHub Issues and the Kanban board within the GitHub Projects view served as the structural framework. The project was organized into several sections:

* To Do - Serving as the initial repository for all user stories.
* In Progress - Active development stories were tracked in this phase.
* Done - Successfully developed stories found their place here.
* Future - This section was reserved for 'could have' stories containing features earmarked for potential implementation at a later stage due to time limitations.

Feel free to explore the Kanban Board for a visual representation of the user stories [here](https://github.com/users/Freedy-FR/projects/6).

### The Scope

#### Main Site Goals

- To provide users with comprehensive information about the products, including detailed product information, images, and options to buy or add to favorites.
- To provide users with a visually pleasing website that is intuitive and easy to navigate, with clear and consistent navigation options.
- To provide a website with a clear purpose, ensuring that users can easily access key functionalities such as account management, order management, and product browsing.
- To provide tools that allow users to search for products, including a search system and sorting options for easy access to specific products and deals.
- To provide users with an easy and safe way to buy their products, ensuring secure payment processing through Stripe, a well-organized shopping cart system, and clear checkout procedures.


## Design

### Colour Scheme for MagnaPlate Website

The Colour scheme for the MagnaPlate website was meticulously selected to enrich the visual appeal of the plates (posters) and provide an engaging user experience. The Colours were chosen from [Coolors](https://coolors.co/), ensuring a harmonious blend that enhances the aesthetic quality of the site.

#### Colour Palette:

- **FBFBFB (White)**: This bright, clean shade is used for the background, offering a crisp and neutral canvas that makes other Colours and content stand out.

- **EEEEEE (Light Gray)**: A soft, light gray tone that adds subtle depth and contrast to the design elements without overpowering them.

- **4F4F4F (Medium Gray)**: Used for text and secondary elements, this medium gray ensures readability and complements the overall Colour scheme.

- **000000 (Black)**: The primary Colour for text, providing strong contrast and excellent legibility against the white and light gray backgrounds.

- **2846A1 (Dark Blue)**: This deep blue shade is employed in headers and key navigation elements, evoking a sense of trust and stability.

- **1C4AB2 (Blue)**: A vibrant blue used for links and call-to-action buttons, drawing attention without being too aggressive.

- **133398 (Navy Blue)**: Incorporated in the logo and other prominent elements, this navy blue adds a touch of professionalism and sophistication.

- **B81916 (Red)**: This bold red is used sparingly to highlight important information and create a sense of urgency or importance.

- **A10F0D (Dark Red)**: A darker red shade that complements the bold red, adding depth and visual interest to the design.

The use of these Colours has been consistently maintained throughout the website and checked for contrast to allow easy accessibility. The combination of these carefully selected Colours ensures that the MagnaPlate website is not only visually appealing but also user-friendly and accessible to all visitors.


<details><summary>Colour palette</summary>
<img src="assets/readme/design/design-colours.webp">
</details>
<br>


### Typography

[Google Fonts](https://fonts.google.com/) were used as below:

* Galada is used for the Logo.
* Signika Negative is used for the Headings.
* Roboto is used for the body of the text.

### Imagery

The MagnaPlate website relies on thumbnails to render nice images, enhancing both efficiency and aesthetics. Thumbnails are rendered on the products page to help with quick loading times, while the product detail pages display the full image. Users also have the option to view images in full screen using [fslightbox](https://fslightbox.com), allowing them to see every detail clearly.

The images and placeholders were sourced from [Pexels](https://www.pexels.com/) and some images were generated using AI with ChatGPT, while the Favicon icon was obtained from [Favicon](https://favicon.io/). Some of the images have also been sourced from a Discord group, noted in the credits.

### Carousel

The carousel on the MagnaPlate website serves as a dynamic and engaging feature to showcase key highlights and promotions. The design of the carousel includes the following elements:

- **Responsive Design**: The carousel is fully responsive, ensuring it looks great on all devices, from desktops to mobile phones.

- **High-Quality Thumbnails**: Each slide in the carousel displays a high-quality thumbnail image, providing a preview of the featured content.

- **Gradient Background**: The gradient background transitions smoothly between shades of blue and red, creating a visually appealing backdrop that enhances the displayed images.

- **Navigation Arrows**: Discreet navigation arrows are placed on either side of the carousel, allowing users to easily browse through the slides.

- **Featured Content**: The carousel prominently features key promotional images, such as new arrivals, special offers, and featured collections, to draw attention and engage users.

- **Efficiency and Aesthetics**: Thumbnails are used in the carousel to maintain quick loading times and enhance the aesthetic appeal of the website.

The use of the carousel helps to keep the website dynamic and interactive, providing users with a visually rich experience that highlights important content and promotions effectively.


### Wireframes

Wireframes were created for desktop/laptop, tablet and mobile.

<details><summary>Home</summary>
<img src="assets/readme/wireframes/Home.webp">
</details>

<details><summary>Products</summary>
<img src="assets/readme/wireframes/Products.webp">
</details>

<details><summary> Products Detail</summary>
<img src="assets/readme/wireframes/Products Detail.webp">
</details>

<details><summary>Cart</summary>
<img src="assets/readme/wireframes/Cart.webp">
</details>

<details><summary>My Profile - Basic Information</summary>
<img src="assets/readme/wireframes/My Profile - Basic Info.webp">
</details>

<details><summary>My Profile - Shipping Address</summary>
<img src="assets/readme/wireframes/My Profile - Shipping.webp">
</details>

<details><summary>My Profile - Orders</summary>
<img src="assets/readme/wireframes/My profile - Order.webp">
</details>

<details><summary>Admin - Product Management</summary>
<img src="assets/readme/wireframes/Admin - Product Management.webp">
</details>




## Magna Plate Database

The project encompasses a variety of models for managing orders, favorites, newsletters, carousels, products, and user profiles. Below is an overview of these models, categorized by their functionality. In total, there are 13 models, with 10 being custom models.



### **Summary**

In total, there are **13 models**:
- **10 Custom Models**:
  - `FavoriteProduct`
  - `FavoriteCreator`
  - `NewsletterSubscribedInfo`
  - `NewsletterSendEmail`
  - `CustomerSupportInquiry`
  - `Carousel`
  - `Collection`
  - `Category`
  - `Creator`
  - `UserProfile`
- **3 Non-Custom Models**:
  - `Order`
  - `OrderLineItem`
  - `Product`

### Database Diagram

<details><summary>Magna Plate Database</summary>
<img src="assets/readme/database/magna_database.webp">
</details>

#### Checkout

**Order Model**

The `Order` model records all relevant details about a user's order.

- `order_number` - Unique identifier for the order.
- `user_profile` - ForeignKey to the `UserProfile` model.
- `full_name` - User's full name.
- `email` - User's email.
- `delivery_phone_number` - User's phone number for delivery.
- `country` - User's country (using `CountryField`).
- `postcode` - Postal code of the delivery address.
- `town_or_city` - Town or city of the delivery address.
- `street_address1` - First line of the street address.
- `street_address2` - Second line of the street address.
- `county` - County of the delivery address.
- `date` - Date and time when the order was placed.
- `delivery_cost` - Cost of delivery.
- `order_total` - Total cost of items in the order.
- `grand_total` - Total cost including delivery.
- `original_cart` - JSON representation of the original shopping cart.
- `stripe_pid` - Stripe payment intent ID.

**OrderLineItem Model**

The `OrderLineItem` model details the specific items within an order.

- `order` - ForeignKey to the `Order` model.
- `product` - ForeignKey to the `Product` model.
- `product_size` - Size of the product.
- `quantity` - Quantity of the product.
- `lineitem_total` - Total price for the line item.

---

#### Favorites

**FavoriteProduct Model** ---- > Custom model

Tracks a user's favorite products.

- `user` - ForeignKey to the `User` model.
- `product` - ForeignKey to the `Product` model.
- `is_favorite` - Whether the product is marked as a favorite.
- `created_at` - Timestamp of when the favorite was created.

**FavoriteCreator Model** ---- > Custom model

Tracks a user's favorite creators.

- `user` - ForeignKey to the `User` model.
- `creator` - ForeignKey to the `Creator` model.
- `is_favorite` - Whether the creator is marked as a favorite.
- `created_at` - Timestamp of when the favorite was created.

---

#### Footer

**NewsletterSubscribedInfo Model** ---- > Custom model

Stores information about newsletter subscribers.

- `name` - Subscriber's name.
- `email` - Subscriber's email address.
- `created_at` - Timestamp of subscription.

**NewsletterSendEmail Model** ---- > Custom model

Details for sending out newsletter emails.

- `subject` - Subject of the email.
- `body` - Body content of the email.
- `created_at` - Timestamp when the email was created.
- `send_now` - Flag to indicate if the email should be sent immediately.
- `recipients` - ManyToManyField to `NewsletterSubscribedInfo`.
- `letter_sent` - Indicates whether the email has been sent.

**CustomerSupportInquiry Model** ---- > Custom model

Handles customer support inquiries.

- `name` - Name of the person making the inquiry.
- `email` - Email address of the person making the inquiry.
- `subject` - Subject of the inquiry.
- `message` - Detailed message of the inquiry.
- `enquiry_type` - Type of inquiry (e.g., Order, Product, Shipping).
- `order_number` - Order number related to the inquiry (optional).
- `ticket_number` - Unique ticket number for the inquiry.
- `created_at` - Timestamp of when the inquiry was created.

---

#### Home

**Carousel Model** ---- > Custom model

Represents items in the homepage carousel.

- `image` - Image associated with the carousel item.
- `link` - URL link for the carousel item.
- `caption` - Caption for the carousel item.
- `order` - Order of the carousel item.

---

#### Products

**Collection Model** ---- > Custom model

Represents a collection of products.

- `name` - Name of the collection.
- `friendly_name` - Friendly name of the collection.

**Category Model** ---- > Custom model

Represents a category of products.

- `name` - Name of the category.
- `friendly_name` - Friendly name of the category.
- `collection` - ForeignKey to the `Collection` model.

**Creator Model** ---- > Custom model

Details about creators of products.

- `name` - Name of the creator.
- `image` - Image of the creator.
- `description` - Description of the creator.

**Product Model**

Represents an individual product in the store.

- `category` - ForeignKey to the `Category` model.
- `collection` - ForeignKey to the `Collection` model.
- `creator` - ForeignKey to the `Creator` model.
- `sku` - Unique stock keeping unit.
- `name` - Name of the product.
- `description` - Product description.
- `has_sizes` - Indicates if the product has size options.
- `size` - Size of the product (if applicable).
- `rating` - Product rating.
- `image_url` - URL of the product image.
- `image` - Image of the product.
- `thumbnail` - Thumbnail image of the product.
- `price` - Price of the product.
- `is_on_deal` - Indicates if the product is on deal.
- `created_at` - Timestamp when the product was created.

---

#### Profile

**UserProfile Model** ---- > Custom model

Stores additional information about a user.

- `user` - OneToOneField to the `User` model.
- `default_contact_full_name` - User's default contact full name.
- `default_contact_email` - User's default contact email.
- `default_contact_phone_number` - User's default contact phone number.
- `default_delivery_phone_number` - User's default delivery phone number.
- `default_country` - User's default country (using `CountryField`).
- `default_postcode` - User's default postal code.
- `default_town_or_city` - User's default town or city.
- `default_street_address1` - User's default street address (line 1).
- `default_street_address2` - User's default street address (line 2).
- `default_county` - User's default county.

---


## Features

### Home Page - Images Carousel

- The home page includes a carousel showcasing images at the top, which can be used for promotions, highlights, or important announcements.<br>

<details><summary>Home Page - Images Carousel</summary>
<img src="assets/readme/features/01-feature-carousel.gif">
</details>

### Home Page - Deals

- - The Deals section features products with discounted prices or special promotions, displayed at random to ensure a fresh and varied selection each time users visit.<br>

<details><summary>Home Page - Deals</summary>
<img src="assets/readme/features/02-feature-home-deals.webp">
</details>

### Home Page - Products

- The Products section on the home page highlights a selection of featured items, new arrivals, or top sellers, offering users a quick view of popular and interesting products.<br>

<details><summary>Home Page - Products</summary>
<img src="assets/readme/features/03-feature-home-products.webp">
</details>

### Home Page - Image Banner

- Features a prominent image banner that can be used for announcements or promotions.<br>

<details><summary>Home Page - Image Banner</summary>
<img src="assets/readme/features/04-feature-home-banner.webp">
</details>

### Home Page - Main Navigation Bar

- The Main Navigation Bar provides easy access to all key sections of the website. It includes links to All Plates, Collections, Categories, Creators, and Special Offers.
 Additionally, it features a search bar for quick product searches, a user account icon for profile access, and a shopping cart icon displaying the current cart total. This intuitive navigation bar ensures users can effortlessly explore and navigate the website.<br>

<details><summary>Home Page - Main Navigation Bar</summary>
<img src="assets/readme/features/04-1-feature-main-navigation-bar.gif">
</details>

### Search Bar

- The Search Bar allows users to quickly find products, collections, categories, and creators on the MagnaPlate website. Located prominently at the top of the page, it provides an easy way for users to navigate and discover specific items they are looking for by entering keywords or phrases.

<details><summary>Search Bar</summary>
<img src="assets/readme/features/04-2-feature-main-navigation-search.gif">
</details>


### Products Page

- Displays a comprehensive list of all available products with filtering and sorting options.<br>

<details><summary>Products Page</summary>
<img src="assets/readme/features/05-feature-products.webp">
</details>

### Products Page - Sorting

- Allows users to organize products by various criteria such as price, popularity. This feature helps users find what they're looking for more efficiently.<br>

<details><summary>Products Page - Sorting</summary>
<img src="assets/readme/features/06-feature-products-sorting.gif">
</details>

### Products Page - Hover Overlay (Laptops/Desktops)

- Displays additional product details or actions when users hover over a product image. This overlay enhances user interaction by providing quick access to essential information.<br>

<details><summary>Products Page - Hover Overlay</summary>
<img src="assets/readme/features/07-feature-products-hover.gif">
</details>

### Product Details

- The Product Details page offers a comprehensive view of each product. Users can see high-resolution full screen images, detailed descriptions, user ratings, and prices. It also provides options to select size and quantity before adding items to the cart. Additionally, the page includes tabs for detailed specifications and shipping information to ensure users have all necessary details. This dynamic presentation enhances the shopping experience by providing a thorough overview of each product.<br>

<details><summary>Product Details</summary>
<img src="assets/readme/features/08-feature-product-detail.gif">
</details>

### All Creators Page

- The All Creators page showcases all the artists and creators featured on the platform. Users can browse through the list of creators, view their profiles, and explore their collections. This page provides an excellent way to discover new artists and follow their work, enhancing the community and diversity of the platform.<br>

<details><summary>All Creators Page</summary>
<img src="assets/readme/features/08-1-feature-all-creators.gif">
</details>

### Creators Details

- The Creators Details page provides an in-depth look at individual creators. Users can learn more about each creator, view their biography, and explore the collections and products they have created. This page helps users connect with the creators and gain insight into their artistic journey and inspirations.<br>

<details><summary>Creators Details</summary>
<img src="assets/readme/features/08-2-feature-creators-details.gif">
</details>

### Shopping Cart

- The Shopping Cart page allows users to review the items they intend to purchase. It displays product images, names, sizes, SKUs, prices, and quantities. Users can update quantities or remove items directly from the cart. The page also shows the subtotal, delivery cost, and grand total, with options to continue shopping or proceed to secure checkout. This dynamic interface ensures a smooth and efficient shopping experience.<br>

<details><summary>Shopping Cart</summary>
<img src="assets/readme/features/09-feature-shopping-cart.gif">
</details>

### Checkout

- The Checkout page allows users to review their order, enter delivery and payment details, and complete their purchase. Users can see a summary of items in their cart, fill in their shipping information, and input payment details securely. This streamlined process ensures a smooth and efficient checkout experience, helping users finalize their orders with ease.<br>

<details><summary>Checkout</summary>
<img src="assets/readme/features/10-feature-checkout.gif">
</details>


### Checkout - Success

- The Checkout Success page confirms that the user's purchase has been completed successfully. It displays an order summary, including product details, sizes, quantities, and subtotals. Additionally, it provides delivery information and the total amount charged. This page reassures users that their order has been processed and includes all relevant details for their reference.<br>

<details><summary>Checkout - Success</summary>
<img src="assets/readme/features/11-feature-checkout-success.gif">
</details>


### Site Management (Site Admin)

- The Site Management section allows administrators to manage various aspects of the website, including products, collections, categories, and special offers. It provides a user-friendly interface for adding, editing, or removing items, ensuring the site remains up-to-date and engaging. This section is essential for maintaining the content and overall functionality of the site.<br>

<details><summary>Site Management</summary>
<img src="assets/readme/features/13-feature-site-management.gif">
</details>


### Profile Page

- The Profile Page allows users to view and update their personal information and check order history. Users can edit their contact details, manage their delivery addresses, and review their past orders. This section ensures that users can easily keep their profile information current and track their purchases.<br>

<details><summary>Profile Page</summary>
<img src="assets/readme/features/14-feature-profile-page.gif">
</details>


#### My Favorites

- The My Favorites section allows users to save and manage their favorite products and creators for easy access later. Users can quickly view and navigate to their preferred items and creators, making it convenient to revisit what they are interested in. This feature enhances the shopping experience by enabling users to curate a personalized collection of their favorite products and creators.<br>


<details><summary>My Favorites</summary>
<img src="assets/readme/features/15-feature-favorites-page.gif">
</details>

<details><summary>My Favorites - Add Products</summary>
<img src="assets/readme/features/15-1-feature-favorites-products.gif">
</details>

<details><summary>My Favorites - Add Creators</summary>
<img src="assets/readme/features/15-2-feature-favorites-creators.gif">
</details>

### Register Page

- The Register Page allows new users to create an account by providing their personal details such as name, email, and password. This page ensures a smooth sign-up process, enabling users to quickly join the platform and start enjoying its features.<br>

<details><summary>Register Page</summary>
<img src="assets/readme/features/16-feature-register-page.webp">
</details>

### Register Page - Verify Email

- The Verify Email page is part of the registration process, where users are required to verify their email address to complete the signup. This step ensures that the email provided is valid and helps in securing the user's account.<br>

<details><summary>Register Page - Email</summary>
<img src="assets/readme/features/16-1-feature-register-verify.webp">
</details>

<details><summary>Register Page - Verify Email</summary>
<img src="assets/readme/features/16-2-feature-register-verify.gif">
</details>


### Register Page - Confirm Email

- The Confirm Email page is shown after a user verifies their email address. This page confirms that the email address has been successfully verified, completing the registration process and allowing the user to access all the features of the platform.<br>

<details><summary>Register Page - Confirm Email</summary>
<img src="assets/readme/features/16-3-feature-register-confirm.gif">
</details>


### Login Page

- The Login Page allows existing users to log in to their account by entering their email and password. This page ensures secure access to user accounts, enabling them to manage their profiles, view order history, and make purchases.<br>

<details><summary>Login Page</summary>
<img src="assets/readme/features/17-feature-login-page.gif">
</details>

### Logout Page

- The Logout Page is shown after a user logs out of their account. This page confirms that the user has successfully logged out, providing options to return to the home page or log back in.<br>

<details><summary>Logout Page</summary>
<img src="assets/readme/features/18-feature-logout-page.gif">
</details>

### Footer

- The footer section contains additional links to various parts of the website, contact information, and other relevant details. It provides quick access to important sections such as Home, About Us, Products, Deals, and support pages like FAQ and Customer Support. The footer also includes social media links for easy navigation to the website's social media profiles. Additionally, there is a subscription form for the newsletter, allowing users to stay updated with the latest news and offers.<br>

<details><summary>Footer</summary>
<img src="assets/readme/features/19-feature-footer.webp">
</details>


### About Us

- The About Us page provides an overview of MagnaPlate's mission, history, and core values. Learn about our dedication to revolutionizing wall decoration with innovative metallic posters, our journey since our founding in 2024, and the principles that guide our work.<br>

<details><summary>About Us</summary>
<img src="assets/readme/features/20-feature-footer-aboutus.gif">
</details>

### FAQ Page

- The FAQ page provides answers to the most frequently asked questions about MagnaPlate's products, services, and policies. This section is designed to help users find quick solutions to common issues and learn more about our offerings.<br>

<details><summary>FAQ Page</summary>
<img src="assets/readme/features/21-feature-footer-faq.gif">
</details>

### Customer Support Page

- The Customer Support Page provides a form for users to fill out if they have any questions or need assistance. Users can enter their name, email, subject, and message. After submission, they will receive a confirmation with a ticket number for tracking their request.

<details><summary>Customer Support Page</summary>
<img src="assets/readme/features/22-1-feature-footer-customer.gif">
</details>

<details><summary>Customer Support Confirmation</summary>
<img src="assets/readme/features/22-2-feature-footer-customer-confirmation.gif">
</details>

### Contact Us Page

- The Contact Us Page allows users to get in touch with our support team for any inquiries or issues. Users can fill out their details and submit their message through the provided form.

<details><summary>Contact Us Page</summary>
<img src="assets/readme/features/23-feature-footer-contactus.gif">
</details>

### Social Media

- Our social media section allows you to stay connected and engaged with MagnaPlate. Follow us on various platforms for the latest updates, exclusive promotions, and exciting news about our innovative products.

<details><summary>Social Media</summary>
<img src="assets/readme/features/24-feature-footer-social.gif">
</details>

### Newsletter Section

- The newsletter section in the footer of MagnaPlate's website allows users to stay connected with the latest updates, special promotions, and exclusive offers. By subscribing, you can receive timely notifications about new arrivals and exciting deals directly in your inbox. Enter your email address in the footer section to join our community and never miss out on any important updates from MagnaPlate.

<details><summary>Newsletter Section</summary>
<img src="assets/readme/features/25-feature-footer-newsletter.gif">
</details>

### 404 Error Page

- The 404 Error Page is displayed when a user tries to access a page that does not exist on the MagnaPlate website. This page informs the user that the requested page could not be found and provides navigation options to help them return to the main site or find what they are looking for.

<details><summary>404 Error Page</summary>
<img src="assets/readme/features/26-feature-404.webp">
</details>


## Site Management - Features


### Product Management - Add Product

- The Product Management section allows admins to manage the product listings on the MagnaPlate website. This includes adding new products, editing existing ones, or deleting products that are no longer available. This section ensures that the product catalog is always up to date and accurately reflects the inventory.

<details><summary>Product Management - Add Product</summary>
<img src="assets/readme/feature-admin/01-admin-feature-add-product.gif">
</details>


### Product Management - Edit Product

- The Product Management section also enables admins to edit existing products. This feature allows for modifications to product details, such as updating descriptions, changing prices, adjusting inventory levels, and more. This functionality ensures that all product information is current and accurate.

<details><summary>Product Management - Edit Product</summary>
<img src="assets/readme/feature-admin/02-admin-feature-edit-product.gif">
</details>


### Product Management - Delete Product

- The Product Management section also provides the functionality for admins to delete products. This feature allows for the removal of products that are no longer available or needed, helping to maintain an accurate and up-to-date product catalog.

<details><summary>Product Management - Delete Product</summary>
<img src="assets/readme/feature-admin/03-admin-feature-delete-product.gif">
</details>


### Creator Management - Add Creator

- The Creator Management section allows admins to manage the creators listed on the MagnaPlate website. The "Add Creator" feature enables admins to introduce new creators to the platform. This ensures the website continually showcases fresh talent and maintains an updated roster of contributors.

<details><summary>Creator Management - Add Creator</summary>
<img src="assets/readme/feature-admin/04-admin-feature-add-creator.gif">
</details>


### Creator Management - Edit Creator

- The Creator Management section allows admins to manage the creators listed on the MagnaPlate website. The "Edit Creator" feature provides admins with the capability to modify the details of existing creators. This helps in keeping the creator information current and relevant, ensuring accurate representation on the platform.

<details><summary>Creator Management - Edit Creator</summary>
<img src="assets/readme/feature-admin/05-admin-feature-edit-creator.gif">
</details>


### Creator Management - Delete Creator

- The Creator Management section allows admins to manage the creators listed on the MagnaPlate website. The "Delete Creator" feature allows admins to remove creators who are no longer associated with the platform. This function helps in maintaining a clean and updated creator directory, reflecting only active contributors.

<details><summary>Creator Management - Delete Creator</summary>
<img src="assets/readme/feature-admin/06-admin-feature-delete-creator.gif">
</details>


### Collection Management - Add Collection

- The Collection Management page allows admins to add new collections to the MagnaPlate catalog. This feature includes fields for collection details, associated products, and more, ensuring that new collections can be seamlessly integrated into the existing lineup. Admins can also edit or delete collections from this page to keep the catalog up-to-date.

<details><summary>Collection Management</summary>
<img src="assets/readme/feature-admin/07-admin-feature-add-collection.gif">
</details>


### Collection Management - Edit Collection

- The Collection Management page allows admins to edit existing collections in the MagnaPlate catalog. This feature includes fields for modifying collection details, associated products, and more, ensuring that collections can be updated to reflect current offerings. Admins can also add or delete collections from this page.

<details><summary>Collection Management</summary>
<img src="assets/readme/feature-admin/08-admin-feature-edit-collection.gif">
</details>


### Collection Management - Delete Collection

- The Collection Management page allows admins to delete collections from the MagnaPlate catalog. This feature ensures that outdated or irrelevant collections can be removed, keeping the catalog up-to-date and relevant.

<details><summary>Collection Management</summary>
<img src="assets/readme/feature-admin/09-admin-feature-delete-collection.gif">
</details>


### Category Management - Add Category

- The Category Management page allows admins to add new categories to the MagnaPlate catalog. This feature includes fields for category details, ensuring that new categories can be seamlessly integrated into the existing structure. 

<details><summary>Category Management</summary>
<img src="assets/readme/features/10-admin-feature-add-category.gif">
</details>


### Category Management - Edit Category

- The Category Management page allows admins to edit existing categories in the MagnaPlate catalog. This feature includes fields for modifying category details, ensuring that categories can be updated to reflect current offerings. Admins can also add or delete categories from this page to keep the catalog organized and up-to-date.

<details><summary>Category Management</summary>
<img src="assets/readme/feature-admin/11-admin-feature-edit-category.gif">
</details>





## Messages and Interaction with Users

### Sign up 1

- Screenshots or descriptions related to the sign-up process.<br>

<details><summary>Sign up 1</summary>
<img src="./images/sign_up_1.png">
</details>

### Sign up 2

- Additional steps or features in the sign-up process.<br>

<details><summary>Sign up 2</summary>
<img src="./images/sign_up_2.png">
</details>

### Login

- Screenshots or descriptions related to user login.<br>

<details><summary>Login</summary>
<img src="./images/login.png">
</details>

### Logout

- Screenshots or descriptions related to user logout.<br>

<details><summary>Logout</summary>
<img src="./images/logout.png">
</details>

### Profile Update

- Screenshots or descriptions of the profile update process.<br>

<details><summary>Profile Update</summary>
<img src="./images/profile_update.png">
</details>

### Service Review - Add Review

- Screenshots or descriptions related to adding a service review.<br>

<details><summary>Service Review - Add Review</summary>
<img src="./images/service_review_add_review.png">
</details>

### Service Review - Update Review 1

- Screenshots or descriptions related to updating a service review.<br>

<details><summary>Service Review - Update Review 1</summary>
<img src="./images/service_review_update_review_1.png">
</details>

### Service Review - Update Review 2

- Additional screenshots or descriptions for updating a service review.<br>

<details><summary>Service Review - Update Review 2</summary>
<img src="./images/service_review_update_review_2.png">
</details>

### Service Review - Delete Review 1

- Screenshots or descriptions related to deleting a service review.<br>

<details><summary>Service Review - Delete Review 1</summary>
<img src="./images/service_review_delete_review_1.png">
</details>

### Service Review - Delete Review 2

- Additional screenshots or descriptions for deleting a service review.<br>

<details><summary>Service Review - Delete Review 2</summary>
<img src="./images/service_review_delete_review_2.png">
</details>

### Service Review - Delete Review 3

- More screenshots or descriptions for deleting a service review.<br>

<details><summary>Service Review - Delete Review 3</summary>
<img src="./images/service_review_delete_review_3.png">
</details>

### Add Product

- Screenshots or descriptions related to adding a new product.<br>

<details><summary>Add Product</summary>
<img src="./images/add_product.png">
</details>

### Edit Product 1

- Screenshots or descriptions related to editing a product.<br>

<details><summary>Edit Product 1</summary>
<img src="./images/edit_product_1.png">
</details>

### Edit Product 2

- Additional screenshots or descriptions for editing a product.<br>

<details><summary>Edit Product 2</summary>
<img src="./images/edit_product_2.png">
</details>

### Edit Product 3

- More screenshots or descriptions for editing a product.<br>

<details><summary>Edit Product 3</summary>
<img src="./images/edit_product_3.png">
</details>

### Delete Product 1

- Screenshots or descriptions related to deleting a product.<br>

<details><summary>Delete Product 1</summary>
<img src="./images/delete_product_1.png">
</details>

### Delete Product 2

- Additional screenshots or descriptions for deleting a product.<br>

<details><summary>Delete Product 2</summary>
<img src="./images/delete_product_2.png">
</details>

### Delete Product 3

- More screenshots or descriptions for deleting a product.<br>

<details><summary>Delete Product 3</summary>
<img src="./images/delete_product_3.png">
</details>

### Add Product to cart

- Screenshots or descriptions related to adding a product to the shopping cart.<br>

<details><summary>Add Product to cart</summary>
<img src="./images/add_product_to_cart.png">
</details>

### Update cart

- Screenshots or descriptions related to updating the shopping cart.<br>

<details><summary>Update cart</summary>
<img src="./images/update_cart.png">
</details>

### Remove Product from cart

- Screenshots or descriptions related to removing a product from the shopping cart.<br>

<details><summary>Remove Product from cart</summary>
<img src="./assets/readme/features/01-feature-remove-product-from-cart.gif">
</details>

### Purchase Success

- Confirmation of a successful purchase.<br>

<details><summary>Purchase Success</summary>
<img src="./images/purchase_success.png">
</details>

### Purchase Success - Confirmation Email

- Confirmation email sent after a successful purchase.<br>

<details><summary>Purchase Success - Confirmation Email</summary>
<img src="./images/purchase_success_confirmation_email.png">
</details>




## Admin Panel / Superuser

![Admin Panel / Superuser](.)

- On the Admin Panel and as an admin/superuser I have full access to CRUD functionality. This means I can view, create, edit and
  delete the following apps:

1.
2. Checkout
3. Products
4. Profiles
5. Reviews

- As admin/superuser I can also approve reviews, change the status and give other permissions.<br>

## Marketing and Social Media

- .<br>

### Statista - Facebook Users

![Statista - Facebook Users](.)

- Distribution of Facebook users worldwide as of 2022 according to [Statista](https:)<br>

### MagnaPlate - Facebook Page

![ - Facebook Page 1](.)
![ - Facebook Page 2](.)

- [ Facebook Page]()<br>

### Meta Pixel - Tracking Audience

- In order to improve the website services, I have set a Meta Pixel service to track the audience.

![Meta Pixel - Tracking Audience](.)<br>

### Mailchimp Subscription Service

- Users are encouraged to signup for newsletters, discounts and information about the products sold at MagnaPlate.
  The signup form is available on the website footer and is present on any page. The email subscription service is run through
  Mailchimp, allowing the website admin to send marketing emails through the platform, increasing engagement within the site. Below
  is a screenshot of the MagnaPlate - Mailchimp dashboard.

![ Mailchimp Subscription Service](.)<br>

## Privacy Policy

- In order to add a page with the MagnaPlate Privacy Policy I used the service [Privacy Policy Generator](https://) to ensure
  that the website is compliant with the European Privacy Policy Rules.<br>

![Privacy Policy](.)

- [MagnaPlate - Privacy Policy Page]()<br>

## Search Engine Optimization

- .<br>

![SEO - Keywords List](.)<br>

### sitemap.xml

- A sitemap file with a list of important URLs was added to ensure that search engines are able to easily navigate through the site
  and understand its structure. This was made using XML-sitemaps.com by following the steps:

1. Paste the URL of the deployed site into XML-sitemaps
2. Download the XML sitemap file
3. Add the file into the projects root folder, named as sitemap.xml<br>

### robots.txt

- A robots.txt file was created to tell search engines where not to go on the website and increase the quality of the site, ultimately improving the SEO rating.

![MagnaPlate - Robots.txt](.)<br>

### Sitemap Google Registration

- To ensure that the Google engine will check the website sitemap file I have registered the MagnaPlate URL on the Google Search Console.

![MagnaPlate - Robots.txt](.)<br>

## AWS Setup Process

### AWS S3 Bucket

The deployed site uses AWS S3 Buckets to store the webpages static and media files. More information on how you can set up an AWS S3 Bucket can be found below:

1. Create an AWS account [here](https://portal.aws.amazon.com/).
2. Login to your account and within the search bar type in "S3".
3. Within the S3 page click on the button that says "Create Bucket".
4. Name the bucket and select the region which is closest to you.
5. Underneath "Object Ownership" select "ACLs enabled".
6. Uncheck "Block Public Access" and acknowledge that the bucket will be made public, then click "Create Bucket".
7. Inside the created bucket click on the "Properties" tab. Below "Static Website Hosting" click "Edit" and change the Static website hosting option to "Enabled". Copy the default values for the index and error documents and click "Save Changes".
8. Click on the "Permissions" tab, below "Cross-origin Resource Sharing (CORS)", click "Edit" and then paste in the following code:

```
  [
      {
          "AllowedHeaders": [
          "Authorization"
          ],
          "AllowedMethods": [
          "GET"
          ],
          "AllowedOrigins": [
          "*"
          ],
          "ExposeHeaders": []
      }
  ]
```

9. Within the "Bucket Policy" section. Click "Edit" and then "Policy Generator". Click the "Select Type of Policy" dropdown and select "S3 Bucket Policy" and within "Principle" allow all principals by typing "\*".
10. Within the "Actions" dropdown menu select "Get Object" and in the previous tab copy the "Bucket ARN number". Paste this within the policy generator within the field labelled "Amazon Resource Name (ARN)".
11. Click "Add statement > Generate Policy" and copy the policy that's been generated and paste this into the "Bucket Policy Editor".
12. Before saving, add /\* at the end of your "Resource Key", this will allow access to all resources within the bucket.
13. Once saved, scroll down to the "Access Control List (ACL)" and click "Edit".
14. Next to "Everyone (public access)", check the "list" checkbox and save your changes.

### IAM Set Up

1. Search for IAM within the AWS navigation bar and select it.
2. Click "User Groups" that can be seen in the side bar and then click "Create group" and name the group 'manage-your-project-name'.
3. Click "Policies" and then "Create policy".
4. Navigate to the JSON tab and click "Import Managed Policy", within here search "S3" and select "AmazonS3FullAccess" followed by "Import".
5. Navigate back to the recently created S3 bucket and copy your "ARN Number". Go back to "This Policy" and update the "Resource Key" to include your ARN Number, and another line with your ARN followed by a "/\*".

- Below is an example of what this should look like:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "YOUR-ARN-NO-HERE",
                "YOUR-ARN-NO-HERE/*"
            ]
        }
    ]
}

```

1. Ensure the policy has been given a name and a short description, then click "Create Policy".
2. Click "User groups", and then the group you created earlier. Under permissions click "Add Permission" and from the dropdown click "Attach Policies".
3. Select "Users" from the sidebar and click "Add User".
4. Provide a username and check "Programmatic Access", then click 'Next: Permissions'.
5. Ensure your policy is selected and navigate through until you click "Add User".
6. Download the "CSV file", which contains the user's access key and secret access key.

### Connecting AWS to the Project

1. Within your terminal install the following packages by typing

```
  pip3 install boto3
  pip3 install django-storages
```

2. Freeze the requirements by typing:

```
pip3 freeze > requirements.txt
```

3. Add "storages" to your installed apps within your settings.py file.
4. At the bottom of the settings.py file add the following code:

```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
```

5. Add the following keys within Heroku: "AWS_ACCESS_KEY_ID" and "AWS_SECRET_ACCESS_KEY". These can be found in your CSV file.
6. Add the key "USE_AWS", and set the value to True within Heroku.
7. Remove the "DISABLE_COLLECTSTAIC" variable from Heroku.
8. Within your settings.py file inside the code just written add:

```
  AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
```

8. Inside the settings.py file inside the bucket config if statement add the following lines of code:

```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

9. In the root directory of your project create a file called "custom_storages.py". Import the following at the top of this file and add the classes below:

```
  from django.conf import settings
  from storages.backends.s3boto3 import S3Boto3Storage

  class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

  class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

10. Navigate back to you AWS S3 Bucket and click on "Create Folder" name this folder "media", within the media file click "Upload > Add Files" and select the images for your site.
11. Under "Permissions" select the option "Grant public-read access" and click "Upload".

## Stripe Payments

- The Stripe payments system is set up as the online payment processing and credit card processing platform for the purchases.
  You will need a stripe account which you can sign up for [here](https://stripe.com/en-ie)

### Payments

- To set up stripe payments you can follow their guid [here](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details)

### Webhooks

1. To set up a webhook, sign into your stripe account and click 'Developers' located in the top right of the navbar.
2. Then in the side-nav under the Developers title, click on "Webhooks", then "Add endpoint".
3. On the next page you will need to input the link to your heroku app followed by /checkout/wh/. It should look something like this:

   ```
   https://your-app-name.herokuapp.com/checkout/wh/
   ```

4. Then click "+ Select events" and check the "Select all events" checkbox at the top before clicking "Add events" at the bottom. Once this is done finish the form by clicking "Add endpoint".
5. Your webhook is now created and you should see that it has generated a secret key. You will need this to add to your heroku config vars.
6. Head over to your app in heroku and navigate to the config vars section under settings. You will need the secret key you just generated for your webhook, in addition to your Publishable key and secret key that you can find in the API keys section back in stripe.
7. Add these values under these keys:

   ```
   STRIPE_PUBLIC_KEY = 'insert your stripe publishable key'
   STRIPE_SECRET_KEY = 'insert your secret key'
   STRIPE_WH_SECRET = 'insert your webhooks secret key'

   ```

8. Finally, back in your settings.py file in django, insert the following near the bottom of the file:
   ```
   STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
   STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
   STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
   ```

- Below is a screenshot of the MagnaPlate - Stripe dashboard.

![ Stripe Payments](.)<br>

## Technologies Used

### Languages Used

- [HTML 5](https://en.wikipedia.org/wiki/HTML/)
- [CSS 3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://www.javascript.com/)
- [Django](https://www.python.org/)
- [Python](https://www.djangoproject.com/)<br>

### Django Packages

- [Gunicorn](https://gunicorn.org/) as the server for Heroku
- [Dj_database_url](https://pypi.org/project/dj-database-url/) to parse the database URL from the environment variables in Heroku
- [Psycopg2](https://pypi.org/project/psycopg2/) as an adaptor for Python and PostgreSQL databases
- [Summernote](https://summernote.org/) as a text editor
- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) for authentication, registration and account management
- [Stripe](https://pypi.org/project/stripe/) for processing all online and credit card purchases on the website
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style the forms
- [Pillow](https://pypi.org/project/Pillow/) to process and save all the images downloaded through the database<br>

### Frameworks - Libraries - Programs Used

- [Bootstrap](https://getbootstrap.com/)
- Was used to style the website, add responsiveness and interactivity
- [Jquery](https://jquery.com/)
- All the scripts were written using jquery library
- [Git](https://git-scm.com/)
- Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub
- [GitHub](https://github.com/)
- GitHub is used to store the project's code after being pushed from Git
- [Heroku](https://id.heroku.com)
- Heroku was used to deploy the live project
- [PostgreSQL](https://www.postgresql.org/)
- Database used through Heroku.
- [VSCode](https://code.visualstudio.com/)
- VSCode was used to create and edit the website
- [Lucidchart](https://lucid.app/)
- Lucidchart was used to create the database diagram
- [Pycodestyle](http://pep8online.com/)
- Pycodestyle was used to validate all the Python code
- [W3C - HTML](https://validator.w3.org/)
- W3C- HTML was used to validate all the HTML code
- [W3C - CSS](https://jigsaw.w3.org/css-validator/)
- W3C - CSS was used to validate the CSS code
- [Fontawesome](https://fontawesome.com/)
- Was used to add icons to the website
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
- To check App responsiveness and debugging
- [Google Fonts](https://fonts.google.com/)
- To add the 2 fonts that were used throughout the project
- [Balsamiq](https://balsamiq.com/)
- To build the wireframes for the project
- [PIXLR](https://pixlr.com)
- To convert the images to webp format
- [CANVA](https://www.canva.com/)
- To build the logos for the project
- [AWS](https://aws.amazon.com/)
- was used to host the static files and media<br>

### Testing

Testing results are [here](TESTING.md)

## Creating the Django app

1. Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click on Use This Template
3. Once the template is available in your repository click on Gitpod
4. When the image for the template and the Gitpod are ready open a new terminal to start a new Django App
5. Install Django and gunicorn: pip3 install django gunicorn
6. Install supporting database libraries dj_database_url and psycopg2 library: pip3 install dj_database_url psycopg2
7. Create file for requirements: in the terminal window type pip freeze --local > requirements.txt
8. Create project: in the terminal window type django-admin startproject your_project_name
9. Create app: in the terminal window type python3 manage.py startapp your_app_name
10. Add app to the list of installed apps in settings.py file: you_app_name
11. Migrate changes: in the terminal window type python3 manage.py migrate
12. Run the server to test if the app is installed, in the terminal "The install worked successfully! Congratulations!"<br>

## Deployment of This Project

- This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New
   App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. Click in resources and select Heroku Postgres database
7. Click Reveal Config Vars and add:

- A new record with SECRET_KEY
- A new record with the AWS_ACCESS_KEY_ID
- A new record with the AWS_SECRET_ACCESS_KEY
- A new record with the EMAIL_HOST_PASS
- A new record with the EMAIL_HOST_USER
- A new record with the STRIPE_PUBLIC_KEY
- A new record with the STRIPE_SECRET_KEY
- A new record with the STRIPE_WH_SECRET
- A new record with the DISABLE_COLLECTSTATIC = 1

8.  The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
9.  Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
10. Scroll to the top of the page and choose the Deploy tab
11. Select Github as the deployment method
12. Confirm you want to connect to GitHub
13. Search for the repository name and click the connect button
14. Scroll to the bottom of the deploy page and select the preferred deployment type
15. Click Enable Automatic Deploys for automatic deployment when you push updates to Github<br>

## Final Deployment

1. Create a runtime.txt "python-3.9.13"
2. Create a Procfile "web: gunicorn your_project_name.wsgi"
3. When development is complete change the debug setting to: DEBUG = False in settings.py
4. In this project the summernote editor was used so for this to work in Heroku add: X_FRAME_OPTIONS = 'SAMEORIGIN' to
   settings.py.
5. In Heroku settings config vars delete the record for DISABLE_COLLECTSTATIC
6. In Heroku settings config vars set the record for USE_AWS to True<br>

## Forking This Project

- Fork this project by following the steps:

1. Open [GitHub](https://github.com/PedroCristo/portfolio_project_5)
2. Find the "Fork" button at the top right of the page
3. Once you click the button the fork will be in your repository<br>

## Cloning This Project

- Clone this project by following the steps:

1. Open [GitHub](https://github.com/PedroCristo/portfolio_project_5)
2. You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order
   to copy the URL
3. Once you click the button the fork will be in your repository
4. Open a new terminal
5. Change the current working directory to the location that you want the cloned directory
6. Type "git clone" and paste the URL copied in step 3
7. Press "Enter" and the project is cloned<br>

## Credits

### Content

- All the products content were taken from [Placeholder](https:)
- The images were taken from [Placeholder](https:)
- The 2 videos used as a background on the Landing Page were taken from [Pexels](https://www.pexels.com/)
- The MagnaPlate logos and favicon are my own designed and build<br>

### Information Sources / Resources

- [W3Schools - Python](https://www.w3schools.com/python/)
- [Stack Overflow](https://stackoverflow.com/)
- [Scrimba - Pyhton](https://scrimba.com/learn/python)
- [Code Institute - Slack Community](https://slack.com/)

## Special Thanks

- Special thanks to my mentor .
