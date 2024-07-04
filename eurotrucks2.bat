@echo off
setlocal
call "%~dp0\.venv\Scripts\activate"
python "%~dp0script.py"
deactivate
endlocal
::
:: Esse arquivo batch será responsável por executar o script.py. Dessa forma, é possível criar um atalho chamado "Euro Truck Simulator 2", substituindo o atalho padrão do jogo.
::
:: Passos:
::
:: 1. Criar Atalho:
::    - Clique com o botão direito do mouse sobre "eurotrucks2.bat" e clique em "Criar atalho".
::    - Renomeie o atalho para "Euro Truck Simulator 2".
::
:: 2. Alterar Ícone:
::    - Clique com o botão direito do mouse sobre o atalho criado e clique em "Propriedades".
::    - Vá para a aba "Atalho" e clique em "Alterar ícone".
::    - Selecione o ícone do ETS2 localizado em "Steam\steamapps\common\Euro Truck Simulator 2\bin\win_x64\eurotrucks2.exe".
::
:: 3. Mover Atalho:
::    - Coloque o atalho onde preferir. Recomendo movê-lo para "C:\ProgramData\Microsoft\Windows\Start Menu\Programs" para facilitar o acesso na lista de aplicativos do Windows.