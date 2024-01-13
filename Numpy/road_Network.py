import numpy as np 


road = np.array( [ [0, 1, 1,	1,	0,	0,	0, 0],
                    [1,	0,	1,	0,	1,	0,	0, 0],
                    [1,	1,	0,	1,	1,	0, 1 , 0 ] ,
                    [1, 0,	1,	0,	1,	0,	1, 1 ] ,
                    [0,	0 , 1 , 1,	0,	1,	0 , 1] ,
                    [0,	0,	0,	0,	1,	0,	1, 1 ] ,
                    [1,	1,	1,	1,	1,	1,	1, 1]  ,
                    [0,	0,	0,	1,	0,	1,	1, 1 ]  ] )

def voisin (ville , road) : 
    voisin = np.array([] , dtype = int)
    for index , element in enumerate(road[ville]) :
        if element == 1 : 
            voisin = np.append(voisin , index)
            
    return voisin
            
def degreReseau(road) : 
    road_length = len(road)
    ville_array = np.arange(road_length).reshape(road_length , -1)
    voisin_array = np.array([ voisin(ville , road ).shape for ville in range(road_length) ])
    degre_array = np.hstack((ville_array , voisin_array ) )
        
        
                 
    return degre_array
        

print(degreReseau(road)) 
    
    
    

def degreReseau(road):
    road_length = len(road)
    degre = np.arange(road_length).reshape(road_length, 1)

    for villes in range(road_length):
        degre = np.hstack((degre, np.array([[villes, 1]])))

    return degre[:, 1:]

# Example road array (replace this with your actual road array)
road = np.array([[0, 1, 1, 1, 0, 0, 0, 0],
                 [1, 0, 1, 0, 1, 0, 0, 0],
                 [1, 0, 1, 1, 0, 0, 0, 0],
                 [1, 0, 1, 0, 1, 1, 0, 0],
                 [0, 1, 0, 1, 0, 1, 1, 0],
                 [0, 0, 0, 1, 0, 1, 0, 1],
                 [0, 0, 0, 0, 1, 0, 1, 0],
                 [0, 0, 0, 0, 0, 1, 0, 1]])

result = degreReseau(road)
print(result)


def premier_Entier(L) : 
    p_entier = 1
    for element in sorted(L) : 
        if  0 < element < p_entier :
            p_entier = element      
        if p_entier in L  :
            p_entier += 1
            
    return p_entier

vecteur = np.array([-1 , 0 , 1, 4 , 3 ,5 ,9 , 2])
print(vecteur)
print(premier_Entier(vecteur))

def couleurVille(road) -> 5 :
    road_length = len(road)
    colors = np.zeros(road_length , dtype = int)
    villes = np.array([ville for ville in reversed(range(road_length))])
    # print (colors , road_length , villes)

    for ville in villes:
        for i , v in enumerate(voisin(ville, road)) :
            if colors[v] == 0 : 
                colors[v] = i*v + 1


    return colors


print(couleurVille(road))     
         


