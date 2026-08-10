from django.db import models

class Atleta(models.Model):
    POSICOES = [
        ("ATA", "Atacante"),
        ("MEI", "Meio-Campo"),
        ("VOL", "Volante"),
        ("LAT", "Lateral"),
        ("ZAG", "Zagueiro"),
        ("GOL", "Goleiro"),
    ]

    nome_artistico = models.CharField("Nome de Jogo", max_length=50)
    foto_rosto = models.ImageField(
        "Foto de Perfil (Rosto)", 
        upload_to="perfil/", 
        null=True, 
        blank=True
    )
    foto_capa = models.ImageField(
        "Foto de Capa (Hero)", 
        upload_to="capa/", 
        null=True, 
        blank=True,
        help_text="Foto de ação para o fundo do Hero (recomendado: 1920x1080)"
    )
    posicao = models.CharField("Posição", max_length=3, choices=POSICOES)
    data_nascimento = models.DateField("Data de Nascimento")
    altura = models.DecimalField("Altura (ex: 1.75)", max_digits=3, decimal_places=2)
    pe_dominante = models.CharField(
        "Pé Dominante", max_length=10, choices=[("D", "Destro"), ("C", "Canhoto")]
    )
    link_video = models.URLField("Link do Vídeo (YouTube)", blank=True, null=True)
    instagram = models.CharField("Instagram (sem @)", max_length=50, blank=True)
    whatsapp = models.CharField(
        "WhatsApp (com DDD)", max_length=20, help_text="Ex: 21970088404"
    )
    sobre_mim = models.TextField(
        "Sobre Mim", 
        blank=True, 
        default="Meio-campista ambidestro clássico com excelente leitura de jogo e capacidade de organização.",
        help_text="Texto pessoal que aparece na seção 'Sobre Mim'"
    )

    # Habilidades
    visao_jogo = models.IntegerField("Visão de Jogo (0-100)", default=80)
    precisao_passe = models.IntegerField("Precisão de Passe (0-100)", default=80)
    controle_bola = models.IntegerField("Controle de Bola (0-100)", default=80)
    velocidade = models.IntegerField("Velocidade (0-100)", default=75)
    dribles = models.IntegerField("Dribles (0-100)", default=70)
    finalizacao = models.IntegerField("Finalização (0-100)", default=65)
    defesa = models.IntegerField("Defesa (0-100)", default=60)
    fisico = models.IntegerField("Físico (0-100)", default=75)
    disputa_aerea = models.IntegerField("Disputa Aérea (0-100)", default=55)
    cavarinha = models.IntegerField("Cavarinha (0-100)", default=70)

    def __str__(self):
        return self.nome_artistico


class Estatistica(models.Model):
    TEMPORADAS = [
        ("2024", "2024"),
        ("2025", "2025"),
        ("2026", "2026"),
    ]
    
    atleta = models.ForeignKey(Atleta, related_name="estatisticas", on_delete=models.CASCADE)
    temporada = models.CharField("Temporada", max_length=4, choices=TEMPORADAS, default="2025")
    gols = models.IntegerField("Gols", default=0)
    assistencias = models.IntegerField("Assistências", default=0)
    jogos = models.IntegerField("Jogos", default=0)
    minutos = models.IntegerField("Minutos em Campo", default=0)
    cartoes_amarelos = models.IntegerField("Cartões Amarelos", default=0)
    cartoes_vermelhos = models.IntegerField("Cartões Vermelhos", default=0)

    class Meta:
        verbose_name = "Estatística"
        verbose_name_plural = "Estatísticas"
        ordering = ['-temporada']

    def __str__(self):
        return f"{self.atleta.nome_artistico} - {self.temporada}"


class Foto(models.Model):
    atleta = models.ForeignKey(Atleta, related_name="fotos", on_delete=models.CASCADE)
    imagem = models.ImageField("Foto de Ação", upload_to="galeria/")
    legenda = models.CharField("Legenda (ex: Jogo na Barra)", max_length=100, blank=True)

    def __str__(self):
        return f"Foto de {self.atleta.nome_artistico} - {self.id}"


class HistoricoClube(models.Model):
    atleta = models.ForeignKey(Atleta, related_name="clubes", on_delete=models.CASCADE)
    nome_clube = models.CharField("Nome do Clube", max_length=100)
    ano_inicio = models.IntegerField("Ano de Início")
    ano_fim = models.CharField("Ano de Fim", max_length=20, help_text="Ex: 2023 ou 'Atual'")
    conquistas = models.CharField("Principais Títulos/Destaques", max_length=255, blank=True)

    class Meta:
        verbose_name = "Histórico de Clube"
        verbose_name_plural = "Histórico de Clubes"
        ordering = ['-ano_inicio']

    def __str__(self):
        return f"{self.nome_clube} ({self.ano_inicio})"


class Depoimento(models.Model):
    atleta = models.ForeignKey(Atleta, related_name="depoimentos", on_delete=models.CASCADE)
    autor = models.CharField("Nome do Autor", max_length=100)
    cargo = models.CharField("Cargo/Função", max_length=100, blank=True, help_text="Ex: Treinador, Companheiro de Time")
    texto = models.TextField("Depoimento")
    foto = models.ImageField("Foto do Autor", upload_to="depoimentos/", null=True, blank=True)

    class Meta:
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"

    def __str__(self):
        return f"{self.autor} sobre {self.atleta.nome_artistico}"
