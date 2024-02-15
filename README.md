# price-alert-system

## Scrip Model (scrip stands for all kind of crypto/digital currencies)
Scrip model stores currency and it's price. for reach currency code there would be only one record in this table

## POST /scrips/ api
expect json body {"code": "BTC", "price": 10000} 
returns json response {"id": <int>, "code": "BTC", "price": 10000}

## PATCH /scrips/1/ api
expects json body {"price": 20000}
update respective scrip's price and returns 200 

## GET /scrips/ api
returns list of scrips [{"id": <int>, "code": <str>, "price": <float>}]

## Alert Model
alert model stores target currency, price and status

## POST /alerts/ api
expects json body {"scrip"}

## PATCH /alerts/<int>/ api
to delete alert use this api and send {"status": "DELETED"} 
this api returns 204 status code

## GET /alerts/ api
this api returns list of alerts. 
this api supports pagination as well 
you can also filter alerts on status field as well by passing status 
url param 

### start service
docker-compose up --build

### test case 1
#### add new currency (scrip)
curl --location 'http://localhost:8000/scrips/' \
--header 'Content-Type: application/json' \
--data '{
    "code": "BTC",
    "price": 10000
}'
#### add new alert 
curl --location 'http://localhost:8000/alerts/' \
--header 'Content-Type: application/json' \
--data '{
    "scrip": "1",
    "target_price": 20000
}'
#### update price of currency (scrip)
curl --location --request PATCH 'http://localhost:8000/scrips/1/' \
--header 'Content-Type: application/json' \
--data '{
    "price": 20000
}'

check logs for alert message

### test case 2
#### add new currency (scrip)
curl --location 'http://localhost:8000/scrips/' \
--header 'Content-Type: application/json' \
--data '{
    "code": "ETH",
    "price": 5000
}'
#### add new alert 
curl --location 'http://localhost:8000/alerts/' \
--header 'Content-Type: application/json' \
--data '{
    "scrip": "2",
    "target_price": 6000
}'
#### update price of currency (scrip)
curl --location --request PATCH 'http://localhost:8000/scrips/2/' \
--header 'Content-Type: application/json' \
--data '{
    "price": 6000
}'

check logs for alert message