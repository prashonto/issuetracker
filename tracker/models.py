from django.db import models

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	
	
	def __str__(self):
		return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
 

	def __str__(self):
    		return self.name
	

class Issue(models.Model):
	STATUS = (
			('Open', 'Open'),
			('Pending', 'Pending'),
			('Closed', 'Closed'),
			)

	Customer_name = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
	Fab = models.CharField(max_length=200, null=True)
	product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
	Esc_Level = models.IntegerField(null=True)
	Issue_description = models.CharField(max_length=500, null=True)
	POA = models.CharField(max_length=500, null=True)
	Resolution = models.CharField(max_length=500, null=True)
	date_created = models.DateField(null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
 
	def __str__(self):
    		return self.Issue_description
