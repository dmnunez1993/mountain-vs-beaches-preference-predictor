#!/usr/bin/env python3
import argparse
import logging

from data.data_config import INDEPENDENT_COLUMNS, TARGET_COLUMN
from data.data_loader import load_data
from data.data_preprocessor import preprocess_data
from data.data_splitter import split_data

from model.evaluator import evaluate_model
from model.trainer import train_model
from model.saver import save_model


def _configure_logging():
    base_logger = logging.getLogger("mountain_vs_beaches_preference_training")
    base_logger.setLevel(logging.DEBUG)
    logger_handler = logging.StreamHandler()
    logger_handler.setFormatter(
        logging.Formatter(
            '%(asctime)s %(name)s: %(levelname)-8s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    )
    base_logger.addHandler(logger_handler)


def main():
    parser = argparse.ArgumentParser(
        description=
        "Trains the model for Mountains vs Beaches preference predictor"
    )
    parser.add_argument(
        '-i',
        '--input',
        help="Path to the input dataset in CSV format",
        type=str,
        required=True,
        dest='input_path',
    )
    parser.add_argument(
        '-o',
        '--output',
        help="Output path for the trained model",
        type=str,
        required=True,
        dest='output_path',
    )

    args = parser.parse_args()

    _configure_logging()

    df = load_data(args.input_path)
    df = preprocess_data(df)

    x_train, x_test, y_train, y_test = split_data(
        df,
        INDEPENDENT_COLUMNS,
        TARGET_COLUMN,
    )

    model = train_model(x_train, y_train)
    evaluate_model(
        model,
        x_test=x_test,
        y_test=y_test,
    )
    save_model(model, args.output_path)


if __name__ == '__main__':
    main()
