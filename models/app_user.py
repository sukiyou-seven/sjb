# coding: utf-8
from models.ex_import import *


# design by seven  2022-11-24 16:06:16


class AppUser(Base, CUdr):
    __tablename__ = 'app_user'

    id = Column(INTEGER(11), primary_key=True)
    nickname = Column(String(20))
    username = Column(String(50))
    password = Column(String(64))
    expiration_time = Column(DateTime, comment='过期时间')
    device_id = Column(String(100))
    is_use = Column(TINYINT(4), server_default=text("'1'"))
    openid = Column(String(200), comment='唯一凭证')
