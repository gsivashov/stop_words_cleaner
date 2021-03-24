# Install

Installation process for Linux, Mac and Windows WSL users:

## 1. Create virtual environment:

```
python -m venv .venv
```

Do it only when you creating project. Dont create it each time.

Sometimes it could be `python3`, `py`, `py3`

## 2. Activating virtual environment:

```
source .venv/bin/activate
```

## 3. Install libraries:

```
pip install -r requirements.txt
```

# Usage

Don't forget that you need to activate virtual environment <b>before</b> using scripts

You can add whatever stopword file you whant. Script is not hardcoded to anything

## universal_stop_words.py

Required arguments:

`--row` - index of row with keywords. Reminder: index starts from zero

`--file` - path to file with keywords

`--good` - path to file where good pharses will be stored

`--bad` - path to file where exclusion pharses will be stored

Supported arguments:
`--stopwords` - path to stopwords file. By default it's: `stopwords.txt`
`--delimiter` - specify delimiter for start file. By default it's: `|`

Usage example:

```
python universal_stop_words.py --file yourfile.csv --row 0 --good good_output.csv --bad bad_output.csv
```

## stop_words_german.txt

Ideas where taked here:

http://official-swiss-national-languages.all-about-switzerland.info/names-swiss-villages-towns-languages.html#A

```
copy($x('//td[@class="bl"]/text()').map(i => i.textContent))
```
