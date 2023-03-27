# Sistema de cotação de moeda Euro - BR

Este projeto foi desenvolvido para buscar preço e cotação da paridade EUR/BRL a partir de uma valor informado.

### Sobre os arquivos disponíveis:

  <strong>winfig.ZIP</strong> = diretório do arquivo executável (.exe)
  
  <strong>winfig.PY e demais arquivos</strong> = arquivos construídos durante desenvolvimento do código.
  
### Sobre a funcionalidade do software:

  O software abre uma interface gráfica desenvolvida com Tkinter, em Python. Nessa janela, é solicitada um valor numérico tipo FLOAT, no padrão americano(usando '.' como separador decimal).
  Ao inserir o valor, faz-se necessário clicar no botão 'Cotar', que tem a função de consultar o preço do EUR/BRL através de uma API, mostrar ao usuário e informar o valor de câmbio da quantia informada.
  Portanto, o valor de entrada é em Reais e o valor de saída em Euro.

### Construção:
  
  O primeiro passo foi montar uma interface gráfica com Figma, agrupar o que era estático e o que seria dinâmico, renomear os objetos para fazer exportação para Tkinter, sendo editável com Python. Depois de exportado com Proxlight Designer, foi criada a funcionalidade do botão, além de ajuste no design deste.
  Após tudo isso, o código estava pronto, porém, fazendo-se necessário testes e ajustes para melhor experiência, como a organização das informações.
  
### Maiores dificuldades:

  Ao realizar a exportação, houveram benefícios nas etapas de ajustar as configurações já com os itens em suas posições. Por outro lado, a caixa de texto não foi exportada, sendo necessária a construção manual. Esta foi a parte mais desafiadora para colocar este item em harmonia com o código todo.
    
### Atualizações:

  Este é um código simples com uma função específica que resolve um "problema" pessoal, portanto, o código está finalizado e deve ter apenas mais uma atualização ou de acordo com as variações de taxas de IOF e/ou SPREAD da casa de câmbio.
  
##### Desenvolvido por Jorge Trajano
