from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets, filters
from rest_framework.decorators import action
from django.db.models import F, Value, Q
from django.core.paginator import Paginator

from notice.models import Notice, Image
from notice.serializers import NoticeSerializer, NoticeDetailSerializer, ImageSerializer


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def instagram(request):
    return render(request, "instagram.html")

def product(request):
    return render(request, "product.html")


class NoticeView(
    generics.ListAPIView,
    generics.RetrieveAPIView,
    generics.CreateAPIView,
    generics.UpdateAPIView,
    viewsets.GenericViewSet,
):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    
    def method(self, *args, **kwargs):
        return super().method(*args, **kwargs)
    
    def get_serializer_class(self):
        if self.action == "retrieve":
            return NoticeDetailSerializer
        return NoticeSerializer
    
    def list(self, request, *args, **kwargs):
        self.queryset = Notice.objects.filter().order_by("-id")
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


def notice(request):
    current_page = request.GET.get("page", 1)
    notices = Notice.objects.filter().order_by("-created_at", "-id")
    # 페이지네이션
    # pagination = Paginator(notices, 8)
    # page = pagination.get_page(current_page)
    # serializer = NoticeSerializer(pagination.page(current_page), many=True)
    serializer = NoticeSerializer(notices, many=True)
    context = {
        "notices": serializer.data,
        # "total_page": pagination.num_pages,
        # "current_page": int(current_page),
        # "page": page,
    }
    return render(
        request,
        "notice.html",
        context,
    )


def notice_detail(request, id):
    notice = Notice.objects.get(id=id)
    serializer = NoticeSerializer(notice)
    return render(
        request,
        "notice__detail.html",
        {"notice": serializer.data},
    )