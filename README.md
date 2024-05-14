# MobileSam Segmentation Model Service

This microservice uses FastAPI to explore the MobileSam segmentation model as a RESTful API. The service allows users to upload images and get segmentation results.

**Note**
- The FastAPI is defined in the server.py file.
- A Dokerfile is created to enable the docker image building and runing.
- This README file is created to provide clear instructions for setting up, running, and interacting with the service.

## Setup

1. **Clone this repository:**

    ```bash
    git clone https://github.com/fxshan/mobilesam-task.git
    cd mobilesam-task
    ```

2. **Install the Requirements**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Service

### Locally
**Run the FastAPI server:** 

```bash
uvicorn server:app --reload 
```
The service will be available at http://localhost:8000/docs.

### Using Docker
1. **Ensure Docker is installed:** Make sure Docker is installed on your system. If not, you can download and install it from Docker's official website.
2. **Build the Docker image:**

    ```bash
    docker build -t mobilesam-service .
    ```
3. **Run the Docker container:**

    ```bash
    docker run -d -p 8000:8000  mobilesam-service 
    ```
The service will be available at http://localhost:8000/docs.

## API Endpoints
- **POST /segment-image** Upload an image file through [Browse] button.
- Then [Execute] it.
- The Server response shows the segmentation results.
