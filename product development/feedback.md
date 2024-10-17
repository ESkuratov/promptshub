Role: you are a data analyst who speaks Russian. 
Main Task: Please give me a list of statisctics for feedback of clients
 
Steps to complete task:
1. take file and parsing 'Feedback ЧДП КН_Ипотека с 09.08.2024 по 17.09.2024.csv'
2. To use this list of resons:
"""
|не возможно сделать чдп при кредитных каникулах|
|не возможно сделать чдп/пдп в приложении|
|как сделать пдп/чдп|
|при аресте не возможно сделать пдп|
|не прошло пдп/чдп|
|почем списана проценты при чдп|
|не понятны правила чдп|
|после чдп появилась просрочка|
|взяли кредит мошеники|
|как узнать сумму на пдп|
|когда проходит чдп/пдп|
|почему для чдп указана минимальная сумма|
|как сделать чдп на дату платежа|
|как отменить чдп|
|при чдп сумма списана больше|
|не понятно как скорректировать сумму|
|увеличивается платеж после чдп|
|как сделать пдп в день подачи|
|как отменить исполненое чдп|
|как проверить на какую суммы было чдп|
|как понять какой тип чдп был сделан|
|не понятно как проверить что есть заявка на чдп/пдп|
|при чдп не в дату платежа делается и текущий платеж|
|как сделать чдп на мальенькую сумму|
|не изменился платеж|
|изменился день списания чдп|
"""
4. for each line in the file 'Feedback ЧДП КН_Ипотека с 09.08.2024 по 17.09.2024.csv', identify and addd a short reason for customer dissatisfaction
5. count the number of repetitions of the reasons for customer dissatisfaction

Goal: give me report that show statistics on the reasons for customer dissatisfaction in a tabular format with this coloumns """ reson | counts """ and sort this report by the quantity column in descending order
