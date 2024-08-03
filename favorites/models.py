"""
Models for the favorites application.

This module defines the models for storing users' favorite products and
creators.
Each favorite is associated with a user and can be marked as a favorite item.
"""

from django.db import models
from django.contrib.auth.models import User
from products.models import Product, Creator


class FavoriteProduct(models.Model):
    """
    Model representing a user's favorite product.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorite_products'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')


class FavoriteCreator(models.Model):
    """
    Model representing a user's favorite creator.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorite_creators'
    )
    creator = models.ForeignKey(
        Creator, on_delete=models.CASCADE
    )
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'creator')
