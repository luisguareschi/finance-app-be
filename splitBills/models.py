from django.db import models
from users.models import User
from django.core.exceptions import ValidationError

# Create your models here.

class BillGroupCurrencyChoices(models.TextChoices):
    USD = "USD"
    EUR = "EUR"

class BillGroup(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, choices=BillGroupCurrencyChoices.choices, default=BillGroupCurrencyChoices.USD)

    @property
    def number_of_members(self) -> int:
        return self.bill_group_members.count() if hasattr(self, 'bill_group_members') else 0

    class Meta:
        unique_together = ('name', 'user')

    def __str__(self):
        return f"{self.name} - {self.user}"

class BillGroupMember(models.Model):
    bill_group = models.ForeignKey(BillGroup, on_delete=models.CASCADE, related_name='bill_group_members')
    name = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('bill_group', 'name')

    def __str__(self):
        return f"{self.bill_group.name} - {self.name}"

class Bill(models.Model):
    bill_group = models.ForeignKey(BillGroup, on_delete=models.CASCADE, related_name='bills', null=True, blank=True)
    payed_by = models.ForeignKey(BillGroupMember, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    payed_for = models.ManyToManyField(BillGroupMember, related_name='bills_payed_for', blank=True)
    payed_for_everyone = models.BooleanField(
        default=False, 
        help_text="If true, the bill is payed for everyone in the bill group (including the payer)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('payed_by', 'description', 'bill_group')

    def __str__(self):
        return f"{self.payed_by.name} - {self.amount}"

    def clean(self):
        # if self.payed_for_everyone and hasattr(self, 'payed_for'):
        #     raise ValidationError("If 'payed_for_everyone' is True, 'payed_for' must be empty.")
        return True

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)