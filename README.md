# GeoDjango Project

This project displays weather forecast using GeoDjango, Leaflet.js, and PostGIS.

## Technologies Used
- Python
- Django
- GeoDjango
- Leaflet.js
- PostGIS

## Installation

### Prerequisites
- Python 3.x
- PostgreSQL
- PostGIS

### Windows

1. Install the required packages:
 ```
  pip install -r requirements.txt
  ```

2. Configure PostGIS extension:
- Windows:
  Download and install the PostGIS extension for PostgreSQL from the official website: https://postgis.net/windows_downloads/.

3. Create a database and enable the PostGIS extension:

- Windows:
  - Open the command prompt as an administrator.
  - Switch to the PostgreSQL user:
    ```
    psql -U postgres
    ```
  - Create a new database:
    ```
    CREATE DATABASE {DATABASE_NAME};
    ```
  - Connect to the newly created database:
    ```
    \c {DATABASE_NAME};
    ```
  - Enable the PostGIS extension:
    ```
    CREATE EXTENSION postgis;
    ```

4. Migrate the database:
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```

5. Run the project:
    ```
    python manage.py runserver
    ```

6. To add a city and location, create a superuser account:
    ```
    python manage.py createsuperuser
    ```


## Usage

1. Access the project by visiting `http://localhost:8000` in your web browser.

2. Login using the superuser account created earlier.

3. Click on "Cities" and add a city and its location.

4. The weather forecast for the selected city will be displayed using Leaflet.js and the data stored in the PostGIS database.



