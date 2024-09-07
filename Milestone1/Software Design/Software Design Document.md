# Software Design Document

## Project Name: Nutrition Information Data Analysis Tool
## Group Number: 027

## Team members

| Student Number | Name          | 
|----------------|---------------|
| s5113175       | Peter Symoniw |
| s222222        | Full name     | 
| s5291335        | Sipa Sunuwar     | 


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
    * [2.2	Software Requirements](#22software-requirements)
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
<!-- TOC -->


<div style="page-break-after: always;"></div>



## 1. System Vision

### 1.1 Problem Background

- Problem Identification: What problem does this system solve?
- Dataset: What is the dataset used?
- Data Input/Output: What kind of data input and output is required?
- Target Users: Who will use the system, and why?

### 1.2 System capabilities/overview

- System Functionality: What will the system do?
- Features and Functionalities: Describe the key features and functionalities of the system.

### 1.3	Benefit Analysis

How will this system provide value or benefit?

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

5. Recipe Builder
* Users should be able to select multiple food items and create a simple recipe.
* System should automatically add up their nutritional values and display them for users.
* Users should be able to save their created recipes for future reference.

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
5. Recipe Builder
  - R5.1 The system shall allow users to select multiple food items.
  - R5.2 The system shall calculate the total nutritional values (e.g., calories, proteins, fats, etc.) for the selected food items.
  - R5.3 The system shall display the combined nutritional values of the selected food items in a clear format.

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
Below is a system-level Use Case Diagram illustrating all required features:

![Use Case Diagram](Use%20Case/UCD.png)

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
| Use Case Name  | Recipe builder |
| Actors         | User |
| Description    | User can select multiple foods and create a simple recipe by summing up their nutritional values. |
| Flow of Events | 1. User searches for food items. |
|                | 2. User adds selected food items to the recipe. |
|                | 3. System calculates and displays the total nutritional values of selected items. |
|                | 4. User names the recipe and saves it for future reference. |
| Alternate Flow | 1. If system cannot retrieve nutritional information for a selected item, it notifies the user and excludes that item from the total calculation. |


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
Present a structural design, a hierarchy chart, showing the overall interface’s structure. Address:

- Structure: How will the software be structured?
- Information Grouping: How will information be organized?
- Navigation: How will users navigate through the software?
- Design Choices: Explain why these design choices were made.

Example:  
![Structural Design](./Structural_Design.png)

### 4.2	Visual Design
Include all wireframes or mock-ups of the interface. Provide a discussion, explanation, and justification for your design choices. Hand-drawn wireframes are acceptable.

- Interface Components: Clearly label all components.
- Screens/Menus: Provide wireframes for different screens, menus, and options.
- Design Details: Focus on the layout and size of components; color and graphics are not required. 

Example:  
![Visual Design](./visual_design.png)



