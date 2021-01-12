.PHONY: all

all: generate_to_tag

join_reviews:
	cat data/raw/x00 data/raw/x01 data/raw/x02 data/raw/x03 data/raw/x04 data/raw/x05 > data/raw/reviews.json && rm data/raw/x0*

generate_to_tag:
	bash utils/generate_reviews_table.sh data/raw/reviews.json data/processed/command_line/unique_reviews.csv
	cd scripts && python user_distribution.py
	cd scripts && python sampling.py

generate_to_train:
	cd scripts && python make_training.py