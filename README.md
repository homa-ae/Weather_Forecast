# Weather_Forecast
## Intro
This software engineering project consists of eleven different parts, each addressing various aspects of development and implementation.  
It provides users with a convenient way to access accurate and up-to-date weather information based on their chosen locations.

## 1. Git
GitHub provides an easy-to-use platform for storing code, collaborating with others, and managing projects.    
It facilitates teamwork on code changes, lets developers track issues, create pull requests for code review, and integrate with other tools to streamline their development process.    
With GitHub Actions, automating tasks like testing and deployment is made even easier.

## 2. UML
I have employed the following UML Diagrams for this project:   
* The [Entity-Relationship Diagram](https://github.com/homa-ae/Weather-Forecast/blob/main/diagrams/Entity-Relationship%20Diagram.jpg) which represents the relationships between entities in the system.
* The [Use Case Diagram](https://github.com/homa-ae/Weather-Forecast/blob/main/diagrams/Use%20Case%20Diagram.jpg) which illustrates the interactions between users and the system, depicting the various functionalities and actions that users can do.
* The [Sequence Diagram](https://github.com/homa-ae/Weather-Forecast/blob/main/diagrams/Sequence%20Diagram.jpg) which shows the chronological order of interactions between objects in the system.
* The [Class Diagram](https://github.com/homa-ae/Weather-Forecast/blob/main/diagrams/Class%20Diagram.jpg) which organizes the structure of the system by illustrating the various classes, their attributes, and the relationships between them.
  
## 3. DDD
The project includes six domains:
* Data Collection
* Data Processing
* Machine Learning
* Forecasting
* Visualization
* User Interface

The [DDD diagram](https://github.com/homa-ae/Weather_Forecast/blob/main/diagrams/ddd-diagram.md) depicts how this project has been divided into distinct domains and the connections between them.    

## 4. Metrics
I applied [SonarCloud](https://sonarcloud.io/projects) and GitHub Actions to analyze my project's metrics, with the goal of enhancing its performance and overall quality.

## 5. Clean Code Development
[Here](https://github.com/homa-ae/Weather-Forecast/blob/main/documents/clean-code.md) are the reasons that I implemented 
<kbd style="font-size: 20px; padding: 10px; border-radius: 5px; background-color: #f0f0f0;">
Clean Code Programming </kbd>.  
[This](https://github.com/homa-ae/Weather-Forecast/blob/main/documents/clean-code-cheat-sheet.md) is a python 
<kbd style="font-size: 20px; padding: 10px; border-radius: 5px; background-color: #f0f0f0;">
[Clean Code Development (CCD) Cheat Sheet] </kbd>.

## 6. Build Management
I have employed [PyBuilder](https://github.com/homa-ae/Weather-Forecast/blob/main/build.py) using the
<kbd style="font-size: 20px; padding: 10px; border-radius: 5px; background-color: #f0f0f0;">
pyb --verbose </kbd>
command to manage the build process of the project along with comprehensive details.

## 7. Continuous Delivery
For the Continuous Delivery Pipeline, I've applied
<kbd style="font-size: 20px; padding: 10px; border-radius: 5px; background-color: #f0f0f0;">
GitHub Action </kbd>
, which consists of two workflows:  
* [Build](https://github.com/homa-ae/Weather_Forecast/blob/main/.github/workflows/build.yml)
* [Metrics](https://github.com/homa-ae/Weather_Forecast/blob/main/.github/workflows/metrics.yml)

## 8. Unit Tests
[This file](https://github.com/homa-ae/Weather-Forecast/blob/main/src/test/test_weather_forecast.py) consistes of small
<kbd style="font-size: 20px; padding: 10px; border-radius: 5px; background-color: #f0f0f0;">
Unit tests </kbd>
of software application to make sure individual parts of code work correctly in isolation.

## 9. IDE
I'm particularly fond of 
<kbd style="font-size: 20px; padding: 10px; border-radius: 5px; background-color: #f0f0f0;">
Visual Studio Code (VS Code) </kbd>
, my all-time favourite IDE. This widely-used, free, and open-source code editor appeals to me for several reasons:
* VS Code supports a wide range of programming languages.
* It provides IntelliSense, an intelligent code completion feature that offers suggestions and auto-completions as you type.
* This lightweight IDE includes built-in support for debugging code, lets you find and fix mistakes in your code easily. 
* It has built-in support for version control systems like Git, allowing you to manage your source code repositories directly within the editor.
* In Visual Studio Code, you can split the editor to see different files or parts of the same file side by side, helping you compare and work on multiple sections at once,     which makes managing your code easier.

Here are some preferred
<kbd style="font-size: 20px; padding: 10px; border-radius: 5px; background-color: #f0f0f0;">
keyboard shortcuts </kbd> 
used by me in Visual Studio Code:
* Ctrl + S: Save the current file  
* Ctrl + Z: Undo the last action 
* Ctrl + Shift + Z: Redo the last undone action
* Ctrl + X: Cut the selected text
* Ctrl + C: Copy the selected text
* Ctrl + V: Paste the copied or cut text
* Ctrl + F: Open the Find dialogue to search for text within the current file
* Ctrl + H: Open the Replace dialogue to search and replace text within the current file.
* Ctrl + G: Go to a specific line number within the current file.  
* Ctrl + B: Toggle the visibility of the sidebar.  
* Ctrl + P: Quick Open, allowing to navigate to files.  
* Ctrl + `: Toggle the terminal panel.  
* Ctrl + Shift + F5: Restart the debug session.  
    
## 10. DSL
I developed a
<kbd style="font-size: 20px; padding: 10px; border-radius: 5px; background-color: #f0f0f0;">
pseudocode language
</kbd> file as a small [Domain-Specific Language (DSL)](https://github.com/homa-ae/Weather-Forecast/blob/main/documents/dsl.pseudo) Demo example snippet for the following reasons:
* Easy comprehension of algorithms.
* Helping developers plan and understand the steps required to solve a problem or implement a particular functionality.
* It outlines the logic of their algorithm or program in a clear and structured manner.
* It can also be used as a form of documentation to explain the logic of the algorithm or program to others.     

## 11. Functional Programming
* Final Data Structures: This code primarily uses dictionaries to structure data, particularly in cleaned_weather_data and airpollution_data. These dictionaries are not        mutated after initialization. Lists are also used to hold pollutant values, which are likewise not mutated. These dictionaries are used as containers to hold data            retrieved from external APIs (OpenWeatherMap and OpenAQ), and their content is not intended to be modified within the application and remain unchanged throughout the         program's execution. Therefore, the code predominantly utilizes final data structures.
* Side-effect-free functions: The functions in the codebase primarily perform their intended tasks without causing side effects. They retrieve data, update GUI                 elements, and display charts without altering external states directly. This means they fetch information they need, like weather data or pollution levels, but don't         modify anything else in the program while doing so.
* [higher-order function](https://github.com/homa-ae/Weather-Forecast/blob/main/src/high-order_function.py)
* [function as parameter](https://github.com/homa-ae/Weather-Forecast/blob/main/src/function_as_parameter.py)
* [closure_anonymous_function](https://github.com/homa-ae/Weather-Forecast/blob/main/src/closure_anonymous_function.py)
