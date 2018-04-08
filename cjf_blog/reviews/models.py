from django.db import models

class Review(models.Model):
	pub_date = models.DateTimeField('publication date')
	score = models.DecimalField(max_digits = 3, decimal_places=1)
	subject_name = models.CharField(max_length = 30)
	review_summary = models.CharField(max_length = 50)
	category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.subject_name

class Category(models.Model):
	category = models.CharField(max_length = 30)

	def __str__(self):
		return self.category
