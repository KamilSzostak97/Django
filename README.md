# Link - http://kszostak.pythonanywhere.com/
# ProjectQuiz
My first web application made in Django.

# Homepage
User is greeted by a bootstrap carousel showcasing 3 most popular items. 
On top of the page is grey taskbar with company logo as well as links that allow us to skip to different sections of site.
At the bottom right corner we can find a sticky button that sends as back to the top of the page.

After scroling futher down we can see entire list of all available quizes. At this point taskbar is set to hide.

Later on we are met with about us section preceded by clean static image and company logo. This section is a template that can be filled by informations about company/product. 

Lastly we can see technologies used in the process of creating the website as well as contact informations.

# Quiz
There are two different type of quizes.
First type is a basic test format, every position in this quiz consists of: question, 4 possible anwsers and one correct anwser.
Example of this is IQ test. User is asked to anwser 10 questions by ticking a box next to position he thinks is correct. 
To recive results user must click "Click For Results" button. This action compares all the anwsers user selected to correct 
anwser in a database ( If user did not select a anwser its consider a wrong one ). After comparing anwsers user is given his
score as well as a diagnosis. Diagnosis is simillar to grading system. Program calculates percentage of correct anwsers and
using switch statement user is given information ( grade/diagnosis of score ). 

Second type is a quiz without correct anwsers, it collects input of user and calculates wich position was choosen most often.
Example of this type is "Favourite Junk Food" you are faced with 5 questions. After anwsering them user is given information
about wich food is perfect for him. User also have option to view details of his anwsers by clicking on a button "Show Details".

# ToDo
- Phone version


