import json
import os
import resend
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from json import JSONDecodeError
from bson.objectid import ObjectId
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any

import uvicorn
from backend.Routes import doctors
from backend.database import connect
from fastapi.middleware.cors import CORSMiddleware

from backend.Schema.schema import UserInput, EmailData
from backend.api.gemini_data import gemini_response

from bson import json_util
from dotenv import load_dotenv

load_dotenv()
resend.api_key = os.getenv('RESEND_API_KEY')
brevo_api_key = os.getenv('BREVO_API_KEY')  # Updated environment variable

# Configure API key authorization for Brevo
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = brevo_api_key

# Create an instance of the API class
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

class ObjectIdEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = FastAPI()
app.include_router(doctors.router)

db = connect.database("medbuddy")

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Location_specialization(BaseModel):
    Location: str
    Specialization: str


@app.get("/")
def read_root():
    return {"message": "Hello! Welcome to Medbuddy."}


@app.post("/gemini_data")
async def root(user_input: UserInput) -> str | dict:
    response = gemini_response(user_input.Text)
    try:
        response_dict = json.loads(response)
        return response_dict
    except JSONDecodeError:
        pass
    return response


@app.post("/match_doctor")
async def match_doctor(details: Location_specialization):
    try:
        print(details)
        doctors_list = db.get_collection('doctors').find({
            "Address.City": details.Location,  # Use a dictionary for filter criteria
            "Specialization": details.Specialization,
        })
        print("search done!")
        matched_doctors = list(doctors_list)  # Convert cursor to a list of matched doctors
        print(matched_doctors)
        if not matched_doctors:
            return []  # Return an empty list if no doctors are found
        for doctor in matched_doctors:
            doctor['_id'] = str(doctor['_id'])
        matched_doctors_str = json.loads(json_util.dumps(matched_doctors))
        return matched_doctors_str  # Return the list of matched doctors
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")


@app.post("/book_appointment/{doctor_id}")
async def book_appointment(doctor_id: str):
    try:
        doctor_id = ObjectId(doctor_id)

        doctor = db.get_collection('doctors').find_one({"_id": doctor_id})
        if doctor:
            return json.loads(json_util.dumps(doctor))
        else:
            return {"message": "Doctor not found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")


@app.post("/send_email")
async def send_email(email_data: EmailData):
    # Define the email details for Brevo
    email_sender = {"name": "Medbuddy", "email": "bhavya12mittal@gmail.com"}
    email_recipient_doctor = [{"email": email_data.doctorEmail}]
    email_recipient_user = [{"email": email_data.userEmail}]

    email_content_doctor = f'<strong>Booked for {email_data.username} at {email_data.time} on {email_data.date}</strong>'
    email_content_user = f'<strong>Booked with {email_data.doctorName} on {email_data.date} at {email_data.time}</strong>'

    # Create the email body for the doctor
    email_doctor = sib_api_v3_sdk.SendSmtpEmail(
        to=email_recipient_doctor,
        sender=email_sender,
        subject='Appointment Booked Doc',
        html_content=email_content_doctor
    )

    # Create the email body for the user
    email_user = sib_api_v3_sdk.SendSmtpEmail(
        to=email_recipient_user,
        sender=email_sender,
        subject='Appointment Booked User',
        html_content=email_content_user
    )

    try:
        # Send the email to the doctor
        response_doctor = api_instance.send_transac_email(email_doctor)
        # Send the email to the user
        response_user = api_instance.send_transac_email(email_user)

        return {"message": "Appointment Booked and Confirmation has been sent to your email"}
    except ApiException as e:
        raise HTTPException(status_code=500, detail=f"Error sending email: {e}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
