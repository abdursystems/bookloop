from django.db import models

class Listing(models.Model):
    LISTING_TYPES = [
        ('OFFER', 'Offering (Lending/Selling)'),
        ('SEEK', 'Seeking (Borrowing/Buying)'),
    ]
    
    CONDITION_CHOICES = [
        ('NEW', 'Like New'),
        ('GOOD', 'Good'),
        ('USED', 'Fair / Heavily Used'),
    ]

    title = models.CharField(max_length=200)
    dept_code = models.CharField(max_length=20, help_text="e.g., CS")
    listing_type = models.CharField(max_length=5, choices=LISTING_TYPES, default='OFFER')
    condition = models.CharField(max_length=4, choices=CONDITION_CHOICES, default='GOOD')
    contact_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.listing_type}] {self.title} ({self.course_code})"