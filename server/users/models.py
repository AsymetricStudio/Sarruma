from django.db import models
from sarruma.models import SarrumaModel

# Create your models here.
class User(SarrumaModel):
	username = models.CharField(unique=True)
	password = models.CharField()
	date_loggedin = models.DateTimeField(null=True, blank=True)

	def __unicode__(self):
		return "%s::%s" % (self.username, self.uuid)