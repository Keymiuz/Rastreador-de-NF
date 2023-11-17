import xml.etree.ElementTree as ET
from openpyxl import Workbook
import os
import tempfile


def extrair_informacoes(xml_path):
    # Definir o mapeamento de prefixos de namespaces
    namespaces = {'cte': 'http://www.portalfiscal.inf.br/cte'}

    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Adicione essas linhas para imprimir o conteúdo do elemento raiz
    print("Conteúdo do elemento raiz:")
    print(ET.tostring(root, encoding='utf-8').decode('utf-8'))

    # Extrair informações específicas do XML com consideração aos namespaces
    numero_nota = root.find(".//cte:xNome", namespaces)
    valor = root.find(".//cte:email", namespaces)
    logradouro = root.find(".//cte:xLgr", namespaces)

    # Adicione essas linhas para imprimir os valores encontrados
    print("Número da Nota:",
          numero_nota.text if numero_nota is not None else "Não encontrado")
    print("Valor:", valor.text if valor is not None else "Não encontrado")
    print("Logradouro:", logradouro.text if logradouro is not None else "Não encontrado")

    # Verificar se os elementos foram encontrados
    numero_nota_text = numero_nota.text if numero_nota is not None else ""
    valor_text = valor.text if valor is not None else ""
    logradouro_text = logradouro.text if logradouro is not None else ""

    return numero_nota_text, valor_text, logradouro_text


def criar_planilha(extracoes, output_dir):
    # Criar um diretório temporário
    temp_dir = tempfile.mkdtemp()

    # nome da planilha (eu dei um nome aleatório, use o que vc quiser)
    output_path = os.path.join(temp_dir, "planilha.xlsx")

    # Criar a planilha Excel
    workbook = Workbook()
    sheet = workbook.active

    # Adicionar cabeçalhos
    sheet.append(["Nome", "Email", "Logradouro"])

    # Adicionar dados extraídos a planilha
    sheet.append(extracoes)

    # Salvar a planilha
    workbook.save(output_path)

    # Imprimir o caminho para a planilha
    print(f"Planilha salva em: {output_path}")


if __name__ == "__main__":
    # Caminho para o arquivo XML (use o do seu diretório)
    xml_path = r"35231109296295000240570030090307961783251005-cte-proc.xml"

    # Extrair informações do XML
    extracoes = extrair_informacoes(xml_path)

    # Criar planilha Excel com os dados extraídos em um diretório temporário (usei pq o meu n estava dando retorno direto)
    criar_planilha(extracoes, tempfile.gettempdir())
