import requests
import time

# Configuration Options
USER_AGENT = 'Mozilla/5.0'
RATE_LIMIT_DELAY = 2  # Delay in seconds between requests
COMMON_DIRECTORIES = ['admin', 'backup', 'uploads', 'images', 'db']
SQL_INJECTION_PAYLOAD = "' OR '1'='1"
XSS_PAYLOAD = '<script>alert(\"XSS\")</script>'
VULNERABILITIES = []

def scan_target(url):
    headers = {
        'User-Agent': USER_AGENT
    }
    
    # Version Detection
    response = requests.get(url, headers=headers)
    server_header = response.headers.get('Server', 'Unknown')
    print(f'Web Server Detected: {server_header}')
    
    # Basic Vulnerability Scanning for exposed directories
    for directory in COMMON_DIRECTORIES:
        time.sleep(RATE_LIMIT_DELAY)  # Rate limiting
        dir_url = f'{url}/{directory}/'
        response = requests.get(dir_url, headers=headers)
        if response.status_code == 200:
            print(f'Exposed Directory Found: {dir_url}')
            VULNERABILITIES.append(f'Exposed Directory: {dir_url}')
    
    # SQL Injection Detection
    sql_url = f'{url}?id={SQL_INJECTION_PAYLOAD}'
    response = requests.get(sql_url, headers=headers)
    if 'SQL syntax' in response.text or 'mysql_fetch' in response.text:
        print(f'SQL Injection Vulnerability Detected: {sql_url}')
        VULNERABILITIES.append(f'SQL Injection: {sql_url}')
    
    # XSS Detection
    xss_url = f'{url}?q={XSS_PAYLOAD}'
    response = requests.get(xss_url, headers=headers)
    if XSS_PAYLOAD in response.text:
        print(f'XSS Vulnerability Detected: {xss_url}')
        VULNERABILITIES.append(f'XSS: {xss_url}')
    
    # Summary Report
    print('\nSummary Report:')
    print('================')
    for vulnerability in VULNERABILITIES:
        print(vulnerability)

if __name__ == '__main__':
    target_url = input('Enter the target URL (e.g., http://example.com): ')
    scan_target(target_url)
