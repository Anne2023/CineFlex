# API_Movie

# 1. Introdução

## 1.1 Visão Geral do Projeto
Este projeto tem como objetivo desenvolver uma API para uma locadora de filmes de realidade virtual, permitindo que os usuários acessem e gerenciem informações sobre filmes disponíveis, clientes, transações de locação e devolução, entre outros aspectos relacionados ao funcionamento da locadora.

## 1.2 Objetivos e Propósito do Sistema
O objetivo principal do sistema é fornecer uma plataforma eficiente e fácil de usar para gerenciar o catálogo de filmes de uma locadora, simplificando os processos de locação, devolução e administração de clientes e estoque. 

## 1.3 Benefícios Esperados do Projeto
- Automatização de processos de locação e devolução.
- Melhoria na gestão de estoque de filmes.
- Facilidade de acesso às informações por meio de uma API.
- Otimização do atendimento ao cliente.
- Redução de erros humanos no processo de locação.

# 2. Visão Geral do Sistema

## 2.1 Descrição do Sistema
A API da locadora de filmes permitirá que os usuários realizem operações CRUD (Create, Read, Update, Delete) em diferentes entidades, como filmes, clientes e transações de locação e devolução. A API será projetada para ser robusta, segura e de fácil integração com outros sistemas.

## 2.2 Público-Alvo do Sistema
O público-alvo inclui:
- Proprietários de locadoras de filmes que desejam uma ferramenta eficiente para gerenciar seus negócios.
- Funcionários responsáveis pelo gerenciamento do estoque e pelo atendimento ao cliente.
- Clientes em busca de filmes para locação, que poderão acessar informações atualizadas sobre a disponibilidade de filmes.

## 2.3 Requisitos Funcionais e Não Funcionais
Os requisitos funcionais incluem:
- Cadastro de filmes, clientes e transações
- Pesquisa e consulta de filmes disponíveis
- Registro de locações e devoluções

Os requisitos não funcionais abordam questões como desempenho, segurança e escalabilidade do sistema.

# 3. Arquitetura do Sistema
## 3.1 Explicação da Arquitetura MVC
A arquitetura MVC será utilizada, separando a lógica de negócios (Model), a apresentação (View) e o controle das requisições (Controller).

## 3.2 Papel de Cada Componente
- Model: Representa os dados e a lógica de negócios.
- View: Responsável pela interface de usuário.
- Controller: Gerencia as requisições do cliente e interage com o Model e View.

## 3.3 Uso do Padrão Repository
O padrão Repository será adotado para isolar o código de acesso a dados, permitindo maior flexibilidade e testabilidade.

# 4. Requisitos Funcionais
## 4.1 Lista Detalhada de Funcionalidades
- Cadastro de filmes e clientes
- Consulta de filmes disponíveis
- Registro de locações e devoluções
- Geração de relatórios de transações

## 4.2 Casos de Uso Principais
- Um cliente busca por filmes disponíveis.
- Um funcionário realiza o cadastro de um novo filme.
- Um cliente aluga um filme disponível.

## 4.3 Fluxos de Trabalho do Usuário
Os usuários interagem com o sistema por meio de uma interface de API, realizando operações conforme suas necessidades.

# 5. Requisitos Não Funcionais
## 5.1 Desempenho Esperado do Sistema
A API deve ser capaz de lidar com um grande volume de transações simultâneas de forma eficiente.

## 5.2 Segurança e Autenticação
Será implementado um sistema de autenticação seguro para proteger as operações sensíveis.

## 5.3 Escalabilidade e Manutenibilidade
A arquitetura do sistema será projetada para facilitar a escalabilidade horizontal e a manutenção futura.

# 6. Tecnologias Utilizadas
## 6.1 Linguagens de Programação
- Python

## 6.2 Frameworks
- Flask (para desenvolvimento da API)

## 6.3 Bancos de Dados
- MySQL (para armazenamento de dados)

## 6.4 Ferramentas de Desenvolvimento
- Git (controle de versão)
- Docker (para empacotamento e distribuição)

# 7. Modelo de Dados
## 7.1 Estrutura do Banco de Dados
O banco de dados terá tabelas para filmes, clientes, transações, entre outras entidades relacionadas.

## 7.2 Relacionamentos entre Entidades
As entidades estarão relacionadas de acordo com as necessidades de negócio, como a relação entre locações e clientes.

## 7.3 Esquema de Armazenamento
Será adotado um esquema relacional para o armazenamento dos dados, garantindo integridade e consistência.

# 8. Interfaces do Usuário
## 8.1 Layout e Design das Interfaces
As interfaces serão na forma de endpoints de API, com respostas em formato JSON.

## 8.2 Funcionalidades Específicas de Cada Tela
Cada endpoint oferecerá funcionalidades específicas, como consulta de filmes ou registro de locações.

## 8.3 Fluxos de Interação do Usuário
Os usuários interagem com a API por meio de requisições HTTP, utilizando métodos como GET, POST, PUT e DELETE.

# 9. Arquitetura de Implementação
## 9.1 Organização do Código-Fonte
O código será organizado em módulos separados de acordo com a funcionalidade, seguindo as diretrizes do padrão MVC.

## 9.2 Divisão em Módulos e Componentes
Cada componente do sistema será encapsulado em um módulo independente, facilitando o desenvolvimento e manutenção.

## 9.3 Dependências entre Componentes
Os componentes se comunicarão por meio de interfaces bem definidas, reduzindo o acoplamento e facilitando a manutenção.

# 10. Planejamento de Implantação
## 10.1 Ambientes de Implantação
Serão definidos ambientes de desenvolvimento, teste e produção para implantação da API.

## 10.2 Procedimentos de Implantação
Serão estabelecidos procedimentos para implantação automatizada da aplicação em cada ambiente.

## 10.3 Migração de Dados
Se necessário, serão elaborados scripts de migração para garantir a integridade dos dados ao implantar novas versões da API.

# 11. Gestão de Configuração e Controle de Versão
## 11.1 Políticas de Controle de Versão
Será adotado o modelo de ramificação GitFlow para gerenciamento do código-fonte.

## 11.2 Ramificação do Código-Fonte
Serão mantidas diferentes ramificações para desenvolvimento, teste e produção
