import time
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

class ResponseTimeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Record the start time
        request.start_time = time.time()

    def process_response(self, request, response):
        # Calculate the duration in nanoseconds
        duration = (time.time() - request.start_time) * 1_000_000_000  # Convert to nanoseconds
        
        # Check if the response is JSON
        if response['Content-Type'] == 'application/json':
            # Parse the existing JSON response
            response_data = JsonResponse(response.content)
            response_data['response_time_ns'] = duration
            return response_data

        # If not JSON, just return the original response
        return response
    