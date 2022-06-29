CREATE TABLE IF NOT EXISTS test (
	timestamp timestamp PRIMARY KEY,
	trip_id varchar NOT NULL,
	depart_airport varchar(4) NOT NULL,
	return_airport varchar(4) NOT NULL,
	depart_date date NOT NULL,
	return_date date NOT NULL,
	total_cost float NOT NULL,
	depart_datetime timestamp NOT NULL,
	depart_duration float NOT NULL,
	depart_stops float NOT NULL,
	return_datetime timestamp NOT NULL,
	return_duration float NOT NULL,
	return_stops float NOT NULL
)

SELECT * FROM test;