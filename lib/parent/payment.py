import os
import requests
import json
import random
from models import Student, session
import webbrowser
from utils import recursion_of_menu

consumer_key = os.environ.__getitem__('CONSUMER_KEY')
consumer_secret = os.environ.__getitem__('CONSUMER_SECRET')



class Payment:
    def __init__(self):
        self.base_url = 'https://pay.pesapal.com/v3/api/'

    def authenticate(self):
        end_point = 'Auth/RequestToken'

        payload = json.dumps({
            "consumer_key": consumer_key,
            "consumer_secret": consumer_secret,
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.request("POST", self.base_url+end_point, headers=headers, data=payload)

        return response.json()['token']

    def ipn_registration(self):
        end_point = "URLSetup/RegisterIPN"

        payload = json.dumps({
            "url": "https://www.calvinarieri.site/ipn",
            "ipn_notification_type": "GET"
        })
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.authenticate()}',
        }

        response = requests.request("POST", self.base_url+end_point, headers=headers, data=payload)
        return response.json()

    def submit_order(self, first_name, last_name, middle_name, payment_id, amount, phone_number, email, description):
        end_point = "Transactions/SubmitOrderRequest"

        payload = json.dumps({
            "id": payment_id,
            "currency": "KES",
            "amount": amount,
            "description": description,
            "callback_url": "https://www.pesapal.com/response-page",   # TODO: change call back url.
            "notification_id": self.ipn_registration()['ipn_id'],
            "billing_address": {
                "email_address": email,
                "phone_number": phone_number,
                "country_code": "254",
                "first_name": first_name,
                "middle_name": middle_name,
                "last_name": last_name,
                "line_1": "",
                "line_2": "",
                "city": "",
                "state": "",
                "postal_code": None,
                "zip_code": None
            }
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.authenticate()}',
        }

        response = requests.request("POST", self.base_url+end_point, headers=headers, data=payload)
        return response

    def tracking_order(self, tracking_id):
        end_point = f"Transactions/GetTransactionStatus?orderTrackingId={tracking_id}"

        payload = {}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.authenticate()}',
        }

        response = requests.request("GET", self.base_url+end_point, headers=headers, data=payload)
        return response


def pay_school_fees(student_code):
    new_fee_payment = Payment()
    first_name = input("Enter first name: ")
    middle_name = input("Enter second name: ")
    last_name = input("Enter last name: ")
    random_code = random.randint(1000, 99999999)
    phone_number = input("Enter phone number format 7XXXX...:  ")
    email = input('Email: ')
    print('Please wait as we initiate school fees')
    student = session.query(Student).filter(Student.unique_code == student_code).first()

    
    request = new_fee_payment.submit_order(first_name, 
                                 last_name, 
                                 middle_name, 
                                f'{student_code} {random_code}',
                                3, 
                                phone_number, 
                                email, 
                                f' Fee payment for {student.student_first_name} {student.student_surname}'
                                  )
    if request.json()['status'] == '200':
        os.system('clear')
        url =request.json()['redirect_url']
          # Try to open the URL in a new tab
        try:
            webbrowser.open_new_tab(url)
           
        except webbrowser.exceptions.OpenNewTabNotSupported:
            # If opening in a new tab is not supported, fall back to opening in a new window
            webbrowser.open(url)
        finally:
            print(f'Click on this link to pay school fees if you are not redirected to your browser: {url} ')
            print('If payment is succefull you will receive confirmation email from school')
           
    print('There might be a problem please check your internet connection then try again Later')