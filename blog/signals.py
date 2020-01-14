from django.db.models import signals
from django.dispatch import receiver
from .models import Post

@receiver(signals.pre_save, sender=Post)
def check_product_description(sender, instance, **kwargs):
	print("pre save signal called")
	if not instance.text:
		instance.text = 'this is default description'

@receiver(signals.post_save, sender=Post)
def create_product(sender, instance, created, **kwargs):
    print("Save method is called")		

