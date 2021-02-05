from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Model을 Amdin 패널에서 직접 보기 위한 절차
# Model을 등록(register)하고
# class로 Model을 조정할 수 있어
# 장고가 register된 Model과 class를 찾은 다음 특정 키워드를 찾을거야
# 예를들면 fieldset 등이 있어.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ 커스텀 유저 어드민 """

    fieldsets = UserAdmin.fieldsets + (
        (
            "추가 정보",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
