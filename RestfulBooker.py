import requests

API = 'https://restful-booker.herokuapp.com/booking'
booking_ids = requests.get(API)
booking_id_data = booking_ids.json()

#Creating an access token for PUT and DELETE booking
CREDS = 'https://restful-booker.herokuapp.com/auth'
user_and_pw = {'username' : 'admin', 'password': 'password123'}
cred_response = requests.post(CREDS, headers = {'Content-type': 'application/json'}, json = user_and_pw)
token = cred_response.json()

#Get booking details for all users
def get_booking_details(nums_list):
    bookings = {}
    for num in nums_list:
        response = requests.get(API + '/' + str(num))
        #In case API is being actively written to and users are deleted, avoid unfound elements
        if response.status_code != 404:
            bookings[num] = response.json()

    return bookings

#Create a booking
booking_details = {'firstname': 'Ben', 'lastname': 'Sherman', 'totalprice': 153, 'depositpaid': False, 'bookingdates': {'checkin': '2021-10-21', 'checkout': '2021-10-31'}, 'additionalneeds': 'Sushi bar in room'}
new_booking = requests.post(API, headers = {'Content-type': 'application/json'}, json = booking_details)
new_booking_data = new_booking.json()



print(new_booking_data)
print(token)
user_ids_list = [23, 25, 11, 10, 3, 24, 19, 28, 21, 7, 34, 30, 27, 20, 29, 15, 5, 14, 35, 22, 18, 31, 12, 9, 4, 33, 16, 36, 32, 1, 17, 26, 8, 13, 6, 2]

print(get_booking_details(user_ids_list))



