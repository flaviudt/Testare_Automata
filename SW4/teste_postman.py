"""

Adaugare teste la request-urile din Postman

- Vom testa din Postman, Simple Book API: https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md
- Documentatie: https://learning.postman.com/docs/writing-scripts/test-scripts/

- Debugging: https://learning.postman.com/docs/sending-requests/troubleshooting-api-requests/#using-log-statements

- Cum rulam toata colectia de teste?

1. Manual, din Postman

2. Cu command-line-ul Newman:
- documentatie: https://learning.postman.com/docs/collections/using-newman-cli/installing-running-newman/
2.1 Instalam nodejs: https://nodejs.org/en#home-downloadhead
2.2 Instalam newman:
- intr-un git bash: npm install -g newman
2.3 Exportam colectia sub format json pe local
2.4 Rulam testele: newman run <fisierul json care reprezinta colectia>
"""