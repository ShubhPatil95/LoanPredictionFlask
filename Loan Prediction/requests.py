# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 23:18:23 2021

@author: hp
"""
import requests

url = 'http://localhost:5000/predict_api'

r = requests.post(url,json={"Gender":0,"Married":0,"Dependents":0,"Education":1,"Self_Employed":0,"ApplicantIncome":5849,"CoapplicantIncome":0,"LoanAmount":146,"Loan_Amount_Term":360,"Credit_History":1,"Property_Area":2})

print(r.json())

