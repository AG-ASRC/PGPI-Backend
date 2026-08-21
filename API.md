# API

## Module organizations

### Endpoints exposes

#### GET /organizations
- Description : retourne toutes les organisations.
- Reponse : liste d'organisations.

#### GET /organization/{organization_key}
- Description : retourne une organisation selon son identifiant ou son UUID.
- Parametres :
  - `organization_key` : `int | UUID`
- Reponse : une organisation.

#### POST /organization
- Description : cree une nouvelle organisation.
- Corps de requete : objet `Organization`
- Reponse : organisation creee.

#### PUT /organization/{organization_key}
- Description : met a jour une organisation existante.
- Parametres :
  - `organization_key` : `int | UUID`
- Corps de requete : objet `Organization`
- Reponse : organisation mise a jour.

## Schema de donnees

### Organization

```json
{
  "name": "string",
  "company_name": "string",
  "city": "string",
  "postal_code": "string",
  "street": "string",
  "country": "string",
  "latitude": 0.0,
  "longitude": 0.0
}
```

### OrganizationResponse

```json
{
  "id": 1,
  "uuid": "<uuid>",
  "name": "string",
  "company_name": "string",
  "city": "string",
  "postal_code": "string",
  "street": "string",
  "country": "string",
  "latitude": 0.0,
  "longitude": 0.0
}
```

## Source

- Routeurs : [app/modules/organizations/routes/main.py](app/modules/organizations/routes/main.py)
- Schemas : [app/modules/organizations/schemas/main.py](app/modules/organizations/schemas/main.py)
- Repository : [app/modules/organizations/repositories/main.py](app/modules/organizations/repositories/main.py)
