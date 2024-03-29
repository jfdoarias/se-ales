from matplotlib import pyplot as plt
from matplotlib import style
import mysignals as sigs


def calc_first_difference(sig_src_arr,sig_dest_arr):
    for x in range(len(sig_dest_arr)):
        sig_dest_arr[x] =0

    for x in range(len(sig_src_arr)):
        sig_dest_arr[x] = sig_src_arr[x] - sig_src_arr[x-1]
        

    style.use('ggplot')
    #style.use('dark_background')

    f,plt_arr = plt.subplots(2,sharex=True)
    f.suptitle("First Difference")

    plt_arr[0].plot(sig_src_arr,color='red')
    plt_arr[0].set_title("Input Signal")

    plt_arr[1].plot(sig_dest_arr,color ='magenta')
    plt_arr[1].set_title("Output Signal")

    plt.show()


output_signal =[None]*320
calc_first_difference(sigs.InputSignal_1kHz_15kHz,output_signal)

