import xml.etree.ElementTree as ET
import openpyxl


def extrair_dados_xml(caminho_xml):
    tree = ET.parse(caminho_xml)
    root = tree.getroot()

    dados_notas = []

    for nota in root.findall('.//sua_tag_nota'):
        numero_nota = nota.find('numero').text
        valor = nota.find('valor').text
        data = nota.find('data').text

        dados_notas.append([numero_nota, valor, data])

    return dados_notas


def organizar_notas_em_excel(dados_notas, caminho_excel):
    planilha = openpyxl.Workbook()
    planilha_ativa = planilha.active

    # Aqui vocÊ adiciona o que quer ler da nota fiscal, podendo ter quantos valores quiser
    planilha_ativa.append(['Número da Nota Fiscal', 'Valor', 'Data'])

    # Adicionar dados das notas
    for nota in dados_notas:
        planilha_ativa.append(nota)

    # Salvar o arquivo Excel
    planilha.save(caminho_excel)


if __name__ == "__main__":
    caminho_xml = 'caminho/do/seu/arquivo/xml.xml'

    # Extrair dados do XML
    dados_notas = extrair_dados_xml(caminho_xml)

    # Organizar notas em um arquivo Excel
    organizar_notas_em_excel(dados_notas, 'caminho/do/seu/arquivo/excel.xlsx')
