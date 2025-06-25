# Academia Strong Fitness - Sistema de Gestão

![Screenshot do Sistema](link_para_a_imagem_que_voce_me_mandou.png)
## 📖 Sobre o Projeto

O **Strong Fitness** é um sistema de software completo (Full-Stack) projetado para otimizar a gestão de alunos em uma academia. A aplicação automatiza tarefas financeiras e administrativas, fornece relatórios e oferece uma interface de gerenciamento intuitiva.

---

## 🌟 Principais Funcionalidades

- **👤 Gestão Completa de Alunos (CRUD):** Cadastro, visualização, edição e exclusão de alunos.
- **🔄 Automação de Status:** O sistema altera o status do aluno para `ativo`, `pendente` ou `inativo` com base na data de vencimento da mensalidade, que é calculada automaticamente.
- **⏰ Verificação Diária Automatizada:** Um cron job é executado diariamente para verificar os vencimentos e atualizar os status, garantindo que os dados estejam sempre precisos.
- **🤖 Notificações via WhatsApp:** Integração com a API do CallMeBot para enviar um relatório diário com a lista de alunos pendentes, agilizando o processo de cobrança.
- **🔍 Busca e Filtragem Avançada:** A interface permite buscar alunos por nome ou CPF e visualizar listas separadas para alunos pendentes e inativos.
- **💳 Reativação de Matrícula Simplificada:** Um aluno pendente ou inativo pode ter sua matrícula renovada com um único clique, atualizando seu status e data de vencimento instantaneamente.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Propósito |
|---|---|
| **Python** | Linguagem principal do back-end |
| **Django & Django REST Framework** | Framework para construção da API RESTful |
| **HTML & CSS & JavaScript** | Construção da interface de usuário (front-end) |
| **PostgreSQL** | Banco de dados relacional |
| **Docker & Docker Compose** | Conteinerização da aplicação e dos serviços |
| **Cron** | Agendamento da tarefa de verificação diária |
| **CallMeBot API** | Integração para envio de mensagens via WhatsApp |

---

## 🚀 Como Rodar o Projeto

1.  Clone o repositório: `git clone https://github.com/DanielErick-dev/project-strong-fitness.git`
2.  Navegue até o diretório do projeto.
3.  Crie um arquivo `.env` baseado no `env.example` e preencha com suas credenciais.
4.  Execute `docker-compose up --build` para construir e iniciar os containers.
5.  Acesse `http://localhost:8000` no seu navegador.

---

## 📝 Roadmap e Próximos Passos

- [ ] Melhorar a responsividade do front-end para dispositivos móveis.
- [ ] Criar documentação detalhada da API com Swagger.
- [ ] Realizar o deploy da aplicação em um serviço de nuvem.
