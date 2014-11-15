from datetime import datetime
from django.db import models
import uuid

class UUIDField(models.CharField) :
	
	def __init__(self, *args, **kwargs):
		kwargs['max_length'] = kwargs.get('max_length', 64 )
		kwargs['blank'] = True
		models.CharField.__init__(self, *args, **kwargs)
	
	def pre_save(self, model_instance, add):
		if add :
			value = str(uuid.uuid4())
			setattr(model_instance, self.attname, value)
			return value
		else:
			return super(models.CharField, self).pre_save(model_instance, add)

class SarrumaObject(models.Model):
	uuid = UUIDField(primary_key=True, editable=False)
	date_created = models.DateTimeField(default=datetime.now)