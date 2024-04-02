# Recommendation Model Website

Recommendation Model Website is a web application developed using Flask that provides users with product recommendations based on their search queries. Users can register, log in, and search for products, and the application will display a list of recommended products based on their input.

## Features

- User Authentication: Users can register for an account and log in securely.
- Product Search: Allows users to search for products using keywords.
- Product Recommendations: Provides users with a list of recommended products based on their search queries.
- Database Integration: Stores user information and product data in a MySQL database.

## Model Used: Sentence Transformers

### About Sentence Transformers

- **What is Sentence Transformers?**: Sentence Transformers is a Python library that provides pre-trained models for generating sentence embeddings. These embeddings capture semantic meaning and contextual information of input sentences, enabling tasks such as similarity matching, clustering, and retrieval.

- **Advantages of Sentence Transformers**:
  1. **Semantic Understanding**: Captures the semantic meaning of sentences.
  2. **Pre-trained Models**: Comes with pre-trained models fine-tuned on large text corpora.
  3. **Transfer Learning**: Enables fine-tuning on specific downstream tasks with limited labeled data.
  4. **Efficiency**: Computationally efficient, suitable for real-time applications.

### Advantages of Using Sentence Transformers in Your Recommendation Model

1. **Semantic Similarity**: Enables accurate recommendations based on semantic similarity between user queries and product descriptions.
2. **Out-of-the-Box Solution**: Comes with pre-trained models, making it easy to implement without extensive training data.
3. **Efficiency**: Computationally efficient, suitable for real-time recommendation systems.

## Setup

To set up the Recommendation Model Website locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/saiguptha2003/Recommendation_model_website.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Recommendation_model_website
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the MySQL database:
   
   - Ensure you have MySQL installed and running on your local machine.
   - Create a new database named `reccommendationmodel`.
   - Modify the database connection details (host, user, password) in the `connect()` function in `utility.py` to match your MySQL setup.

5. Run the Flask application:

    ```bash
    python app.py
    ```

6. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage

1. Register for an account using a valid email address and password.
2. Log in to the application using your registered credentials.
3. Use the search bar to enter keywords related to the products you're interested in.
4. View the recommended products based on your search query.

## Technologies Used

- Flask: Web application framework for Python
- MySQL: Relational database management system
- Sentence Transformers: Library for generating sentence embeddings
- pandas: Data manipulation and analysis library for Python

## Contributing

Contributions to the Recommendation Model Website project are welcome! If you encounter any issues, have suggestions for improvements, or would like to contribute new features, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
