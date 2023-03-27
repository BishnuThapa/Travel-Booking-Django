from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Slider(models.Model):
    image = models.ImageField(upload_to='slider',
                              help_text='1920*1280 px')
    heading = models.CharField(max_length=255, null=True, blank=True)
    sub_heading = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'


class AboutUs(models.Model):
    heading = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


class WhyUs(models.Model):
    heading = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Why Us'
        verbose_name_plural = 'Why Us'


class OurStory(models.Model):
    heading = models.CharField(max_length=255)
    description = RichTextField()

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Story & Award'
        verbose_name_plural = 'Story & Awards'


class AwardImages(models.Model):
    ourstory = models.ForeignKey(OurStory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='awards', null=True, blank=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Award"
        verbose_name_plural = "Award"


class Destination(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    featured_image = models.ImageField(upload_to='destination',
                                       help_text='1920*1280 px')
    description = RichTextField()
    ordering = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Destination'
        verbose_name_plural = 'Destination'


class CompanyInfo(models.Model):
    favicon = models.ImageField(
        upload_to='images', default='', blank=True, null=True)
    logo = models.ImageField(
        upload_to='images', default='', blank=True, null=True)
    phone = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    secondary_email = models.EmailField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=100)

    short_description = models.TextField(max_length=255, blank=True, null=True)
    location_map = models.TextField(null=True, blank=True)
    video_url = models.CharField(max_length=255, null=True, blank=True)
    footer_text_copyright = models.CharField(
        max_length=100, null=True, blank=True)
    footer_copyright_url = models.URLField(
        default='', null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    meta_title = models.CharField(
        max_length=255, default='', null=True, blank=True)
    meta_keyword = models.TextField(null=True, blank=True)
    meta_description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Setting'


class Tour_Type(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    icon = models.ImageField(upload_to='tour_type')
    image = models.ImageField(upload_to='tour_type')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    description = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tour Category'
        verbose_name_plural = 'Tour Category'


# class Includes(models.Model):
#     title = models.CharField(max_length=255)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = 'Includes'
#         verbose_name_plural = 'Includes'


# class Excludes(models.Model):
#     title = models.CharField(max_length=255)

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = 'Excludes'
#         verbose_name_plural = 'Excludes'


class Tour(models.Model):
    DIFFICULTY_CHOICES = (
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('High', 'High')
    )
    PUBLISH_CHOICES = (
        ('Enable', 'Enable'),
        ('Disable', 'Disable'),
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    publish = models.CharField(
        choices=PUBLISH_CHOICES, default=1, max_length=15, null=True, blank=True)
    featured_image = models.ImageField(upload_to='tour')
    route_map = models.ImageField(upload_to='tour')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    activity = models.ForeignKey(
        Tour_Type, on_delete=models.CASCADE)
    duration = models.IntegerField(null=True, blank=True)
    difficulty = models.CharField(
        choices=DIFFICULTY_CHOICES, max_length=50, default='Low', null=True, blank=True)
    max_altitude = models.CharField(max_length=100, null=True, blank=True)
    trip_start = models.CharField(
        max_length=100, default='Kathmandu', null=True, blank=True)
    trip_end = models.CharField(
        max_length=100, default='Kathmandu', null=True, blank=True)
    group_size = models.CharField(max_length=100, null=True, blank=True)
    meals = models.TextField(null=True, blank=True)
    accomodation = models.TextField(null=True, blank=True)
    regular_price = models.IntegerField(null=True, blank=True)
    sell_price = models.IntegerField(null=True, blank=True)
    overview = RichTextField()
    includes = RichTextField(null=True, blank=True)
    excludes = RichTextField(null=True, blank=True)
    additional_information = RichTextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tour'


class Gallery(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tour/gallery', null=True, blank=True)

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"


class Itinerary(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    day = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Faq(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    question = models.CharField(max_length=255, null=True, blank=True)
    answer = models.TextField(null=True, blank=True)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    featured_image = models.ImageField(upload_to='blog')
    description = RichTextField()
    readtime = models.CharField(
        max_length=10, help_text='eg: 5 min', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'


class TeamCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team Category'
        verbose_name_plural = 'Team Category'


class Team(models.Model):
    image = models.ImageField(upload_to='team', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    category = models.ForeignKey(TeamCategory, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'


class FooterUseFulInfo(models.Model):
    companyinfo = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Useful Info'
        verbose_name_plural = 'Useful Info'


class Inquiry(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Inquiry'
        verbose_name_plural = 'Customer\'s Inquiry'


class Booking(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    trip = models.ForeignKey(Tour, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Inquiry'
        verbose_name_plural = 'Customer\'s Inquiry'
