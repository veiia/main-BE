# main-BE

auth
-MADEN
sign in
sign up         
sugn out
check token
reset token
update token


Overview
- GET /projects list
- POST /project - create new project
- POST /domain - create new domain

Overview Project view
- GET /project - get info of project
- PATCH /project - update project info
- POST /start
- POST /stop
- POST /pause
- GET /logs etc

Overview Project Deployments - for each container

Overview Project Settings
- GET /project/settings/general 
- POST /project/settings/general 
- PATCH /project/settings/general 
- DELETE /project/settings/general


Activity 
- GET /activity/containers/logs get logs for each container for user
- GET /activity/user/logs - all logs for user actions

Usage 
- GET /usage

Settings
- GET /settings (general)
- PATCH /settings (general)


FEEDBACK
- POST /feedback - создать обращение
- GET /feedback/id - взять обращение одно
- GET /feedback - взять список своих обращений