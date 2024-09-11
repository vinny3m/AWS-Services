## Setup Installations:
Initially created a table in DynamoDb named <b>StudentRecords</b> with <b>student_id</b> as a primary key. <br><br>
![DynamoDb](images/DynamoDb.png)
<br><br>
Then lambda function named <b>"serverless-api-p"</b> is created <br><br>
![lambda](images/lambda-1.png)
<br><br>
I used python as a programming language to write the lambda function. 
 Role permisisions are also set to access the dynamoDb from lambda function and also gave permission access for CloudWatchLogsFullAccess.
 <br><br>
 ![lambda](images/lambda-2.png)
<br><br>
 Then created API gateway and created resource and methods for those and deployed them. 
</br>
After deployment the url is:
<b> "https://shrvt75jte.execute-api.us-east-1.amazonaws.com/production/students?student_id=126" </b> 
<br><br>
below is the pic for created url's
![API-Gateway](images/APIGateway-1.png)
<br><br>


### Testing the Urls's
Below are the pics for test images in postman for those url's
<br><br>
First posting the data to database
<br><br>
![post](images/post.png)
<br><br>
get students data using student_id
<br><br>
![get](images/get.png)
<br><br>

## Data in DynamoDb
Sample data in the table
<br><br>
![db-items-1](images/db-items-1.png)
<br><br>


delete student data with using student_id
<br><br>
![delete](images/delete.png)
<br><br>
check student data is present in database or not after deleting by using get method.
<br><br>
![get-2](images/get-2.png)
<br><br>

Items in dynamoDb are as follows:
<br><br>
![db-items](images/db-items.png)
<br><br>


## Challenges faced:
Need to check location and time while creating the table in DynamoDb, lambda Function and API gateway also need to configure permissions correctly for DynamoDbfull access and then checked ClodWatchlogs for 500 internal server errors and rectified them. 