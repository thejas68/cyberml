from urllib.parse import urlparse

def extract_features(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path

    suspicious_keywords = ['login', 'verify', 'secure', 'update', 'free', 'bank', 'account', 'confirm']

    features = [
        len(url),                                      # URL length
        1 if '@' in url else 0,                        # has @ symbol
        1 if '-' in domain else 0,                     # has hyphen in domain
        url.count('.'),                                # number of dots
        1 if url.startswith('https') else 0,           # uses HTTPS
        domain.count('.') - 1,                         # subdomain count
        1 if any(k in url.lower() for k in suspicious_keywords) else 0,  # suspicious word
        len(domain),                                   # domain length
        1 if '//' in path else 0,                      # double slash in path
        url.count('/'),                                # slash count
    ]
    return features