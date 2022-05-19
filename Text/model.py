from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from Text.config.path import DB_ENGINE

engine = create_engine(
    DB_ENGINE, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

Base = declarative_base()


class Zi(Base):
    '''数据提取与现代汉语语料库
    '''
    __tablename__ = 'zis'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # 汉字
    name = Column(String(2), index=True, nullable=False)
    # 笔画
    bihua = Column(Integer)
    # 该汉字在语料库里所出现的次数
    jishu = Column(Integer)
    # 该汉字在语料库里所出现的频率
    pinlv = Column(Float)
    # 值1代表常用2500汉字，值1+值2代表常用3500汉字
    c3500 = Column(Integer)
    # 常用7000汉字
    t7000 = Column(Integer)
    # 该字的一个构词能力
    gouci = Column(Float)
    # 等级
    mhk = Column(String(2))

    @classmethod
    def get_by_name(cls, name: str) -> 'Zi':
        try:
            ins = session.query(cls).filter_by(name=name).one()
        except NoResultFound:
            ins = None
        return ins

    @classmethod
    def contain(cls, name: str) -> bool:
        return bool(cls.get_by_name(name))

    @classmethod
    def get_by_2500(cls, name: str) -> 'Zi':
        session = Zi.get_by_name(name)
        if session and session.c3500 == 1:
            ins = session
        else:
            ins = None
        return ins

    @classmethod
    def get_by_3500(cls, name: str) -> 'Zi':
        session = Zi.get_by_name(name)
        if session and session.c3500 and session.c3500 < 3:
            ins = session
        else:
            ins = None
        return ins

    @classmethod
    def get_by_7000(cls, name: str) -> 'Zi':
        session = Zi.get_by_name(name)
        if session and session.t7000 == 1:
            ins = session
        else:
            ins = None
        return ins


class Ci(Base):
    '''数据提取于现代汉语语料库词语分词类频率表
    '''
    __tablename__ = 'cis'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 汉字
    name = Column(String(8), index=True, nullable=False)
    # 词类标记
    cat = Column(String(length=4))
    # 出现次数
    count = Column(Integer)
    # 频率
    pinlv = Column(Float)
    # 累积频率
    acc_pinlv = Column(Float)

    @classmethod
    def get_by_name(cls, name: str, cat: str) -> 'Ci':
        '''根据name字段找到该词， 返回Ci实例，如果没有找到，返回None'''
        try:
            ins = session.query(cls).filter_by(name=name, cat=cat).one()
        except NoResultFound:
            ins = None
        return ins

    @classmethod
    def is_hard(cls, name: str, cat: str) -> 'Ci':
        '''累计频率超过75%的词汇, e.g. acc_pinlv>=0.75'''
        ci = Ci.get_by_name(name, cat)
        if ci and ci.acc_pinlv >= 75:
            ins = ci
        else:
            ins = None
        return ins


class Ci_Lv(Base):
    '''数据提取于现代汉语分类词典
    '''
    __tablename__ = 'ci_lv'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 汉字
    name = Column(String(8), index=True, nullable=False)
    # 类别
    level = Column(String(2))

    @classmethod
    def get_by_name(cls, name):
        try:
            ins = session.query(cls).filter_by(name=name).one()
        except NoResultFound:
            ins = None
        return ins
