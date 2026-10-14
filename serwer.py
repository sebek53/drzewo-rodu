# Serwer aplikacji drzewa: pliki z tego katalogu + /api/odczyt (odczyt aktu przez Claude).
# Klucz: ANTHROPIC_API_KEY w pliku .env obok tego skryptu. Uruchom: python serwer.py  ->  http://localhost:8770/drzewo.html
import http.server, json, os, re, sys, base64

DIR = os.path.dirname(os.path.abspath(__file__))
env = os.path.join(DIR, '.env')
if os.path.exists(env):
    for l in open(env, encoding='utf-8'):
        m = re.match(r'\s*([A-Z_]+)\s*=\s*"?([^"\n]*)"?', l)
        if m: os.environ.setdefault(m.group(1), m.group(2).strip())

PROMPT = """To jest skan polskiego aktu metrykalnego (XVIII–XX w., łacina, polski lub rosyjski, pismo odręczne).
Odczytaj go i zwróć WYŁĄCZNIE obiekt JSON (bez komentarzy) o polach:
{"transkrypcja": "tekst aktu w oryginalnym języku", "tlumaczenie": "przekład na polski",
 "typ": "chrzest|slub|zgon|inny", "numer": "", "data": "dzień miesiąc rok np. 9 MAY 1784 (format GEDCOM, angielskie skróty miesięcy)", "miejscowosc": "",
 "osoba": {"imie": "", "nazwisko": "", "wiek": ""},
 "rodzice": {"ojciec": "", "matka": ""}, "malzonek": "", "chrzestni_swiadkowie": [""],
 "uwagi": "niepewne odczyty oznacz (?)"}
Puste pola zostaw jako "". Nie zgaduj – lepiej puste niż zmyślone."""

def odczyt(data_url, key=None):
    import anthropic
    mt, b64 = re.match(r'data:([^;]+);base64,(.*)', data_url, re.S).groups()
    client = anthropic.Anthropic(api_key=key) if key else anthropic.Anthropic()
    r = client.beta.messages.create(
        model='claude-opus-5-5', max_tokens=16000,
        output_config={'effort': 'medium'},
        betas=['server-side-fallback-2026-07-01'], extra_body={'fallbacks': 'default'},
        messages=[{'role': 'user', 'content': [
            {'type': 'image', 'source': {'type': 'base64', 'media_type': mt, 'data': b64}},
            {'type': 'text', 'text': PROMPT}]}])
    if r.stop_reason == 'refusal': raise RuntimeError('Model odmówił odczytu.')
    txt = ''.join(b.text for b in r.content if b.type == 'text')
    m = re.search(r'\{.*\}', txt, re.S)
    return json.loads(m.group(0)) if m else {'transkrypcja': txt}

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s, *a, **k): super().__init__(*a, directory=DIR, **k)
    def do_POST(s):
        if s.path != '/api/odczyt': return s.send_error(404)
        try:
            body = json.loads(s.rfile.read(int(s.headers['Content-Length'])))
            key = (s.headers.get('X-Api-Key') or '').strip()  # klucz z ustawień aplikacji (przeglądarka) ma pierwszeństwo przed .env
            if not key and not os.environ.get('ANTHROPIC_API_KEY'): raise RuntimeError('Brak klucza: wpisz go w aplikacji (☰ → Klucz Claude) albo w pliku .env')
            out, code = odczyt(body['image'], key or None), 200
        except Exception as e:
            msg = str(e)
            if 'authentication_error' in msg: msg = 'Nieprawidłowy klucz API – sprawdź go w aplikacji (☰ → Klucz Claude).'
            elif 'credit balance' in msg: msg = 'Brak środków na koncie Anthropic – doładuj je na console.anthropic.com.'
            out, code = {'blad': msg}, 500
        d = json.dumps(out, ensure_ascii=False).encode()
        s.send_response(code); s.send_header('Content-Type', 'application/json; charset=utf-8'); s.send_header('Content-Length', len(d)); s.end_headers(); s.wfile.write(d)

if __name__ == '__main__':
    import webbrowser, threading
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8770
    url = f'http://localhost:{port}/drzewo.html'
    import socket
    if socket.socket().connect_ex(('127.0.0.1', port)) == 0:  # serwer już działa (drugie uruchomienie) – tylko otwórz przeglądarkę
        webbrowser.open(url); sys.exit()
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', port), H)
    print(f'Drzewo rodu działa: {url}')
    print('Nie zamykaj tego okna – zamknięcie wyłącza aplikację.')
    threading.Timer(1, lambda: webbrowser.open(url)).start()
    srv.serve_forever()
