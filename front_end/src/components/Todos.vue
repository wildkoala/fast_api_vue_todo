<template>
  <div class="hello">
      <h1>TODOS BOX</h1>
      <ul>
        <li v-for="todo in api_todos"  v-bind:key="todo.id">
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
      api_todos: [{ id: 1, title: 'First', is_complete: false }, { id: 2, title: 'Bar', is_complete: false }]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
