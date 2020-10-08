import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "projeto/index.html", {
        "newyear": now.month == 1 and now.day == 1
        
    })

def metodologia(request):
    return render(request, "projeto/metodologia.html")
    
def arquitetura(request):
    return render(request, "projeto/arquitetura.html")

def descricao(request):
    return render(request, "projeto/descricao.html")

def descricao2(request):
    return render(request, "projeto/descricao2.html")

def comentarios(request):
    return render(request, "projeto/comentarios.html")

def descricaov2(request):
    return render(request, "projeto/descricaov2.html")

texts = ["A interação do usuário com a página se dá por meio do acesso às informações financeiras a respeito da bolsa de valores do Brasil. Através de um menu bastante sugestivo, é possível consultar informações de inúmeras empresas por ordem alfabética, com opções para gráficos, notícias, análise técnica, entre outras coisas. A página também oferece um sistema de cadastro gratuito para que o usuário tenha acesso a conteúdos exclusivos como negócios em tempo real e a possibilidade de salvar informações das empresas de sua preferência. A navegabilidade dá ao usuário o poder de explorar o website de forma intuitiva, entretanto, seu visual é bastante ultrapassado.",                             
        "A facilidade de uso, ou seja, a usabilidade é um elemento essencial para um website. Ela consiste em tornar um website mais fácil para o usuário, tornando possível uma navegação intuitiva e com mais exatidão. O site ADVFN é simples no que diz respeito  facilidade de uso. Os botões dispostos ao longo do site, embora não sejam preliminarmente atrativos, facilitam significativamente que seu usuário encontre o que necessita. Pode-se dizer que a interação com o usuário é seguramente falha, isso se deve principalmente ao fato de que os botões disponibilizados pelo site são nitidamente apagados (mal parecem botões).",
        "O principal serviço do site consiste em mostrar informações sobre o Bovespa, as ações e seus preços, além de gráficos correspondendo ao status atual do Bovespa no dia em que for acessado e  todo seu histórico. É possível pesquisar sobre as ações mais detalhadamente e encontrar muitas informações sobre o histórico de preços e o preço atual, porcentagem de quanto subiu ou caiu, gráfico, notícias da ação e entre outros.",
        "O principal benefício do ADVFN pode ser usufruido por investidores assíduos, visto que esses podem acompanhar o histórico de preços e o preço atual, entre outras informações sobre as ações.",
        "A área ou nicho, nada mais é que a área de atuação na qual o website possui seu público específico. No caso da página em questão, seu nicho consiste basicamente em investimento e financeiro."]

def section(request, num):
    if 1 <= num <= 5:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")

def dadosgerais(request):
    return render(request, "projeto/dadosgerais.html")

def videos(request):
    return render(request, "projeto/videos.html")