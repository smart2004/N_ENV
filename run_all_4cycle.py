import subprocess
import time

for s in range(4):
    setup_path = r'/home/smart200481xx/spvk/n_env/test_ids.exe'
    a_process = subprocess.Popen([setup_path])
    a_process.wait()

    setup_path_b = r'/home/smart200481xx/spvk/n_env/vk_form_pic_mode.exe'
    b_process = subprocess.Popen([setup_path_b])
    b_process.wait()

    time.sleep(87000)
    s += 1
