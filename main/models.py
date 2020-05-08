from dataclasses import dataclass
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from .constants import TABLE_SHAPES

# Temporary functionality for Hall
@dataclass
class Hall:
    width: float
    height: float

    @property
    def square(self):
        return self.width * self.height


HALL = Hall(width=10, height=10)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Table(models.Model):
    number = models.PositiveIntegerField(
        unique=True,
        validators=[MinValueValidator(1)],
        help_text='Table number. Ensure this value is greater than or equal to 1.'
    )
    seats = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text='Seats quantity. Ensure this value is greater than or equal to 1.'
    )
    shape = models.CharField(max_length=50, choices=TABLE_SHAPES)
    coordinate_x = models.DecimalField(max_digits=4, decimal_places=2)
    coordinate_y = models.DecimalField(max_digits=4, decimal_places=2)
    width = models.DecimalField(
        max_digits=4, decimal_places=2,
        help_text='size data in meters'
    )  # TODO: width
    height = models.DecimalField(
        max_digits=4, decimal_places=2,
        help_text='size data in meters'
    )

    @property
    def square(self) -> Decimal:
        return self.width * self.height

    @property
    def top_left(self) -> Decimal:
        return self.coordinate_y + self.height

    @property
    def bottom_right(self) -> Decimal:
        return self.coordinate_x + self.width

    def is_size_acceptable(self) -> bool:
        return self.bottom_right <= HALL.width and self. top_left <= HALL.height

    def is_table_overlap(self):
        tables = self.__class__.objects.all()
        this_top_left = Point(self.coordinate_x, self.top_left)
        this_bottom_right = Point(self.bottom_right, self.coordinate_y)
        is_overlap = False
        _table = None
        for table in tables:
            other_top_left = Point(table.coordinate_x, table.top_left)
            other_bottom_right = Point(table.bottom_right, table.coordinate_y)
            if this_top_left.x > other_bottom_right.x or other_top_left.x > this_bottom_right.x \
                    or this_top_left.y < other_bottom_right.y or other_top_left.y < this_bottom_right.y:
                continue
            else:
                is_overlap = True
                _table = table
        return is_overlap, _table

    def clean(self):
        if not self.is_size_acceptable():
            raise ValidationError('Table size is higher than hall size')
        # check if tables overlap
        status, table = self.is_table_overlap()
        if status:
            raise ValidationError(
                f'Incorrect table size and coordinates. This table overlaps with table number {table.number}'
            )

    def __str__(self):
        return f'Table {self.number}, seats {self.seats}'


class TableOrder(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, help_text='Table number')
    created_at = models.DateField(auto_now=True, help_text='Order created at')
    order_date = models.DateField(help_text='Order on')
    additional_info = models.TextField(blank=True, help_text='Additional information')
    # TODO: better to use user saved in BD
    order_by_name = models.CharField(max_length=100, help_text='Guest name')
    order_by_email = models.EmailField(help_text='Guest email')

    class Meta:
        unique_together = ('table', 'order_date')

    def __str__(self):
        return f'Order #{self.id}'
