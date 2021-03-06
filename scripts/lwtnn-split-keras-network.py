#!/usr/bin/env python3
"""
Convert a keras model, saved with model.save(...) to a weights and
architecture component.
"""
import argparse

def get_args():
    d = '(default: %(default)s)'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('model')
    parser.add_argument('-w','--weight-file-name', default='weights.h5',
                        help=d)
    parser.add_argument('-a', '--architecture-file-name',
                        default='architecture.json', help=d)
    return parser.parse_args()

def run():
    args = get_args()
    from h5py import File
    import json
    m = File(args.model,'r')
    with File(args.weight_file_name,'w') as w:
        for name, wt in w.items():
            w.copy(wt, name)

    arch = json.loads(m.attrs['model_config'])
    with open(args.architecture_file_name,'w') as arch_file:
        arch_file.write(json.dumps(arch,indent=2))


if __name__ == '__main__':
    run()
