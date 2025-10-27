import time, sys
from urllib import request, parse

url = 'http://127.0.0.1:5000/sign-up'
data = parse.urlencode({
    'email': 'testuser+copilot@example.com',
    'firstName': 'CopilotTest',
    'password1': 'password123',
    'password2': 'password123'
}).encode()

for i in range(12):
    try:
        req = request.Request(url, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        with request.urlopen(req, timeout=5) as resp:
            print('STATUS', resp.getcode())
            body = resp.read().decode(errors='replace')
            print(body[:2000])
        break
    except Exception as e:
        print(f'Attempt {i} failed: {e}')
        time.sleep(0.7)
else:
    print('Server did not respond after retries')
    sys.exit(1)
