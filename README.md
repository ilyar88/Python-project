# Full Stack Automation Final Project

This project was created to demonstrate my knowledge and skills in Automation Testing.

---

## About

The project demonstrates a smart automation infrastructure. It is built in a hierarchical order of modules. The modules contain several classes with methods. There are main/common/actions/page object modules. This approach allows tests to be created in a very simple way with minimal lines of code. The infrastructure supports different kinds of applications and is designed to be easily maintained!

## Project Overview

The project is an example of infrastructure for automation testing of different kinds of applications:

- **Web-based application**
- **Mobile application**
- **Web API**
- **Electron application**
- **Desktop application**

## Prerequisites

1. Install [Pycharm](https://www.jetbrains.com/pycharm/download/?section=windows)
2. Install [Grafana](https://grafana.com/grafana/download/8.3.3?platform=windows&edition=oss)
3. Install [Allure Report](https://allurereport.org/docs/install-for-windows/)
4. Install [Grafana last version for running API automation](https://grafana.com/grafana/download?edition=oss)
5. Run Grafana server from the installation folder.

## To Run the Project

1. Run this command in the terminal:
   ```bash
   pip install -r requirements.txt
   ```
2. Add the following folders:
   - `allure-results`
   - `allure-screen-shots`
3. Run the following command from the `test_cases` package for example:
   ```bash
   pytest -v -s .\test_web.py --alluredir="../allure-results/$(Get-Date -Format yyyy-MM-dd-HH-mm)"
   ```
4. Run Allure Serve:
   ```bash
   allure serve ../allure-results/[with current date]
   ```
   Example:
   ```bash
   allure serve ../allure-results/2025-01-03-20-59
   ```

## Infrastructure Highlights

- **Page Object Design Pattern**
- **Project Layers** (Extensions/Work Flows/Test Cases...)
- **Support of Different Clients/Browsers**
- **Failure Mechanism**
- **Common Functionality**
- **External Files Support**
- **Reporting System** (including screenshots and screen recordings)
- **Visual Testing**
- **DB Support**
- **CI Support**

## Applications Used

- **Grafana** - Web-based Grafana site
- **Metric Conversions** - Mobile application
- **Students.jar** - Test API (needs download)
- **Electron application** - Todolist App application
- **Desktop application** - Windows Calculator

## Tools & Frameworks

- **Listeners** - Interface used to generate logs and `EventFiringWebDriver` module
- **MySQL Free Online DB** - Used for login to Swag Labs web page and filling information in the Checkout page
- **Jenkins** - For tests execution
- **REST API** - For API testing
- **Allure Reports** - Main reporting system

---

This project demonstrates a robust and modular approach to full-stack automation testing, providing support for various platforms and ensuring maintainability.
