# Euro Truck Simulator 2 1-Click

No meu caso, que possuo dois monitores, sendo um dedicado a jogos que precisam apenas do mouse e teclado e o outro para jogos de simuladores que usam o volante, o Euro Truck Simulator 2 não possui a opção de escolher em qual monitor será executado. Isso exige que eu entre nas configurações de exibição do Windows e marque a opção “Tornar este meu vídeo principal”.

Além disso, uso aplicativos complementares como FanaLEDs, que controla as luzes do volante, e SIM Dashboard, que exibe informações adicionais do jogo. Diante de tantos detalhes, criei um script para realizar todas essas configurações com apenas um clique e, claro, finalizar todos os aplicativos abertos e voltar ao monitor principal quando encerrar o jogo.

Inicialmente, criei um script em PowerShell que funcionou muito bem, apesar de alguns pequenos problemas que foram rapidamente resolvidos. No entanto, em Python, tive uma experiência mais segura, sem riscos de bugs aleatórios.

# Como usar

### Requisitos
- Python 3.6 ou superior - [Download](https://www.python.org/downloads/)
- MultiMonitorTool - [Download](https://www.nirsoft.net/utils/multi_monitor_tool.html)
- FanaLEDs - [Download](https://fanaleds.com/downloads)
- SIM Dashboard - [Download](https://www.stryder-it.de/simdashboard/index.php#install)

### Os pacotes já estão instalados no .venv
```
pip install psutil
pip install colorama
```

### Informe os caminhos para os paths
```
multimonitortool_path = "C:\\Programas\\MultiMonitorTool\\MultiMonitorTool.exe"
fanaleds_path = "C:\\Programas\\FanaLEDs\\FanaLEDs.exe"
simdashboard_path = "C:\\Programas\\SIM Dashboard Server\\SIMDashboardServer.exe"
```

### Você pode nomear seus monitores
```
monitor_name = "LG UltraWide" if monitor_number == 2 else "LG UltraGear"
```

# Crie um atalho para o Euro Truck Simulator 2

### Crie o atalho:
1. Clique com o botão direito do mouse sobre "eurotrucks2.bat" e clique em "Criar atalho".
2. Renomeie o atalho para "Euro Truck Simulator 2".

### Altere o ícone:
1. Clique com o botão direito do mouse sobre o atalho criado e clique em "Propriedades".
2. Vá para a aba "Atalho" e clique em "Alterar ícone".
3. Selecione o ícone do ETS2 localizado em "Steam\steamapps\common\Euro Truck Simulator 2\bin\win_x64\eurotrucks2.exe".

### Mover o atalho:
1. Coloque o atalho onde preferir. Recomendo movê-lo para "C:\ProgramData\Microsoft\Windows\Start Menu\Programs" para facilitar o acesso na lista de aplicativos do Windows.