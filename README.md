Full Stack Automation Final Project
This project was created to demonstrate my knowledge and skills in Automation Testing.
________________________________________
About
The project demonstrates a smart automation infrastructure. It is built in hierarchical order of modules. The modules contain several classes with methods. There are main/common /actions/page object modules. In this way, the tests can be created in a very simple way with a minimum line of code. Also, the infrastructure allows us to work with different kinds of applications. A big advantage of the infrastructure is that it can be easily maintained!
Project Overview
The project is an example of infrastructure for automation testing of different kinds of applications:
•	Web based application
•	Mobile application 
•	Web API 
•	Electron application 
•	Desktop application 
Prerequisites:
1.	Install Grafana from the following website: https://grafana.com/grafana/download/8.3.3?platform=windows&edition=oss
2.	Install Allure report from the following website: https://allurereport.org/docs/install-for-windows/
To run the project, do the following:
1.	Run this command in the terminal: pip install -r requirements.txt
2.	Add the following folders: allure-results and allure-screen-shots
3.	Run the following command from test_cases package: pytest -v -s .\test_web.py --alluredir="../allure-results/$(Get-Date -Format yyyy-MM-dd-HH-mm)"
4.	Run allure serve ../allure-results/[with current date] - for example: 2025-01-03-20-59
Infrastructure project includes using of:
•	Page Object Design Pattern
•	Project Layers (Extensions/Work Flows/Test Cases...)
•	Support of Different Clients/Browsers
•	Failure Mechanism
•	Common Functionality
•	External Files Support
•	Reporting System (including screenshots and screen recordings)
•	Visual Testing
•	DB support 
•	CI support 
________________________________________
List of applications were used in this project:
•	Grafana - Web based Grafana site
•	Metric Conversions - Mobile application
•	Students.jar - Test API(need download for it)
•	Electron application - Todolist App application
•	Desktop application - Windows calculator
Tools & Frameworks used in the project:
•	Listeners - interface used to generate logs and EventFiringWebDriver module.
•	MySQL Free Online DB - used for login to Swag Labs web page and fill information in the Checkout page
•	Jenkins- for tests execution
•	REST Assured - for API testing
•	Allure Reports- as the main reporting system

