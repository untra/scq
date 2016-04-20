  # scq
Our main repo for the SCQ senior project.

## Installing:

Make sure you have python3 and [gulp](https://github.com/gulpjs/gulp/blob/master/docs/getting-started.md) installed on your computer. Then run:

```
make build
```

This will install all of the pip modules as well as the

## Running:

To run the server, make sure you have rethinkDB is up.

```
make serve
```

## Installing (Hard Way):
We are using virtual environments to manage our dependencies and make sure they are the same between dev environments. If you don't have a virtualenv setup for this project, this is how to do it.

To setup virtualenvs in general on your computer, do the following:
```
brew install nodejs
sudo easy_install pip
sudo pip install virtualenvwrapper
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh
```

To setup our specific environment:
```
mkvirtualenv scq
```

Whenever you are going to work on the project to ensure that we are all using the same dependencies:
```
workon scq
```

Add the following to ~/.bashrc (or zshrc if you use one):

```
export WORKON_HOME=$HOME/Envs
source /usr/local/bin/virtualenvwrapper.sh
```

Then source it (bashrc example below):
```
source ~/.bashrc
```

Then go to the project and run this command in your project directory to install the dependencies.
```
make build
```
you will likely be asked for sudo privileges to install all needed packages

## Install [rethinkdb]( https://rethinkdb.com/docs/install/):

On Mac:

```
brew update && brew install rethinkdb
```

[On Linux](https://www.rethinkdb.com/docs/install/ubuntu/):

Copy and past the entire codeblock:

```
source /etc/lsb-release && echo "deb http://download.rethinkdb.com/apt $DISTRIB_CODENAME main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list
wget -qO- http://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install rethinkdb
```

## API

### List user information
*Test: PASS*
```
GET /api/me
```
**Response:**
```
 Status: 200 OK
 {
   "registration": "registration_culdap",
   "primary_affiliation": "Student",
   "majors": ["Computer Science"],
   "dob": "1990-01-01",
   "status": "Senior",
   "pending_groups": [],
   "survey_responses": [],
   "answers": [],
   "departments": ["Computer Science"],
   "email": "sung.bae@colorado.edu",
   "last_sign_in": 1461132923.425379,
   "minors": ["Mathematics"],
   "subscribed_groups": [],
   "ethnicity": "Asian",
   "answered_surveys": [],
   "username": "suba8204",
   "created_surveys": [],
   "gender": "Male",
   "accepted_tos": true,
   "id": "0510b13d-ea5d-45e7-9a85-503fa984a257",
   "date_registered": 1461132919.8357852,
   "native_language": "English",
   "unanswered_surveys": []
 }
 ```

### Change user information
*Test: PASS*
```
POST /api/me
```
**Parameter: Must be in JSON format, take a look at schema/sampleMe.json**

| Field               | Type          | Description                                                       |
| ------------------- | ------------- | ----------------------------------------------------------------- |
| email               | String        | User's email must be Colorado domain (i.e. user@colorado.edu).    |
| status              | String        | User's academic year (i.e. Freshman, Sophomore, Junior, Senior).  |
| primary_affiliation | String        | User's affiliation to CU (i.e. Student, Faculty, Both).           |
| dob                 | String        | User's date of birth in the form of year-month-day.               |
| native_language     | String        | User's native language.                                           |
| gender              | String        | User's gender.                                                    |
| ethnicity           | String        | User's, ethnicity.                                                |
| major               | String[]      | User's major(s).                                                  |
| minor               | String[]      | User's minor(s).                                                  |
| departments         | String[]      | User's departments.                                               |

**Response:**
```
 Status: 200 OK
{
  "registration": "registration_culdap",
  "courses_taught": [],
  "primary_affiliation": "Faculty",
  "majors": ["Computer Science"],
  "dob": "1991-01-23",
  "status": "Senior",
  "pending_groups": [],
  "survey_responses": [],
  "answers": [],
  "departments": ["Computer Science", "Mathematics"],
  "email": "sung@colorado.edu",
  "last_sign_in": 1461132923.425379,
  "minors": ["Mathematics"],
  "subscribed_groups": [],
  "ethnicity": "Asian",
  "answered_surveys": [],
  "username": "suba8204",
  "courses": [],
  "created_surveys": [],
  "gender": "Male",
  "accepted_tos": true,
  "id": "0510b13d-ea5d-45e7-9a85-503fa984a257",
  "date_registered": 1461132919.8357852,
  "native_language": "English",
  "unanswered_surveys": []
}
 ```

### Display surveys taken by user
*Test: PASS*
```
GET /api/surveys
```
**Response:**
```
Status: 200 OK
[
  {
    "creator_id": "3a1ae272-8eea-4dd5-8ba8-1d1aee042a8c",
    "created_timestamp": 1456181796.9387083,
    "responses": [],
    "item_id": "1d1eda7f-9f53-42e3-b030-5e1977c354e1",
    "id": "36057d08-dfe2-44a7-a368-29b19fd89bdc",
    "closed_timestamp": null,
    "deleted": false,
    "questions": [
      {
        "id": "5839dadf-d840-4973-be35-e66903e7ade0",
        "title": "nam illud quidem adduci vix possum, ut ea, quae senserit ille, tibi non vera videantur.",
        "response_format": "multipleChoice",
        "options": [
          "alpha",
          "beta",
          "gamma",
          "delta"
        ]
      },
      {
        "id": "ca88eae6-8200-4307-b465-bef63c54bad3",
        "title": "Nec vero, ut noster Lucilius, recusabo, quo minus omnes mea legant.",
        "response_format": "trueOrFalse",
        "options": [
          "yes",
          "no"
        ]
      },
      {
        "id": "27fe2556-5a91-490a-9481-1aa7729f2d6d",
        "title": "Qui autem alia malunt scribi a nobis, aequi esse debent, quod et scripta multa sunt, sic ut plura nemini e nostris, et scribentur fortasse plura, si vita suppetet; et tamen, qui diligenter haec, quae de philosophia litteris mandamus, legere assueverit, iudicabit nulla ad legendum his esse potiora.",
        "response_format": "rating",
        "options": []
      },
      {
        "id": "41ff5241-0ec2-4849-a608-45e48f6e7707",
        "title": "Contra quos omnis dicendum breviter existimo.",
        "response_format": "trueOrFalse",
        "options": [
          "yes",
          "no"
        ]
      }
    ],
    "item_name": "test_course",
    "item_type": "Course",
    "creator_name": "suba8204"
  }
]
```

### Create/update user's survey questions.
*Test: PASS*
```
POST /api/surveys
```
**Parameter: Must be in JSON format, take a look at schema/sampleSurvey.json**
**Note: If this survey already exists, then this post request will update the survey with the new questions given and delete the old questions.**

| Field            | Type          | Description                                                                                |
| ---------------- | ------------- | ------------------------------------------------------------------------------------------ |
| id               | String        | **Required**. Id of the survey.                                                            |
| item_id          | String        | **Required**. Id of item (i.e. Course, Instructor, User).                                  |
| item_type        | String        | **Required**. Types can be of the following: Instructor, Course, User.                     |
| item_name        | String[]      | **Required**. The name for the survey.                                                     |
| creator_id       | String        | **Required**. User's rethinkdb generated id, who created the survey.                       |
| creator_name     | String        | **Required**. User's username, who created the survey.                                     |
| questions        | String[]      | **Required**. Questions must be a contain a list with title, response_format, and options. |
| title            | String        | **Required**. This is the actual question itself (i.e. Did you like this course?).         |
| response_format  | String        | **Required**. Types of responses are: trueOrFalse, multipleChoice, freeResponse, etc.      |
| options          | String[]      | **Required**. If it is a multipleChoice question, you must provide the options.            |

**Response:**
```
Status: 200 OK
```

### Answer user's questions to a survey
*Test: PASS*
```
POST /api/response
```
**Parameter: Must be in JSON format, take a look at schema/sampleResponse.json**

| Field              | Type          | Description                                               |
| ------------------ | ------------- | --------------------------------------------------------- |
| responder_id       | String        | **Required**. User's id associated with to account.       |
| survey_id          | String        | **Required**. Survey id associated to User's survey.      |
| question_responses | String[]      | **Required**. User's answers to the survey questions.     |

**Response:**
```
Status: 200
```

### Refresh user's cookie
*Test: PASS*
```
GET /api/refresh
```
**Response:**
```
Status: 200 OK
```
