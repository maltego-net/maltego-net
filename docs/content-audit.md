# README content audit

Source of professional facts: the current README at baseline `bbe1f90` and the user's brief only. Existing SVGs were inspected to understand presentation; no additional career claims have been imported. The two existing metrics below also appear in README image alt text.

## Preservation checklist

- Identity: Rostyslav Zhludko; Hamburg, Germany; infrastructure, systems, automation.
- Builds and operates deployment infrastructure, Linux servers, web applications, and tools that remove repetitive work.
- Leads a technical operations team of **3–4 technicians at Notebook-Pro**; daily planning, onboarding, hardware diagnostics, process automation.
- **Co-built** the network OS deployment platform with Proxmox, Windows Server, PXE/MDT; moved imaging from hands-on USB installs to unattended network deployment. Do not imply sole ownership.
- NEKO: NFT community platform, Twitter OAuth, quests, wallet registration; **10,800+ wallet registrations**, not users, unique wallets, revenue, or a new growth claim.
- Mempoolio: React/Express application with a meme generator, Docker, GitHub Actions.
- terraform-aws-mempoolio: Terraform configuration for VPC, EC2, security groups, S3; infrastructure counterpart of Mempoolio. No production claim.
- k8s-neko: Kubernetes deployment **learning project** around NEKO. Do not label production infrastructure.
- Toolkit: preserve Linux, Proxmox VE, Windows Server, Active Directory, PXE/MDT, Nginx; AWS, Terraform, Docker, Docker Compose, GitHub Actions, GHCR; Python, Bash, TypeScript, Node.js, REST APIs, MCP; React, Next.js, Fastify, PostgreSQL, SQLite, MongoDB, Redis. Kubernetes is supported by the brief and lab description.
- Kityz: self-hosted AI coding-agent coordination on own machines; **in progress**; TypeScript/Fastify orchestrator, WebSocket runners, MCP integration, isolated execution, human approval for consequential actions. No invented repository link or launch claim.
- Operates a multi-user Linux server with Docker services, Nginx routing, SSH key access, firewall rules, separate user environments.
- Website for early-stage rental startup; delivered commercial Next.js/Sanity website for a client.
- University studies in cybersecurity, network design, Linux administration, practical VM labs. No degree-completion claim.
- Languages: English, German, Ukrainian, Russian.

## Recommended semantic structure and copy

Identity remains actual Markdown above the art: `# Rostyslav Zhludko`, followed by `Infrastructure / Systems / Automation` and `Hamburg, Germany`. Illustration is decorative context; it must not be the only source of identity or career information.

### About

I build and operate deployment infrastructure, Linux servers, web applications, and tools that remove repetitive work. My interests meet where software has to run reliably on real hardware.

### Experience

I lead **3–4 technicians** at **Notebook-Pro** across daily planning, onboarding, hardware diagnostics, and process automation. I co-built our network OS deployment platform with **Proxmox, Windows Server, and PXE/MDT**, moving device imaging from hands-on USB installs to unattended network deployment.

I also built a website for an early-stage rental startup and delivered a commercial **Next.js / Sanity** website for a client.

### Selected work

Use four stacked, linked project names with short text descriptions. Keep long repository slugs out of unbreakable inline code or narrow table cells. Optional two-digit monospace indices can provide the editorial rhythm without extra ornaments.

- **AWS infrastructure** → terraform-aws-mempoolio: Terraform configuration for VPC, EC2, security groups, and S3, supporting Mempoolio.
- **NEKO** → neko: NFT community platform with Twitter OAuth, quests, and wallet registration. 10,800+ wallet registrations.
- **Mempoolio** → mempoolio: React and Express application with a meme generator, Docker, and GitHub Actions.
- **Kubernetes lab** → k8s-neko: A learning project exploring Kubernetes deployment for NEKO.

### Toolkit

Use four short paragraphs or list items, one domain per line. The original table is valid but less forgiving at 360 px.

### Currently building

**Kityz — in progress.** A self-hosted platform for coordinating AI coding agents on my own machines. I'm working on a TypeScript/Fastify orchestrator, WebSocket runners, and MCP integration, with isolated execution and human approval for consequential actions.

I also run a **multi-user Linux server** with Docker services, Nginx routing, SSH key access, firewall rules, and separate user environments.

Keep education foundations and spoken languages in a short `details` disclosure after this section, or a compact Background paragraph. The disclosure must retain text outside an image.

### Footer

Repeat LinkedIn and email links as readable text; a small classical ornament may be decorative with empty alt text.

## Link checks

On 2026-10-27, `gh repo view OWNER/REPO --json url,name` successfully returned each of the four exact existing repository URLs:

- https://github.com/maltego-net/terraform-aws-mempoolio
- https://github.com/maltego-net/neko
- https://github.com/maltego-net/mempoolio
- https://github.com/maltego-net/k8s-neko

Preserve the existing navigation and contact targets verbatim:

- `https://github.com/maltego-net?tab=repositories` — syntactically valid HTTPS URL; no separate browser check performed.
- `https://www.linkedin.com/in/rostickzlud/` — syntactically valid HTTPS URL; account ownership and page availability were not independently verified.
- `mailto:rostyslav@zhludko.dev` — syntactically valid mailto link; mailbox deliverability was not tested and no message was sent.

The initial sandboxed GitHub CLI requests failed because of the sandbox proxy. Read-only reruns with approved network access succeeded. Repository existence is verified; project descriptions remain sourced solely from the original README.
