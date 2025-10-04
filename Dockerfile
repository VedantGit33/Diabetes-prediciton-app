# Base Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app1

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app and model files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app1.py", "--server.port=8501", "--server.address=0.0.0.0"]
