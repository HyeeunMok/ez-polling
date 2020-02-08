# EZ Polling(Built with Python and Django)

![Bridge School Survey](bridgeSurvey.gif)

# Overview

Bridge School always do their survey from students when each cohort finishes. 

# Purpose

I created an EZ Polling is web application which will allow an administrator from  Bridge School to create survey questions and view survey results. Students can vote from student view page.

# Functionalities:

**1. Different view pages for students and the administrator :**  
&nbsp; &nbsp; * Added the admin's email and password to make sure only admin can reach to admin page <br />

**2.  Add questions:**  
    Be able to add questions in admin page

**3. Edit and delete questions:**  
    Be able to edit and delete questions in admin page

**4. Vote**  
    Students can select their answers for each questions

**5. Display result:**  
    Students and the administrator both are able to see the result

# How to run

**\# Install dependencies** <br />
pipenv install

cd ez_polling <br />

**\# Serve on localhost:8000** <br />
python manage.py runserver
