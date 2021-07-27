<template>
    <td v-if="is_complete === true" class="complete">{{ title }}</td>
    <td v-else>{{ title }}</td>
    <td>      
      <label class="container">
        <input v-on:click="toggle_complete" v-if="is_complete === true" type="checkbox" checked="checked">
        <input v-on:click="toggle_complete" v-else type="checkbox" >
        <span class="checkmark"></span>
      </label>
    </td>
</template>

<script>
export default {
  name: 'Todo',
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
      //alert(!this.$props.is_complete)
      fetch(`http://localhost:8000/update/${this.$props.id}?new_is_complete=${!this.$props.is_complete}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        }
      })
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
