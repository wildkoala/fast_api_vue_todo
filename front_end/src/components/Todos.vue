<template>
  <div class="hello">
      <h1>TODOS BOX</h1>
      <ul class="todos-box">  
        <li v-for="todo in api_todos" v-bind:key="todo.id">
            <Todo v-bind:="todo" />
        </li>
      </ul>
  </div>
</template>

<script>
import Todo from './Todo.vue'

export default {
  name: 'Todos',
  components: {
    Todo
  },
  data: function () {
    return {
      api_todos: [
        { "id": 1, "title": "Foo", "is_complete": false }, 
        { "id": 2, "title": "Bar", "is_complete": false }
        ]
    }
  },
  mounted() {
      fetch('http://localhost:8000/todos/')
        .then((resp) => resp.json())
        .then(data => this.api_todos = data)
        .catch(err => console.log(err.message))
  }
  /**/
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.todos-box {
  display: flex;
  flex-direction: column;
}

ul {
  list-style-type: none;
}
</style>
