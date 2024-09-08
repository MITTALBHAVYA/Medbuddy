
---

# MedBuddy MyCut Backend

The backend for the **MedBuddy MyCut** project is built with FastAPI and integrates with the Gemini AI model to provide an efficient and intelligent healthcare assistant service. This backend handles API requests, interacts with the MongoDB database, and manages email notifications.

## Features

- **AI Integration**: Uses the Gemini AI model to handle user queries and match doctors based on location and specialization.
- **Doctor Management**: Provides endpoints to add, retrieve, and manage doctor information.
- **Appointment Booking**: Allows users to book appointments and receive automated email confirmations.
- **Database Interaction**: Connects to MongoDB for storing and retrieving doctor data.

## Project Structure

```
backend/
├── api/
│   └── gemini_data.py
├── database/
│   └── connect.py
├── Routes/
│   └── doctor.py
└── Schema/
    └── schema.py
```

### `api/`

Contains files related to integrating with external APIs. For example:

- **`gemini_data.py`**: Manages interactions with the Gemini AI model for generating responses and handling user queries.

### `database/`

Handles database connections and interactions. For example:

- **`connect.py`**: Contains the logic to connect to MongoDB.

### `Routes/`

Defines the API routes and handles incoming requests. For example:

- **`doctor.py`**: Provides endpoints to add and retrieve doctor information.

### `Schema/`

Contains Pydantic models for request and response validation. For example:

- **`schema.py`**: Defines the data models used throughout the backend.

## Setup and Installation

1. **Create and Activate Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Environment Variables**

    Create a `.env` file in the root directory with the following variables:

    ```
    GOOGLE_API_KEY=<Your Google API Key>
    DB_URI=<Your MongoDB URI>
    RESEND_API_KEY=<Your Resend API Key>
    BREVO_API_KEY=<Your Brevo API Key>
    ```

4. **Run the FastAPI Server**

    ```bash
    uvicorn main:app --reload
    ```

## API Endpoints

### `/gemini_data`

- **Method**: POST
- **Description**: Handles user queries and generates responses using the Gemini AI model.
- **Request Body**:
    ```json
    {
        "Text": "Your query here"
    }
    ```
- **Response**: JSON object with the AI-generated response.

### `/match_doctor`

- **Method**: POST
- **Description**: Finds doctors based on location and specialization.
- **Request Body**:
    ```json
    {
        "Location": "City",
        "Specialization": "Specialization"
    }
    ```
- **Response**: List of matched doctors.

### `/book_appointment/{doctor_id}`

- **Method**: POST
- **Description**: Retrieves information about a specific doctor by ID.
- **Path Parameter**: `doctor_id` (string)
- **Response**: JSON object with doctor details.

### `/send_email`

- **Method**: POST
- **Description**: Sends appointment confirmation emails to both patients and doctors.
- **Request Body**:
    ```json
    {
        "username": "User Name",
        "userEmail": "user@example.com",
        "doctorName": "Doctor Name",
        "doctorEmail": "doctor@example.com",
        "date": "Appointment Date",
        "time": "Appointment Time"
    }
    ```
- **Response**: Confirmation message indicating that emails have been sent.

## Contributing

Contributions to the backend are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
