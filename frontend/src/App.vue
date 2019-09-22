<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
      <user-name/>
      <logout/>
    </div>
    <router-view/>
  </div>
</template>

<script>
import Logout from './components/Logout'
import UserName from './components/UserName'

export default {
  components: { UserName, Logout }
}
</script>
