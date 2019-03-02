from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager

class AdminUserManager(models.Manager) :
    def create_user(self, username, email=None, password=None, **extra_fields):
        pass


class AdminUser(models.Model) :
    """
    管理ユーザ
    """

    """
    insert into admin_user
    (
        username,
        first_name,
        last_name,
        email,
        password,
        is_staff,
        is_active,
        detail,
        date_joined
    )
    values
    (
        'user1',
        'トオヤマ',
        'ヨシタカ',
        'yoshitaka_8an9drums@icloud.com',
        '4e1243bd22c66e76c2ba9eddc1f91394e57f9f83',
        1,
        1,
        'テストユーザ',
        '2018-02-07 18:00:00'
    );
    echo test | openssl sha1 
    """
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        # validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    password = models.CharField(_('password'), max_length=150, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    detail =models.CharField(_('detail content'), max_length=300, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)



    objects = AdminUserManager()

    class Meta:
        db_table = "admin_user"
        # swappable = 'AUTH_USER_MODEL'

    # class Meta:
    #     verbose_name = _('user')
    #     verbose_name_plural = _('users')
    #
    # def get_full_name(self):
    #     """Return the first_name plus the last_name, with a space in
    #     between."""
    #     full_name = '%s %s' % (self.first_name, self.last_name)
    #     return full_name.strip()
    #
    # def get_short_name(self):
    #     """Return the short name for the user."""
    #     return self.first_name
    #
    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this user."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)
