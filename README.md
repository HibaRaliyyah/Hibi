# Hibi AI Personal Assistant

## Project Overview
Hibi AI Personal Assistant is a versatile tool designed to assist users in daily tasks through intelligent and conversational interactions. Utilizing advanced AI capabilities, Hibi aims to enhance productivity and simplify everyday decisions.

## Features
- **Natural Language Processing**: Understand and respond to user queries in real-time.
- **Task Management**: Create, track, and manage tasks effortlessly.
- **Integration with APIs**: Connect with various services for seamless data retrieval and task execution.
- **Smart Reminders**: Set reminders that adapt to your schedule and preferences.
- **User Personalization**: Tailors responses and suggestions based on user behavior and preferences.

## Tech Stack
- **Programming Language**: Python
- **Framework**: FastAPI for building APIs
- **Database**: PostgreSQL for data storage
- **Deployment**: Docker for containerization
- **Cloud Service**: AWS for hosting and scalability

## Setup Instructions
1. **Clone the repository**
   ```bash
   git clone https://github.com/HibaRaliyyah/Hibi.git
   cd Hibi
   ```
2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up database**
   - Create a PostgreSQL database and update the `DATABASE_URL` in the `.env` file.
5. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints
- **GET /api/tasks**: Retrieves all tasks.
- **POST /api/tasks**: Creates a new task.
- **PUT /api/tasks/{id}**: Updates a task by its ID.
- **DELETE /api/tasks/{id}**: Deletes a task by its ID.

## Contributing
If you'd like to contribute to this project, please open an issue or submit a pull request. All contributions are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.