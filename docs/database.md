# Databases

Mongo DB Atlas is used for storing basic information (name, longitude, latitude, categories and accessibility) about the Point of Interests (POI's). If database is lost, the POI's are recovered automatically from a static JSON file. 

There are two Atlas accounts in use, **development** and **production**. Refer to a team member for the password, connection strings for the accounts are:

- **Development**
  - `mongodb+srv://helsinkiunicollab:<password>@development.qebxr8j.mongodb.net/?retryWrites=true&w=majority`

- **Production**
  - `mongodb+srv://helsinkiunicollab:<password>@production.djrvu6z.mongodb.net/?retryWrites=true&w=majority`

## Accessing the Databases

To access the databases, you need credentials. The username for both databases is `helsinkiunicollab`. Please ask a team member for the respective passwords.

To securely store the passwords, add them to as environment variable `DEVELOPMENT_DB_URI` in an `.env` file in the project root directory. You can do that using the script, instructions given in the [README.md](/README.md).

## Cluster and IP Restrictions

Our MongoDB clusters are hosted in Stockholm, ensuring compliance with data protection regulations within the EU area.

There are no IP restrictions on the clusters, so they can be accessed from any IP address.

## MongoDB Atlas Admin Access

For administrative access to each database on MongoDB Atlas an email account is needed. Reach out to a team member to obtain the necessary credentials. These credentials are not the same the databases use.

## PyMongo

We use PyMongo, the official MongoDB driver for Python, to establish connections and interact with the MongoDB databases in our Flask application.

For more details on PyMongo and how it is used in the project, refer to the relevant code and comments within the codebase.
