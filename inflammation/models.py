"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data (each row contains
    measurements for a single patient across all days).
    :returns: An array of mean values of measurements for each day.
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data (each row contains
    measurements for a single patient across all days).
    :returns: An array of max values of measurements for each day."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data (each row contains
    measurements for a single patient across all days).
    :returns: An array of min values of measurements for each day.
    """
    return np.min(data, axis=0)


def daily_above_threshold(data, patient_number, threshold):

    """ Determine if a value is above a threshold

    :param threshold: A number for the threshold
    :param data: An array of data
    :param patient_number: a list of patient numbers
    :returns: A boolean output if data is above threshold
    """

    return map(lambda x: x > threshold, data[patient_number,:])


def daily_std(data):

    '''compute standard deviation of data

    :param data: an array of data
    :returns standard deviation of each day
    '''

    return np.std(data, axis=0)

