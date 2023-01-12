import requests

def main():
  
    # print the library's version
    print('Requests library version: ' + requests.__version__)


    # get the Google home page, display the intial "moved" status, then the "ok" after redirect
    res = requests.get('http://google.com')
    
    print('Initial status code: ' + str(res.history[0].status_code))
    print('Status code after auto-redirect: '+ str(res.status_code))


    # get the raw file of this script off of GitHub, and print it out
    raw = requests.get('https://raw.githubusercontent.com/mattsheydwasser/CMPUT404-Lab01/master/script.py')

    print('\nSource code of this file: \n\n'+raw.text)

    
if __name__ == '__main__':
    main()