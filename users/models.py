from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    """ 커스텀 유저 모델 """

    # 초이스 상수 섹션 ---------------
    # 성별 초이스
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "남자"),
        (GENDER_FEMALE, "여자"),
        (GENDER_OTHER, "기타"),
    )
    # 언어 초이스
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "영어"), (LANGUAGE_KOREAN, "한국어"))
    # 통화 초이스
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "달러"), (CURRENCY_KRW, "원"))

    # 필드 섹션 -------------------
    avatar = models.ImageField(_("프로필 사진"), blank=True)
    gender = models.CharField(
        _("성별"), choices=GENDER_CHOICES, max_length=10, blank=True
    )
    bio = models.TextField(_("자기 소개"), blank=True)
    birthdate = models.DateField(_("생일"), blank=True, null=True)
    language = models.CharField(
        _("사용하는 언어"),
        choices=LANGUAGE_CHOICES,
        max_length=2,
        blank=True,
    )
    currency = models.CharField(
        _("통화 선택"),
        max_length=3,
        choices=CURRENCY_CHOICES,
        blank=True,
        help_text="사용하는 통화를 선택하세요",
    )
    superhost = models.BooleanField(_("슈퍼 호스트"), default=False)
