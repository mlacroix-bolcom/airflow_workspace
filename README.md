# Codespaces Airflow training environment

This repository contains the code for the Airflow training environment.

## Getting started

1. Check that you have enough memory allocated to your codespaces instance. In the terminal (ctrl + ` ) check you have more than 4GB of allocated memory:

    ```
    docker run --rm "debian:bullseye-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))'
    ```

    And no, 3.9 is not enough. If you see 3.9 means that you did not select the right machine in step 2.

2. Run database migrations *(ONLY RUN ONCE)*

    You need to run database migrations and create the first user account. It is all defined in the docker compose file so just run:
    ```
    docker compose up airflow-init
    ```

3. Now you can start all services:
    ```
    docker compose up
    ```

    This will make Airflow available at: http://localhost:8080

4. Login to Airflow:

    ![image](images/codespaces4.png)


# Running Airflow in a Python Environment
If for some reason it's not possible to you to run Airflow using docker, you can also do it using python.

1. Install airflow
    ```
    pip install apache-airflow
    ```
    or
    ```
    poetry add apache-airflow
    ```

    Make sure you have a virtual environment activated in which you can isolate your code/dependencies

2. initialize the database
    ```
    airflow db init
    ```

3. Create a new user
    ```
    airflow users create --username airflow --password airflow --firstname anon --lastname nymus --role Admin --email user@company.com 
    ```

4. Copy your dags to the dags/ folder
    ```
    cp dags/mydag.py ~/airflow/dags/
    ```

5. In a terminal initialize the webserver
    ```
    airflow webserver -p 8080
    ```

6. In a second terminal initialize the scheduler
    ```
    airflow scheduler
    ```
