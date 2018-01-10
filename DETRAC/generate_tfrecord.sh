python3 generate_tfrecord.py --csv_input=data/DETRAC_train_labels.csv --output_path=data/DETRAC_train.tfrecord
python3 generate_tfrecord.py --csv_input=data/DETRAC_test_labels.csv --output_path=data/DETRAC_test.tfrecord
python3 generate_tfrecord.py --csv_input=data/DETRAC_validation_labels.csv --output_path=data/DETRAC_validation.tfrecord
