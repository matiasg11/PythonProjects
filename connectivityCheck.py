# Import urllib
# Request the data from the url
# Write the function to take the url
# Response

import urllib.request as urllib


def main(url):
    print("Checking!... ")
    response = urllib.urlopen(url)
    print("Connected to", url, "succesfully")
    print("Response: ", response.getcode())

print("This program checks the connectivity of the site.")
inputUrl = input("Input the URL to check ")

main(inputUrl)
    




