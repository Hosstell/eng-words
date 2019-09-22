<template>
  <div>
    <v-card width="400">
      <v-card-title>
        Cat
      </v-card-title>
      <v-card-text>
        <v-card>
          <v-list>
            <v-list-item-group color="primary">
              <v-list-item>
                  Как дела
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
  import {getAllUsers} from './queries'

  export default {
    name: "Test",
    apollo: {
      query: {
        query: getAllUsers,
        update(data) {
          console.log(data)
        }
      }
    }
  }
</script>

<style scoped>

</style>