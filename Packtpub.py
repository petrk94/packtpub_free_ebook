import urllib.request
import urllib
from bs4 import BeautifulSoup


# Read the html content of the URL into the variable "soup"
soup = BeautifulSoup(urllib.request.urlopen("https://www.packtpub.com/packt/offers/free-learning"), "html.parser")

# Looking up for the title which is in the HTML content related to the information we want to read out and than write the html code into "result"
raw = soup.find_all("div", {"class":"dotd-title"})


print("Packt Publishing - Notifier - Latest Free Learning ebook")
# read the result and strip the white spaces and the html code to get the text 
for result in raw:
     print("latest free ebook title: " + result.get_text().strip())

	 
# Optional: If you want to save the name of the current ebook into a file to processed items
f = open("Packtpub_free_book", "w")
# Write the extracted content as string into the file
f.write(str(result.get_text().strip()))
f.close()


	 
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#strings-and-stripped-strings

# http://stackoverflow.com/questions/20889790/get-text-of-childrens-in-a-div-with-beautifulsoup

#EOF