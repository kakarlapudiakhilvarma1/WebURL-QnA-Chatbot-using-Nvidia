# Nvidia NIM Q&A Application - Web URL 🚀

This project allows users to interact with a Q&A system that fetches relevant information from a given web URL. Using Nvidia's API for NLP tasks and Langchain, the app processes the text from a web page, splits it into smaller chunks, and performs a vector-based retrieval to answer questions based on the content. 🤖

## Features ✨
- 🌐 Extracts content from a provided web URL.
- 🔍 Splits the content into smaller chunks for better indexing and retrieval.
- ⚡ Uses Nvidia's embeddings and LLM models to answer questions based on the web content.
- 📑 Displays relevant document snippets to improve answer transparency.
- 🔄 Utilizes FAISS vector store for efficient document retrieval.

## Technologies Used 🛠️
- **Streamlit** for building the interactive web app 🌍.
- **Langchain** for managing document loading, splitting, vector storage, and retrieval 📚.
- **Nvidia API** for advanced embeddings and large language model inference 🧠.
- **FAISS** for high-performance similarity search 🚀.

## Setup Instructions ⚙️

### Prerequisites 📝
1. Python 3.7+
2. Access to Nvidia's API (you will need an Nvidia API key)

### Installation Steps 🛠️

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/nvidia-nim-qa.git
   cd nvidia-nim-qa
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your `.env` file:**
   Create a `.env` file in the project root and add your Nvidia API key as follows:
   ```
   NVIDIA_API_KEY=your_api_key_here
   ```

5. **Run the Streamlit app:**
   After setting up the environment and installing the dependencies, run the app with:
   ```bash
   streamlit run app.py
   ```

### Usage 💡

1. After running the app, navigate to the local Streamlit interface in your browser 🌐.
   
2. **Enter a URL** from which you want to fetch content. The app will extract and index the content for further processing 📄.

3. **Ask a question** related to the content on the webpage by typing it in the provided input box ❓.

4. The application will fetch relevant content from the URL, process it, and provide a response based on the context of the page ⚡.

5. The relevant sections of the webpage used to generate the answer will be displayed for transparency 🔍.

### Example Use Case 📝
- **URL:** [GeeksforGeeks - NLP Overview](https://www.geeksforgeeks.org/natural-language-processing-overview/)
- **Question:** "What is Natural Language Processing?"
- The application will fetch content related to NLP from the webpage and provide an accurate answer based on the content.

### How It Works 🔄

1. The app loads a webpage and extracts its content using `WebBaseLoader` from Langchain 🌍.
2. The content is split into chunks for better document indexing 📑.
3. FAISS is used to create a vector store to enable fast similarity search 🚀.
4. When a user asks a question, the relevant document chunks are retrieved, and Nvidia's LLM (`ChatNVIDIA`) provides an answer based on the context of the fetched content 🧠.

### Example Screenshots 📸
(Insert screenshots of the application interface and output here.)

### Future Improvements 🚀
- Adding support for multiple web URLs at once.
- Enhancing document chunking strategies for better retrieval.
- Implementing user authentication to save personal question histories.

## Acknowledgements 🙏
- Langchain: for document processing and retrieval 📚.
- FAISS: for vector-based similarity search 🔍.
- Nvidia: for providing state-of-the-art embeddings and LLM models 🤖.
