# Description

Development of a RESTful API by using python and flask.

# Status

Works as is. Working on making it more interesting!

# To run the API

```
pipenv install

./bootstrap.sh
```

# GET and POST commands

```
# inserting a new income
curl -X POST -H "Content-Type: application/json" -d '{
    "amount": 300.0,
    "description": "loan payment"
}' http://localhost:5000/incomes

# listing all incomes
curl http://localhost:5000/incomes
```



