from jira import JIRA
from requests_toolbelt import user_agent
from config import JIRA_EP, EMAIL, TOKEN, PROJECT_NM

jira = JIRA(JIRA_EP,
            basic_auth=(EMAIL, TOKEN),
            options={"headers": {"User-Agent": user_agent("my_package", "0.0.1")}}
            )

def get_my_open_tasks():
    issues = jira.search_issues(PROJECT_NM)
    for x in range(len(issues)):
        print(issues[x])

get_my_open_tasks()


#issue = jira.issue('DYO-1')
#print(issue.fields.project.key)
#print(issue.fields.issuetype.name)
#print(issue.fields.reporter.displayName)
#print(issue.fields.summary)
#print(issue.fields.comment.comments)