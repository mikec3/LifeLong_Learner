# LifeLong_Learner

### Setup

install python

COMMAND LINE
% cd this_file_path
% python3.7 -m venv learner_env		// Creates a virtual env called learner_env
% cd learner_env					// enter the newly created virtual env
% source bin/activate				// Activate the virtual env

// Install required packages
% pip install pandas
% pip install flask
% pip install plotly
% pip install google-cloud-bigquery
$ pip install pyarrow

GitHub
// Create a new github repository @ github.com
// Command line below from activated learner_env
// Create a readme doc & import the newly created repo from github, then commit & push this directory
% echo "# Lifelong_Learner" >> README.md
% git init
% git add README.md
% git commit -m "first commit"
% git remote add origin https://github.com/mikec3/Lifelong_Learner.git
% git push -u origin master


### Running on local

% cd this_file_path
% source bin/activate
% python flask_app.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


% CTRL+C 			// to exit the server
% deactivate		// to exit the venv


### Web Setup

-Create pythonanywhere account - free/basic
-Create a new web app - select flask & python version (used later when using pip)
-Import files and create file structure ex: mysite/templates/index.html
-Open bash console & install requirements
% pip3.7 install google-cloud-bigquery --user
% pip3.7 install plotly==4.8.1 --user
% pip3.7 install pyarrow --user

ADDING FILES USING GITHUB
$ cd mysite
$ git init
$ git remote add origin URL_FOR_GITHUB_REPO
$ git pull origin master
-Navigate to web settings, open WSGI configuration file and alter the 'project_home' to the desired path




### requirements
% pip freeze > requirements.txt 	// creates a requirements.txt file with all packages

% pip install -r requirements.txt   // installs all required packages DOESNT ACTUALLY WORK


# pt 2
#### Adding a graph

$ pip install jupyter				// Command to open jupyter notebook : $ jupyter notebook
