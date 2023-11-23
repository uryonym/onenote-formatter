import requests
from msal import PublicClientApplication

app = PublicClientApplication(
    "ede6ffd5-bb73-4f26-a75c-f87026b9b52c",
    authority="https://login.microsoftonline.com/consumers",
)
scopes = ["https://graph.microsoft.com/.default"]

result = app.acquire_token_interactive(scopes=scopes)
access_token = result["access_token"]

headers = {"Authorization": f"Bearer {access_token}"}
params = {"$select": "id,displayName,sectionsUrl"}
response = requests.get(
    "https://graph.microsoft.com/v1.0/me/onenote/notebooks",
    headers=headers,
    params=params,
).json()

notes_list = response["value"]

# print(notes_list)

params2 = {"$select": "id,displayName,pagesUrl"}
response2 = requests.get(
    notes_list[1]["sectionsUrl"], headers=headers, params=params2
).json()

sections_list = response2["value"]

# print(sections_list)

params3 = {"$select": "id,title,contentUrl"}
response3 = requests.get(
    sections_list[1]["pagesUrl"], headers=headers, params=params3
).json()

pages_list = response3["value"]

# print(pages_list)

params4 = {"includeIDs": "true"}
for page in pages_list:
    response4 = requests.get(page["contentUrl"], headers=headers, params=params4)
    response4.encoding = response4.apparent_encoding
    print(response4.text)

# content = [
#     {
#         "target": "div:{482ea122-e398-80ee-b8a8-40423cfaa5e2}{32}",
#         "action": "replace",
#         "content": """<div id="div:{482ea122-e398-80ee-b8a8-40423cfaa5e2}{32}" style="position:absolute;">
#                         <p id="p:{482ea122-e398-80ee-b8a8-40423cfaa5e2}{34}" style="font-family:游ゴシック;margin-top:0pt;margin-bottom:0pt">スマホから作成テスト</p>
#                         <p id="p:{482ea122-e398-80ee-b8a8-40423cfaa5e2}{37}" style="font-family:游ゴシック;margin-top:0pt;margin-bottom:0pt">スマホから作成テスト</p>
#                 </div>""",
#     }
# ]

# response5 = requests.patch(
#     "https://graph.microsoft.com/v1.0/users/uryonym@outlook.com/onenote/pages/0-8ca02d3a58d8a8ebad26151439ea4e97!1-5FE289DDED4922A9!4100/content",
#     headers=headers,
#     json=content,
# )

# print(response5)
