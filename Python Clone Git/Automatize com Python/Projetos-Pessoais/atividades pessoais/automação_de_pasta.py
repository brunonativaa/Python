import os           # importei módulos da Biblioteca Padrão do Python
import shutil
import time

# 1. Defina o caminho exato da sua pasta de Downloads
# Use o 'r' na frente da string para o Python ler as barras invertidas do Windows corretamente
pasta_downloads = r"C:\Users\Bruno Rodrigues\Downloads"

# 2. Defina o nome das pastas para onde os arquivos irão
pasta_pdfs = os.path.join(pasta_downloads, " PDFs")
pasta_mp4 = os.path.join(pasta_downloads, " Musicas")
pasta_imagens = os.path.join(pasta_downloads, " Imagens")
pasta_exe = os.path.join(pasta_downloads, "Programas")
pasta_xlsx = os.path.join(pasta_downloads, "Arquivos Excel")

# 3. Cria as pastas de destino, caso elas ainda não existam
os.makedirs(pasta_pdfs, exist_ok=True)
os.makedirs(pasta_mp4, exist_ok=True)
os.makedirs(pasta_imagens, exist_ok=True)
os.makedirs(pasta_exe, exist_ok=True)
os.makedirs(pasta_xlsx, exist_ok=True)

# pastas protegida para manter a integridade de arquivos já existentes
pasta_protegidas = [pasta_pdfs, pasta_mp4, pasta_imagens, pasta_exe,  pasta_xlsx ] 

print("Iniciando o Robo Faxineiro de Downloads...")
print("Precione CTRL+C no terminal para parar.")


# 4. O laço infinito que faz o programa rodar para sempre

try:

    while True:

        for pasta_atual, subpastas, arquivos in os.walk(pasta_downloads):

            if pasta_atual in pasta_protegidas:
                  continue

        # 5. Lista todos os arquivos que estão em Downloads no momento
        #arquivos = os.listdir(pasta_downloads)

            print(f"O robô olhou a pasta e encontrou: {arquivos}")

            for arquivo in arquivos: # Pega o caminho completo do arquivo atual
                caminho_arquivo = os.path.join(pasta_atual, arquivo)

                # Pula se for uma pasta, queremos apenas mover arquivos
                if os.path.isdir(caminho_arquivo):
                        continue

                    # Toma a decisão é PDF? é MP3 etc...

                if arquivo.lower().endswith(".pdf"):
                        caminho_destino = os.path.join(pasta_pdfs, arquivo)
                        shutil.move(caminho_arquivo, caminho_destino) # move o arquivo
                        print(f" ✅ ARQUIVO MOVIDO  PARA PDF: {arquivo}")
                        

                elif arquivo.lower().endswith(".mp4") or arquivo.lower().endswith(".mp3"):
                        caminho_destino = os.path.join(pasta_mp4, arquivo)
                        shutil.move(caminho_arquivo, caminho_destino) 
                        print(f" ✅ ARQUIVO MOVIDO PARA MUSICAS: {arquivo}")

                elif arquivo.lower().endswith(".png")  or arquivo.lower().endswith(".jpg"):
                        caminho_destino = os.path.join(pasta_imagens, arquivo)
                        shutil.move(caminho_arquivo, caminho_destino)
                        print(f" ✅ ARQUIVO MOVIDO PARA IMAGENS: {arquivo}")

                elif arquivo.lower().endswith(".exe"):
                        caminho_destino = os.path.join(pasta_exe, arquivo)
                        shutil.move(caminho_arquivo, caminho_destino)
                        print(f" ✅  ARQUIVO EXCUTAVEL MOVIDO: {arquivo}")



                elif arquivo.lower().endswith(".xlsx"):
                      caminho_destino = os.path.join(pasta_xlsx, arquivo)
                      shutil.move(caminho_arquivo, caminho_destino)
                      print(f" ✅ ARQUIVO EXCEL MOVIDO: {arquivo}")

                time.sleep(0.8)
        # pausa o robo por 0.8 segundo antes de mover outro arquivo


    
    # Permite que você encerre o programa de forma elegante apertando CTRL + C

except KeyboardInterrupt:
    print("\nRobô desligado") 
    print(f"✅ Missão cumprida!")  
         