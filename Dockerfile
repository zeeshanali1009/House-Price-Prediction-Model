# 1. Use official Python 3.10 image as base
FROM python:3.10-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the project files into container
COPY . .

# 5. Expose Streamlit default port
EXPOSE 8501

# 6. Run Streamlit app on all network interfaces
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
