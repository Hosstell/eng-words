<template>
  <div>
    <div v-if="currentUser">
      Вы вошли как {{ currentUser.firstName }} {{ currentUser.lastName }}
    </div>
    <div v-else>
      Вы не залогиненны
    </div>
  </div>
</template>

<script>
import { getCurrentUser } from './queries'

export default {
  name: 'UserName',
  data() {
    return {
      currentUser: null
    }
  },
  apollo: {
    query: {
      query: getCurrentUser,
      update (data) {
        console.log(data.getCurrentUser)
        this.currentUser = data.getCurrentUser
      }
    }
  }
}
</script>

<style scoped>

</style>