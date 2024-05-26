# Code Analysis Tool

This project is a code analysis tool that uses OpenAI's GPT-3.5-turbo model to review and provide recommendations for code files. The tool can identify syntax and logical errors, suggest code refactoring, performance optimizations, security vulnerabilities, and best practices. It is built using Streamlit for the user interface.

## Features

- Analyze multiple code files at once.
- Select between different types of analysis:
  - **REVIEW**: General code review for syntax, logical errors, code quality, performance, security, and best practices.
  - **SECURITY**: Focused review for security vulnerabilities.
- Provide detailed recommendations and improvements.

## Requirements

- Python 3.7 or higher
- Streamlit
- OpenAI API key
- tiktoken

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sarag5/fixer-code-review.git
   cd code-analysis-tool
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key:
   ```python
   openai.api_key = 'your-api-key-here'  # Ensure your OpenAI API key is set here
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Upload your code files and select the type of analysis you want.

4. Click the "Analyze" button to get the analysis results.

## Code Overview

### `analyze_code_files`

This function takes a list of code file paths and an analysis type, and returns an iterable of dictionaries containing file information and recommendations.

### `analyze_code_file`

This function reads the content of a code file, logs the file being analyzed, and calls `get_code_analysis` to get the analysis result.

### `get_num_tokens_from_messages`

This function calculates the number of tokens used by a list of messages to ensure the request stays within the token limit.

### `get_code_analysis`

This function constructs the prompt based on the analysis type, calculates the number of tokens for the response, sends the request to the OpenAI API, and returns the response.

## Example

```python
if __name__ == "__main__":
    st.title("Code Analysis Tool")
    uploaded_files = st.file_uploader("Choose code files", accept_multiple_files=True, type=["py", "txt"])
    analysis_type = st.selectbox("Select analysis type", ["REVIEW", "SECURITY"])

    if st.button("Analyze"):
        if uploaded_files:
            file_paths = [file.name for file in uploaded_files]
            results = analyze_code_files(file_paths, analysis_type)
            for result in results:
                st.write(result)
```

## License

This project is licensed under the MIT License.

## Acknowledgements

- [OpenAI](https://www.openai.com/) for the GPT-3.5-turbo model.
- [Streamlit](https://streamlit.io/) for the user interface framework.
