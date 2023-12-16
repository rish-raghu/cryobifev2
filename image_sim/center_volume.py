from cryodrgn import mrc

array, header = mrc.parse_mrc('images/ctf/images_1.mrcs')
# header.fields['xorg'] = 0.0
# header.fields['yorg'] = 0.0
# header.fields['zorg'] = 0.0
#header.fields['mz'] = 1
array *= -1
mrc.write('images/ctf/images_1_invert.mrcs', array, header=header)