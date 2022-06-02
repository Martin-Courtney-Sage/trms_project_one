# TRMS Application Project
Contains the TRMS Python Project 1

## Project Description

The Tuition Reimbursement System, TRMS, allows users to submit reimbursements for courses and training. The submitted reimbursement must be approved by that employee's supervisor, department head, and benefits coordinator. The benefits coordinator then reviews the grade received before finalizing the reimbursement.

## Technologies Used

* Postgres SQL through Amazon RDS - version 13.4
* Python - version 3
* Psycopg2
* PyTest
* Flask 
* Postman
* Selenium
* JavaScript
* HTML
* CSS

## Features

Users have the ability to create, update, read, and delete different types of request options for reimbursement.
These reimbursement requests can then be submitted to the system, where they will then become viewable by the different departments (Supervisor, Department Head, BenCo).
Once visiable, the different departments must approve the requests in a specific order. First the Supervisor, then the Department Head, and finally BenCo.
After the request is approved by all three, then the approved amount of reimbursement will be available to the employee that created the reimbursement.

There is also a login feature that is still in progress of restricting webpage assess to certain individuals that are logged-in. Login parameters are completed.

## Getting Started

Create a local repository on your computer from the following command:
* git clone https://github.com/Martin-Courtney-Sage/trms_project_one.git

## Usage

* Place the SQL information into your database and connect the information in dbconnection.py
* Then open up the app.py and hit the run button
* Navigate to the website by copying the source path from the home-page.html file

## License

Copyright (C) 2022 - Authors at Revature LLC. 

The {TRMS Application} project can not be copied and/or distributed without the express
permission of authors <{courtney306@revature.net}>.
