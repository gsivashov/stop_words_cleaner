import csv
from collections import defaultdict
from argparse import ArgumentParser


def main(params):
    stop_words = params.stopwords
    row_index = params.row
    delimiter = params.delimiter
    start_file = params.file
    good_file = params.good
    bad_file = params.bad

    good_phrases = []
    bad_phrases = []
    unique_stop_words = set()

    with open(stop_words) as f:
        for line in f:
            line_lower = line.strip().lower()
            unique_stop_words.add(line_lower)

    stop_words_map = defaultdict(int)

    with open(start_file) as f:
        reader = csv.reader(f, delimiter=delimiter)
        next(reader)

        for line in reader:
            if not line:
                continue

            term = line[row_index]
            line_words = set(term.lower().split())

            intersection = line_words & unique_stop_words
            if intersection:
                for stop_word in intersection:
                    stop_words_map[stop_word] += 1
                bad_phrases.append(term)
                # bad_phrases.append(line)
            else:
                good_phrases.append(term)
                # good_phrases.append(line)

    with open(good_file, 'w') as good_output:
        for word in good_phrases:
            good_output.write(f'{word}\n')
            # good_output.write(f'{"|".join(word)}\n')

    with open(bad_file, 'w') as bad_output:
        for word in bad_phrases:
            bad_output.write(f'{word}\n')
            # bad_output.write(f'{"|".join(word)}\n')


if __name__ == "__main__":
    parser = ArgumentParser()

    # REQUIRED PARAMS

    parser.add_argument(
        '--stopwords',
        type=str,
        help='stopwords file path',
        default='stop_words.txt',
    )
    parser.add_argument(
        '--row',
        type=int,
        help='index of line with keywords',
        required=True,
    )
    parser.add_argument(
        '--delimiter',
        type=str,
        help='csv delimiter (default "|")',
        default='|',
    )
    parser.add_argument(
        '--file',
        type=str,
        help='file path',
        required=True,
    )
    parser.add_argument(
        '--good',
        type=str,
        help='file path for good phrases',
        required=True,
    )
    parser.add_argument(
        '--bad',
        type=str,
        help='file path for bad phrases',
        required=True,
    )
    params = parser.parse_args()

    main(params)
