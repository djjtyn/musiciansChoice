import os
import boto3
import traceback
# Import the file that has the environment variables
if os.path.exists("env.py"):
    import env as env_variables

class S3Utils:
    
    @staticmethod
    def upload_photo(file_name, object_name):
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(file_name, env_variables.get_s3_bucket_name(), object_name)
        except:
            print("Issue with upload_photo method")
            traceback.print_exc()
            
        
        
        
    
