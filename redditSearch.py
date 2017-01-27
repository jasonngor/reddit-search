import praw, pyperclip
from pprint import pprint

user_agent = "Search my saved links"
r = praw.Reddit(user_agent = user_agent)
r.login('username', 'password', disable_warning = True)
a = r.user.get_saved(time='all', limit=None)

print('Please input search term:')
searchTerm = input()

resultslist = []

for link in a:
    try:
        if searchTerm in link.title.lower():
            resultslist.append(link)

    except AttributeError:
        if searchTerm in link.body.lower():
            resultslist.append(link)

for index, link in enumerate(resultslist):
    if isinstance(link, praw.objects.Submission):
        try:
            print('{}. Post:'.format(index+1), link.title, '\n')
        except:
            pass
    elif isinstance(link, praw.objects.Comment):
        try:
            print('{}. Comment:'.format(index+1), link.body[0:200], '\n')
        except:
            pass
print('Please select your choice:')
choice = input()
choiceIndex = int(choice) - 1
print('\n')

chosenlink = resultslist[choiceIndex]
if isinstance(chosenlink, praw.objects.Submission):
    pyperclip.copy(chosenlink.short_link)
    print('{} copied to clipboard.'.format(chosenlink.short_link))
elif isinstance(chosenlink, praw.objects.Comment):
    pyperclip.copy(chosenlink.permalink)
    print('{} copied to clipboard.'.format(chosenlink.permalink))
