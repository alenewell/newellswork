import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient
import requests
import os
import json
import mimetypes

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Triggered function to analyze blob and reupload results')

    # Blob Storage settings
    blob_connection_str = os.getenv("")
    container_name = "livesolutionstech"
    blob_name = "extracted_document.json"  # Could be .pdf, .xlsx, .docx, etc.
    result_container = "extracted_document.json"
 
 blob_connection_str = os.getenv("")
    container_name = "livesolutionstech"
    blob_name = "Requirements_Traceability_Matrix.json"  # Could be .pdf, .xlsx, .docx, etc.
    result_container = "Requirements_Traceability_Matrix.json"

    # Document Intelligence settings
    endpoint = os.getenv("")
    api_key = os.getenv("")
    model_id = "/subscriptions/5e345896-dea9-46b8-859a-504a5cab5df4/resourceGroups/Cycle18-Mke/providers/Microsoft.CognitiveServices/accounts/livesolutiontech-resource/projects/livesolutiontech"  # or use prebuilt-read, custom models, etc.

    try:
        # Set up blob client
        blob_service_client = BlobServiceClient.from_connection_string(blob_connection_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_data = blob_client.download_blob().readall()

        # Detect file type
        #content_type, _ = mimetypes.guess_type(blob_name)
        #file_type = "excel" if blob_name.lower().endswith((".xls", ".xlsx")) else "other"

        # Send to Document Intelligence
        headers = {
            "Content-Type": content_type or "application/octet-stream",
            "Ocp-Apim-Subscription-Key": api_key
        }
        url = f"{endpoint}/formrecognizer/documentModels/{model_id}:analyze?api-version=2023-10-31"

        response = requests.post(url, headers=headers, data=blob_data)
        response.raise_for_status()
        result = response.json()

        # Store analysis back in Blob
        result_blob_name = f"{blob_name}-analysis.json"
        result_blob_client = blob_service_client.get_blob_client(container=result_container, blob=result_blob_name)
        result_blob_client.upload_blob(json.dumps(result), overwrite=True)

        return func.HttpResponse(
            f"Analysis complete. File type: {file_type}. Results uploaded to '{result_container}/{result_blob_name}'",
            status_code=200
        )

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return func.HttpResponse("Something went wrong during analysis or upload.", status_code=500)
