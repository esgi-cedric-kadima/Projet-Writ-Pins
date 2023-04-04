<template>
    <div class="container my-4">
      <h2>Users</h2>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Email</th>
            <th>Password</th>
            <th>Username</th>
            <th>Bio</th>
            <th>Image</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id">
            <td>{{ user.id }}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.password }}</td>
            <td>{{ user.username }}</td>
            <td>{{ user.bio }}</td>
            <td><img :src="user.image" alt="User Image" class="img-fluid"></td>
            <td>
              <button class="btn btn-danger" @click="deleteUser(user.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
      <hr>
      <h2>Add User</h2>
      <form @submit.prevent="addUser">
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="text" class="form-control" id="email" v-model="newUser.email">
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" class="form-control" id="password" v-model="newUser.password">
        </div>
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" class="form-control" id="username" v-model="newUser.username">
        </div>
        <div class="form-group">
          <label for="bio">Bio:</label>
          <textarea class="form-control" id="bio" v-model="newUser.bio"></textarea>
        </div>
        <div class="form-group">
          <label for="image">Image:</label>
          <input type="text" class="form-control" id="image" v-model="newUser.image">
        </div>
        <button type="submit" class="btn btn-primary">Add User</button>
      </form>
    </div>
</template>

<script>
import {makeRequest} from "@/request/makeRequest";

export default {
  data() {
    return {
      users: [],
      newUser: {
        email: '',
        password: '',
        username: '',
        bio: '',
        image: ''
      }
    }
  },
  mounted() {
    // Récupération de tous les utilisateurs depuis l'API
    makeRequest(`/users/`, "get").then((res) => {
      this.users = res.data;
    }).catch(error => {
      console.log(error);
    });
  },
  methods: {
    /*
      La méthode addUser est utilisée pour ajouter un nouveal utilisateur à la base de données. 
      Elle utilise la méthode POST d'Axios pour envoyer le nouvel utilisateur à l'API. 
      Si la requête est réussie, le nouvel utilisateur est ajouté au tableau d'utilisateurs.
    */
    addUser() {
      makeRequest(`/users`, "POST", this.newUser).then((res) => {
        // Ajout du user au tableau
        this.users.push(res.data);
        // Réinitialisation du formulaire
        this.newUser = {
          email: '',
          password: '',
          username: '',
          bio: '',
          image: ''
        };
      }).catch(error => {
        console.log(error);
      });
    },
    /*
      La méthode deleteUser est utilisée pour supprimer un utilisateur à la base de données. 
      Elle utilise la méthode DELETE d'Axios pour envoyer la demande de suppresion de l'utilisateur à l'API. 
      Si la requête est réussie, l'utilisateur est retiré au tableau d'utilisateurs.
    */
    deleteUser(id) {
      makeRequest(`/users/${id}`, "DELETE").then(() => {
        this.users = this.users.filter(user => user.id !== id);
      }).catch(error => {
        console.log(error);
      });
    }
  }
}
</script>
