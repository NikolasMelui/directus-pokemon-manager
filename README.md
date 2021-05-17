# DIRECTUS-POKEMON-MANAGER

Simple `server` application using directus as backoffice (with python realizations of `client` and `loader` standalone applications).

## Server

### Stores the data about the pokemons

> The server application is using the `sqlite3` so there is no need to install any additional DBs

Install the application:

```bash
  npm i
```

Copy the `.env.example` file (and configure the application):

```bash
  cp .env.example .env
```

Run the application:

```bash
  npx directus start
```

#### Credentials

- email: admin@example.com
- password: 9XcqYED1_5Pj
- secret_token: sUperSEcreTtoKEn6662

There is a special custom endpoint `/custom/know-more/:name` which gets pockemon name fom the request, find it in the directus, go by the directus url to the `pokeAPI` for additional data about the pokemon and responde with it. Try it free now :D

> There are 10 pokemons now in the directus, you can load more using the `loader` python application

---

## Loader

### Loads the data from `pokeAPI` (`name` and `url` only) to the directus

Copy the `.env.example` file (and configure the application):

```bash
  cp .env.example .env
```

Run the application:

```bash
  python loader/loader.py
```

---

## Client

### Gets the data from the directus (and prints it)

Copy the `.env.example` file (and configure the application):

```bash
  cp .env.example .env
```

Run the application:

```bash
  python client/client.py
```

Implemented methods:

| Method      | Description                                                               |
| ----------- | ------------------------------------------------------------------------- |
| `get_all`   | information about all existing pokemons                                   |
| `get_by_id` | information about the current pokemon (by id)                             |
| `know_more` | additional information about the current pokemon (by name) from `pokeAPI` |
