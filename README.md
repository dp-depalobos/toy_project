# Target of this application
 Simulate a scenario where an item is on discount. Upon check-out the markdown price should be 
 displayed instead. The approach here is to create three databases, which are 

Item
.ID
.Name
.Price

1. Create clothing endpoints
    1a. [GET] {{url}}/item/<string:name> #Read item data
    1b. [POST] {{url}}/item/<string:name> #Create item data
    1c. [PUT] {{url}}/item/<string:name> #Update item data
    1d. [DELETE] {{url}}/item/<string:name> #Delete item data
    1e. [GET] {{url}}/items/ #Read all item data

Promotion
.ID
.Name
.Discount

2. Create promotion endpoints
    2a. [GET] {{url}}/promotion/<string:name> #Read promotion data
    2b. [POST] {{url}}/promotion/<string:name> #Create promotion data
    2c. [PUT] {{url}}/promotion/<string:name> #Update promotion data
    2d. [DELETE] {{url}}/promotion/<string:name> #Delete promotion data
    2e. [GET] {{url}}/all-promotion/ #Read all promotion data

OrderItems  

3. Create order_item endpoints
    3a. [GET] {{url}}/order_item/<string:name> #Read order_item data
    3b. [POST] {{url}}/order_item/<string:name> #Create order_item data
    3c. [PUT] {{url}}/order_item/<string:name> #Update order_item data
    3d. [DELETE] {{url}}/order_item/<string:name> #Delete order_item data


Order
.ID
.Total

#Implementation
- create virtual environment
./code$ python3 -m venv venv
./code$ source venv/bin/activate
- install dependencies (from previous flask session)
(venv)./code$ pip install -r requirements.txt


initialize postgresql
./workspace$ sudo service postgresql start