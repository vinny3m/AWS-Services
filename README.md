## Setup Installations:

Initially created a table in DynamoDb named StudentRecords with student_id as a primary key. </br>
![DynamoDb](images/DynamoDb.png)

Then lambda function named <b>"serverless-api-p" is created </br>
![lambda](images/lambda-1.png)
I used python as a programming language to write the lambda function. 
 Role permisisions are also set to access the dynamoDb from lambda function and also gave permission access for CloudWatchLogsFullAccess.
 <br/>
 ![lambda](images/lambda-2.png)

 Then created API gateway and created resource and methods for those and deployed them. 
</br>
below is the pic for created url's
![API-Gateway](images/APIGateway-1.png)

### Testing the Urls's
below are the pics for test images in postman for those url's
</br>
First posting the data to db </br>
![post](images/post.png)

get students data using student_id </br>
![get](images/get.png)

delete student data with using student_id</br>
![delete](images/lambda-2.png)

check student data is present in database or not after deleting by using get method 
![get-2](images/get-2.png)

