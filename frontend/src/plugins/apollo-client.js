import { ApolloClient } from "apollo-client";
import { HttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";
import { ApolloLink, concat } from "apollo-link";
import Cookie from "js-cookie";

const opts = {
  // Для разработки используем локальный сервер на другом порту
  uri: "http://localhost:8000/api_v1/",
  credentials: "include"
};
const httpLink = new HttpLink(opts);

const csrfMiddleware = new ApolloLink((operation, forward) => {
  console.log('cookie', Cookie.get("csrftoken"))
  operation.setContext({
    headers: {
      "X-CSRFToken": Cookie.get("csrftoken") || null
    }
  })
  return forward(operation)
})

const link = concat(csrfMiddleware, httpLink);

// Create the apollo client
const apolloClient = new ApolloClient({
  link: link,
  cache: new InMemoryCache()
});

export default apolloClient;
