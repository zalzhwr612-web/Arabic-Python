name: Build Android APK

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install Dependencies
      run: |
        sudo apt update
        sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev libffi-dev libssl-dev
        pip install --upgrade pip
        pip install buildozer kivy

    - name: Prepare Main Entry and Buildozer Spec
      run: |
        # إنشاء ملف main.py ليشغل الكود العربي تلقائياً
        cat << 'EOF' > main.py
        import arabic_python
        if __name__ == "__main__":
            try:
                arabic_python.تشغيل_كود_عربي("app.عرب")
            except Exception as e:
                print("Error:", e)
        EOF

        # إنشاء وتحديث ملف buildozer.spec
        buildozer init
        sed -i 's/title = My Application/title = تطبيق عربي/g' buildozer.spec
        sed -i 's/package.name = myapp/package.name = arabicapp/g' buildozer.spec
        sed -i 's/requirements = python3,kivy/requirements = python3,kivy/g' buildozer.spec

    - name: Accept Android SDK Licenses & Build APK
      run: |
        # قبول كافة تراخيص Android SDK تلقائياً
        yes | buildozer -v android debug

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v4
      with:
        name: Arabic-Python-App
        path: bin/*.apk

