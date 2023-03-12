# Resume_Maker
WebApp that makes an editable resume for you using your LinkedIn and GitHub profiles.

The above app is ready to deploy, there was a server error I was not able to fix due to a time constraint.
To run it in your system follow the below steps.

Run below command in terminal after replacing path to install all dependancies
'''
pip install -r /path/to/requirements.txt
'''

Then go to the directory which contains the 'manage.py' file and run the below command in terminal
'''
python manage.py runserver
'''

Click in the link generated and fill the required details.
On clicking 'save' you will be redirected to the next page after the app scrapes your profile and saves the required information.
The next form will have information already filled in, you may edit the information or the order of information.
The first 5 skills, 3 jobs and 2 of every other list will be put into the resume, so feel free to edit it.4
Then choose either the 1st or 2nd template and click download for it to automatically download the resume to your downloads file.

Make sure to open the downloaded .docx files as Word documents to maintain formatting.
