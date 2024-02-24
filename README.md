# Weather-Forecast
## Intro
This project provides users with a convenient way to access accurate and up-to-date weather information based on their preferences and chosen locations.

## 1. Git

## 2. UML
* The [Entity-Relationship Diagram](https://github.com/homa-ae/Weather-Forecast/blob/main/Diagrams/Entity-Relationship%20Diagram.jpg) 
* The [Use Case Diagram](https://github.com/homa-ae/Weather-Forecast/blob/main/Diagrams/Use%20Case%20Diagram.jpg)
* The [Sequence Diagram](https://github.com/homa-ae/Weather-Forecast/blob/main/Diagrams/Sequence%20Diagram.jpg)
* The [Class Diagram](https://github.com/homa-ae/Weather-Forecast/blob/main/Diagrams/Class%20Diagram.jpg)
  
## 3. DDD

## 4. Metrics
I integrated [SonarCloud](https://sonarcloud.io/projects?reliability=1) with GitHub Actions to analyze my project's metrics, with the goal of enhancing its performance and overall quality.

## 5. Clean Code Development
[Clean Code](https://github.com/homa-ae/Weather-Forecast/blob/main/documents/clean-code.md)  
[Clean Code Development (CCD) Cheat Sheet](https://github.com/homa-ae/Weather-Forecast/edit/main/documents/clean-code-cheat-sheet.md)

## 6. Build Management
I have employed [PyBuilder](https://github.com/homa-ae/Weather-Forecast/blob/main/build.py)  to manage the build process of the project.   
The build process will be initiated using the 
<kbd style="font-size: 20px; padding: 10px; border-radius: 5px; background-color: #f0f0f0;">
pyb --verbose
</kbd>
command.   
This command will provide comprehensive details, including the outcomes of individual tests, identifying both those that passed successfully and those that failed.  
Additionally, the command will indicate whether the overall build process was successful or encountered any issues.

## 7. Continuous Delivery
(https://github.com/homa-ae/Weather-Forecast/blob/main/.github/workflows/ci.yml)

## 8. Unit Tests
(https://github.com/homa-ae/Weather-Forecast/blob/main/src/test/test_weather_forecast.py)

## 9. IDE
I'm particularly fond of 
<kbd style="font-size: 20px; padding: 10px; border-radius: 5px; background-color: #f0f0f0;">
Visual Studio Code (VS Code)
</kbd>
, my all-time favourite IDE. This widely-used, free, and open-source code editor appeals to me for several reasons:
* VS Code supports a wide range of programming languages.
* It provides IntelliSense, an intelligent code completion feature that offers suggestions and auto-completions as you type.
* This lightweight IDE includes built-in support for debugging code, lets you find and fix mistakes in your code easily. 
* It has built-in support for version control systems like Git, allowing you to manage your source code repositories directly within the editor.
* In Visual Studio Code, you can split the editor to see different files or parts of the same file side by side, helping you compare and work on multiple sections at once,     which makes managing your code easier.

Here are some preferred keyboard shortcuts commonly used in Visual Studio Code:

* Ctrl + S (Cmd + S on macOS): Save the current file.  
* Ctrl + Z (Cmd + Z on macOS): Undo the last action.  
* Ctrl + Shift + Z (Cmd + Shift + Z on macOS): Redo the last undone action.  
* Ctrl + X (Cmd + X on macOS): Cut the selected text.  
* Ctrl + C (Cmd + C on macOS): Copy the selected text.  
* Ctrl + V (Cmd + V on macOS): Paste the copied or cut text.  
* Ctrl + F (Cmd + F on macOS): Open the Find dialogue to search for text within the current file.  
* Ctrl + H (Cmd + Option + F on macOS): Open the Replace dialogue to search and replace text within the current file.  
* Ctrl + Shift + F (Cmd + Shift + F on macOS): Open the Find in Files dialogue to search for text across multiple files in the project.  
* Ctrl + G (Cmd + G on macOS): Go to a specific line number within the current file.  
* Ctrl + B (Cmd + B on macOS): Toggle the visibility of the sidebar.  
* Ctrl + P (Cmd + P on macOS): Quick Open, allowing you to quickly navigate to files within the project.  
* Ctrl + ` (Cmd + ` on macOS): Toggle the terminal panel.  
* Ctrl + Shift + E (Cmd + Shift + E on macOS): Focus on the file explorer sidebar.  
* Ctrl + Shift + F5 (Cmd + Shift + F5 on macOS): Restart the debug session.  
    
## 10. DSL
I developed a
<kbd style="font-size: 20px; padding: 10px; border-radius: 5px; background-color: #f0f0f0;">
pseudocode language
</kbd> file as a small [DSL](https://github.com/homa-ae/Weather-Forecast/blob/main/documents/dsl.pseudo) Demo example snippet for the following reasons:
* Easy comprehension of algorithms.
* Helping developers plan and understand the steps required to solve a problem or implement a particular functionality.
* They can outline the logic of their algorithm or program in a clear and structured manner.
* It can also be used as a form of documentation to explain the logic of the algorithm or program to others.     

## 11. Functional Programming
* Final Data Structures: This code primarily uses dictionaries to structure data, particularly in cleaned_weather_data and airpollution_data. These dictionaries are not        mutated after initialization. Lists are also used to hold pollutant values, which are likewise not mutated. These dictionaries are used as containers to hold data            retrieved from external APIs (OpenWeatherMap and OpenAQ), and their content is not intended to be modified within the application and remain unchanged throughout the         program's execution. Therefore, the code predominantly utilizes final data structures.
* Side-effect-free functions: The functions in the codebase primarily perform their intended tasks without causing side effects. They retrieve data, update GUI                 elements, and display charts without altering external states directly. This means they fetch information they need, like weather data or pollution levels, but don't    modify anything else in the program while doing so.
* (https://github.com/homa-ae/Weather-Forecast/blob/main/src/high-order_function.py)
