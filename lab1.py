import requests

def main():
  
    # print the library's version
    print('Requests library version: ' + requests.__version__)


    # get the Google home page and print it out
    res = requests.get('http://google.com')
    print('\nGET result: \n\n' + res.text)


    # get the raw file of this script off of GitHub, and print it out
    raw = requests.get('https://raw.githubusercontent.com/mattsheydwasser/CMPUT404-Lab01/master/lab1.py')
    print('\nSource code of this file: \n\n'+raw.text)

    
if __name__ == '__main__':
    main()