from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):

    CAR_TYPE_CHOICES = [
        ("SEDAN", 'Sedan'),
        ("SUV", 'SUV'),
        ("WAGON", 'Wagon'),
        ("COUPE", 'Coupe'),
        ("HATCHBACK", 'Hatchback'),
        ("CONVERTIBLE", 'Convertible'),
        ("TRUCK", 'Truck'),
    ]
    # Many-to-One relationship to CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    car_type = models.CharField(max_length = 20, choices = CAR_TYPE_CHOICES, default = "SEDAN")
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
