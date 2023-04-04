<template>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
  <img alt="Vue logo" src="./assets/logo.png">
  <Citations/>
  <Users/>
</template>
<script>
import Citations from './components/CitationsComponent.vue'
import Users from './components/UsersComponent.vue'

export default {
  name: 'App',
  components: {
    Citations,
    Users
  }
}
</script>
