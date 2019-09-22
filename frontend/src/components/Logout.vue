<template>
  <div>
    <v-btn @click="logout">
      Выход
    </v-btn>
  </div>
</template>

<script>
import { Logout } from './queries'
import Cookie from 'js-cookie'

export default {
  name: 'Logout',
  methods: {
    logout () {
      this.$apollo.mutate({
        mutation: Logout
      }).then(({ data }) => {
        Cookie.remove('custom-cookie')
        window.location.href = '/login'
      })
    }
  }
}
</script>

<style scoped>

</style>