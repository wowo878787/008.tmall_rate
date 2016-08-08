# coding:utf-8
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_RATE_PER_PAGE=2

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


config = {
    'default': DevelopmentConfig
}


class colors:
    good_colors = [u'颜色分类:银河系',
                   u'颜色分类:白羊座', u'颜色分类:金牛座',
                   u'颜色分类:双子座', u'颜色分类:巨蟹座',
                   u'颜色分类:狮子座', u'颜色分类:处女座',
                   u'颜色分类:天秤座', u'颜色分类:天蝎座',
                   u'颜色分类:射手座', u'颜色分类:摩羯座',
                   u'颜色分类:水瓶座', u'颜色分类:双鱼座']
