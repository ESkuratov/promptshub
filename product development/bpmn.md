Create a BPMN XML flow of the process described below between
<process>...</process>
Make sure to use the right
namespaces,
prefixes

definitions(
 xmlns:tns="http://bpmn.io/schema/bpmn"
  xmlns:activiti="http://activiti.org/bpmn"
)
and BPMNDI elements.

For this process:
<process>
Process Name: Grant Application Processing
Participants (Pools):

Granty(Main Pool)
Citizen (Collapsed Pool)
Sart Event: "Grant Application Submitted"

Task:"Receive and Log Grant Application"

Gateway: "Is Application Complete?"

if Yes:
Task:"Verify Application Documents"
Task:"Check Financial Eligibility"
Gateway:"Is Financial Eligibility Met?"
if Yes:
Task:"Approve Application"
Task:"Notify Citizen of Approval"
End Event:"Grant Approved and Citizen Notified"
if No:
Task:"Disapprove Application"
Task:"Notify Citizen of Disapproval"
End Event:"Grant Disapproved and Citizen Notified"
if No:
Task:"Request Missing of Corrected Information from Citizen"
Task:"Receive Corrected Information"
Gateway:"Is Application Now Complete?"
If Yes, return to "Verify Application Documents"
if No:
Task:"Disapprove Application Due to Incomplete Submission"
Task:"Notify Citizen of Disapproval"
End Event:"Grant Disapproved and Citizen Notified"
</process>
```