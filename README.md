# main-BE

auth
- MADEN
- POST /sign-in
- POST/sign-up         
- POST /sign-out
- POST /check-token
- POST /reset-token
update token


Overview
- GET /projects list
- POST /projects/{project_id} - create new project
- GET /projects/{project_id}/domain - get domain (default exists for each project)
- PATCH /projects/{project_id}/domain - patch domain

Overview Project view
- GET /projects/{project_id} - get info of project
- PATCH /projects/{project_id} - update project info
- POST /projects/{project_id}/start
- POST /projects/{project_id}/stop
- POST /projects/{project_id}/pause
- GET /projects/{project_id}/logs etc

Overview Project Deployments - for each container

Overview Project Settings
- GET /projects/settings/general 
- POST /projects/settings/general 
- PATCH /projects/settings/general 
- DELETE /projects/settings/general


Activity 
+- GET /activity/containers get logs for each container for user
+- GET /activity/containers/{container_id}/ get logs for one container for user
+- GET /activity/user - all logs for user actions
+- GET /activity/user/{user_id} - all one log for user actions

Usage 
+- GET /usage/id
+- GET /usage/ - list

Profile Settings
- GET /profile/{id}/settings (general)
- PATCH /profile/{id}/settings (general)


FEEDBACK
+- POST /feedback - создать обращение
+- GET /feedback/id - взять обращение одно
+- GET /feedback - взять список своих обращений
+- GET /feedback/themes - взять список тем