# Software Design Document

## Project Name: Nutrition Information Data Analysis Tool
## Group Number: 027

## Team members

| Student Number | Name            | 
|----------------|-----------------|
| s5113175       | Peter Symoniw   |
| s5094725       | Sean O'Sullivan | 
| s5291335       | Sipa Sunuwar    | 


<div style="page-break-after: always;"></div>



# Table of Contents

<!-- TOC -->
* [Software Design Document](#software-design-document)
  * [Project Name: Nutrition Information Data Analysis Tool](#project-name-nutrition-information-data-analysis-tool)
  * [Group Number: 027](#group-number-027)
  * [Team members](#team-members)
* [Table of Contents](#table-of-contents)
  * [1. System Vision](#1-system-vision)
    * [1.1 Problem Background](#11-problem-background)
    * [1.2 System capabilities/overview](#12-system-capabilitiesoverview)
    * [1.3	Benefit Analysis](#13benefit-analysis)
  * [2. Requirements](#2-requirements)
    * [2.1 User Requirements](#21-user-requirements)
      * [Core User Requirements](#core-user-requirements)
      * [Fictional User Profile:](#fictional-user-profile)
    * [2.2	Software Requirements](#22software-requirements)
      * [Functional Requirements](#functional-requirements)
      * [Non-Functional Requirements](#non-functional-requirements)
    * [2.3 Use Case Diagram](#23-use-case-diagram)
    * [2.4 Use Cases](#24-use-cases)
  * [3.	Software Design and System Components](#3-software-design-and-system-components-)
    * [3.1	Software Design](#31software-design)
    * [3.2	System Components](#32system-components)
      * [3.2.1 Functions](#321-functions)
      * [3.2.2 Data Structures / Data Sources](#322-data-structures--data-sources)
      * [3.2.3 Detailed Design](#323-detailed-design)
      * [3.2.4 Test Entry](#324-test-entry)
  * [4. User Interface Design](#4-user-interface-design)
    * [4.1 Structural Design](#41-structural-design)
    * [4.2	Visual Design](#42visual-design)
    * [4.3 General UI Considerations](#43-general-ui-considerations)
<!-- TOC -->


<div style="page-break-after: always;"></div>



## 1. System Vision

### 1.1 Problem Background

- Problem Identification: What problem does this system solve?
- Dataset: What is the dataset used?
- Data Input/Output: What kind of data input and output is required?
- Target Users: Who will use the system, and why?

The nutrition visualiser software aims to enhance end users health and eating habits by allowing them to see and visualise the nutrients of foods they consume. It will give them all the important information they need to know in a easily digestible manner.

The dataset being utilised for the application is about food nutrition in a comma separated value (CSV) format. The values present are different items of food, and the macronutrients and micronutrients of the respective food items.

The user will be able to interact with the application through its GUI. They will be able to enter strings into the nutrition visualiser when searching for specific food items and nutrient values. The software will deliver the searched items nutrition composition in a readable format with models of the data also being presented.

There is a range of target users for the nutrition visualiser software, depending on the users nutritional goals. They can be infrequent users that use the application to look up specific food items occasionally to get a quick breakdown of its nutritional value. Additionally, they could be frequent users that enter all the food items they want to consume into the nutrition visualiser application. The software will allow them to easily keep track of their total nutrition consumption.

### 1.2 System capabilities/overview

- System Functionality: What will the system do?
- Features and Functionalities: Describe the key features and functionalities of the system.

The nutrition visualiser application will allow for quick and orderly retrieval of information regarding foods nutritional composition. The food nutrition dataset csv will be used as the database that the user will be able to interact with as part of the software. 

The user will be able to search for specific food items and their corresponding nutritional values by typing into a search bar. It will present the nutritional information in written text as well as through various models of important values, depending on the user's selection. Additionally,the user will be able to filter through foods depending on their nutritional composition. All features and functions will be accessible through the integrated GUI.

### 1.3	Benefit Analysis

How will this system provide value or benefit?

This system will be practical and provide great benefits to the user, by helping them make more informed decisions related to their eating habits. Correspondingly, this will aid users health and make it easier for them to improve, due to the quantifiable nature of the application. For example a user could be trying to lose weight, and they want to figure out the composition of their diet. They can search the database and get concrete numbers on their current situation. Then by using the search and filtering functions the user will be able to find food items that provide better macro and micronutrients, and take actionable steps to improving their diet.

## 2. Requirements

### 2.1 User Requirements
Users of the system are likely to be individuals who are health-conscious and interested in managing their diet by making informed food choices based on nutritional information. The system must be user-friendly, offering simple navigation and clear presentation of nutritional data. 

#### Core User Requirements
1.	Food search
* Users enter a food item into search bar and system will display the results to match the search query. Each result will display their nutritional information like caloric value, fat content, etc.
* System should be able to present search results using general or broad terms.
* Example: 
  * User searches cheese.
  * System displays all food items with ‘cheese’ like goat cheese, cheddar cheese, cream cheese.
  * User can select the specific food item.
  * Nutritional information of selected item is displayed.

2.	Nutrition breakdown
* System should display detailed nutritional information for food items.
* Information must be presented in a clear way using visual elements like pie charts and bar graphs to facilitate better understanding.

3.	Nutrition range filter
* Users should be able to select a nutrient (e.g. fat, sugar) and input minimum and maximum values (e.g. 5g to 15g).
* When filters are applied, the system should display a list of foods that fall within the specified range.

4.	Nutrition level filter
* Users should be able to select one of several nutrients and choose a level (low, mid, high) based on predefined thresholds.
* The levels are defined as:
  * Low: Less than 33% of the highest value.
  * Mid: Between 33% and 66% of the highest value.
  * High: Greater than 66% of the highest value.

5.	Additional feature: Nutritional tracker(?)

#### Fictional User Profile:
**Name:** Alex Li\
**Occupation:** Student\
**Age:** 22\
**Comments:** Fitness enthusiast, tech-savvy\
**Goals:** Find healthy food options, keep track of his nutritional intake to maintain a balanced diet.Looking for low sugar, high protein diet.

**Expected flow of events:**
1. Alex opens the application.
2. Food Search:
- The system displays a list of food items, but Alex is looking for a specific dietary criteria.
3. Apply nutrition range filters:
- Alex chooses ‘sugar’ as the nutrient to filter.
- Alex sets the maximum ‘sugar’ to be ‘5g’.
- The system updates the list to show food items that fall within this low sugar range.
4. Apply nutrition level filter:
- Alex selects “protein” as the nutrient to filter.
- The system then updates the list again to show food items that meet both criteria: 
  - low in sugar (up to 5g)
  - high in protein
- This allows Alex to make informed decisions about his diet.

### 2.2	Software Requirements
This section provides a detailed overview of the capabilities and features of the software. It defines what the system should do and how it should perform. It covers the functional requirements, which refer to specific tasks and functions the software must perform, and non-functional requirements, which refer to the performance standards to perform efficiently.

#### Functional Requirements
1.	Food Search Functionality
  - R1.1 The system shall allow users to enter a food item into a search bar.
  - R1.2 The system shall display a list of food items matching the search query.
  - R1.3 Each search result shall include nutritional information such as caloric value, fat content, etc.
  - R1.4 The system shall allow users to select a food item from the search results to view detailed nutritional information.
2.	Nutrition Breakdown
  - R2.1 The system shall display a detailed view of nutritional information upon
  - R2.2 The detailed view shall use pie charts and bar graphs to represent different nutrients such as fats, carbohydrates, and proteins.
3.	Nutrition Range Filter
  - R3.1 The system shall provide a feature to select a nutrient (e.g. fat, sugar).
  - R3.2 The system shall allow users to input a desired range (e.g. 5g to 15g) for the selected nutrient.
  - R3.3 The system shall display a list of food items that fall within the specified nutrient range.
4.	Nutrition Level Filter
  - R4.1 The system shall allow users to select a nutrient (e.g. protein) and choose a level (low, mid, high).
  - R4.2 The system shall filter the database based on predefined thresholds for each nutritional level.
  - R4.3 The system shall display a list of foods categorized into the selected nutrient levels (low, mid, high).
5.	Additional Feature: (TBD)
  - 

#### Non-Functional Requirements
1.	Performance
  - N1.1 The system shall respond to search queries within 2 seconds.
  - N1.2 The system shall display detailed nutritional information within 3 seconds of selecting a food item.
2.	Usability
  - N2.1 The system shall provide a user-friendly interface with intuitive navigation.
  - N2.2 The system shall include clear labels and a logical flow to facilitate easy use.
3.	Scalability
  - N3.1 The system shall handle up to 10,000 food items without performance degradation.
  - N3.2 The system shall allow for future expansion of nutritional data without requiring significant modifications.
  - N3.3 The system shall handle up to 5,000 simultaneous user sessions during peak hours.
4.	Security
  - N4.1 The system shall protect user data from unauthorized access.
  - N4.2 The system shall implement secure data storage and transmission protocols.


### 2.3 Use Case Diagram
Provide a system-level Use Case Diagram illustrating all required features.

Example:  
![Use Case Diagram](./UCD.png)

### 2.4 Use Cases

| User Case ID   | 1  |
|----------------|------|
| Use Case Name  | Food Search |
| Actors         | User |
| Description    | User can search for food items by entering a keyword into the search bar. |
| Flow of Events | 1. User enters a search term into the search bar.
|                | 2. System processes the search request.
|                | 3. System displays a list of food items that match the search.
|                | 4. User selects a food item from the results to view the nutritional information about it. |
| Alternate Flow | 1. If no matching items are found, system displays message to inform users that no results were found.
|                | 2. User can modify their search term and try again. |






| User Case ID   | 2  |
|----------------|------|
| Use Case Name  | Nutritional Breakdown |
| Actors         | User |
| Description    | User can view nutritional information for a selected food item. |
| Flow of Events | 1. User selects a food item from the search results. |
|                | 2. System retrieves the nutritional information for selected food item. |
|                | 3. System displays detailed nutritional information. |
| Alternate Flow | 1. If nutritional information is not available, the system will display a message indicating the details are not available.
|                | 2.  Users can return to search results to select another item. |




| User Case ID     | 3  |
|------------------|------|
| Use Case Name    | Nutrition Range Filter |
| Actors           | User |
| Description      | Users can filter food items based on their desired range for any one of the nutrition.  |
| Flow of Events   | 1. User sets a nutritional range filter (e.g. 10g fat). |
|                  | 2. System applies the filter to the list of food items. |
|                  | 3. System displays the filtered list of food items that meet the range set by user. |
|                  | 4. User reviews the filtered list. |
| Alternate Flow   | 1. If no food items meet the filter set by user, the system displays a message indicating that no results were found. |
|                  | 2. User can adjust the filter and try again. |

| User Case ID     | 4  |
|------------------|------|
| Use Case Name    | Nutrition Level Filter |
| Actors           | User |
| Description      | Users can filter food items based on the predefined nutritional content levels (low, mid, and high) for one of the following nutrient: `fat`, `protein`, `carbohydrates`, `sugar`, or `nutritional density`. |
| Flow of Events   | 1. User selects a nutritional level filter option. |
|                  | 2. System applies the nutritional level filter to the list of food items. |
|                  | 3. System displays the filtered list of food items that meet the nutritional level set by user. |
|                  | 4. User reviews the list. |
| Alternate Flow   | 1. If no food items meet the filters set by the user, the system displays a message indicating that no results were found. |
|                  | 2. Users can then readjust the filter. |

| User Case ID   | 5  |
|----------------|------|
| Use Case Name  | TBD |
| Actors         |  |
| Description    |  |
| Flow of Events |  |
| Alternate Flow |  |


## 3.	Software Design and System Components 

### 3.1	Software Design
Include a flowchart that illustrates how your software will operate.

Example:  
![Software Design](./software_design_flowchart.png)

### 3.2	System Components

#### 3.2.1 Functions
List all key functions within the software. For each function, provide:
- Description: Brief explanation of the function’s purpose.
- Input Parameters: List parameters, their data types, and their use.
- Return Value: Describe what the function returns.
- Side Effects: Note any side effects, such as changes to global variables or data passed by reference.

#### 3.2.2 Data Structures / Data Sources
List all data structures or sources used in the software. For each, provide:

- Type: Type of data structure (e.g., list, set, dictionary).
- Usage: Describe where and how it is used.
- Functions: List functions that utilize this structure.

#### 3.2.3 Detailed Design
Provide pseudocode or flowcharts for all functions listed in Section 3.2.1 that operate on data structures. For instance, include pseudocode or a flowchart for a custom searching function.

#### 3.2.4 Test Entry
This is a test.


## 4. User Interface Design

### 4.1 Structural Design

Hierarchy Chart:
![UI Hierarchy.png](..%2FUI%2FUI%20Hierarchy.png)


### 4.2	Visual Design

Welcome View:  
![NutritionApp-View1.png](..%2FUI%2FNutritionApp-View1.png)

Purpose:

Serves as the main entry point to the application and provides the user with context about the tool.

Components:

- __Title__ - The title of the application, large and centered.
- __Welcome Message__ - A brief message informing the user about the capabilities of the application readable and centered to ensure they know what they can get out of the application.
- __Get Started__ - Takes the user to the main UI of the application when they're ready clearly visible when they're ready to proceed.


Main View:
![NutritionApp-View2.png](..%2FUI%2FNutritionApp-View2.png)

Purpose:

The Main Search View serves as the starting point for users to query the database for food items, apply desired filters and view their search results. It's the central hub between all the application's functions that allows the user to interact with data.

Components:

- __Search Bar__ - Text input field positioned at the top for immediate access allowing users to identify the most essential operation. It allows users to query the dataset for a certain food.
- __Search Button__ - Starts the search for the desired item positioned immediately next to the field for intuitive display.
- __Filter Button__ - Opens a new view overlay that offers advanced filter options that the user can select for their search. Compiled into an overlay as it is unessential once specified so the user does not need to see it at all times. This is positioned next to search to denote its association with the feature.
- __Search Results Area__ - Displays a list of the fetched search results from the dataset and grows downwards sorted into columns for each attribute. The area is large and can be scrolled to maximise space as it is the element the user will be parsing.
- __Interactive Buttons__ - The plus symbol and magnifying glass depict buttons that will allow the user to add the item to a pending recipe or inspect the food item for a more graphical display. They're positioned such that the user knows which item they are associated with and the symbols are intuitive the depict th action to be taken.
- __Tab Navigation Area__ - The different views of the app can be navigated to by clicking the tabs at the top. Again they are placed in an intuitive and visible location whilst not impeding any display. 


Apply Filter View:
![NutritionApp-View3.png](..%2FUI%2FNutritionApp-View3.png)

Purpose:

This view allows users to apply selected filters to their search queries. It is presented to the user as a modal or overlay to conserve space on the main screen whilst still providing comprehensive functionality. 


Components:

- __Optional Filter Range Values__ - Allows the user to search for nutrient values within the specified range for the associated nutrient. It will list the nutrient components of foods and can be scrolled if necessary.
- __Optional Nutrient Level Values__ - Radial buttons that allows a user to specify the various levels of a particular nutrient they want to have in their results. Only one button will be selected at a time and double tapping the same button should de-select it.
- __Close Button__ - Intuitive symbol and positioning. Closes the filters without saving.
- __Clear Filters__ - Clears the search filters if any are set. Positioned in a clear location but separated from the apply filters button to reduce the likelihood of accidentally clearing.
- __Apply Filters__ - Applies the search filters to be used and closes the overlay window.


Graphical Display View:
![NutritionApp-View4.png](..%2FUI%2FNutritionApp-View4.png)

Purpose:

This view presents the user with the graphical analysis made by the application.


Components:

- __Food Name__ - Displays the currently inspected food item. Positioned within the main viewing area as a clear indicator of what information is being displayed.
- __Pie Chart Region__ - Displays the calculated pie chart visual representation for the associated food. Takes up half the view space as it is an important element.
- __Bar Chart Region__ - Displays the calculated bar graph for the associated food. Takes up half the space as it is an important element.

Additional considerations:

Depending how the visualisations are rendered an option may be to switch to full view width displays and placing the graphs on top of each other with a scrollable view space.

Recipe Builder View:
![NutritionApp-View5.png](..%2FUI%2FNutritionApp-View5.png)

Purpose:

This view allows the user to compile a list of various food items into a 'recipe' and sum its total nutritional value.

Components:

- __Name Popup__ - When initialised the recipe must be named so the popup ensures that the user names their recipe. It is displayed as a prominent screen element and requires confirmation to proceed to operating the view. Once named it closes and moves out of the way populating a region of the screen to denote clear association with the recipe being constructed.
- __Total Accumulated Nutrients__ - A region that displays the total accumulated nutritional value of the recipe. Positioned at the top so the user always has a clear indication of their recipe.
- __Save__ - Allows the user to save their recipe. Positioned at the top with other important information but far to the right as it is not always applicable to the user.
- __Remove Button__ - Removes an item from the recipe. Uses an X symbol for intuitive understanding. Positioned next to the item it should remove.
- __Quantity__ - Allows the user to specify the amount of the associated food to calculate the nutrients for as the dataset lists quantities per 100g so amounts need to be adjusted for more realistic recipes.
- __Imported Food Item__ - Displays the nutrient information for the associated food as a general reference to the user. Presented in a recognisable format from the previous search view. 

### 4.3 General UI Considerations
Tab Limitations:

- Users can have up to two additional tabs open at any time:
- One Recipe Builder Tab (to manage an active recipe).
- One Nutrition Breakdown Tab (for graphical information on the last viewed food item).
- If the user requests a new graphical breakdown, it will replace the current Nutrition Breakdown Tab, ensuring only one graphical summary is viewable at a time.

Handling Recipe Creation:

- If a user attempts to add an item to a recipe and no recipe tab is open, the system will prompt the user to create a new recipe (similar to manually starting a new recipe).
- The user will be asked to name their recipe before the Recipe Builder Tab opens, keeping the flow intuitive.

Feedback and Error Display:

- Errors (e.g., "invalid input" or "no foods added") and user actions (e.g., "food added to recipe") will be handled in a clear, consistent region of the UI. Errors should be visually distinct (e.g., red for errors, green for success).







