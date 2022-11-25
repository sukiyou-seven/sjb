# coding: utf-8
from models.ex_import import *

# design by seven  2022-11-25 09:42:18


class WebInfo(Base,CUdr):
    __tablename__ = 'web_info'
    __table_args__ = {'comment': '世界杯生成网页'}

    time = Column(String(20))
    battery = Column(INTEGER(11), server_default=text("'46'"))
    info1 = Column(String(40))
    info2 = Column(String(20))
    info3 = Column(String(60))
    info4 = Column(String(20))
    is_use = Column(TINYINT(4), server_default=text("'0'"))
    id = Column(INTEGER(11), primary_key=True)
