# Dark Calculator

## How to run the service

### Run nativaly

Please run under python 3. Other versions are not tested.

```
pip install -i requirements.txt
python web.py
```

### Run via Docker

```
docker build -t dark .
docker run -p 922:922 dark
```

### Run via docker-compose

```
docker-compose up --build dark
```

## How to test

Run `./test.sh`

## How to use the service

Follow examples in `test.sh`