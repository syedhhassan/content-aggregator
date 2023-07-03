# News Aggregator
This is a web application which scrapes news website, in this case NYTimes and returns the headlines of some categories.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/syedhhassan/content-aggregator.git
   ```
2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:
- On MacOS
    ```bash
    source venv/bin/activate
    ```
- On Windows
    ```bash
    venv\Scripts\activate
    ```

4. Install the project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the development server:
    ```bash
    python3 manage.py runserver