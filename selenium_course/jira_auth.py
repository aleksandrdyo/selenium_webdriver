import re
from jira import JIRA

jira = JIRA('https://dyo999.atlassian.net/',
            basic_auth=('dyoalex@gmail.com', ''))