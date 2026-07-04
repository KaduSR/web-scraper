"""Web Scraper"""
import argparse, csv
def scrape(url: str, output: str):
    print(f"Coletando: {url}")
    dados = [{"titulo":"Ex 1","descricao":"Desc","data":"2026-01-15"},{"titulo":"Ex 2","descricao":"Desc 2","data":"2026-02-20"}]
    with open(output, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["titulo","descricao","data"])
        w.writeheader(); w.writerows(dados)
    print(f"{len(dados)} registros salvos em {output}")
if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--url", required=True); p.add_argument("--output", default="dados.csv")
    args = p.parse_args(); scrape(args.url, args.output)
