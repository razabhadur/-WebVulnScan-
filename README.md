# Advanced Web Vulnerability Scanner (AWVS)

AWVS is a web vulnerability scanner designed to detect common vulnerabilities in web applications and servers. It provides an in-depth analysis with additional features to enhance the scanning process.

## Features

- **Version Detection**: Identifies the web server type and version from the HTTP headers.
- **Exposed Directory Detection**: Checks for common exposed directories.
- **SQL Injection Detection**: A basic check for SQL injection vulnerabilities.
- **XSS Detection**: A basic check for Cross-Site Scripting (XSS) vulnerabilities.
- **Summary Reporting**: Generates a summary report at the end of the scan listing all detected vulnerabilities.

## Usage

1. Clone the repository or download the script.
2. Install the required Python libraries:
   ```
   pip install requests
   ```
3. Run the script:
   ```
   python awvs.py
   ```

## Configuration

You can modify the configuration options at the beginning of the script to customize the behavior, such as setting a custom user-agent, adjusting the rate limit delay, or adding more directories to check.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to suggest improvements or add new features.

## License

This project is licensed under the MIT License.

## Disclaimer

This tool is for educational purposes only. Always seek permission before conducting any security testing. Unauthorized scanning is illegal and unethical.
