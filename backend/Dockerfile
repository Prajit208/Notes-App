FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend files (including the 'app' folder)
COPY . .

# Run FastAPI (pointing to app.main because main.py is inside the app folder)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]