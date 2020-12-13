Microsoft Windows [Version 10.0.18363.1198]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\farha\Documents\GitHub\Smart-G-forms>mkdir FormsEnv

C:\Users\farha\Documents\GitHub\Smart-G-forms>virtualenv FormsEnv
created virtual environment CPython3.7.6.final.0-64 in 20739ms
  creator CPython3Windows(dest=C:\Users\farha\Documents\GitHub\Smart-G-forms\FormsEnv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\farha\AppData\Local\pypa\virtualenv)
    added seed packages: pip==20.2.4, setuptools==50.3.2, wheel==0.35.1
  activators BashActivator,BatchActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

C:\Users\farha\Documents\GitHub\Smart-G-forms>FormsEnv\Scripts\activate

(FormsEnv) C:\Users\farha\Documents\GitHub\Smart-G-forms>pip install -r reqs.txt
Collecting Flask==1.1.1
  Using cached Flask-1.1.1-py2.py3-none-any.whl (94 kB)
Collecting Werkzeug>=0.15
  Using cached Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Collecting Jinja2>=2.10.1
  Using cached Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
Collecting click>=5.1
  Using cached click-7.1.2-py2.py3-none-any.whl (82 kB)
Collecting itsdangerous>=0.24
  Using cached itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting MarkupSafe>=0.23
  Using cached MarkupSafe-1.1.1-cp37-cp37m-win_amd64.whl (16 kB)
Installing collected packages: Werkzeug, MarkupSafe, Jinja2, click, itsdangerous, Flask
Successfully installed Flask-1.1.1 Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 itsdangerous-1.1.0
WARNING: You are using pip version 20.2.4; however, version 20.3.1 is available.
You should consider upgrading via the 'C:\Users\farha\Documents\GitHub\Smart-G-forms\FormsEnv\Scripts\python.exe -m pip install --upgrade pip' command.

(FormsEnv) C:\Users\farha\Documents\GitHub\Smart-G-forms>