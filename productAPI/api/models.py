from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50, null=True)
    availableStock = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.title
    


class Product(models.Model):
    name = models.CharField(max_length=50)
    Class = models.CharField(max_length=50)
    variants = models.ForeignKey(Category, related_name="variants", on_delete=models.CASCADE ,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to='productimage',blank=True, null=True)
    stock = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __unicode__(self):
        return(self.name)

    def image_img(self):
        if self.image:
            return u'<img src="%s" width="50" height="50" />' % self.image.url

