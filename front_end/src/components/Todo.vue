<template>
    <td>{{ id }}</td>
    <td>{{ title }}</td>
    <td>{{ is_complete }}</td>
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
a {
  color: #42b983;
}
</style>
