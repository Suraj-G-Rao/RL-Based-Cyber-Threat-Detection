# 🔍 Cyber Threat Intelligence Chatbot

A powerful AI-powered chatbot that leverages Neo4j's Cyber Knowledge Graph (CKG) and Groq API to provide intelligent cybersecurity threat intelligence through natural language queries.

## 🚀 Features

- **Natural Language to Cypher Query**: Convert plain English questions into optimized Neo4j Cypher queries
- **Real-time Threat Intelligence**: Query comprehensive cybersecurity database including CVEs, CWEs, CVSS scores, and more
- **Interactive Web Interface**: User-friendly Streamlit-based interface
- **Fast Response**: Powered by Groq's high-performance LLM for quick query generation

## 📋 Prerequisites

- Neo4j Desktop (version 1.6.1 or higher)
- Python 3.8 or higher
- Groq API Key

## 🛠️ Installation & Setup

### Step 1: Setup Neo4j Desktop

1. Download and install Neo4j Desktop from [https://neo4j.com/download/](https://neo4j.com/download/)
2. Create a new project (e.g., "Graph DBMS")
3. Set up a new DBMS with version 4.4.9
4. Start the database server

![Neo4j Desktop Setup](https://via.placeholder.com/800x400/1E293B/FFFFFF?text=Neo4j+Desktop+Setup+Screenshot)

### Step 2: Import Database Dump

1. In your Neo4j Desktop project, click on the database
2. Navigate to the "Files" section
3. Import the `neo4j.dump` file provided in this repository
4. Wait for the import to complete
5. Ensure the database status shows "Active"

![Neo4j Import](https://via.placeholder.com/800x400/1E293B/FFFFFF?text=Neo4j+Database+Import)

### Step 3: Create Python Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure Environment Variables

1. Copy the `.env` file and update it with your credentials:
```env
GROQ_API_KEY="your_actual_groq_api_key"
GOOGLE_API_KEY="your_google_api_key"
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_neo4j_password
```

### Step 6: Run the Application

```bash
streamlit run final.py
```

## 🎯 Usage

1. Open your browser and navigate to `http://localhost:8501`
2. Enter your Groq API Key in the provided field
3. Type your cybersecurity query in natural language (e.g., "Give me the description of the cve with id 39")
4. Click "Generate Cypher Query & Fetch Data"
5. View the generated Cypher query and the results

![Streamlit Application](https://via.placeholder.com/800x600/1E293B/FFFFFF?text=Streamlit+Cyber+Threat+Chatbot+Interface)

## 🔗 Database Schema

The Cyber Knowledge Graph (CKG) contains the following node types:

- **CVE**: Common Vulnerabilities and Exposures
- **CWE**: Common Weakness Enumeration  
- **CVSS_2/3**: Common Vulnerability Scoring System
- **CPE**: Common Platform Enumeration
- **Reference_Data**: External references and sources

## 💡 Example Queries

- "List all threats with high severity"
- "Get the description of CVE with ID 39"
- "Find all CVEs related to buffer overflow"
- "Show vulnerabilities published in 2023"
- "Get CVSS scores for critical vulnerabilities"

## 🔧 Configuration

### Neo4j Connection
- URI: `bolt://localhost:7687`
- Default Username: `neo4j`
- Password: Set during Neo4j setup

### Groq API
- Get your API key from [https://groq.com/](https://groq.com/)
- Supports Llama 3.1 8B Instant model for fast responses

## 🐛 Troubleshooting

### Common Issues

1. **Neo4j Connection Failed**
   - Ensure Neo4j Desktop is running
   - Check if the database is active
   - Verify connection credentials

2. **Groq API Errors**
   - Verify your API key is correct
   - Check your Groq account credits

3. **Import Issues**
   - Ensure the `neo4j.dump` file is not corrupted
   - Check available disk space

## 📝 Project Structure

```
RL Based Cyber Threat Detection/
├── final.py              # Main Streamlit application
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables
├── neo4j.dump           # Database backup file
├── README.md            # This file
└── GraphKer/            # Additional graph processing modules
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Neo4j for the graph database technology
- Groq for the high-performance LLM API
- Streamlit for the web application framework

---

**Note**: Replace the placeholder images in this README with the actual screenshots you have. The current image URLs are placeholders and should be updated with your actual screenshot files.
