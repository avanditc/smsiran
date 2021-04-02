import requests

try:
    import json
except ImportError:
    import simplejson as json

class APIException(Exception):
    pass

class HTTPException(Exception):
    pass

class SmsIR(object):
    def __init__(self, UserApiKey,SecretKey):
        self.version = 'v1'
        self.host = 'RestfulSms.com/api'
        self.headers = {
	    'Content-Type': 'application/json',
        'charset': 'utf-8'
        }
        self.bodies = {
            "UserApiKey": UserApiKey,
            "SecretKey": SecretKey
        }
        self.TokenUrl = 'https://RestfulSms.com/api/Token'    
        self.TokenKey = ""
        try:
            content = requests.post(self.TokenUrl , headers=self.headers, json = self.bodies).content
            try:
                response = json.loads(content.decode("utf-8"))
                print("IsSuccessful : " + str(response["IsSuccessful"]))
                print("Message : " + response["Message"])
                print("----------------------")
                print("TokenKey : \n" + response["TokenKey"])
                print("----------------------")
                self.TokenKey = response["TokenKey"]
            except ValueError as e:
                raise HTTPException(e)
        except requests.exceptions.RequestException as e:
            raise HTTPException(e)

    def otp(self,MobileNumber, Code):
        url = "https://RestfulSms.com/api/VerificationCode"
        headers = {
        'Content-Type': 'application/json',
        'x-sms-ir-secure-token':self.TokenKey,
        'charset': 'utf-8',
        }
        bodies = {
            "Code": Code,
            "MobileNumber": MobileNumber,
        }
        try:
            content = requests.post(url , headers=headers, json = bodies).content
            try:
                response = json.loads(content.decode("utf-8"))
                print("VerificationCodeId : " + str(response["VerificationCodeId"]))
                print("IsSuccessful : " + str(response["IsSuccessful"]))
                print("Message : " + response["Message"])
                print("Verification Code is: ",Code)
            except ValueError as e:
                raise HTTPException(e)
        except requests.exceptions.RequestException as e:
            raise HTTPException(e)

# tt = SmsAPI("14769c3b5e4af9518bd69c4","it66)%#teBC!@*&123445")
# tt.otp("09150938139","951234")


    def getToken(self,UserApiKey,SecretKey):
        host = 'RestfulSms.com/api'
        headers = {
	    'Content-Type': 'application/json',
        'charset': 'utf-8'
        }
        bodies = {
            "UserApiKey": UserApiKey,
            "SecretKey": SecretKey
        }
        TokenUrl = 'https://RestfulSms.com/api/Token'  
        TokenKey = ""
        try:
            content = requests.post(TokenUrl , headers=headers, json = bodies).content
            try:
                response = json.loads(content.decode("utf-8"))
                print("IsSuccessful : \n" + str(response["IsSuccessful"]))
                print("Message : \n" + response["Message"])
                print("TokenKey : \n" + response["TokenKey"])
                self.TokenKey = response["TokenKey"]
            except ValueError as e:
                raise HTTPException(e)
        except requests.exceptions.RequestException as e:
            raise HTTPException(e)
