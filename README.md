# Facebook Scraper With FastAPI

Simple overview of use/purpose.

## Description

A fastAPI aaplication that uses facebook-scraper to scrape a given facebook page and saves the results into mongodb.

## Getting Started

### Installing and Runing

* clone this repo
* Open terminal session pointing to the project and run:
```
docker-compose up
```
* Once the container are up, Open the application throw: 
```
http://localhost:8008/docs

```

### Unit Tests
If you want to run unit tests, run the container using :
```
docker-compose run scraper bash
```
This will create the containers and start a Bash session.

Then to stat tests, run the command:
```
python -m pytest
```
## Project Structure
```
scraper
├── database
│   ├── __init.py__
│   ├── database_manager.py
│
│── service
│   ├── __init__.py
│   ├── app.py
│   ├── constants.py
│   ├── scraper.py
│ 
├── tests
│   ├── __init__.py
│    ├── test_app.py
│
├── __init__.py
│
├── main.py

```
## Packages  

* The ```database``` package responsible for the database connection and persistance .
* The ```service``` package contains the fastAPI app and the scraping script.


