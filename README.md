# Streamlit User Authentication and Text Analysis App

This app allows users to register, log in, and perform text analysis using Streamlit.

## Requirements

- Python 3.11
- Docker (optional but recommended)
- Streamlit
- psycopg2 (for PostgreSQL connection)
- hashlib (for password hashing)

## How to Run

### Option 1: Running Locally

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:
    ```bash
    streamlit run streamlit_app.py
    ```

### Option 2: Running with Docker

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Build and run the Docker container:
    ```bash
    docker-compose up
    ```

3. The app will be available at `http://localhost:8501`.

## Database Configuration

Ensure your PostgreSQL credentials are set correctly, either in the code or through environment variables.

