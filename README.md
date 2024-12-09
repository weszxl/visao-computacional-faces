# Sistema de Identificação Facial de Funcionários

Sistema de reconhecimento facial desenvolvido por Lucas e Wesley, projetado para identificação e controle de acesso de funcionários em ambientes corporativos. Utilizando tecnologia avançada de visão computacional com OpenCV e face_recognition.


## Desenvolvedores
- Lucas Ribeiro Gades
- Wesley Stark

## Como Funciona

O sistema é dividido em vários módulos que trabalham em conjunto:

1. **Captura de Rosto** (`capting.py`):
   - Captura imagens do rosto através da webcam
   - Cria uma pasta para cada usuário
   - Salva até 50 frames do rosto

2. **Treinamento** (`train_model.py`):
   - Processa as imagens capturadas
   - Cria o modelo de reconhecimento
   - Salva os dados no arquivo `recognition_model.pkl`
   
3. **Reconhecimento Facial** (`face_recognition.py`):
   - Identifica rostos em tempo real
   - Mostra nomes das pessoas reconhecidas
   - Desenha caixas verdes ao redor dos rostos

4. **Validação do Modelo** (`validate_models.py`)
   - Verifica a integridade do arquivo `recognition_model.pkl` para garantir que o modelo está carregado corretamente.
   - Caso o arquivo esteja corrompido ou vazio, uma mensagem de erro será exibida.

5. **Verificação de Câmeras** (`verifica_camera.py`)
   - Detecta as câmeras disponíveis no sistema.
   - Permite testar as conexões com a webcam para garantir que a câmera está funcionando antes de iniciar a captura ou o reconhecimento facial.

6. **Teste de Exibição de Imagem** (`open_cv.py`)
   - Testa a funcionalidade do OpenCV ao exibir uma janela simples com uma imagem gerada dinamicamente.
   - Exibe um ícone de rosto ('-') usando o OpenCV, útil para verificar se a instalação do OpenCV está funcionando corretamente.


## Requisitos de Instalação

1. Primeiro, crie um ambiente virtual:
   ```bash
   python -m venv env-visao
   ```

2. Ative o ambiente virtual:
   - Windows:
     ```bash
     .\env-visao\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source ./env-visao/bin/activate
     ```

3. Instalação de Dependências 
Certifique-se de que seu ambiente virtual esteja ativado. Instale as dependências listadas no arquivo requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

4. Conteúdo do arquivo requirements.txt:
   ```bash
    opencv-python
    face-recognition
    install numpy
   ```

## Como Usar

1. **Capturar Frames**:
   ```bash
   python capting.py
   ```
   - Digite seu nome quando solicitado
   - Olhe para a câmera
   - Caso precise, pressione 'Q' para parar

2. **Treinar o Modelo**:
   ```bash
   python training.py
   ```
   - Isso criará o arquivo `models/recognition_model.pkl`
   - Aguarde o processo terminar

3. **Usar o Reconhecimento**:
   ```bash
   python face_recognition.py
   ```
   - A webcam será ativada
   - Caso precise, pressione 'Q' para encerrar

## Estrutura de Pastas
```bash
visao-computacional-faces-master/
├── env-visao/                   # Ambiente virtual para o projeto
├── models/                      # Modelos treinados
│   └── recognition_model.pkl    # Modelo de reconhecimento treinado para identificar faces
├── scripts/ 
│   ├── capturing.py             # Script para capturar imagens das câmeras
│   ├── face_recognition.py      # Script para realizar o reconhecimento facial usando o modelo treinado
│   └── train_model.py           # Script para treinar o modelo de reconhecimento facial
├── utils/
│   ├── test_opencv.py           # Script para testar a instalação do OpenCV
│   ├── validate_models.py       # Script para validar a precisão dos modelos treinados
│   └── verifica_cameras.py      # Script para verificar a disponibilidade e funcionamento das câmeras
├── README.md                    # Arquivo de documentação do projeto
├── requirements.txt             # Lista de dependências necessárias para o projeto
└── .gitignore                   # Arquivo para especificar quais arquivos/diretórios devem ser ignorados pelo Git
```

## Dicas Importantes

- Use boa iluminação
- Mantenha o rosto centralizado
- Capture pelo menos 50 fotos
- Verifique se a webcam está funcionando
- O arquivo `recognition_model.pkl` é criado automaticamente na pasta `models/`

## Solução de Problemas

1. Se a webcam não abrir:
   - Verifique as permissões da webcam
   - Confira se a câmera está conectada
   - Altere a linha 'capture = cv2.VideoCapture(0)' para '0' ou '1'

2. Se os rostos não forem detectados:
   - Melhore a iluminação
   - Ajuste a posição do rosto
   - Verifique se o ambiente virtual está ativo

3. Se o modelo não for criado:
   - Certifique-se de que existem fotos na pasta `data/`
   - Verifique se a pasta `models/` existe
   - Execute o treinamento novamente