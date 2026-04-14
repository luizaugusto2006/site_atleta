from django.db import models

class Atleta(models.Model):
    # Opções para o campo de posição
    POSICOES = [
        ("ATA", "Atacante"),
        ("MEI", "Meio-Campo"),
        ("VOL", "Volante"),
        ("LAT", "Lateral"),
        ("ZAG", "Zagueiro"),
        ("GOL", "Goleiro"),
    ]

    nome_artistico = models.CharField("Nome de Jogo", max_length=50)
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
    
    # Habilidades
    visao_jogo = models.IntegerField("Visão de Jogo (0-100)", default=80)
    precisao_passe = models.IntegerField("Precisão de Passe (0-100)", default=80)
    controle_bola = models.IntegerField("Controle de Bola (0-100)", default=80)

    def __str__(self):
        return self.nome_artistico

# A classe Foto agora está fora de Atleta (sem espaços no começo da linha)
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
        ordering = ['-ano_inicio'] # Mostra o mais recente primeiro

    def __str__(self):
        return f"{self.nome_clube} ({self.ano_inicio})"