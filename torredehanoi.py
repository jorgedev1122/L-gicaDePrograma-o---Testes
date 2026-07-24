def mover_discos(num_discos, origem, destino, auxiliar):
    if num_discos == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
    else: 
        mover_discos(num_discos - 1, origem, auxiliar, destino)
        print(f'Mover disco {num_discos} de {origem} para {destino}')
        mover_discos(num_discos - 1, auxiliar, destino, origem)

mover_discos(3, "torre 1", "torre 3", "torre 2")    

"""o objetivo do código é resolver o problema da Torre de Hanoi, que consiste em mover uma pilha de uma torre pra outra"""
"""Quando o código é rodado, ele imrpime o passo a passo de como mover os discos, independente da quantidade de discos que o usuário escolher."""