from optparse import OptionParser
import configparser as cg


def read_list(filename):
    file = open(filename,'r')
    lines = file.readlines()
    list_signal = []
    for x in lines:
        list_signal.append(x.rstrip())
    file.close()
    return list_signal


def read_config(cfg_file = None):
    parser = OptionParser()
    parser.add_option("--cfg") #Compulsory
    (options, _args) = parser.parse_args()
    if cfg_file is None:
        cfg_file = options.cfg
    if options.cfg is None and cfg_file is None:
        cfg_file = 'configuration/sincnet_nikita.cfg'
    Config = cg.ConfigParser()
    Config.read(cfg_file)

    #[data]
    options.tr_lst = Config.get('data','tr_lst')
    options.te_lst = Config.get('data', 'te_lst')
    options.lab_dict = Config.get('data', 'lab_dict')
    options.data_folder = Config.get('data', 'data_folder')
    options.output_folder = Config.get('data', 'output_folder')
    options.pt_file = Config.get('data', 'pt_file')
    options.lowest_id = Config.get('data', 'lowest_id')

    #[windowing]
    options.fs = Config.get('windowing', 'fs')
    options.cw_len = Config.get('windowing', 'cw_len')
    options.cw_shift = Config.get('windowing', 'cw_shift')

    #[cnn]
    options.cnn_N_filt = Config.get('cnn', 'cnn_N_filt')
    options.cnn_len_filt = Config.get('cnn', 'cnn_len_filt')
    options.cnn_max_pool_len = Config.get('cnn', 'cnn_max_pool_len')
    options.cnn_use_laynorm_inp = Config.get('cnn', 'cnn_use_laynorm_inp')
    options.cnn_use_batchnorm_inp = Config.get('cnn', 'cnn_use_batchnorm_inp')
    options.cnn_use_laynorm = Config.get('cnn', 'cnn_use_laynorm')
    options.cnn_use_batchnorm = Config.get('cnn', 'cnn_use_batchnorm')
    options.cnn_act = Config.get('cnn', 'cnn_act')
    options.cnn_drop = Config.get('cnn', 'cnn_drop')

    #[dnn]
    options.fc_lay = Config.get('dnn', 'fc_lay')
    options.fc_drop = Config.get('dnn', 'fc_drop')
    options.fc_use_laynorm_inp = Config.get('dnn', 'fc_use_laynorm_inp')
    options.fc_use_batchnorm_inp = Config.get('dnn', 'fc_use_batchnorm_inp')
    options.fc_use_batchnorm = Config.get('dnn', 'fc_use_batchnorm')
    options.fc_use_laynorm = Config.get('dnn', 'fc_use_laynorm')
    options.fc_act = Config.get('dnn', 'fc_act')

    #[classes]
    options.class_lay = Config.get('class', 'class_lay')
    options.class_drop = Config.get('class', 'class_drop')
    options.class_use_laynorm_inp = Config.get('class', 'class_use_laynorm_inp')
    options.class_use_batchnorm_inp = Config.get('class', 'class_use_batchnorm_inp')
    options.class_use_batchnorm = Config.get('class', 'class_use_batchnorm')
    options.class_use_laynorm = Config.get('class', 'class_use_laynorm')
    options.class_act = Config.get('class', 'class_act')

    #[optimization]
    options.lr = Config.get('optimization', 'lr')
    options.batch_size = Config.get('optimization', 'batch_size')
    options.N_epochs = Config.get('optimization', 'N_epochs')
    options.N_batches = Config.get('optimization', 'N_batches')
    options.N_eval_epoch = Config.get('optimization', 'N_eval_epoch')
    options.seed = Config.get('optimization', 'seed')

    print(options)
    return options


def str_to_bool(s):
    if s == 'True':
        return True
    elif s == 'False':
        return False
    else:
        raise ValueError
