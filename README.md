# Spam Email Classifier

## Overview

This project is a simple email classification tool designed to differentiate between spam and legitimate emails using a Multinomial Naive Bayes classifier. The tool processes email text data, trains a model, and allows for the classification of new emails. The model and vectorizer are saved and can be reloaded for future use.

## Prerequisites

Ensure you have Python installed along with the necessary libraries:

- pandas
- scikit-learn
- joblib

You can install these libraries using pip:
```bash
pip install pandas scikit-learn joblib
```

# Dataset

The dataset (`mail_data.csv`) should be in the following format:

| Email        | Label |
|--------------|-------|
| Email text 1 | 0     |
| Email text 2 | 1     |
| ...          | ...   |

- **Email**: The text content of the email.
- **Label**: The label indicating whether the email is spam (1) or legitimate (0).

# Usage

## Training and Saving the Model

1. Ensure your dataset (`mail_data.csv`) is in the same directory as the script.
2. Run the script to train the model and save it along with the vectorizer.

## Loading the Model and Classifying Emails

To classify a new email, use the saved model and vectorizer.

## Measuring Execution Time

To measure the execution time of the classification:

## License

This plugin is open-source and licensed under the MIT License. Feel free to modify and distribute it as needed.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## Changelog

### v1.0

- Initial release.

## Support

If you have any questions or need support, please open an issue in the GitHub repository.
