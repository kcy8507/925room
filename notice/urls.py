from django.urls import path
from rest_framework.routers import SimpleRouter

from notice.views import (
    index, about, contact, instagram, product,
    NoticeView, notice, notice_detail
)


router = SimpleRouter()
router.register("notice", NoticeView)
urlpatterns = router.get_urls()
urlpatterns += [
    path("", index, name="index"),
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
    path("instagram", instagram, name="instagram"),
    path("product", product, name="product"),
    path("notices", notice, name="notice"),
    path("notices/<int:id>", notice_detail, name="notice_detail"),
]