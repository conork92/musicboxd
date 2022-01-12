
make build_db_image:
	docker build -t musicboxd-image .

make create_conatiner_db:
	docker run -d --name musicboxd-postgres -p 5555:5432 musicboxd-image

make run_container:
	docker container start musicboxd-postgres   

make create_airflow:
	cd airflow
	airflow db init
	airflow scheduler

make run_airflow:
	cd airflow
	airflow webserver