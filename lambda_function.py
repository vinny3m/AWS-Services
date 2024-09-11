import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecords')  

def lambda_handler(event, context):
    print('Request event:', event)
    response = {}
    
    if event['httpMethod'] == 'GET' and event['path'] == '/students':
        student_id = event.get('queryStringParameters', {}).get('student_id')
        response = get_student(student_id)
    
    elif event['httpMethod'] == 'POST' and event['path'] == '/students':
        request_body = json.loads(event['body'])
        response = save_student(request_body)

    elif event['httpMethod'] == 'DELETE' and event['path'] == '/students':
        student_id = event.get('queryStringParameters', {}).get('student_id')
        response = delete_student(student_id)
    
    else:
        response = build_response(404, '404 Not Found')

    return response
    
    
    
    
    
    

def get_student(student_id):
    try:
        response = table.get_item(Key={'student_id': student_id})
        item = response.get('Item')
        if item:
            return build_response(200, item)
        else:
            return build_response(404, {'message': 'Student not found'})
    except Exception as e:
        print('Error fetching student:', e)
        return build_response(500, {'message': 'Internal Server Error'})
        
        
        
        
        
        

def save_student(student):
    try:
        table.put_item(Item=student)
        return build_response(200, {
            'Operation': 'SAVE',
            'Message': 'SUCCESS',
            'Item': student
        })
    except Exception as e:
        print('Error saving student:', e)
        return build_response(500, {'message': 'Internal Server Error'})





def delete_student(student_id):
    try:
        response = table.delete_item(Key={'student_id': student_id})
        if response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
            return build_response(200, {'message': 'Student deleted successfully'})
        else:
            return build_response(404, {'message': 'Student not found'})
    except Exception as e:
        print('Error deleting student:', e)
        return build_response(500, {'message': 'Internal Server Error'})

def build_response(status_code, body):
    return {
        'statusCode': status_code,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(body)
    }
