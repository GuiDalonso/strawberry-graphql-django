from django.db import models

from django.utils.translation import gettext_lazy as _
class Fruit(models.Model):
    """
    how we currently define choices
    FRUIT_TYPE_CHOICES = [
        ("db_value", "human_readable"),
        ("CTR", "Citrical"),
        ("BER", "Berry"),
    ]

    We need to convert that to a Enumeration Type Choices
    https://docs.djangoproject.com/en/4.1/ref/models/fields/#enumeration-types
    """
    """
    query{
    fruits {
            name, 
            fruitType
        }
    }

    """
    class FRUIT_TYPE_CHOICES(models.TextChoices):
        CTR = "CTR", _("Citrical")
        BER = "BER", _("Berry")

    name = models.CharField(max_length=20)
    color = models.ForeignKey(
        "Color",
        blank=True,
        null=True,
        related_name="fruits",
        on_delete=models.CASCADE,
    )
    fruitType = models.CharField(
        max_length=255,
        choices=FRUIT_TYPE_CHOICES.choices,
        default=FRUIT_TYPE_CHOICES.BER
    )


class Color(models.Model):
    name = models.CharField(max_length=20)
