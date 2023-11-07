![Python3](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

# Food Product Barcode Parser

## Overview

This repository contains a barcode parser that takes the input of a food product's barcode and queries OpenFoodFacts to retrieve information about the product. 
This tool is useful for quickly accessing information about food products.

## Features

- Retrieve detailed information about a food product using its barcode.
- Utilizes the OpenFoodFacts database for product data.
- Designed for easy integration into other projects.

## Usage

To use this barcode parser, follow these steps:

1. Clone the repository to your local machine:

   ```(bash)
   git clone https://github.com/yourusername/food-barcode-parser.git
   ```

2. Open a terminal and navigate to the project directory.

3. Run the parser with a barcode as an argument:

   ```(bash)
   python main.py
   ```

4. The tool will query OpenFoodFacts and display information about the product associated with the given barcode.

## Installation

To install the required dependencies, use the following command:

```(bash)
pip install requests
```


## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to OpenFoodFacts for providing the product data.
