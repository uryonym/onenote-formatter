from msal import PublicClientApplication

app = PublicClientApplication(
    "7cc25356-51f2-46a8-80c6-8c7114df1b8a",
    authority="https://login.microsoftonline.com/consumers",
)
result = None

accounts = app.get_accounts()
if accounts:
    account = accounts[0]
    print(account["username"])
    result = app.acquire_token_silent(["User.Read"], account=account)

if not result:
    result = app.acquire_token_interactive(scopes=["User.Read"])

print(result["access_token"])

# token = credential.get_token(scopes=["User.Read"])
# print(token)
# print("hello world")
