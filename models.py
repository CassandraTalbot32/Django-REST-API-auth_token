from django.db import models
from django.urls import reverse

# Create your models here.
class PolicyForm(models.Model):
	Policy_reference	= models.CharField(max_length=120)
	cover_type 	= models.TextField(blank=True, null=True)
	car			= models.DecimalField(decimal_places=2, max_digits=10)
	address		= models.TextField()
	
	
	def get_absolute_url(self):
		return reverse("accounts:policy_template", kwargs={"id": self.id})
