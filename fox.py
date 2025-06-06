import os

print("✅ بدأ تشغيل سكريبت ngrok الخاص بفوكس...")

# 1️⃣ أمر التثبيت الكامل
os.system('curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
  && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list \
  && sudo apt update \
  && sudo apt install ngrok')

# 2️⃣ أمر إضافة التوكن
os.system('ngrok config add-authtoken 2xuAIS8zlgXDXfYLIOSo5VUXrwf_7CZ6LVvxrpRY2fJ68RW5q')

# 3️⃣ أمر تشغيل النفق
os.system('ngrok http http://localhost:3001')
