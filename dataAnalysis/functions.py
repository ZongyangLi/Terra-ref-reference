def image2npPoints(image_data, sliceID=0):
    
    indexs = np.nonzero(image_data)
    
    row_size = len(indexs[0])
    
    rel_array = np.zeros((row_size, 3))
    
    rel_array[:,0] = indexs[0]
    rel_array[:,1] = indexs[1]
    rel_array[:,2] = sliceID
    
    return rel_array


def plot_counting_to_csv(plot_counting, csv_dir, str_date):
    
    out_file = os.path.join(csv_dir, str_date+'_panicle_counting.csv')
    csv = open(out_file, 'w')
    
    (fields, traits) = get_traits_table_panicle()
    
    csv.write(','.join(map(str, fields)) + '\n')
    
    for i in range(0, 1728):
        plotNum = i+1
        if plot_counting[plotNum] == 0:
            continue
        
        str_time = str_date+'T12:00:00'
        traits['local_datetime'] = str_time
        traits['panicle_counting'] = plot_counting[plotNum]
        traits['site'] = parse_site_from_plotNum_1728(plotNum)
        trait_list = generate_traits_list_panicle(traits)
        csv.write(','.join(map(str, trait_list)) + '\n')
    
    csv.close()
    #betydb.submit_traits(out_file, filetype='csv', betykey=betydb.get_bety_key(), betyurl=betydb.get_bety_url())
    return

def get_traits_table_panicle():
    
    fields = ('local_datetime', 'panicle_counting', 'access_level', 'species', 'site',
              'citation_author', 'citation_year', 'citation_title', 'method')
    
    traits = {'local_datetime' : '',
              'panicle_counting' : [],
              'access_level' : '2',
              'species' : 'Sorghum bicolor',
              'site': [],
              'citation_author': 'ZongyangLi',
              'citation_year' : '2018',
              'citation_title' : 'Maricopa Field Station Data and Metadata',
              'method' : 'Scanner 3d ply data to panicle counting'
        }
    
    return (fields, traits)

def generate_traits_list_panicle(traits):
    
    trait_list = [  traits['local_datetime'],
                    traits['panicle_counting'],
                    traits['access_level'],
                    traits['species'],
                    traits['site'],
                    traits['citation_author'],
                    traits['citation_year'],
                    traits['citation_title'],
                    traits['method']
                  ]
    
    return trait_list
