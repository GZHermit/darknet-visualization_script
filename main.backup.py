# coding: utf-8
import argparse
from operations import train, valid, compute_mAP,draw


def start(args):
    if args.order == 'train':
        train(args)
    elif args.order == 'valid':
        valid(args)
        compute_mAP(args)
        draw(args, 'loss')
    elif args.order == 'draw':
        draw(args)


def get_arguments():
    """Parse all the arguments provided from the CLI.

    Returns:
      A list of parsed arguments.
    """

    Order = ''
    DarkNet_PATH = ''
    CfgFile = ''
    DataFile = ''
    ClsNames = ''
    Weight = ''
    Result = ''
    Dataset = ''
    ImageNames = ''
    TrainSteps = ''
    GPUs = ''
    DrawOption = 'loss'

    parser = argparse.ArgumentParser(description="Unity Scripts Project for Model Training")
    parser.add_argument("--order", type=str, default=Order,
                        help="")
    parser.add_argument("--darknet_path", type=str, default=DarkNet_PATH,
                        help="")
    parser.add_argument("--cfg_file", type=str, default=CfgFile,
                        help="")
    parser.add_argument("--data_file", type=str, default=DataFile,
                        help="")
    parser.add_argument("--clsnames", type=str, default=ClsNames,
                        help="")
    parser.add_argument("--weight", type=str, default=Weight,
                        help="")
    parser.add_argument("--result", type=str, default=Result,
                        help="")
    parser.add_argument("--dataset", type=str, default=Dataset,
                        help="")
    parser.add_argument("--image_names", type=str, default=ImageNames,
                        help="")
    parser.add_argument("--train_steps", type=str, default=TrainSteps,
                        help="")
    parser.add_argument("--gpus", type=str, default=GPUs,
                        help="")
    parser.add_argument("--draw_option", type=str, default=DrawOption,
                        help="")
    return parser, parser.parse_args()


if __name__ == '__main__':
    parser, args = get_arguments()

    ModelName = args.Cfg_PATH.split('/')[-1].strip('.cfg')
    DataName = args.Data_PATH.split('/')[-1].strip('.data')
    parser.add_argument("--model_name", type=str, default=ModelName,
                        help="")
    parser.add_argument("--data_name", type=str, default=DataName,
                        help="")
    if args.darknet_path != '':
        args.cfg_file += args.darknet_path + 'cfg/'
        args.data_file += args.darknet_path + 'cfg/'
        args.clsnames += args.darknet_path + 'data/'
        args.weight += args.darknet_path + 'weight/'
        args.result += args.darknet_path + 'result/'
    args = parser.parse_args()
    start(args)
