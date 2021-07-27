<template>
  <div class="hello">
      <h1>TODOS BOX</h1>

      <table id="customers">
        <tr>
          <th>ID</th>
          <th>Title</th>
          <th>Is Complete</th>
        </tr>
        <tr v-for="todo in api_todos" v-bind:key="todo.id">
            <Todo v-bind:="todo" />
        </tr>
      </table>
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

table {
  margin-left: auto;
  margin-right: auto;
}

ul {
  list-style-type: none;
}

#customers {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  text-align: center;
  width: 80%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
