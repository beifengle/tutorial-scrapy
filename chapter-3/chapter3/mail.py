# -*- coding: utf-8 -*-
import smtplib
import logging
import os
import time
import datetime
import traceback
from typing import Dict
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from chapter3 import settings


log = logging.getLogger()

def send_mail(subject, content, mail_format="html", mail_charset="utf-8", attachs=None, default_receivers="mail_to"):

    log.info('[mail-subject] %s',subject)
    """
        发送邮件
        参数:
            receiver:接收人邮箱列表,
            subject:邮件主题,
            content:邮件主题,
            mail_format:邮件格式,取值有plain和html,
            mail_charset:邮件字符集,
            attachs:附件路径列表
    """
    try:
        mail_host = settings.MAIL_HOST
        mail_port = settings.MAIL_PORT
        mail_pass = settings.MAIL_PASS
        mail_from = settings.MAIL_FROM
        if default_receivers:
            receivers = settings.MAILL_TO
        else:
            receivers = settings.MAILL_TO
        if not settings.MAILL_TO:
            print("[Note] 没有添加收件人！！！")
            return False
    except:
        print(traceback.format_exc())
        #
        return False

    me = "爬虫监控" + "<" + mail_from + ">"

    # 转换正文类型为规范类型
    if mail_format == "text":
        mail_format = "plain"

    # 处理邮件正文格式
    if mail_format == "plain":
        # print content
        pass
    elif mail_format == "html":
        # content = "<html><body>%s</body></html>" % content
        content = content.replace("\n","<p>")
    else:
        log.info('邮件格式输入错误: %s, 应该为text或html',mail_format)
        return 1
    msg = MIMEText(content, mail_format, mail_charset)
    msg["Subject"] = Header(subject, mail_charset)
    msg["From"] = Header(me, mail_charset)
    if isinstance(receivers, (list, tuple)):
        msg["To"] = Header(', '.join(receivers))
    else:
        msg["To"] = Header(receivers, mail_charset)

    # 处理附件
    if attachs:
        msg = attachment(msg, attachs)
    try:
        if 'easub.tech' in mail_from:
            server = smtplib.SMTP_SSL(mail_host, mail_port)
            server.login(mail_from, mail_pass)
            server.sendmail(me, receivers, msg.as_string())
            server.quit()
        else:
            smtp = smtplib.SMTP()
            smtp.connect(mail_host)
            smtp.login(mail_from, mail_pass)
            smtp.sendmail(me, receivers, msg.as_string())
            smtp.quit()
        print('[From]{%s} [To]%s [result]Email send succeed!' %(mail_from,receivers))
        return True
    except:
        print('[From]%s [To]%s  [result]Email send falied!' %(mail_from,receivers))
        print(traceback.format_exc())
        # 前面发送失败，这里在反馈
        return False


def attachment(self, msg, attachs):
    """处理附件,将附件添加到邮件中"""
    msg_part = MIMEMultipart()
    msg_part["From"] = msg["From"]
    msg_part["To"] = msg["To"]
    msg_part["Subject"] = msg["Subject"]
    # print msg.get_payload(decode=True)
    msg_part.attach(msg)
    if isinstance(attachs, (list, tuple)):
        for attach in attachs:
            msg_part = self.add_attach(msg_part, attach)
    else:
        msg_part = self.add_attach(msg_part, attachs)
    return msg_part


def add_attach(self, attobj, filename):
    """将单个文件添加到附件对象中"""
    if os.exists(filename):
        attachname = filename.split('/')[-1]
        if len(filename) == 0:
            attachname = filename.split('\\')[-1]
    else:
        raise IOError("文件不存: %s" % filename)
    attach = MIMEText(open(filename, "rb").read(), "base64", "utf-8")
    attach["Content-Type"] = "application/octet-stream"
    attach["Content-Disposition"] = "attachment; filename='%s'" % attachname
    attobj.attach(attach)
    return attobj


def build_html_except_email(templ_file, email_data: Dict) -> str:
    cwd = os.path.dirname(os.path.abspath(__file__))
    config_filepath = cwd  + os.sep + templ_file
    with open(config_filepath, 'r',encoding="utf-8") as f:
        html = f.read()
        return html.format(
            exceptionNo = email_data.get("exceptionNo",""),
            exceptionOccurDate = email_data.get("exceptionOccurDate",""),
            exceptionType = email_data.get("exceptionType",""),
            exceptionSpider = email_data.get("exceptionSpider",""),
            exceptionHost = email_data.get("exceptionHost",""),
            exceptionEnv = email_data.get("exceptionEnv",""),
            exceptionPlayer = email_data.get("exceptionPlayer",""),
            exceptionProcess = email_data.get("exceptionProcess",""),
            exceptionEvent = email_data.get("exceptionEvent",""),
            exceptionDetail = email_data.get("exceptionDetail",""),
            exceptionSourceUrl = email_data.get("exceptionSourceUrl",""),
        )
if __name__ == '__main__':
    email_data = {
        "exceptionNo": "s{}".format(int(time.time() * 1000)),
        "exceptionOccurDate": "{}".format(datetime.datetime.now().strftime("%F %T")),
        "exceptionType": "download",
        "exceptionSpider": "{}".format("spider.name"),
        "exceptionHost": "{}[{}]".format("spider-a", "127.0.0.1"),
        "exceptionEnv": "{}".format("dev"),
        "exceptionPlayer": "{}".format("test"),
        "exceptionProcess": "{}".format(1111),
        "exceptionEvent": "{}".format("exception"),
        "exceptionDetail": "{}".format("traceback.format_exc()"),
        "exceptionSourceUrl": "{}".format("url")
    }
    # 发送异常邮件
    send_mail("爬虫出现异常啦!", build_html_except_email("email_exception.html", email_data))