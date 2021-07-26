<template>
  <div class="todo-box">
      <h1>TODO: {{ title }}</h1>
  </div>
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
