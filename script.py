import requests

def main():
  
    # print the library's version
    print('Requests library version: ' + requests.__version__)


    # get the Google home page, display the intial "moved" status, then the "ok" after redirect
    res = requests.get('http://google.com')
    
    print('Initial status code: ' + str(res.history[0].status_code))
    print('Status code after auto-redirect: '+ str(res.status_code))
    

main()