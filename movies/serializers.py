"""
📌 დავალება 1 – ModelSerializer-ები

შექმენით ModelSerializer კლასები Director, Movie და Review მოდელებისთვის.
თითოეულ სერიალაიზერს უნდა ჰქონდეს Meta კლასი, სადაც განსაზღვრულია:
    - model: მოდელის კლასი
    - fields: ველების სია ან '__all__'

💡 მინიშნება:
    from rest_framework import serializers

    class ExampleSerializer(serializers.ModelSerializer):
        class Meta:
            model = ...
            fields = ...
"""

from rest_framework import serializers
from .models import Director, Movie, Review


# ============================================================
# TODO: შექმენით DirectorSerializer
# მოდელი: Director
# ველები: ყველა ველი ('__all__')
# ============================================================




# ============================================================
# TODO: შექმენით MovieSerializer
# მოდელი: Movie
# ველები: ყველა ველი ('__all__')
# ============================================================




# ============================================================
# TODO: შექმენით ReviewSerializer
# მოდელი: Review
# ველები: ყველა ველი ('__all__')
# ============================================================


