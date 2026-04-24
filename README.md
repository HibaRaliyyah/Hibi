# Hibi AI Personal Assistant

## Project Overview
Hibi AI Personal Assistant is a versatile tool designed to assist users in daily tasks through intelligent and conversational interactions. Utilizing advanced AI capabilities, Hibi aims to enhance productivity and simplify everyday decisions.

<img width="1358" height="610" alt="hibiweb" src="https://github.com/user-attachments/assets/2885326b-4736-4100-9c90-6f9c6038805a" />

## Link
https://hibi-personalassistant.vercel.app/

## Features
- **Natural Language Processing**: Understand and respond to user queries in real-time.
- **User Personalization**: Tailors responses and suggestions based on user behavior and preferences about me.

## Tech Stack
- **Programming Language**: Python
- **Framework**: FastAPI for building APIs
- **AI**: Gemini API
- **Deployment**: vercel for hosting and scalability

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
