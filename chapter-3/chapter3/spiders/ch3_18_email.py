import scrapy
from scrapy.mail import MailSender
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

class Ch318EmailSpider(scrapy.Spider):
    name = 'ch3.18-email'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://toscrape.com/']

    def parse(self, response):
        #方式一
        # mailer = MailSender(mailfrom="luhuanyan@lspcyjjt.onexmail.com", smtphost="smtp.exmail.qq.com", smtpport=465,
        #                     smtpuser="luhuanyan@lspcyjjt.onexmail.com", smtppass="Nn2020",smtptls=True, smtpssl=True)
        print("url:",response.url)

        # 方式一
        # mailer = MailSender(mailfrom=settings['MAIL_FROM'],
        #                     smtphost=settings['MAIL_HOST'],
        #                     smtpport=settings['MAIL_PORT'],
        #                     smtpuser=settings['MAIL_USER'],
        #                     smtppass=settings['MAIL_PASS'],
        #                     smtptls=settings['MAIL_TLS'],
        #                     smtpssl=settings['MAIL_SSL'])

        # 方式一
        mailer = MailSender(mailfrom=self.settings['MAIL_FROM'],
                            smtphost=self.settings['MAIL_HOST'],
                            smtpport=self.settings['MAIL_PORT'],
                            smtpuser=self.settings['MAIL_USER'],
                            smtppass=self.settings['MAIL_PASS'],
                            smtptls=self.settings['MAIL_TLS'],
                            smtpssl=self.settings['MAIL_SSL'])

        #方式二
        # mailer = MailSender.from_settings(self.settings)
        return mailer.send(to=["luhuanyan@lspcyjjt.onexmail.com"], subject="title test", body="text test")
        print("end")