<template>
  <div class="container my-4">
    <h2>Citations</h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Content</th>
          <th>Source</th>
          <th>Preference</th>
          <th>Tags</th>
          <th>User ID</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="citation in citations" :key="citation.id">
          <td>{{ citation.id }}</td>
          <td>{{ citation.title }}</td>
          <td>{{ citation.content }}</td>
          <td>{{ citation.source }}</td>
          <td>{{ citation.preference }}</td>
          <td>{{ citation.tags }}</td>
          <td>{{ citation.id_utilisateur }}</td>
          <td>
            <button class="btn btn-danger" @click="deleteCitation(citation.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
    <hr>
    <h2>Add Citation</h2>
    <form @submit.prevent="addCitation">
      <div class="form-group">
        <label for="title">Title:</label>
        <input type="text" class="form-control" id="title" v-model="newCitation.title">
      </div>
      <div class="form-group">
        <label for="content">Content:</label>
        <textarea class="form-control" id="content" v-model="newCitation.content"></textarea>
      </div>
      <div class="form-group">
        <label for="source">Source:</label>
        <input type="text" class="form-control" id="source" v-model="newCitation.source">
      </div>
      <div class="form-group">
        <label for="preference">Preference:</label>
        <input type="number" class="form-control" id="preference" v-model="newCitation.preference">
      </div>
      <div class="form-group">
        <label for="tags">Tags:</label>
        <input type="text" class="form-control" id="tags" v-model="newCitation.tags">
      </div>
      <div class="form-group">
        <label for="user_id">User ID:</label>
        <input type="number" class="form-control" id="user_id" v-model="newCitation.id_utilisateur">
      </div>
      <button type="submit" class="btn btn-primary">Add Citation</button>
    </form>
  </div>
</template>

<script>
import {makeRequest} from "@/request/makeRequest";

export default {
  data() {
    return {
      citations: [],
      newCitation: {
        title: '',
        content: '',
        source: '',
        preference: 0,
        tags: {},
        id_utilisateur: 0
      }
    }
  },
  mounted() {
    // Récupération de toutes les citations depuis l'API
    makeRequest('/pins', 'GET').then((r) => {
      this.citations = r.data;
    }).catch(error => {
        console.log(error);
      });
  },
  methods: {
    /*
      La méthode addCitation est utilisée pour ajouter une nouvelle citation à la base de données. 
      Elle utilise la méthode POST d'Axios pour envoyer la nouvelle citation à l'API. 
      Si la requête est réussie, la nouvelle citation est ajoutée au tableau de citations.
    */
    addCitation() {
      makeRequest('/pins', 'POST', this.newCitation).then((r) => {
        this.citations.push(r.data);
        this.newCitation = {
          title: '',
          content: '',
          source: '',
          preference: 0,
          tags: {},
          id_utilisateur: 0
        };
      }).catch(error => {
        console.log(error);
      });
    },
    /*
      La méthode deleteCitation est utilisée pour supprimer une citation à la base de données. 
      Elle utilise la méthode DELETE d'Axios pour envoyer la demande de suppresion de la citation à l'API. 
      Si la requête est réussie, la citation est retirée au tableau de citations.
    */
    deleteCitation(id) {
      console.log(id)
      makeRequest('/pins/' + id, 'DELETE').then(() => {
        this.citations = this.citations.filter(citation => citation.id !== id);
      }).catch(error => {
        console.log(error);
      });
    }
  }
}
</script>