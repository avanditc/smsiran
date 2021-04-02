# Welcome to SMSIRAN python module

"A library for using SMS web services in IRAN"
Unfortunately, Iranian web services do not have the necessary code to use the texting tools for Python. The module that you see here is a set of codes so that you can easily perform texting operations with all text messaging web services.
We will be continuously adding more web services to the module.
Please join us in completing the module if you have Python programming skills and have access to one of the web SMS services.

## ماژول پایتون ارسال پیامک برای وب سرویس های ایرانی

متاسفانه وب سرویس های ایرانی فاقد کدهای لازم برای استفاده ابزارهای ارسال پیامک برای پایتون می باشند. ماژولی که اینجا شاهد آن هستید مجموعه کدهایی است تا بتوانید به آسانی عملیات ارسال پیامک را با تمامی وب سرویس های ارسال پیامک انجام دهید.
ما به صورت ممتد وب سرویس های بیشتری را به ماژول اضافه خواهیم کرد.
لطفا اگر مهارتی در برنامه نویسی به زبان پایتون دارید و دسترسی به یکی از وب سرویس های ارسال پیامک دارید ما را در کامل کردن ماژول همراهی کنید.

## How to use

Each web service in the form of a Python class will be able to embed in your applications.

## نحوه استفاده

هر وب سرویس به صورت یک کلاس پایتون قابلیت درون سپاری در برنامه های شما خواهد داشت.

## Example for SMS.IR

``` python
>>> from smsiran import SmsIR
# Create object with "UserApiKey","SecretKey" inputs.
# it will create token for you and print it:
>>> smsir = SmsIR("14769***********9c4","it66*********445")
# Send OTP with otp fucntion and "mobile number" and "otp code" as input:
>>> smsir.otp("0915***8139","951234")
"""
VerificationCodeId : [a float number]
IsSuccessful : True
Message : your verification code is sent
Verification Code is: 951234
"""
```

## Web Services

List of supported SMS web services: (Other web services will be added over time)
لیست وب سرویس های پیامکی که پشتیبانی می شوند: (به مرور زمان دیگر وب سرویس ها نیز اضافه می شوند)

|SMS Web Service |Module Name                          |Class Name                         |
|----------------|-------------------------------|-----------------------------|
|SMS.ir          |`sms_ir.py`                    |`SmsIR`                  |
|Kavenegar.com   |`Not Yet`                      |`Not Yet`              |
|Ghasedak.io     |`Not Yet`                      |`Not Yet`              |
|etc.            |`Not Yet`                      |`Not Yet`              |
