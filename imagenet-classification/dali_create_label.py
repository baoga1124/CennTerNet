import numpy as np
import scipy.io
import tarfile
import argparse
import os
import glob


def main(args):
    # File list for training
    print("File list for training")
    dname_label = {}
    with open(args.label_wordnetid) as fp:
        for l in fp:
            label, dname = l.rstrip().split(",")
            dname_label[dname] = label

    paths = glob.glob("{}/*/*".format(args.train_file_dir))
    with open("train_label", "w") as fp:
        for path in paths:
            dname, fname = path.rstrip().split("/")[-2:]
            label = dname_label[dname]
            local_path = os.path.join(dname, fname)
            fp.write("{} {}\n".format(local_path, label))

    # File list for valdiation
    print("File list for valdiation")
    with open("val_label", "w") as fp:
        with open(args.validation_data_label) as fpin:
            for i, label in enumerate(fpin):
                fname = "ILSVRC2012_val_{:08}.JPEG".format(i + 1)
                fp.write("{} {}\n".format(fname, label.rstrip()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='ImageNet classification example.')
    parser.add_argument("--label-wordnetid", "-L", type=str,
                        default="./label_wordnetid.csv")
    parser.add_argument("--validation-data-label", "-V",
                        type=str, default="./validation_data_label.txt")
    parser.add_argument("--train-file-dir", "-T", type=str, required=True)

    args = parser.parse_args()
    main(args)
