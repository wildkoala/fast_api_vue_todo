<template>
    <!-- <td>{{ id }}</td> -->
    <td v-if="is_complete === true" class="complete">{{ title }}</td>
    <td v-else>{{ title }}</td>
    <td>      
      <label class="container">
        <input v-if="is_complete === true" type="checkbox" checked="checked">
        <input v-else type="checkbox" >
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
