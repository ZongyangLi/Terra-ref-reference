def image2npPoints(image_data, sliceID=0):
    
    indexs = np.nonzero(image_data)
    
    row_size = len(indexs[0])
    
    rel_array = np.zeros((row_size, 3))
    
    rel_array[:,0] = indexs[0]
    rel_array[:,1] = indexs[1]
    rel_array[:,2] = sliceID
    
    return rel_array
