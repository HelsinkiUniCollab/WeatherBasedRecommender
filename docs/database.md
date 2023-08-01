# Databases

We use two databases for this project: **development** and **production**.

- **Development Database:**
  - Connection String: `mongodb+srv://helsinkiunicollab:<password>@development.qebxr8j.mongodb.net/?retryWrites=true&w=majority`

  Development database has two collections: development and test. 
  Development collection is used When Flask App is run with:
```bash 
  $poetry run invoke start
```
  Test collection is used When Flask App is run with:
```bash 
  $poetry run invoke test
```

- **Production Database:**
  - Connection String: `mongodb+srv://helsinkiunicollab:<password>@production.djrvu6z.mongodb.net/?retryWrites=true&w=majority`

## Accessing the Databases

To access the databases, you need credentials. The username for both databases is `helsinkiunicollab`. Please ask a team member for the respective passwords.

To securely store the passwords, add them to your environment variables by creating a `.env` file in the project root directory. 

## Cluster and IP Restrictions

Our MongoDB clusters are hosted in Stockholm, ensuring compliance with data protection regulations within the EU area.

There are no IP restrictions on the clusters, so they can be accessed from any IP address.

## MongoDB Atlas Admin Access

For administrative access to each database on MongoDB Atlas, an account connected to Pia's email is used. Please reach out to Pia to obtain the necessary credentials if needed. These credentials are not the same the databases use.

## PyMongo

We use PyMongo, the official MongoDB driver for Python, to establish connections and interact with the MongoDB databases in our Flask application.

For more details on PyMongo and how it is used in the project, refer to the relevant code and comments within the codebase.
