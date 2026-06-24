def success_response(message, data=None, status_code=200):
    response = {
        "success": True,
        "message": message
    }
    
    if data:
        response["data"] = data
        
    return response, status_code

def error_response(message, status_code=400):
    return {
        "success": False,
        "message": message
    }, status_code