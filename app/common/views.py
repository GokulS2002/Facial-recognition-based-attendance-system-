
from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Employee
from .aws_utils import upload_image_to_s3,detect_faces,compare_faces
import uuid
import time
import json
import base64
from io import BytesIO
from django.conf import settings
# Create your views here.

def index(request):
   
   
    return render(request, 'common/index.html')


def video(request):
   
   
    return render(request, 'common/video.html')

def check(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone')
        captured_image = request.POST.get('captured_image')

        
        image_data = base64.b64decode(captured_image.split(",")[1])
        filename = f"compare_{phone_number}_{uuid.uuid4()}.png"
        
        
        bucket_name = settings.AWS_S3_BUCKET_NAME
        upload_image_to_s3(captured_image, filename)

        
        try:
            employee = Employee.objects.get(phone_number=phone_number )
            stored_image = employee.s3_image_url.split('/')[-1]  
            
            face_comparison_results = compare_faces(filename, stored_image, bucket_name)

            
            print("Comparison Results:", face_comparison_results)

            return JsonResponse({
             
                'face_comparison_results': face_comparison_results,
            
            })
            
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'NO employee'}, status=404)

    return render(request, 'common/check.html')    


def employee_signup(request):
    if request.method == 'POST':
        name = request.POST.get('empname')
        phone_number = request.POST.get('phone')
        captured_image = request.POST.get('captured_image')

     
        image_data = base64.b64decode(captured_image.split(",")[1])
        filename = f"{phone_number}_{uuid.uuid4()}.png"

     
        s3_image_url = upload_image_to_s3(captured_image, filename)

        
        bucket_name = settings.AWS_S3_BUCKET_NAME
        face_detection_results = detect_faces(filename, bucket_name)

       
        employee = Employee.objects.create(
            name=name,
            phone_number=phone_number,
            s3_image_url=s3_image_url
        )

        return JsonResponse({
            'message': 'Employee registered',
                's3_image_url': s3_image_url,
            'face_detection_results': face_detection_results  
        })

    return render(request, 'common/employee_signup.html')



def employee_compare(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone')
        captured_image = request.POST.get('captured_image')

        
        image_data = base64.b64decode(captured_image.split(",")[1])
        filename = f"compare_{phone_number}_{uuid.uuid4()}.png"
        
        
        bucket_name = settings.AWS_S3_BUCKET_NAME
        upload_image_to_s3(captured_image, filename)

        
        try:
            employee = Employee.objects.get(phone_number=phone_number )
            stored_image = employee.s3_image_url.split('/')[-1]  
            
            face_comparison_results = compare_faces(filename, stored_image, bucket_name)

            
            print("Comparison Results:", face_comparison_results)

            return JsonResponse({
             
                'face_comparison_results': face_comparison_results,
            
            })
            
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'NO employee'}, status=404)

    return render(request, 'common/employee_compare.html')




# def employee_compare(request):
#     if request.method == 'POST':
#         captured_image = request.POST.get('captured_image')

     
#         image_data = base64.b64decode(captured_image.split(",")[1])
#         filename = f"compare_{uuid.uuid4()}.png"

        
#         bucket_name = settings.AWS_S3_BUCKET_NAME
#         upload_image_to_s3(captured_image, filename)

#         # Initialize S3 client to list objects in the bucket
#         s3_client = boto3.client(
#             's3',
#             aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#             region_name=settings.AWS_REGION_NAME,
#         )

#         # List all the objects (images) in the S3 bucket
#         response = s3_client.list_objects_v2(Bucket=bucket_name)

#         face_comparison_results = []
        
#         if 'Contents' in response:
#             for obj in response['Contents']:
#                 stored_image = obj['Key'] 

              
#                 comparison = compare_faces(filename, stored_image, bucket_name)
                
#                 print("Compare Faces Response:", response)
#         if face_comparison_results:
#             return JsonResponse({
#                 'message': 'Face comparison completed successfully',
#                 'face_comparison_results': face_comparison_results
#             })
#         else:
#             return JsonResponse({'error': 'No faces matched in the comparison.'}, status=404)

#     return render(request, 'common/employee_compare.html')
