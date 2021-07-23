# TransactionHandler
Serverless application for processing transactions data

The application will have a single purpose.
The lambda function inside of it will be invoked by calls to an API via the 
POST HTTP method.
In result:

- Lambda will return a status code of 400 for inconvenient payload
- Lambda will return a status code of 201 for successfully processed payload
