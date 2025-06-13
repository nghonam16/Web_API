## FastAPI Performance Test Project

### 1. Introductions

This project builds a simple RESTful API using [FastAPI](https://fastapi.tiangolo.com/) and utilizes [Pydantic](https://docs.pydantic.dev/) for input validation. The API supports CRUD operations for products and includes performance testing using [Locust](https://locust.io/)

### 2. Technologies Used

- Python 3.10+
- FastAPI
- Uvicorn (ASGI server)
- Pydantic
- Locust (for performance testing)

### 3. Installation
Step 1: Clone the repository
```bash
git clone https://github.com/your-username/fastapi-performance.git
cd fastapi-performance
```
Step 2: Create and activate a virtual environment
```bash
# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate
```
Step 3: Install libs
```bash
pip install -r requirements.txt
```

### 4. Run FastAPI Server
```bash
uvicorn main:app --reload
```
Access Swagger UI: http://127.0.0.1:8000/docs


#### Supported Endpoints
| Method | Endpoint           | Description                  |
| ------ | ------------------ | ---------------------------- |
| POST   | `/products/`       | Create a new product         |
| GET    | `/products/{name}` | Retrieve product information |
| PUT    | `/products/{name}` | Fully update a product       |
| PATCH  | `/products/{name}` | Partially update a product   |
| DELETE | `/products/{name}` | Delete a product             |

### 5. Run Locust
```bash
locust -f locustfile.py --host http://127.0.0.1:8000
```
Open Locust UI at: http://localhost:8089
```
Enter:
Number of users: 50
Spawn rate: 10
Click: Start swarming
```

### 6. Save Performance Logs
```bash
locust -f locustfile.py --host http://127.0.0.1:8000 --csv=logs/perf
```
```
perf_stats.csv         - Response times, speed, and error stats
perf_failures.csv      - Failure details
perf_distribution.csv  - Response time distribution
```
### 7. Project Goals
- Build a RESTful API using FastAPI
- Use Pydantic for data validation
- Implement complete CRUD functionality
- Conduct performance testing using Locust
- Analyze logs to evaluate and optimize API performance
