
## Automated_Scrapy_Web
- Scrapy is a powerful and flexible Python framework for web scraping and crawling. It allows you to easily extract data from websites, follow links, and navigate through web pages in an organized and efficient manner.

### Bookscraper Pipeline
- The BookscraperPipeline is responsible for processing scraped book data and transforming it before saving it to a MySQL database.

#### Item Processing
- The pipeline processes various fields of the scraped book data to ensure consistency and suitability for database storage. Here's an overview of the transformations performed:

1. Strip Whitespace: Removes leading and trailing whitespace from string fields except for the 'description' field.
2. Lowercase Category and Product Type: Converts 'category' and 'product_type' fields to lowercase.
3. Price Conversion: Removes the '£' symbol from price-related fields and converts them to floating-point numbers.
4. Availability Extraction: Extracts the number of books available from the 'availability' field.
5. Reviews Conversion: Converts the 'num_reviews' field from a string to an integer.
5. Stars Conversion: Converts the 'stars' field from text to a numeric value.
#### SaveToMySQLPipeline
- The SaveToMySQLPipeline is responsible for connecting to a MySQL database and storing the processed book data.

#### Initialization
Upon initialization, the pipeline establishes a connection to the MySQL database using the provided credentials. It creates a cursor for executing commands and checks if the 'books' table exists. If not, it creates the table with the required columns.

##### Process Item
The process_item method takes a processed book item and inserts its data into the 'books' table using an SQL INSERT statement. The data is committed to the database.

##### Close Spider
The close_spider method is called when the spider finishes its work. It closes the cursor and the connection to the database.

### Conclusion
These pipelines provide a robust solution for processing and storing scraped book data in a MySQL database. The BookscraperPipeline performs necessary transformations on the scraped data, while the SaveToMySQLPipeline manages the connection and storage process. By configuring these pipelines in your spider's settings, you can seamlessly integrate them into your book scraping project.

## Unit Testing for Bookscraper Pipelines
- This repository contains unit tests for the BookscraperPipeline and SaveToMySQLPipeline classes in the pipelines module. These tests are designed to ensure the correct functionality of these pipelines during the book scraping process.

- Setup
Before running the tests, make sure you have the necessary dependencies installed. You can install them using the following command:

`pip install -r requirements.txt`
## Usage
- To run the tests, execute the following command:

`python test_pipelines.py`
## Tests
#### TestBookscraperPipeline
- This test suite verifies the functionality of the BookscraperPipeline class.

#### test_process_item
- This test ensures that the process_item method of the BookscraperPipeline processes the mock item correctly.

- Create a mock item and spider.
- Instantiate the BookscraperPipeline.
- Call process_item with the mock item and spider.
- Verify that the item's title, price, and availability are processed correctly.
#### TestSaveToMySQLPipeline
- This test suite verifies the functionality of the SaveToMySQLPipeline class.

#### setUp
- This method is called before each test to set up the necessary mocks and pipeline instance.

- Mock the mysql.connector.connect function using the @patch decorator.
- Instantiate the SaveToMySQLPipeline.
- Create mock connection and cursor instances.
#### test_process_item
- This test ensures that the process_item method of the SaveToMySQLPipeline class performs the required database operations correctly.

#### Create a mock item and spider.
- Call process_item with the mock item and spider.
- Verify that the insert statement was executed.
- Verify that the commit operation was called.
#### test_close_spider
- This test ensures that the close_spider method of the SaveToMySQLPipeline class closes the cursor and connection properly.

#### Create a mock spider.
- Call close_spider with the mock spider.
- Verify that the cursor and connection were closed.
## Conclusion
These unit tests provide comprehensive coverage for the BookscraperPipeline and SaveToMySQLPipeline classes, ensuring that the book scraping process and database operations are functioning as expected. Running these tests will help maintain the reliability and correctness of these pipeline components.