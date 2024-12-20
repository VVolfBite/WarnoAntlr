# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# import os

# # 配置邮件服务器和发件人信息
# SMTP_SERVER = 'smtp.163.com'  # 163 邮箱 SMTP 服务器地址
# SMTP_PORT = 465  # SMTP 端口（使用 SSL 时为 465）
# SENDER_EMAIL = 'liguoze163@163.com'  # 发送方 163 邮箱地址
# SENDER_PASSWORD = 'liguoze'  # 发送方邮箱的授权码（而不是登录密码）
# RECIPIENT_EMAIL = '1327256274@qq.com'  # 收件方 QQ 邮箱地址

# # 邮件主题和正文
# SUBJECT = '新分析的文件'
# BODY = '新分析的文件已经发送.'

# # 附件文件路径
# ATTACHMENT = 'global_dict.json'

# # 创建邮件消息
# msg = MIMEMultipart()
# msg['From'] = SENDER_EMAIL
# msg['To'] = RECIPIENT_EMAIL
# msg['Subject'] = SUBJECT

# # 邮件正文内容
# msg.attach(MIMEText(BODY, 'plain'))

# # 确保附件文件存在
# if os.path.isfile(ATTACHMENT):
#     # 打开附件文件
#     with open(ATTACHMENT, 'rb') as file:
#         # 创建 MIMEBase 对象
#         part = MIMEBase('application', 'octet-stream')
#         part.set_payload(file.read())
#         # 编码附件为 Base64
#         encoders.encode_base64(part)
#         # 添加文件头
#         part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(ATTACHMENT)}')
#         # 将附件添加到邮件中
#         msg.attach(part)
# else:
#     print(f"Error: {ATTACHMENT} not found!")
#     exit(1)

# # 连接到 SMTP 服务器并发送邮件
# try:
#     # 使用 SSL 安全连接
#     server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
#     server.login(SENDER_EMAIL, SENDER_PASSWORD)  # 登录到邮箱
#     text = msg.as_string()  # 将邮件对象转换为字符串
#     server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, text)  # 发送邮件
#     server.quit()  # 退出服务器
#     print(f"Email sent successfully to {RECIPIENT_EMAIL}.")

# except Exception as e:
#     print(f"An error occurred: {str(e)}")
