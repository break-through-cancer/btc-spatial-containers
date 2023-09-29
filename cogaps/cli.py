#!/usr/bin/env python3

import argparse
import logging

import PyCoGAPS.parameters
import PyCoGAPS.pycogaps_main
import scanpy
import anndata

logger = logging.getLogger(__name__)

def configure_logging(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(name)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def get_args():
    parser = argparse.ArgumentParser(description='CoGAPS')
    parser.add_argument('--input', type=str,
                        help='Input AnnData .h5ad archive', required=True)
    parser.add_argument('--output', type=str,
                        help='Output AnnData .h5ad archive', required=True)
    parser.add_argument('--n-patterns', type=int, required=True)

    parser.add_argument('--n-iterations', type=int, default=50000)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('-v', '--verbose',
                        action='store_true', help='Enable verbose logging')
    return parser.parse_args()


def main():
    args = get_args()
    configure_logging(verbose=args.verbose)
    adata = scanpy.read_h5ad(args.input)

    scanpy.log1p(adata, copy=False)

    params = PyCoGAPS.parameters.CoParams()
    PyCoGAPS.parameters.setParams(params, {
        'nIterations': args.n_iterations,
        'seed': args.seed,
        'nPatterns': args.n_patterns
    })
    result = PyCoGAPS.pycogaps_main.CoGAPS(adata, params)

    result.write(args.output)


if __name__ == '__main__':
    main()
