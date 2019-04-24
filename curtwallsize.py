# How big is my curt wall should be:
curt_wall_id = input('Please input glass curt wall id or name: ')
print('All units are millimeters(mm).')
width_curt = input('Input total length of curt wall: ')
width_unit_min = input('Input length of each glass(min):  ')
width_unit_max = input('Input length of each glass(max): ')

filename = curt_wall_id + ' ' + str(width_curt) + 'mm' + '.txt'
with open(filename,'a') as f:
    f.write(filename + '\n')
    for range_index in range(int(width_unit_min)//50,int(width_unit_max)//50 + 1):
        remainder_width = int(width_curt) % (int(range_index)*50)
        div_length = abs(int(range_index) * 50 - int(remainder_width))
        if div_length < remainder_width:
            dif = div_length
        else:
            dif = remainder_width
        f.write('GlassLength: ' + str(range_index*50) + '    ')
        f.write('Deviation: ' + str(dif) + '\n')
print('File has been saved to ' + filename)
