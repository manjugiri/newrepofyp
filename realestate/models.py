from django.db import models

# Create your models h
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from PIL import Image
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile

import accounts
from accounts.models import Account
# Create your models here.
STATUS_CHOICES = [
    ('Rent', 'Rent'),
    ('Sale', 'Sale'),
    ('Auction', 'Auction')
]

TYPE_CHOICES = [
    ('Home', 'Home'),
    ('Land', 'Land'),
    ('Room', 'Room'),
]

class Properti(models.Model):
    added_by = models.ForeignKey(
    settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    ptype = models.CharField(max_length=50, choices=TYPE_CHOICES)
    area = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True)
    number_of_rooms = models.IntegerField(null=True, blank=True)
    price = models.IntegerField()
    has_installment = models.BooleanField(default=False)
    has_insurance = models.BooleanField(default=False)
    description = models.TextField()
    address = models.CharField(max_length=455)
    garden = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    bathtub = models.BooleanField(default=False)
    ac = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    play_ground = models.BooleanField(default=False)
    video = models.URLField(blank=True, null=True)
    photo = models.ImageField(upload_to='prop/%Y/%m/%d')
    paid = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    seodescription = models.TextField(blank=True)
    bidding_start_time = models.DateTimeField(blank=True, null=True)
    bidding_end_time = models.DateTimeField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)



    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
        ordering = ['-paid', '-timestamp', ]

    def __str__(self):
        return self.title

    def is_bid_start(self):
        import datetime
        time_now = datetime.datetime.now(self.bidding_start_time.tzinfo)
        if self.bidding_start_time:
            if self.bidding_start_time < time_now:
                return True
        return False

    def maximum_bid_till_now(self):
        from django.db.models import Max
        try:
            return self.bidders_prop.all().aggregate(Max('bid_amount')).get('bid_amount__max')
        except:
            return 'No any Bid'


    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.id}-{self.title}-{self.address}')
        self.seodescription = str(self.description[:145])+' '+str(self.address)
        if self.ptype == "Land":
            self.garden = self.garage = self.swimming_pool = self.bathtub = self.ac = self.internet = self.play_ground = False
        if not self.id:
            self.photo = self.compressImage(self.photo)

        # Call the real save() method
        super(Properti, self).save(*args, **kwargs)

    def compressImage(self, uploadedImage):
        new = Image.open(uploadedImage)
        imageTemproary = new.resize((1200, 675))
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize((1020, 573))
        imageTemproary.save(outputIoStream, format='PNG', quality=60)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % uploadedImage.name.split('.')[
0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return uploadedImage


class Bidders(models.Model):
    properti = models.ForeignKey(Properti, related_name = 'bidders_prop', on_delete=models.CASCADE)
    bid_amount = models.FloatField()
    user = models.ForeignKey(Account, related_name = 'bidder_user', on_delete = models.PROTECT)


# Bankloan
class Bank(models.Model):
    Bank_image = models.ImageField(upload_to='prop/%Y/%m/%d')
    Bank_name = models.CharField(max_length=50)
    Phone_number = models.CharField(max_length=50)
    Rate =  models.CharField(max_length=50)
    Tenure = models.CharField(max_length=50)

    def __str__(self):
            return self.Bank_name

class ApplyAgent(models.Model):
    user = models.OneToOneField(Account, related_name = 'agent', on_delete = models.CASCADE, blank=True)
    Agency_name = models.CharField(max_length=50)
    Agency_Location = models.CharField(max_length=50)
    Agency_Contact = models.CharField(max_length=50)
    Agency_Email = models.EmailField()
    Agency_Description = models.CharField(max_length=255)
    Agency_logo = models.ImageField(blank=True,null=True, upload_to='prop/%Y/%m/%d')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
            return self.Agency_name

    def total_rating(self):
        from django.db.models import Avg
        if self.rating_of_agent.all().exists():
            return range(int(self.rating_of_agent.aggregate(Avg('value')).get('value__avg')))
        return False


class AgentRating(models.Model):
    agent  = models.ForeignKey(ApplyAgent, related_name = 'rating_of_agent', blank = True, on_delete = models.CASCADE)
    value = models.IntegerField()
    rating_by = models.ForeignKey(Account, related_name = 'agent_rater', blank = True, on_delete = models.CASCADE)

   
