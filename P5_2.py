'''
2. Convierta el código de la parte del ejercicio 5 de la práctica anterior
que pintaba la proteína en una función que reciba ats_chains, de manera que 
pueda llamarse de la siguiente manera:
                pinta_proteina(ats_chains)
'''
def pinta_proteina(Cadena,AtGlobal):
    """
    
    Parameters
    ----------
    1° - lista con las cadenas de la proteina separadas.
    2° - lista con todos los atomos, para usar su tamaño en la dimension de 
         la grafica

    Returns
    -------
    - Una grafica con cada cadena colorida con distintas colores
    
    Requires
    --------
    - Ya debe tener la lista de cadenas (el 1° parametro) y la lista de todos
      los atomos ya listas
    - Sera usado Numpy y matplotlib.pyplot

    """
    import numpy as np
    import matplotlib.pyplot as plt
    
    
    fig = plt.figure(figsize = (8,8), dpi = 175, frameon = False)
    ax = fig.add_subplot(projection='3d') 
    atGl = np.array(AtGlobal)
    atChains = []
    for w in range(0,len(Cadena)):
        atChains.append(np.array(Cadena[w]))
   
   
    
    min_x = np.min(atGl[:,0])
    max_x = np.max(atGl[:,0])
    min_y = np.min(atGl[:,1])
    max_y = np.max(atGl[:,1])
    min_z = np.min(atGl[:,2])
    max_z = np.max(atGl[:,2])
    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)
    ax.set_zlim(min_z, max_z)
    #ax.set_xlim(-50, 50)
    #ax.set_ylim(-50, 50)
    #ax.set_zlim(-50, 50)
    
    edcol = 'brgmykcbrgmykcbrgmykc'
    col = 'kkkkkkkwwwwwwwmmmymmm'
    i = 0 #para ir cambiando el color de cada cadena
    for k in atChains:
        x = k[:,0]
        y = k[:,1]
        z = k[:,2]
        ax.scatter3D(x, y, z, c=col[i], edgecolors=edcol[i],
        marker='o', s=5, depthshade=False)
        i += 1 #i = i + 1
    
    plt.show()