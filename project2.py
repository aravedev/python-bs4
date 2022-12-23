from bs4 import BeautifulSoup as bs
import requests

# Load the webpage content
r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

# Convert to BeautifulSoup Object
soup = bs(r.content,'lxml')

# Print out the html
# print(soup.prettify()) # prettify() give us a nice identation as a normal html code

# Grabbing h2 tag
#print(soup.h2)

# Using find and find_All :
# Grabbing the same h2 using find
first_h2 = soup.find('h2')
#print(first_h2)

# Now using find_all
allH2 = soup.find_all('h2') # the result returns a list with all matches.
#print(allH2)

# Passing a list of elements to look for
first_header = soup.find(['h1','h2'])
#print(first_header) # it returns the first occurency in this case h1 because h2 comes after in the html code

# Doing the same but with find_all
headers = soup.find_all(["h1","h2"])
#print(headers)

# You can pass also attributes with find / find_all
paragraph = soup.find_all('p', attrs={"id":"paragraph-id"})
#print(paragraph)

# You can nest find/find_all
body = soup.find("body")
div = body.find("div")
header = div.find("h1")
#print(header)

# We can search for specific string with find/find_all using re library

import re

search_some = soup.find_all("p", string=re.compile("Some")) # specific word
headers = soup.find_all("h2", string=re.compile("(H|h)eader")) # doesnt matter upper or lower case
#print(search_some)
#print(headers)


### Using select method:
# This is used for CSS selectors, its function is similar to find_all
#  ###

content = soup.select("p")
select_div_p = soup.select("div p") # selecting p tags inside div
#print(content)
#print(select_div_p)

select_p_after_h2 = soup.select("h2 ~p")
print(select_p_after_h2)

#min 23:07