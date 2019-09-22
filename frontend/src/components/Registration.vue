<template>
  <div>
    <v-card width="500">
      <v-card-title>
        Регистрация
      </v-card-title>
      <v-card-text>
        <v-form v-model="validForm">
          <v-text-field
            label="Имя"
            v-model="firstName"
            required
            clearable
            outlined
          />
          <v-text-field
            label="Фамилия"
            v-model="lastName"
            required
            clearable
            outlined
          />
          <v-text-field
            label="Электронная почта"
            v-model="email"
            required
            :rules="[rules.email]"
            clearable
            outlined
          />
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
          <v-text-field
            label="Повторите пароль"
            v-model="repeatPassword"
            :rules="[rules.equalPasswords]"
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
          @click="registration"
        >
          Зарегистрироваться
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import {userRegistration} from './queries'

export default {
  name: 'Registration',
  data () {
    return {
      validForm: false,
      firstName: '',
      lastName: '',
      email: '',
      login: '',
      password: '',
      repeatPassword: '',
      birthday: '',
      showPasswordFlag: false,
      rules: {
        email: value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          return pattern.test(value) || 'Invalid e-mail.'
        },
        equalPasswords: value => {
          return value === this.password || 'Пароли не совпадают'
        }
      }
    }
  },
  methods: {
    registration () {
      this.$apollo.mutate({
        mutation: userRegistration,
        variables: {
          form: {
            firstName: this.firstName,
            lastName: this.lastName,
            email: this.email,
            login: this.login,
            password: this.password
          }
        }
      }).then(data => {
        console.log(data)
      })
    }
  }
}
</script>

<style scoped>

</style>