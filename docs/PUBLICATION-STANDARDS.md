# Public Portfolio Publication Standards

These standards apply to material published in this repository.

## 1. Ownership and permission

- Publish only material Indigo Prodigy or UniversoulCo owns or is authorized to share.
- Identify collaborators and third-party assets where appropriate.
- Do not upload samples, artwork, code, datasets, or documentation with unclear rights.
- Do not imply ownership of work created by another person or organization.

## 2. Confidentiality

Never publish:

- API keys, tokens, passwords, private keys, recovery codes, or environment files.
- Personal identity documents, private contact details, financial records, or health records.
- Private business records, contracts, legal drafts, tax records, or entity formation documents.
- Unreleased music, masters, stems, publishing data, private demos, or confidential deal terms.
- Private source code, database exports, production configuration, or internal agent instructions.

## 3. Technical safety

- Use synthetic or deliberately public sample data in demonstrations.
- Keep secrets out of source control; use environment variables and approved secret stores in actual deployments.
- Review dependencies, licenses, and external services before publishing.
- Do not expose internal endpoints, infrastructure diagrams, or operational details that create avoidable security risk.

## 4. Review before publication

For every new public project or material change, confirm:

1. The content is intended for public release.
2. Ownership and third-party permissions are clear.
3. No secrets or sensitive personal/business data are present.
4. Links and demonstrations do not expose private systems.
5. The description accurately states what is built and what remains planned.

## 5. Corrections and incident response

If sensitive material is accidentally published, treat it as exposed. Revoke or rotate affected credentials immediately and assess the exposure. Removing a file from the latest commit does not erase it from Git history or guarantee that copies are gone.

For suspected vulnerabilities, do not publish exploit details or sensitive information in public issues. Use GitHub's private vulnerability reporting if it is enabled for this repository.

---

These standards are operational guidance for this public portfolio. They do not replace legal, security, or intellectual-property review where required.
