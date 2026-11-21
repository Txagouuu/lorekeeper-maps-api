# Changelog

Todas as mudanças relevantes deste projeto são documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e o projeto utiliza referências diretas aos commits do Git.

## Não lançado

### 2026-11-21

- **Adicionado** endpoint `POST /maps` para criar mapas e persistir o estado inicial no banco.
- **Adicionado** endpoint `GET /maps/{map_id}` com busca primeiro em memória e fallback no banco.
- **Adicionado** roteador WebSocket em `/ws/{map_id}` para receber, validar e transmitir ações em tempo real.
- **Adicionado** middleware CORS na aplicação FastAPI para permitir integrações com clientes externos.
- **Adicionado** instância global do `ConnectionManager` para compartilhar conexões e estados entre os endpoints.
- **Alterado** a configuração da aplicação principal para registrar os roteadores de mapas e WebSockets.
- **Corrigido** imports relativos e absolutos dos módulos para manter a consistência da aplicação.
- **Corrigido** a carga das variáveis de ambiente por meio do `python-dotenv`.
- **Adicionado** este changelog e sua referência no `README`.
- **Adicionado** suporte a `UUID` no `ConnectionManager`, estado de mapas em memória e manipulação de ações WebSocket.
- **Adicionado** operações para mover tokens e adicionar ou remover entidades.
- **Adicionado** transmissão das ações recebidas para todas as conexões de um mapa.
- Referências: `0c07ad7`, `ea92577`, `d418bb5`, `ef1fc7a`, `ff07967`, `a7ddd43`

## Histórico

### 2026-11-18

- **Alterado** os identificadores das ações, mapas, entidades e fundos para utilizar `UUID`.
- **Alterado** o `ConnectionManager` para remover um endpoint FastAPI WebSocket não utilizado e simplificar as responsabilidades da classe.
- **Corrigido** os campos e correções de nomenclatura no esquema de fundos.
- **Adicionado** a configuração inicial do Alembic e a validação de `DATABASE_URL` no ambiente.
- **Adicionado** a primeira migração de banco de dados, criando a tabela `maps` com `id` e `state_data`.
- Referências: `c026e6a`, `c21abad`, `164596f`, `aee6441`, `7556397`

### 2026-11-17

- **Adicionado** o esquema `Action`, com tipo da ação, entidade afetada e payload.
- **Adicionado** o `sessionmaker` e a configuração inicial da sessão do banco de dados.
- **Adicionado** o modelo inicial do banco de dados para mapas.
- **Adicionado** as primeiras entidades de estado da API, incluindo `MapLayers` e `MapState`.
- **Corrigido** a nomenclatura de obstáculos e os campos do estado de mapas.
- **Corrigido** a criação dos identificadores das entidades com `uuid4`.
- **Alterado** as definições dos esquemas para melhorar a estrutura e a composição das camadas.
- **Removido** imports desnecessários dos esquemas de tokens.
- Referências: `2bedc35`, `44dc165`, `d1986ee`, `7e9084e`, `e4e3fed`, `eb4bc14`, `2a1e54b`, `8d7d38e`, `67c00f5`

### 2026-11-16

- **Adicionado** os esquemas para personagens, entidades base, obstáculos e fundos.
- **Adicionado** entidades de fundo globais e tiles individuais.
- **Adicionado** propriedades de bloqueio de movimento e visão aos obstáculos.
- **Corrigido** o campo `asset_id` da entidade base.
- Referências: `5b41393`, `46bc220`, `9716cfd`, `409e14f`, `24e2d7c`

### 2026-11-12

- **Adicionado** o gerenciador inicial de conexões WebSocket para mapas.
- Referência: `568185c`

### 2026-11-11

- **Adicionado** a implementação inicial da API com FastAPI.
- **Adicionado** o suporte inicial a WebSockets.
- Referências: `45d3293`, `20a45d6`
