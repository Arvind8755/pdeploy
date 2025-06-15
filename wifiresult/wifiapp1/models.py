from django.db import models
# from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('public', 'Public'),
]

    # Result Models

class Result(models.Model):
    title = models.CharField(max_length=400, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    keywords = models.TextField(max_length=300,blank=True, null=True)
    image = models.ImageField(upload_to='og_images/', blank=True, null=True, help_text="Open Graph image for social sharing")
    image_alt = models.CharField(max_length=255,blank=True,null=True,help_text="Alternate text for OG Image (used in og:image:alt)")
    updated_at = models.DateTimeField(auto_now=True)  # automatic on update
    post_date = models.CharField(max_length=100,blank=True, null=True)
    vacancy_info = RichTextField(blank=True, null=True)
    online_application_date= models.CharField(max_length=100,blank=True, null=True)
    online_last_date = models.CharField(max_length=100,blank=True, null=True)
    receipt_of_application = models.CharField(max_length=100,blank=True, null=True)
    last_date_fee = models.CharField(max_length=100,blank=True, null=True)
    correction_date = models.CharField(max_length=100,blank=True, null=True)
    exam_date = models.CharField(max_length=100,blank=True, null=True)
    admit_card_available = models.CharField(max_length=100,blank=True, null=True)
    answerkey_available_date = models.CharField(max_length=100,blank=True, null=True)
    result_available = models.CharField(max_length=100,blank=True, null=True)
    final_result_available = models.CharField(max_length=100,blank=True, null=True)
    applecation_fee= RichTextField(blank=True, null=True)
    vacancy_details = RichTextField(blank=True, null=True)
    eligibility_criteria=RichTextField(blank=True, null=True)
    selection_process= RichTextField(blank=True, null=True)
    important_information= RichTextField(blank=True, null=True)
    how_to_apply= RichTextField(blank=True, null=True)
    apply_online_link=models.URLField(blank=True, null=True)
    admitcard_link=models.URLField(blank=True, null=True)
    answerkeyI_link=models.URLField(blank=True, null=True)
    answerkeyII_link=models.URLField(blank=True, null=True)
    result_link=models.URLField(blank=True, null=True)
    resultI_link=models.URLField(blank=True, null=True)
    resultII_link=models.URLField(blank=True, null=True)
    result_final_link=models.URLField(blank=True, null=True)
    notification_link=models.URLField(blank=True, null=True)
    officialwebsite_link=models.URLField(blank=True, null=True)

    slug=models.SlugField(unique=True, blank=True)
    active = models.BooleanField(default=True )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='public')

    def get_absolute_url(self):
        return reverse("resultpost", kwargs={"slug": self.slug}) 
    
# class Meta:
#         model = Result
#         fields = '__all__'

def save(self, *args, **kwargs):
    if not self.slug:
        base_slug = slugify(self.title)
        unique_slug = base_slug
        num = 1
        while Result.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{base_slug}-{num}'
        num += 1
        self.slug = unique_slug
    super().save(*args, **kwargs)


def __str__(self):
        return self.title
    

    # Admitcard Models
        
class Admitcard(models.Model):
    title = models.CharField(max_length=400, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    keywords = models.TextField(max_length=300,blank=True, null=True)
    image = models.ImageField(upload_to='og_images/', blank=True, null=True, help_text="Open Graph image for social sharing")
    image_alt = models.CharField(max_length=255,blank=True,null=True,help_text="Alternate text for OG Image (used in og:image:alt)")
    updated_at = models.DateTimeField(auto_now=True)  # automatic on update
    post_date = models.CharField(max_length=100,blank=True, null=True)
    vacancy_info = RichTextField(blank=True, null=True)
    online_application_date= models.CharField(max_length=400,blank=True, null=True)
    online_last_date = models.CharField(max_length=100,blank=True, null=True)
    receipt_of_application = models.CharField(max_length=100,blank=True, null=True)
    last_date_fee = models.CharField(max_length=100,blank=True, null=True)
    correction_date = models.CharField(max_length=100,blank=True, null=True)
    exam_date = models.CharField(max_length=100,blank=True, null=True)
    exam_date1 = models.CharField(max_length=100,blank=True, null=True)
    exam_date2 = models.CharField(max_length=100,blank=True, null=True)
    exam_date3 = models.CharField(max_length=100,blank=True, null=True)
    admit_card_available = models.CharField(max_length=100,blank=True, null=True)
    answerkey_available_date = models.CharField(max_length=100,blank=True, null=True)
    result_available = models.CharField(max_length=100,blank=True, null=True)
    final_result_available = models.CharField(max_length=100,blank=True, null=True)
    applecation_fee= RichTextField(blank=True, null=True)
    vacancy_details = RichTextField(blank=True, null=True)
    eligibility_criteria=RichTextField(blank=True, null=True)
    selection_process= RichTextField(blank=True, null=True)
    important_information= RichTextField(blank=True, null=True)
    how_to_apply= RichTextField(blank=True, null=True)
    apply_online_link=models.URLField(blank=True, null=True)
    admitcard_link=models.URLField(blank=True, null=True)
    answerkeyI_link=models.URLField(blank=True, null=True)
    answerkeyII_link=models.URLField(blank=True, null=True)
    result_link=models.URLField(blank=True, null=True)
    resultI_link=models.URLField(blank=True, null=True)
    resultII_link=models.URLField(blank=True, null=True)
    result_final_link=models.URLField(blank=True, null=True)
    notification_link=models.URLField(blank=True, null=True)
    officialwebsite_link=models.URLField(blank=True, null=True)
    slug=models.SlugField(unique=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='public')

    def get_absolute_url(self):
        return reverse("admitcardpost", kwargs={"slug": self.slug}) 

class Meta:
        model = Admitcard
        fields = '__all__'

def save(self, *args, **kwargs):
    if not self.slug:
        base_slug = slugify(self.title)
        unique_slug = base_slug
        num = 1
        while Admitcard.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{base_slug}-{num}'
        num += 1
        self.slug = unique_slug
    super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    # Syllabus  Models 

class Syllabus(models.Model):
    title = models.CharField(max_length=400, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    keywords = models.TextField(max_length=300,blank=True, null=True)
    image = models.ImageField(upload_to='og_images/', blank=True, null=True, help_text="Open Graph image for social sharing")
    image_alt = models.CharField(max_length=255,blank=True,null=True,help_text="Alternate text for OG Image (used in og:image:alt)")
    updated_at = models.DateTimeField(auto_now=True)  # automatic on update
    post_date = models.CharField(max_length=100,blank=True, null=True)
    vacancy_info = RichTextField(blank=True, null=True)
    online_application_date= models.CharField(max_length=400,blank=True, null=True)
    online_last_date = models.CharField(max_length=100,blank=True, null=True)
    receipt_of_application = models.CharField(max_length=100,blank=True, null=True)
    last_date_fee = models.CharField(max_length=100,blank=True, null=True)
    correction_date = models.CharField(max_length=100,blank=True, null=True)
    exam_date = models.CharField(max_length=100,blank=True, null=True)
    exam_date1 = models.CharField(max_length=100,blank=True, null=True)
    exam_date2 = models.CharField(max_length=100,blank=True, null=True)
    exam_date3 = models.CharField(max_length=100,blank=True, null=True)
    admit_card_available = models.CharField(max_length=100,blank=True, null=True)
    answerkey_available_date = models.CharField(max_length=100,blank=True, null=True)
    result_available = models.CharField(max_length=100,blank=True, null=True)
    final_result_available = models.CharField(max_length=100,blank=True, null=True)
    applecation_fee= RichTextField(blank=True, null=True)
    subject_details = RichTextField(blank=True, null=True)
    eligibility_criteria=RichTextField(blank=True, null=True)
    selection_process= RichTextField(blank=True, null=True)
    important_information= RichTextField(blank=True, null=True)
    how_to_apply= RichTextField(blank=True, null=True)
    apply_online_link=models.URLField(blank=True, null=True)
    admitcard_link=models.URLField(blank=True, null=True)
    answerkeyI_link=models.URLField(blank=True, null=True)
    answerkeyII_link=models.URLField(blank=True, null=True)
    result_link=models.URLField(blank=True, null=True)
    resultI_link=models.URLField(blank=True, null=True)
    resultII_link=models.URLField(blank=True, null=True)
    result_final_link=models.URLField(blank=True, null=True)
    notification_link=models.URLField(blank=True, null=True)
    officialwebsite_link=models.URLField(blank=True, null=True)
    slug=models.SlugField(unique=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='draft')

    def get_absolute_url(self):
        return reverse("syllabuspost", kwargs={"slug": self.slug}) 

class Meta:
        model = Syllabus
        fields = '__all__'

def save(self, *args, **kwargs):
    if not self.slug:
        base_slug = slugify(self.title)
        unique_slug = base_slug
        num = 1
        while Syllabus.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{base_slug}-{num}'
        num += 1
        self.slug = unique_slug
    super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
# Answerkey models
    
class Answerkey(models.Model):
    title = models.CharField(max_length=400, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    keywords = models.TextField(max_length=300,blank=True, null=True)
    image = models.ImageField(upload_to='og_images/', blank=True, null=True, help_text="Open Graph image for social sharing")
    image_alt = models.CharField(max_length=255,blank=True,null=True,help_text="Alternate text for OG Image (used in og:image:alt)")
    updated_at = models.DateTimeField(auto_now=True)  # automatic on update
    post_date = models.CharField(max_length=100,blank=True, null=True)
    vacancy_info = RichTextField(blank=True, null=True)
    online_application_date= models.CharField(max_length=400,blank=True, null=True)
    online_last_date = models.CharField(max_length=100,blank=True, null=True)
    receipt_of_application = models.CharField(max_length=100,blank=True, null=True)
    last_date_fee = models.CharField(max_length=100,blank=True, null=True)
    correction_date = models.CharField(max_length=100,blank=True, null=True)
    exam_date = models.CharField(max_length=100,blank=True, null=True)
    exam_date1 = models.CharField(max_length=100,blank=True, null=True)
    exam_date2 = models.CharField(max_length=100,blank=True, null=True)
    exam_date3 = models.CharField(max_length=100,blank=True, null=True)
    admit_card_available = models.CharField(max_length=100,blank=True, null=True)
    answerkey_available_date = models.CharField(max_length=100,blank=True, null=True)
    result_available = models.CharField(max_length=100,blank=True, null=True)
    final_result_available = models.CharField(max_length=100,blank=True, null=True)
    applecation_fee= RichTextField(blank=True, null=True)
    vacancy_details = RichTextField(blank=True, null=True)
    eligibility_criteria=RichTextField(blank=True, null=True)
    selection_process= RichTextField(blank=True, null=True)
    important_information= RichTextField(blank=True, null=True)
    how_to_apply= RichTextField(blank=True, null=True)
    apply_online_link=models.URLField(blank=True, null=True)
    admitcard_link=models.URLField(blank=True, null=True)
    answerkeyI_link=models.URLField(blank=True, null=True)
    answerkeyII_link=models.URLField(blank=True, null=True)
    result_link=models.URLField(blank=True, null=True)
    resultI_link=models.URLField(blank=True, null=True)
    resultII_link=models.URLField(blank=True, null=True)
    result_final_link=models.URLField(blank=True, null=True)
    notification_link=models.URLField(blank=True, null=True)
    officialwebsite_link=models.URLField(blank=True, null=True)
    slug=models.SlugField(unique=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='public')

    def get_absolute_url(self):
        return reverse("answerkeypost", kwargs={"slug": self.slug}) 

class Meta:
        model = Answerkey
        fields = '__all__'

def save(self, *args, **kwargs):
    if not self.slug:
        base_slug = slugify(self.title)
        unique_slug = base_slug
        num = 1
        while Answerkey.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{base_slug}-{num}'
        num += 1
        self.slug = unique_slug
    super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    # Job Models
    
class Job(models.Model):
    title = models.CharField(max_length=400, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    keywords = models.TextField(max_length=300,blank=True, null=True)
    image = models.ImageField(upload_to='og_images/', blank=True, null=True, help_text="Open Graph image for social sharing")
    image_alt = models.CharField(max_length=255,blank=True,null=True,help_text="Alternate text for OG Image (used in og:image:alt)")
    updated_at = models.DateTimeField(auto_now=True)  # automatic on update
    post_date = models.CharField(max_length=100,blank=True, null=True)
    vacancy_info = RichTextField(blank=True, null=True)
    online_application_date= models.CharField(max_length=400,blank=True, null=True)
    online_last_date = models.CharField(max_length=100,blank=True, null=True)
    receipt_of_application = models.CharField(max_length=100,blank=True, null=True)
    last_date_fee = models.CharField(max_length=100,blank=True, null=True)
    correction_date = models.CharField(max_length=100,blank=True, null=True)
    exam_date = models.CharField(max_length=100,blank=True, null=True)
    exam_date1 = models.CharField(max_length=100,blank=True, null=True)
    exam_date2 = models.CharField(max_length=100,blank=True, null=True)
    exam_date3 = models.CharField(max_length=100,blank=True, null=True)
    admit_card_available = models.CharField(max_length=100,blank=True, null=True)
    answerkey_available_date = models.CharField(max_length=100,blank=True, null=True)
    result_available = models.CharField(max_length=100,blank=True, null=True)
    final_result_available = models.CharField(max_length=100,blank=True, null=True)
    applecation_fee= RichTextField(blank=True, null=True)
    vacancy_details = RichTextField(blank=True, null=True)
    eligibility_criteria=RichTextField(blank=True, null=True)
    selection_process= RichTextField(blank=True, null=True)
    important_information= RichTextField(blank=True, null=True)
    how_to_apply= RichTextField(blank=True, null=True)
    apply_online_link=models.URLField(blank=True, null=True)
    admitcard_link=models.URLField(blank=True, null=True)
    answerkeyI_link=models.URLField(blank=True, null=True)
    answerkeyII_link=models.URLField(blank=True, null=True)
    result_link=models.URLField(blank=True, null=True)
    resultI_link=models.URLField(blank=True, null=True)
    resultII_link=models.URLField(blank=True, null=True)
    result_final_link=models.URLField(blank=True, null=True)
    notification_link=models.URLField(blank=True, null=True)
    officialwebsite_link=models.URLField(blank=True, null=True)
    slug=models.SlugField(unique=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='public')

    def get_absolute_url(self):
        return reverse("jobpost", kwargs={"slug": self.slug}) 

class Meta:
        model = Job
        fields = '__all__'

def save(self, *args, **kwargs):
    if not self.slug:
        base_slug = slugify(self.title)
        unique_slug = base_slug
        num = 1
        while Job.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{base_slug}-{num}'
        num += 1
        self.slug = unique_slug
    super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Admission(models.Model):
    title = models.CharField(max_length=400, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    keywords = models.TextField(max_length=300,blank=True, null=True)
    image = models.ImageField(upload_to='og_images/', blank=True, null=True, help_text="Open Graph image for social sharing")
    image_alt = models.CharField(max_length=255,blank=True,null=True,help_text="Alternate text for OG Image (used in og:image:alt)")
    updated_at = models.DateTimeField(auto_now=True)  # automatic on update
    post_date = models.CharField(max_length=100,blank=True, null=True)
    vacancy_info = RichTextField(blank=True, null=True)
    online_application_date= models.CharField(max_length=400,blank=True, null=True)
    online_last_date = models.CharField(max_length=100,blank=True, null=True)
    receipt_of_application = models.CharField(max_length=100,blank=True, null=True)
    last_date_fee = models.CharField(max_length=100,blank=True, null=True)
    correction_date = models.CharField(max_length=100,blank=True, null=True)

    Merit_list_released = models.CharField(max_length=100, blank=True, null=True)
    Counseling = models.CharField(max_length=100, blank=True, null=True)

    exam_date = models.CharField(max_length=100,blank=True, null=True)
    exam_date1 = models.CharField(max_length=100,blank=True, null=True)
    exam_date2 = models.CharField(max_length=100,blank=True, null=True)
    exam_date3 = models.CharField(max_length=100,blank=True, null=True)
    admit_card_available = models.CharField(max_length=100,blank=True, null=True)
    answerkey_available_date = models.CharField(max_length=100,blank=True, null=True)
    result_available = models.CharField(max_length=100,blank=True, null=True)
    final_result_available = models.CharField(max_length=100,blank=True, null=True)
    applecation_fee= RichTextField(blank=True, null=True)

    admission_details = RichTextField(blank=True, null=True)

    eligibility_criteria=RichTextField(blank=True, null=True)
    selection_process= RichTextField(blank=True, null=True)
    important_information= RichTextField(blank=True, null=True)
    how_to_apply= RichTextField(blank=True, null=True)
    apply_online_link=models.URLField(blank=True, null=True)
    admitcard_link=models.URLField(blank=True, null=True)
    answerkeyI_link=models.URLField(blank=True, null=True)
    answerkeyII_link=models.URLField(blank=True, null=True)
    download_course_list_link=models.URLField(blank=True, null=True)
    result_link=models.URLField(blank=True, null=True)
    resultI_link=models.URLField(blank=True, null=True)
    resultII_link=models.URLField(blank=True, null=True)
    result_final_link=models.URLField(blank=True, null=True)
    notification_link=models.URLField(blank=True, null=True)
    officialwebsite_link=models.URLField(blank=True, null=True)
    slug=models.SlugField(unique=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='draft')

    def get_absolute_url(self):
        return reverse("admissionpost", kwargs={"slug": self.slug}) 

class Meta:
        model = Admission
        fields = '__all__'

def save(self, *args, **kwargs):
    if not self.slug:
        base_slug = slugify(self.title)
        unique_slug = base_slug
        num = 1
        while Admission.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{base_slug}-{num}'
        num += 1
        self.slug = unique_slug
    super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    
# Contact Models

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField(blank=True, null=True)
    content=models.TextField()
    timeStapm=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "messages from  " + self.name+ "-" + self.email
    


