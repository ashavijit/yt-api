
# YouTube Video API

## Project Overview

This project aims to create an API for fetching the latest YouTube videos based on a predefined search query, storing them in a database, and providing paginated responses through a GET API endpoint. The project is built using Django and includes features like continuous background fetching, support for multiple API keys, and scalability.

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/ashavijit/yt-api
cd yt-api
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Set up the Django environment variables:

   - Create a `.env` file in the project directory.
   - Add the following environment variables to the `.env` file:

     ```plaintext
     SECRET_KEY=your_django_secret_key
     YOUTUBE_API_KEYS=your_api_key_1,your_api_key_2,your_api_key_3
     ```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Start the Django server:

```bash
python manage.py runserver
```

6. Access the API at `http://localhost:8000/api/videos/`.

## API Endpoints

- `GET /api/videos/`: Returns the stored video data in a paginated response sorted in descending order of published datetime.

## Dashboard (Optional)

To access the dashboard for viewing stored videos with filters and sorting options:

1. Ensure the Django server is running.
2. Visit `http://localhost:8000/admin/` in your browser.
3. Log in with your admin credentials.
4. Navigate to the "Videos" section.
## Docker Instructions

1. Build the Docker image:

```bash
docker build -t youtube-video-api .
```

2. Run the Docker container:

```bash
docker run -p 8000:8000 youtube-video-api
```

## Terraform Instructions

1. Install Terraform from [here](https://www.terraform.io/downloads.html).
2. Navigate to the `terraform` directory:

```bash
cd terraform
```

3. Initialize the Terraform working directory:

```bash
terraform init
```

4. Create a `terraform.tfvars` file in the `terraform` directory and add the following variables:

   ```plaintext
   project = "your_project_id"
   region = "your_region"
   ```

5. Apply the Terraform configuration:

  ```bash
  terraform apply
  ```

6. Access the API at `http://<EXTERNAL_IP>:8000/api/videos/`.



3. Access the API at `http://localhost:8000/api/videos/`.

## Contributing

Feel free to contribute to this project by submitting bug reports, feature requests, or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
