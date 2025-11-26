# Soluções Desafios IA PPCI - UTFPR

Este repositório contém os bots desenvolvidos para a Competição de IA PPCI.
Abaixo estão as instruções para executar cada desafio, visto que eles possuem requisitos de ambiente diferentes.

## Desafio 1: PONG

**Estratégia:**
Utiliza uma abordagem de Cálculo Preditivo (Geometria Analítica). O bot calcula a trajetória futura da bola baseada no vetor de velocidade e posiciona a raquete no ponto de intersecção previsto, simulando os rebatimentos nas paredes.

**Requisito Importante** (Ambiente Legado): Este desafio utiliza bibliotecas antigas (Arcade 2.x) que não funcionam em versões recentes do Python. É necessário ter o Python 3.8 instalado.

**Requisitos:**
`py -3.8 -m pip install "arcade==2.6.17" "gym==0.26.2" "numpy==1.21.0"`

**Como Executar:**
`py -3.8 pongPlayGUI.py`

##

## Desafio 2: QWOP

**Estratégia:**
Foi desenvolvida uma abordagem matemática determinística ("hardcoded") baseada em ciclos de marcha com tempos fixos. O bot utiliza um "soft start" para evitar instabilidade inicial e possui travas de segurança baseadas na altura do tronco para impedir capotagens (backflips).

**Requisitos:**

- Python 3.10+ (Versão atual/moderna)
- Bibliotecas: `pip install pyglet pymunk gym numpy`

**Como Executar:**

```bash
python qwopPlayGUI.py
```
