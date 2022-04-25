from pymongo import MongoClient
from telegram.ext import *
from telegram import *


client = MongoClient('mongodb+srv://test:test@cluster0.p1jkn.mongodb.net/test_bot?retryWrites=true&w=majority')
db = client["test_bot"]
user_ph_number = db["phone_number"]
user_fullname = db["Full name"]
user_region = db["region"]
user_attempt = db["attempt"]
user_balans = db["balans"]
user_test_dates = db["test_dates"]
user_first_subject = db["first_subject"]
user_second_subject = db["second_subject"]

#------------------------------------------------------------------tables---------------------------------#
def user_ph_number_func(id,number):
    insert_number = { "id": id, "number": number }
    user_ph_number.insert_one(insert_number)
def user_full(id,fullname):
    user_full = { "id":id, "fullname":fullname }
    user_fullname.insert_one(user_full)
def user_reg(id,region):
    user_regg = { "id":id, "region":region }
    user_region.insert_one(user_regg)
def user_att(id,attempt):
    user_atm = { "id":id, "attempt":attempt }
    user_attempt.insert_one(user_atm)
def user_bls(id,balans):
    user_bls = { "id":id, "balans":balans }
    user_balans.insert_one(user_bls)
def user_dates(id,name,dates):
    user_date = { "id":id, "name":name, "dates":dates }
    user_test_dates.insert_one(user_date)
def user_1_sub(id,subject):
    user_frs = { "id":id, "subject":subject }
    user_first_subject.insert_one(user_frs)
def user_2_sub(id,subject):
    user_sec = { "id":id, "subject":subject }
    user_test_dates.insert_one(user_sec)























