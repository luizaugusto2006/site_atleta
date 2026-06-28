# Deploy no PythonAnywhere

## 1. Criar conta no PythonAnywhere
- Acesse https://www.pythonanywhere.com e crie uma conta (plana Beginner gratuita)

## 2. Abrir Bash Console
- No Dashboard, clique em "Consoles" > "Start a new console" > "Bash"

## 3. Clonar o projeto do GitHub
```bash
git clone https://github.com/luizaugusto2006/site_atleta.git
cd site_atleta
```

## 4. Criar virtualenv e instalar dependências
```bash
mkvirtualenv --python=python3.10 site_atleta
pip install -r requirements.txt
```

## 5. Configurar Static Files e Migrations
```bash
python manage.py collectstatic --noinput
python manage.py migrate
```

## 6. Criar superusuário (admin)
```bash
python manage.py createsuperuser
```

## 7. Configurar Web App no PythonAnywhere
- Vá para "Web" no menu superior
- Clique em "Add a new web app"
- Escolha "Manual Configuration" > "Python 3.10"
- Em "Code":
  - **Source code:** `/home/SEU_USER/site_atleta`
  - **Working directory:** `/home/SEU_USER/site_atleta`
  - **WSGI configuration file:** clique no link para abrir

## 8. Configurar o arquivo WSGI
Substitua TODO conteúdo do arquivo WSGI por:

```python
import os
import sys

path = '/home/SEU_USER/site_atleta'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'configuracao.settings'
os.environ['SECRET_KEY'] = 'sua-chave-secreta-aqui'
os.environ['DEBUG'] = 'False'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## 9. Configurar Virtualenv no PythonAnywhere
- Na página "Web", em "Virtualenv":
  - Clique no campo e digite: `/home/SEU_USER/.virtualenvs/site_atleta`

## 10. Configurar Static Files
- Na página "Web", em "Static files":
  - **URL:** `/static/`
  - **Directory:** `/home/SEU_USER/site_atleta/staticfiles`
  - **URL:** `/media/`
  - **Directory:** `/home/SEU_USER/site_atleta/media`

## 11. Configurar ALLOWED_HOSTS
- Edite `configuracao/settings.py` e altere:
  ```python
  ALLOWED_HOSTS = ['luizatleta.pythonanywhere.com']
  ```

## 12. Recarregar o site
- Na página "Web", clique no botão verde **"Reload"**

## 13. Acessar
- https://luizatleta.pythonanywhere.com

## 14. Gerenciar conteúdo
- Admin: https://luizatleta.pythonanywhere.com/admin/
- Login: admin / senha definida no passo 6
- Lá você pode editar o atleta, adicionar fotos, clubes, etc.

---

## Container MySQL (opcional, para ter banco mais robusto)
No PythonAnywhere pago, você pode usar MySQL:
```bash
python manage.py migrate
```
