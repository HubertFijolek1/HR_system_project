import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        logger.info(f"Incoming request: {request.method} {request.get_full_path()}")

    def process_exception(self, request, exception):
        logger.error(f"Error occurred: {exception}", exc_info=True)
