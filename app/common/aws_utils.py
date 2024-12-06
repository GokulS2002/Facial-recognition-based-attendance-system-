# employee/aws_utils.py

import boto3
import base64
from django.conf import settings
from io import BytesIO
import os
import json



s3_client = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION_NAME,
)

def upload_image_to_s3(image_base64, filename):
    
    image_data = base64.b64decode(image_base64.split(",")[1])
    
    
    image_file = BytesIO(image_data)
    image_file.seek(0)  

 
    s3_client.upload_fileobj(
        image_file,
        settings.AWS_S3_BUCKET_NAME,
        filename,
        ExtraArgs={'ContentType': 'image/png'}
    )

    return f"https://{settings.AWS_S3_BUCKET_NAME}.s3.amazonaws.com/{filename}"


    


def detect_faces(photo, bucket):
   
    client = boto3.client(
        'rekognition',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION_NAME,
    )

    # Call detect_faces with the photo and bucket details
    response = client.detect_faces(
        Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        Attributes=['ALL']
    )

    print('Detected faces for ' + photo)

    if 'FaceDetails' in response and response['FaceDetails']:
        results = []
        for faceDetail in response['FaceDetails']:
            face_info = {
                'AgeRange': faceDetail['AgeRange'],
                'Gender': faceDetail['Gender'],
                'Smile': faceDetail['Smile'],
                'Eyeglasses': faceDetail['Eyeglasses'],
                'FaceOccluded': faceDetail['FaceOccluded'],
                'Emotions': faceDetail['Emotions'],
                'Confidence': faceDetail['Confidence'],
            }
            results.append(face_info)

            # Print detailed attributes for debugging
            print(json.dumps(face_info, indent=4, sort_keys=True))

        return {'faces': results} 
    else:
        return {'error': 'No face detected in the image'}





def compare_faces(source_image, target_image, bucket):
    
    client = boto3.client(
        'rekognition',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION_NAME,
    )

    # Call compare_faces with the source and target images
    response = client.compare_faces(
        SourceImage={'S3Object': {'Bucket': bucket, 'Name': source_image}},
        TargetImage={'S3Object': {'Bucket': bucket, 'Name': target_image}},
        SimilarityThreshold=99  # Adjust the threshold as needed
    )

    
    # print("Comparison Response:", response)

    
    if 'FaceMatches' in response and response['FaceMatches']:
        matches = []
        for match in response['FaceMatches']:
            matches.append({
                'Similarity': match['Similarity'],
                'Face': match['Face']
            })
        return matches  
    else:
        return {'error': 'No faces matched in the comparison.'}  
