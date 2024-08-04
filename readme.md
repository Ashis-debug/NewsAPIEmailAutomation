# Tesla News Emailer

This project fetches the latest Tesla news articles and sends them via email in a neatly formatted HTML format. It uses the [News API](https://newsapi.org/) to gather news articles about Tesla and sends an email using SMTP with Gmail.

## Features

- Fetches real-time news articles about Tesla.
- Sends an email with the latest news in a structured HTML format.
- Uses SMTP with SSL for secure email delivery.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.12
- [News API Key](https://newsapi.org/register) (for fetching news articles)
- Gmail account (for sending emails)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://[github.com/your-username/NewsAPIEmailAutomation.git](https://github.com/Ashis-debug/NewsAPIEmailAutomation.git)
   cd NewsAPIEmailAutomation
   ```

2. **Install the required packages:**

   ```bash
   pip install requests
   ```

3. **Configure Email Credentials:**

   Edit the `main.py` file and update the following variables with your credentials:

   ```python
   username = "your-email@gmail.com"
   password = "your-app-password"
   receiver = "receiver-email@gmail.com"
   ```

   **Note:** It's recommended to use an [App Password](https://support.google.com/accounts/answer/185833?hl=en) for Gmail instead of your regular password.

4. **Set the News API Key:**

   Replace the `API_KEY` variable in the `main.py` file with your News API key:

   ```python
   API_KEY = "your-news-api-key"
   ```

## Usage

Run the script to fetch the latest Tesla news and send an email:

```bash
python main.py
```

The email will contain the latest news articles with titles, descriptions, and links to read more. The HTML formatting ensures a clean presentation in your inbox.

## Customization

You can customize the query and sort options by modifying the `params` dictionary in the `main.py` file:

```python
params = {
    "apiKey": API_KEY,
    "language": 'en',
    "sortBy": "publishedAt",
    "q": "tesla"
}
```

- `language`: Specify the language of the articles (e.g., `'en'` for English).
- `sortBy`: Change the sorting order (options include `'relevancy'`, `'popularity'`, `'publishedAt'`).
- `q`: Change the query to fetch news about different topics.

## Troubleshooting

### Common Issues:

- **Authentication Failed:** Ensure your Gmail credentials are correct and that you've enabled [less secure apps](https://myaccount.google.com/lesssecureapps) or used an App Password.
- **News API Error:** Double-check your API key and verify that you haven't exceeded the API rate limit.

### Debugging Tips:

- Print the response from the News API to check for errors:

- Check the SMTP connection for any SSL-related issues.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.

---

### Contact

For questions or support, please contact [Ashis Tripathy](mailto:ashistripathy897@gmail.com).

```

### Explanation:

1. **Project Overview**:
   - Brief introduction to the project, describing its functionality and purpose.

2. **Features**:
   - Highlights the key features of the project, such as fetching news and sending formatted emails.

3. **Prerequisites**:
   - Lists the requirements needed before setting up the project.

4. **Installation**:
   - Step-by-step guide on how to install and configure the project.

5. **Usage**:
   - Instructions on how to run the script to send the news email.

6. **Customization**:
   - Information on how to modify the query parameters to fetch different news.

7. **Troubleshooting**:
   - Provides common issues and tips to help debug problems.

8. **License and Contributing**:
   - Details about the license and how others can contribute to the project.

9. **Contact**:
   - Provides contact information for support and inquiries.

Feel free to customize this README to better fit your project's specific details and style preferences.
