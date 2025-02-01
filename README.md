<!DOCTYPE html>
<html>
<head>
    <title>Full Stack Automation Final Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2 {
            color: #2c3e50;
        }
        ul {
            margin: 10px 0;
            padding-left: 20px;
        }
        li {
            margin-bottom: 5px;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            overflow-x: auto;
        }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Full Stack Automation Final Project</h1>
    <p>This project was created to demonstrate my knowledge and skills in Automation Testing.</p>

    <hr>

    <h2>About</h2>
    <p>The project demonstrates a smart automation infrastructure. It is built in a hierarchical order of modules. The modules contain several classes with methods. There are main/common/actions/page object modules. This approach allows tests to be created in a very simple way with minimal lines of code. The infrastructure supports different kinds of applications and is designed to be easily maintained!</p>

    <h2>Project Overview</h2>
    <p>The project is an example of infrastructure for automation testing of different kinds of applications:</p>
    <ul>
        <li>Web-based application</li>
        <li>Mobile application</li>
        <li>Web API</li>
        <li>Electron application</li>
        <li>Desktop application</li>
    </ul>

    <h2>Prerequisites</h2>
    <ol>
        <li>Install <a href="https://grafana.com/grafana/download/8.3.3?platform=windows&edition=oss">Grafana</a></li>
        <li>Install <a href="https://allurereport.org/docs/install-for-windows/">Allure Report</a></li>
    </ol>

    <h2>To Run the Project</h2>
    <ol>
        <li>Run this command in the terminal: 
            <pre>pip install -r requirements.txt</pre>
        </li>
        <li>Add the following folders: <code>allure-results</code> and <code>allure-screen-shots</code></li>
        <li>Run the following command from the <code>test_cases</code> package:
            <pre>pytest -v -s .\test_web.py --alluredir="../allure-results/$(Get-Date -Format yyyy-MM-dd-HH-mm)"</pre>
        </li>
        <li>Run Allure Serve:
            <pre>allure serve ../allure-results/[with current date]</pre>
            Example:
            <pre>allure serve ../allure-results/2025-01-03-20-59</pre>
        </li>
    </ol>

    <h2>Infrastructure Highlights</h2>
    <ul>
        <li>Page Object Design Pattern</li>
        <li>Project Layers (Extensions/Work Flows/Test Cases...)</li>
        <li>Support of Different Clients/Browsers</li>
        <li>Failure Mechanism</li>
        <li>Common Functionality</li>
        <li>External Files Support</li>
        <li>Reporting System (including screenshots and screen recordings)</li>
        <li>Visual Testing</li>
        <li>DB Support</li>
        <li>CI Support</li>
    </ul>

    <h2>Applications Used</h2>
    <ul>
        <li>Grafana - Web-based Grafana site</li>
        <li>Metric Conversions - Mobile application</li>
        <li>Students.jar - Test API (needs download)</li>
        <li>Electron application - Todolist App application</li>
        <li>Desktop application - Windows Calculator</li>
    </ul>

    <h2>Tools & Frameworks</h2>
    <ul>
        <li>Listeners - Interface used to generate logs and <code>EventFiringWebDriver</code> module</li>
        <li>MySQL Free Online DB - Used for login to Swag Labs web page and filling information in the Checkout page</li>
        <li>Jenkins - For tests execution</li>
        <li>REST Assured - For API testing</li>
        <li>Allure Reports - Main reporting system</li>
    </ul>

</body>
</html>
