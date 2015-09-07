import argparse
import os

import cobra


def sbml_to_mat():
    parser = argparse.ArgumentParser()
    parser.add_argument("sbml", help="SBML filename")
    parser.add_argument("-o", "--output",
                        help="output MAT filename")
    parser.add_argument("-n", "--name",
                        help="name of the variable in the MAT file")

    args = parser.parse_args()
    sbml_filename = args.sbml
    mat_filename = args.output
    var_name = args.name

    # attempt to guess output filename
    if mat_filename is None:
        if sbml_filename.endswith(".xml.gz"):
            file_base = sbml_filename[:-7]
        elif sbml_filename.endswith(".xml.bz2"):
            file_base = sbml_filename[:-8]
        elif sbml_filename.endswith(".xml"):
            file_base = sbml_filename[:-4]
        else:
            file_base = sbml_filename
        mat_filename = file_base + ".mat"

    model = cobra.io.read_sbml_model(sbml_filename)
    cobra.io.save_matlab_model(model, mat_filename, var_name)


def mat_to_sbml():
    parser = argparse.ArgumentParser()
    parser.add_argument("mat", help="MAT filename")
    parser.add_argument("-o", "--output",
                        help="output SBML filename")
    parser.add_argument("-n", "--name",
                        help="name of the variable in the MAT file")

    args = parser.parse_args()
    sbml_filename = args.output
    mat_filename = args.mat
    var_name = args.name

    # attempt to guess output filename
    if sbml_filename is None:
        if mat_filename.endswith(".mat"):
            sbml_filename = mat_filename[:-4] + ".mat"
        else:
            sbml_filename = mat_filename + ".mat"

    model = cobra.io.load_matlab_model(mat_filename, var_name)
    cobra.io.write_sbml_model(model, sbml_filename)


if __name__ == "__main__":
    mat_to_sbml()
