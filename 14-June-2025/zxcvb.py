#Consider you are HR operations Manager in Vignan Software Solutions,
#You will be receiving Apllications from the candidate from multiple roles
# You are having list of job roles. WAPP to:-
# View the candidate Application , shortlisted applications,job roles.
# based on your evaluation on CV of a candidate. print whether his/her CV is short listed or not.
# Schedule an interview for the particular shortlisted candidates.
# send a message to the candidate to update the status of their  Level-1: interview feedback and inform
# whether they are qualified or not for further level interview.
# send an offer letter to the shortlisted candidates.

Job_Roles=['Full Stack Developer', 'Data Engineer', 'Java Developer', 'Data Analyst', 'HR', 'Data Scientist']
Can_App=[
    #Name, Mailid, contactno, job applied for
    ['Jyothi','jyothi@gmail.com',1234567890, 'Data Analyst'],
    ['Nadeem','nadeem@gmail.com',89453256776, 'Data Engineer'],
    ['Niharika','niharika@mail.com',9123458908, 'Java Developer'], 
    ['Sravya','sravya@gmail.com',78462672398, 'Full Stack Developer',],
    ['Harshith','harshith@gmail.com',79124867983, 'HR']
]
Shortlisted_App=[
    ['Jagadeesh','abc@gmail.com',68251432876, 'Tech Support'], ['Shraddha','xyz@gmail.com',2635116747, 'SQL Admin' ]
]
Completed=[]
def View_Details():
    while(True):
        print("1. To View the Candidates Applications, ShortListed Applications,Job Roles")
        print("2.To ShortList the Profiles")
        print("3.Schedule an Interview for Shortisted Candidates")

val=Can_App[0][0]
print(val)