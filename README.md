"# DJANGO_PROJECT" 


Follow the Instruction to run the application.

1. Download The Docker and Docker Compose for your environment.
2. docker-compose -f docker-compose-mysql.yml up. 
NOTE:
(IMPORTANT) Wait for 2 minute before to execute the step 3 just to make sure that the database is ready.

3. open another terminal and run the docker-compose -f docker-compose-inventory.yml up. The application is ready when the container is finish to build 

You should see this 
************************************************************************
*inventory | Django version 2.1.2, using settings 'inventory.settings'  *
*inventory | Starting development server at http://0.0.0.0:3000/        *
*inventory | Quit the server with CONTROL-C.                            *
************************************************************************

Access the application via http://localhost:3000


LIST OF ENDPOINT
uri = http://localhost:3000/store
methid = POST
param = {
    name: "",
    url: ""
}


uri = http://localhost:3000/products
method = POST
param = {
    name: "",
    sku: "",
    quantity: "",
    created_at: "",
    updated_at: "",
    store_id: ""
}

uri = http://localhost:3000/products
method = GET
param = {
    store_id: ""
}


uri = http://localhost:3000/products/:store_id/:product_id 
method = GET

uri = http://localhost:3000/products/inventory
method = POST
param = {
    store_id: "",
    product_id: "",
    quantity: "",
    updated_at: "",
}

uri = http://localhost:3000/store/products
method = GET
param = {
    store_id: "",
    product_id: "",
    quantity: "",
    created_at: "",
}