<template>
  <div>
    <v-card width="500">
      <v-card-title>
        Регистрация
      </v-card-title>
      <v-card-text>
        <v-form v-model="validForm">
          <v-text-field
            label="Логин"
            v-model="login"
            required
            clearable
            outlined
          />
          <v-text-field
            label="Пароль"
            v-model="password"
            required
            clearable
            outlined
            :type="showPasswordFlag ? 'text' : 'password'"
            :append-icon="showPasswordFlag ? 'mdi-eye-off' : 'mdi-eye'"
            @click:append="showPasswordFlag = !showPasswordFlag"
          />
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer/>
        <v-btn
          color="green"
          :disabled="!validForm"
          @click="logIn"
        >
          Войти
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import { Login } from './queries'
import Cookie from 'js-cookie'

export default {
  name: 'Login',
  data () {
    return {
      validForm: false,
      login: '',
      password: '',
      showPasswordFlag: false
    }
  },
  methods: {
    logIn () {
      this.$apollo.mutate({
        mutation: Login,
        variables: {
          login: this.login,
          password: this.password
        }
      }).then(({data}) => {
        Cookie.set('custom-cookie', data.login.cookie)
        window.location.href = '/test'
        // this.$router.push('/test')
      })
    }
  }
}
</script>

<style scoped>

</style>