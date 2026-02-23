

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer


# ============================================================
# TODO: DirectorListCreateView
#
# GET  → დააბრუნეთ ყველა რეჟისორის სია
#        1. წამოიღეთ ყველა Director ობიექტი
#        2. გადაეცით DirectorSerializer-ს (many=True)
#        3. დააბრუნეთ Response(serializer.data)
#
# POST → შექმენით ახალი რეჟისორი
#        1. შექმენით DirectorSerializer(data=request.data)
#        2. შეამოწმეთ is_valid()
#        3. თუ ვალიდურია - save() და დააბრუნეთ 201
#        4. თუ არა - დააბრუნეთ errors და 400
# ============================================================




# ============================================================
# TODO: DirectorDetailView
#
# GET    → დააბრუნეთ კონკრეტული რეჟისორი pk-ით
#          1. გამოიყენეთ get_object_or_404(Director, pk=pk)
#          2. სერიალიზაცია და Response
#
# PUT    → განაახლეთ რეჟისორი მთლიანად
#          1. იპოვეთ ობიექტი get_object_or_404-ით
#          2. DirectorSerializer(director, data=request.data)
#          3. is_valid() → save() → Response
#
# DELETE → წაშალეთ რეჟისორი
#          1. იპოვეთ ობიექტი
#          2. object.delete()
#          3. Response(status=204)
# ============================================================




# ============================================================
# TODO: MovieListCreateView
#
# GET  → დააბრუნეთ ყველა ფილმის სია
# POST → შექმენით ახალი ფილმი
# ============================================================




# ============================================================
# TODO: MovieDetailView
#
# GET    → დააბრუნეთ კონკრეტული ფილმი pk-ით
# PUT    → განაახლეთ ფილმი მთლიანად
# PATCH  → განაახლეთ ფილმი ნაწილობრივ (partial=True)
# DELETE → წაშალეთ ფილმი
# ============================================================




# ============================================================
# TODO: ReviewListCreateView
#
# GET  → დააბრუნეთ ყველა შეფასება
# POST → შექმენით ახალი შეფასება
# ============================================================




# ============================================================
# TODO: ReviewDetailView
#
# GET    → დააბრუნეთ კონკრეტული შეფასება pk-ით
# DELETE → წაშალეთ შეფასება
# ============================================================


