# Euro Truck Simulator 2 1-Click

No meu caso, que possuo dois monitores, sendo um dedicado a jogos que precisam apenas do mouse e teclado e o outro para jogos de simuladores que usam o volante, o Euro Truck Simulator 2 não possui a opção de escolher em qual monitor será executado. Isso exige que eu entre nas configurações de exibição do Windows e marque a opção “Tornar este meu vídeo principal”.

Além disso, uso aplicativos complementares como FanaLEDs, que controla as luzes do volante, e SIM Dashboard, que exibe informações adicionais do jogo. Diante de tantos detalhes, criei um script para realizar todas essas configurações com apenas um clique e, claro, finalizar todos os aplicativos abertos e voltar ao monitor principal quando encerrar o jogo.

Inicialmente, criei um script em PowerShell que funcionou muito bem, apesar de alguns pequenos problemas que foram rapidamente resolvidos. No entanto, em Python, tive uma experiência mais segura, sem riscos de bugs aleatórios.