# ⚽ Site Institucional de Atleta de Futebol

Site profissional para divulgação de atleta de futebol: perfil com posição, dados técnicos, **gráficos de habilidades**, galeria de fotos de ação, histórico de clubes e vídeo de destaques.

> 🌐 **Online:** [luizinho.pythonanywhere.com](https://luizinho.pythonanywhere.com)

---

## ✨ Funcionalidades

### 👤 Perfil do Atleta
- Nome de jogo, posição, data de nascimento, altura e pé dominante.
- **Atributos técnicos** (0-100): visão de jogo, precisão de passe, controle de bola, etc.
- Vídeo de destaques (YouTube) e links para **Instagram** e **WhatsApp**.

### 📸 Galeria de Fotos
- Fotos de ação com legendas personalizadas.
- Gerenciamento completo pelo painel administrativo.

### 🏆 Histórico de Clubes
- Linha do tempo com clubes, período e principais conquistas.

### 🔒 Painel Administrativo
- Autenticação de administrador.
- Edição de perfil, upload de fotos e gerenciamento do histórico.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| **Python** | Linguagem principal |
| **Django** | Framework web, ORM, autenticação e admin |
| **SQLite** | Banco de dados |
| **Bootstrap** | Interface responsiva |
| **PythonAnywhere** | Hospedagem em produção |

---

## 🚀 Como rodar localmente

```bash
# 1. Clonar
git clone https://github.com/luizaugusto2006/site_atleta.git
cd site_atleta

# 2. Ambiente virtual
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/macOS

# 3. Dependências
pip install -r requirements.txt

# 4. Migrar e criar superusuário
python manage.py migrate
python manage.py createsuperuser

# 5. Rodar
python manage.py runserver
```

Acesse `http://127.0.0.1:8000`.

O arquivo [`DEPLOY_PYTHONANYWHERE.md`](DEPLOY_PYTHONANYWHERE.md) contém o passo a passo completo de deploy no PythonAnywhere.

---

## 📄 Licença

Este projeto é de uso pessoal e está licenciado sob a [MIT License](LICENSE).
