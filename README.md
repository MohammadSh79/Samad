# Samad
An automatic food reservation script for [Guilan University Self-Service](https://food.guilan.ac.ir "Guilan University Self-Service") using [Selenium](https://pypi.org/project/selenium/ "Selenium") library and [Python](https://www.python.org/ "Python").

# Usage
Edit `.env` file using a text editor and enter your credentials.

`STUDENT_ID`: The student id of the account that you want to buy food with.

`PASSWORD`: Password of the account.

`FOOD_NAME`: Part of the food name, ie: `شنیسل کارخانه ای`

`SELF_NAME`: Full name of the self-service, ie: `1 - سلف مرکزی`

`NEXT_WEEK`: True if you want to reserve the food which is for next week

Example:


    STUDENT_ID='980122680100'
    PASSWORD='123456789'
    FOOD_NAME='شنیسل کارخانه ای'
    SELF_NAME='سلف مرکزی - 1'
    NEXT_WEEK=False

Then run the code:

    py Samad.py
