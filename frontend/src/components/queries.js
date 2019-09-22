import gql from 'graphql-tag'

const getAllUsers = gql`
query{
  allUsers {
    id
    lastName
  }
}`

const userRegistration = gql`
mutation ($form: UserRegistrationType) {
  userRegistration(form:$form) {
    result
  }
}`

const Login = gql`
mutation ($login: String!, $password: String!) {
  login(login: $login, password:$password) {
    cookie
  }
}`

const Logout = gql`
mutation {
  logout {
    result
  }
}`

const getCurrentUser = gql`
query {
  getCurrentUser {
    id
    firstName
    lastName
  }
}`

export {getAllUsers, userRegistration, Login, Logout, getCurrentUser}