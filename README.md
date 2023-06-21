
<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)
Inpsired by [https://github.com/bereketkibru/Data_engineering_sensor_data](https://github.com/bereketkibru/Data_engineering_sensor_data)

Using a docker-compose file, developed a completely dockerized ELT pipeline with MySQL for data storage, Airflow for automation and orchestration, DBT for data transformation, and a Redash dashboard connected to the MySQL database.

### Built With

Tech Stack used in this project
* [MYSQL](https://dev.mysql.com/doc/)
* [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/)
* [dbt](https://docs.getdbt.com/)
* [Redash](https://redash.io/help/)


<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

Make sure you have docker installed on local machine.
* Docker
* DockerCompose
  
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/pyjavo/update_csv_pipeline
   ```

2. Create directory `/data` at the root of the project.

3. Save file `archivo.csv` within `/data` directory.

4. Build
   ```sh
    docker-compose build
   ```
5. Create DB for server service
   ```sh
   docker-compose run --rm server create_db
   ```
6. Run
   ```sh
    docker-compose up
   ```
7. Open Airflow web browser
   ```JS
   Navigate to `http://localhost:8000/` on the browser
   use `admin` for username
   use `admin` for password
   ```
8. Access redash dashboard
   ```JS
   Navigate to `http://localhost:5000/` on the browser
   ```
9. Access your mysql database using adminar
   ```JS
   Navigate to `http://localhost:8080/` on the browser
   choose mysql databse
   use `root` for username
   use `pssd` for password
   ```

### Documentation
Recommended docstring format is [Google format](https://google.github.io/styleguide/pyguide.html#381-docstrings)

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.


<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: Capture.PNG

