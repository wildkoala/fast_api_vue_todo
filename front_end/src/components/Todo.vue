<template>
  <div>
      <h3>{{ id }}, {{ title }}, {{ is_complete }}</h3>
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
a {
  color: #42b983;
}
</style>
