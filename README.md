# u-test

scripts to login to account, scrape html data, and print to terminal

## Getting Started

Clone the repository

Start Docker

In a terminal cd to the repository

Start up the container with:
```
$ docker-compose up
```

To run the scripts open a new terminal and cd to the repository

Enter the container with:
```
$ docker exec -it u-test-server /bin/bash
```

To execute the script without third party libraries run:
```
$ python3 read.py --username <username> --password <password>
```

To execute the script with third party libraries run:
```
$ python3 read_r_bs4.py --username <username> --password <password>
```

To run unit tests:
```
$ python3 -m unittest discover -v
```
```
$ python3 -m u_test.tests.test_models -v
```

To exit the container:
```
$ Ctrl+z
```

To bring down the container:
```
$ Ctrl+c
```
```
$ docker-compose down
```
