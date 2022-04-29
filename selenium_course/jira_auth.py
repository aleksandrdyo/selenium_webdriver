import re
from jira import JIRA
from requests_toolbelt import user_agent

jira = JIRA('https://dyo999.atlassian.net/',
            basic_auth=('dyoalex@gmail.com', ''),
            options={"headers": {"User-Agent": user_agent("my_package", "0.0.1")}}
            )

project = 'project = dyo'

def get_my_open_tasks():
    issues1 = jira.search_issues(project)
    for x in range(len(issues1)):
        print(issues1[x])

get_my_open_tasks()


#issue = jira.issue('DYO-1')
#print(issue.fields.project.key)
#print(issue.fields.issuetype.name)
#print(issue.fields.reporter.displayName)
#print(issue.fields.summary)
#print(issue.fields.comment.comments)