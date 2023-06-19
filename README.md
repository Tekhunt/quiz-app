# Quiz-app Assessment

## App Description
Our quiz app is used by Shopify merchants on their online stores. Some stores may have have more than one quiz. Each quiz has a unique quiz ID number assigned to it to differentiate it. Stores are typically identified by their store/Shopify URL (in some cases the human-readable vendor name may also be used). 

### Your assignment should aim to:-
1. Query a clone of our database (RDS PostgreSQL) to return all the quiz IDs associated with a store (this can be in multiple potentially valid formats like URL or store name etc. so please use your discretion to parse and check/accept inputs accordingly).
2. Create an API endpoint (on an AWS server in Python) to be able to accept a store as argument and return all quiz IDs associated with the store as payload. Please define your return codes, expected input and output formats in detail to create clear API documentation that can be used by a third-party developer without any need to consult you directly.