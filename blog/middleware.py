from django.utils.deprecation import MiddlewareMixin
#from django.http import HttpResponse

class BlogMiddleware(MiddlewareMixin):
	def process_request(self, request):
		print ("Middleware executed")
