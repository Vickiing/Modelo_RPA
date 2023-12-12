# Modelo_RPA
digitador de quantidades faturadas de notas fiscais 
- Esse RPA foi feito para ser usado exclusivamente com o sistema RMS da TOTV's
Primeiro o usuário informa quantas notas devem ser digitadas.
Em seguida é verificado se a nota correspondente está presente no arquivo txt, que é gerado pelo SGDB (TOAD).
Se sim, é feito a digitação das quantidades.
O arquivo TXT foi definido pra ter o delimitador "|"(pipe), pra que não houvesse problemas com digitação de quantidades fracionadas.
A titulo de curiosidade: Os dois módulos de nome "projetorpa_nivel2.py" e rpa_nlv2_bettercod.py" são o mesmo scrip. Do mais antigo ao mais recente respectivamente.
