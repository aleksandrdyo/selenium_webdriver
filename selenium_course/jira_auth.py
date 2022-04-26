import re
from jira import JIRA
from requests_toolbelt import user_agent

jira = JIRA('https://dyo999.atlassian.net/',
            basic_auth=('dyoalex@gmail.com', ''),
            options={"headers": {"User-Agent": user_agent("my_package", "0.0.1")}}
            )



issue = jira.issue('DYO-1', fields='summary,comment')

summary = issue.fields.summary         # 'Field level security permissions'
