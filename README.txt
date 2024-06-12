How to run the file!!!
1. Clone the repository.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install django requests
3. Install dependencies:
bash
pip install django requests
4. Set up environment variables for Gemini API credentials in a .env file:
env
GEMINI_API_KEY=your_gemini_api_key
5. Run migrations and start the development server:
bash
python manage.py migrate
python manage.py runserver

Open the browser and navigate to http://127.0.0.1:8000/.