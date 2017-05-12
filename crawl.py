from bs4 import BeautifulSoup
import urllib
print "start"
r = urllib.urlopen('https://www.ncbi.nlm.nih.gov/genomes/GenomesGroup.cgi?taxid=10239').read()
print "opened"
soup = BeautifulSoup(r,"lxml")
print type(soup)