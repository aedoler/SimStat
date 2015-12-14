#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simstat: A Simple Confidence Interval Calculator."""

from scipy import stats
import numpy as np
import math
import sys
import argparse


def get_data(args):
    """Function to use raw sample data as input to calculate
    confidence interval.

    Args:
        datafile (string): Name of a csv file with sample data.
        conf (float, optional): Confidence level

    Returns:
        conf_interval (tuple): Confidence interval

    Example:
        python simstat.py data data.txt 0.99
        Num: 10, Min: 1.0, Max: 10.0, Mean: 5.5000, Variance: 9.1667
        (3.0338311998291538, 7.9661688001708466)

    """
    try:
        sample = np.loadtxt(args.datafile, delimiter=',')
    except IOError:
        print 'Cannot open datafile. Run this program with -h for help.'
        sys.exit(2)
    num, (smin, smax), mean, var, skew, kurt = stats.describe(sample)
    std = math.sqrt(var)
    interval = stats.norm.interval(args.conf, loc=mean,
                                   scale=std/math.sqrt(len(sample)))
    message = 'Num: {0}, Min: {1}, Max: {2}, Mean: {3:.4f}, Variance: {4:.4f}'
    sumstat = message.format(num, smin, smax, mean, var)
    print sumstat
    print interval


def get_summary(args):
    """Function to use summary data as input to calculate
    confidence interval.

    Args:
        mean (float): Sample mean
        std (float): Sample standard deviation
        num (int): Number of sample data points
        conf (fload, default=0.95) Confidence level

    Returns:
        interval (tuple): Confidence interval.

    Example:
        get_summary(55.0, 3.2, 102, 0.95)
        >>> (54.378990872443168, 55.621009127556832)
    """
    interval = stats.norm.interval(args.conf, loc=args.mean,
                                   scale=args.std/math.sqrt(args.num))
    print interval


def main():
    """This is the main function."""
    parser = argparse.ArgumentParser(description='Simstat Utility')
    subparsers = parser.add_subparsers()
    parser_sum = subparsers.add_parser('sum')
    parser_sum.add_argument('num', type=int,
                            help='Number of sample points (int)')
    parser_sum.add_argument('mean', type=float,
                            help='Sample mean (float)')
    parser_sum.add_argument('std', type=float,
                            help='Sample standard deviation float)')
    parser_sum.add_argument('conf', type=float, nargs='?', default=0.95,
                            help='Confidence interval (float) 0.01:0.99')
    parser_sum.set_defaults(func=get_summary)
    parser_data = subparsers.add_parser('data')
    parser_data.add_argument('datafile',
                            help='Name of the csv file containing sample data.')
    parser_data.add_argument('conf', type=float, nargs='?', default=0.95,
                            help='Optional confidence interval (float) .01:.99')
    parser_data.set_defaults(func=get_data)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
