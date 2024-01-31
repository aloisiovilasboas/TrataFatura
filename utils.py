import re
import xml.etree.ElementTree as et
import os
import pandas as pd




def converterPastaOFXemXML(caminhoPasta):
    arquivos = [caminhoPasta+'/'+arquivo for arquivo in os.listdir(caminhoPasta) if arquivo.endswith('.ofx') ]
    for arquivo in arquivos:
        conteudo = ler_arquivo(arquivo)
        arquivoxml = re.sub('ofx$', 'xml', arquivo)
        conteudo = apagar_primeiras_linhas(conteudo)
        escrever_em_arquivo(conteudo, arquivoxml)
     
        


    return arquivos

def apagar_primeiras_linhas(texto, num_linhas=10):
    linhas = texto.split('\n')
    novo_texto = '\n'.join(linhas[num_linhas:])
    return novo_texto

def limparString(texto):
    #remove cabeçalho da string até a primeira tag <OFX>
    texto = re.sub('^.*?<OFX>', '<OFX>', texto, flags=re.DOTALL)
    return texto

def leTransacoes(xmlroot):
    transacoes = []
    for child in xmlroot:
        if child.tag == "STMTTRN":
            transacao={}
            for tagtransacao in child:
                if tagtransacao.tag=="DTPOSTED":
                    data_string = tagtransacao.text
                    # seleciono apenas os 8 primeiros caracteres da string que contém à data
                    data_string = data_string[:8]
                    date = pd.to_datetime(data_string, format='%Y%m%d')
                    transacao.update({'Data Convertida': date.strftime('%d/%m/%Y')}) 
                else:
                    if tagtransacao.tag=="TRNAMT":
                        transacao.update({'Valor Convertido': pd.to_numeric(tagtransacao.text)})
                transacao.update({tagtransacao.tag: tagtransacao.text})
            transacoes.append(transacao)
    return transacoes

    


def ler_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='ISO-8859-14') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        print(f"O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo '{caminho_arquivo}': {e}")
        return None


def escrever_em_arquivo(texto, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto)


def transform_xml(xmlroot):
    transacoes = []
    for child in xmlroot:
        if child.tag == "STMTTRN":
            transacao={}
            for tagtransacao in child:
                if tagtransacao.tag=="DTPOSTED":
                    data_string = tagtransacao.text[:-14]
                    print(tagtransacao.text)
                    date = data_string
                    transacao.update({'DataConvertida': date})
                    # date = pd.to_datetime(data_string, format='%Y%m%d')
                    # transacao.update({'DataConvertidadt': date}) 
                    # transacao.update({'DataConvertida': date.strftime('%d/%m/%Y')}) 
                else:
                    if tagtransacao.tag=="TRNAMT":
                        transacao.update({'ValorConvertido': pd.to_numeric(tagtransacao.text)})
                transacao.update({tagtransacao.tag: tagtransacao.text})
            transacoes.append(transacao)
    
    return transacoes

def lerTodosXMLemPasta(caminhoPasta):
    arquivos = [caminhoPasta+'/'+arquivo for arquivo in os.listdir(caminhoPasta) if arquivo.endswith('.xml') ]
    todasAstransacoes =[]
    for arquivo in arquivos:
        etree = et.parse(arquivo)
        eroot = etree.getroot()
        transactions = eroot[1][0][2][2]
        transacoes = transform_xml(transactions)
        todasAstransacoes = todasAstransacoes+transacoes
    return todasAstransacoes