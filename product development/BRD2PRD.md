VARS:

Replace the following shortcodes according to your needs:

* = Required
*[TECHNOLOGY]* = Describe that technology do you use to create application.
*[PLATFORMS]* = Describe that platforms do you use to deploy your application. | Example: Desctope, Mobile, Anroid, iOS,  etc...
*[PROJECT_NAME]* = Name of product or features.
*[PRODUCT_OWNER]* = A Name of a person who is responsible for the project. 
*[TEAM]* = Team name.
*[TEAM_MEMBERS]* = Names of team members.
*[TEAM_SIZE]* = Number of team members.
*[PROJECT_DESCRIPTION]* = Describe your
*[PROJECT_GOALS]* = Describe your goals.
*[PROJECT_REQUIREMENTS]* = Describe your requirements.
*[PROJECT_MILESTONE1]* = Describe milestone 1.
*[DOC_LANGUAGE]* = Language in which you want your story to be written | Example: French

--------
START OF PROMPT:

>>>>> CREATE A Product Requirement Document
[PLATFORMS] = Web, Anroid, iOS
[Technology] = Java, JavaScript, Backend Driven UI 
[PROJECT_NAME] = Онлайн ЧДП
[ROLE] = Product owner
[TEAM] = Angry Birds Team
[TEAM_MEMBERS] = Константин, Александр, Сергей
[DOC_LANGUAGE] = Russian
[BRD] = BRD_ER_online_20.09.2024

you are a [ROLE], Write Product Requirement Document for [PROJECT_NAME] use information from file [BRD] include the next elements:

# INSTRUCTIONS
1. write summary all problems break into the buckets and prioritize them
2. write metrics for [PROJECT_NAME] project
3. formulate a main hypothesis for [PROJECT_NAME] project how we impact on metrics 
4. write list JTBD use Format: Situation, Job, Outcome that resolve [PROJECT_NAME] project and prioritize on frequence 
5. write for each JTBD 10 pains of customers
6. write for each JTBD 10 desires of customers
7. write for each JTBD 10 fears of customers
8. describe shortly profile users for each JTBD
9. write list of user stories 
10. write description for each stories iclude next point:
   - short description that contains user flow or script for user
   - Acceptance criteries. 
   - Add [PLATFORM] to Acceptance criteires 
11. give me all answers on [DOC_LANGUAGE]



