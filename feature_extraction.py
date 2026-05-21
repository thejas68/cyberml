from urllib.parse import urlparse

def extract_features(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path

    suspicious_keywords = ['login', 'verify', 'secure', 'update', 'free', 'bank', 'account', 'confirm']

    features = [
        len(url),
        1 if '@' in url else 0,
        1 if '-' in domain else 0,
        url.count('.'),
        1 if url.startswith('https') else 0,
        domain.count('.') - 1,
        1 if any(k in url.lower() for k in suspicious_keywords) else 0,
        len(domain),
        1 if '//' in path else 0,
        url.count('/'),
    ]
    return features