<template>
    <td v-if="todo_is_complete === true" class="complete">{{ todo_title }}</td>
    <td v-else>{{ todo_title }}</td>
    <td>      
      <label class="container">
        <input v-on:click="toggle_complete" v-if="todo_is_complete === true" type="checkbox" checked="checked">
        <input v-on:click="toggle_complete" v-else type="checkbox" >
        <span class="checkmark"></span>
      </label>
    </td>
</template>

<script>
export default {
  name: 'Todo',
  data: function() {
    return {
      todo_id: this.$props.id,
      todo_title: this.$props.title,
      todo_is_complete: this.$props.is_complete
    }
  },
  props: {
    id: {
        type: Number,
    },
    title: {
        type: String,
    },
    is_complete: {
        type: Boolean,
    }
  },
  methods: {
    toggle_complete: function() {
      fetch(`http://localhost:8000/update/${this.$data.todo_id}?new_is_complete=${!this.$data.todo_is_complete}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then((resp) => resp.json())
        .then(data => this.$data.todo_is_complete = data.is_complete)
        .catch(err => console.log(err.message))
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  color: #42b983;
}

.complete {
  text-decoration: line-through;
}

</style>
