'''
Sistema de numeração de Eyzinger-Sosa-Stradonitz

Regras Gerais

•O n.º 1 pode ser de sexo feminino ou masculino (o sujeito);
•Todos os outros números ímpares são pessoas do sexo feminino;
•Os números pares são sempre pessoas do sexo masculino;
•O pai de n é 2n, a mãe de n é 2n +1;
•Os antepassados por varonia (linhagem masculina) têm sempre números que são potência 2.
•Uma análise mais avançada exige algumas noções matemáticas:
•O grau de ascendência obtém-se a partir do logaritmo de base 2 do número de ascendência (mais exatamente a sua parte inteira);
•Uma vez conhecido o grau de ascendência, a escrita do número em sistema binário dá-nos o detalhe da filiação.
•Por exemplo: o número 39.
•39 está compreendido entre 25=32 e 26=64, está então no 5º grau de ascendência.
•Converte-se 39 em base 2: 38=32+4+2=1*32+0*16+0*8+1*4+1*2+1*1, ou seja o número binário 100111. Retira-se o 1 inicial e convertem-se os números restantes substituíndo 0 por pai e 1 por mãe.
•A partir do de cujus o antepassado n.º 39 obtém-se tomando o seu pai (0), o pai deste (0), a mãe deste último (1), a mãe desta (1), e finalmente a mãe desta última (1).
•Deste modo, quando um genealogista se refere ao n.º 70, deduzimos que se trata do marido da n.º 71, pai do n.º 35, que é avo paterno do n.º 17, o trisavô casado como a trisavó por varonia do de cujus.'''