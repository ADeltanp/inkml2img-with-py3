import inkml2img, glob, os
# test_dir: path to the file of test data to be converted
test_dir = '/YOUR_PATH/ICFHR_package/CROHME2011_data/CROHME_test/CROHME_test/'
test_names = [os.path.splitext(name)[0] for name in os.listdir(test_dir)
              if (os.path.isfile(os.path.join(test_dir, name))
                  and os.path.splitext(name)[-1].lower() == '.inkml')]
t_img_path = './test_img'

for name in test_names:
    i_name = name + '.inkml'
    p_name = name + '.png'
    t_path = os.path.join(test_dir, i_name)
    t_img = os.path.join(t_img_path, p_name)
    inkml2img.inkml2img(t_path, t_img)
