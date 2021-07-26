<template>
  <div class="hello">
      <h1>TODOS BOX</h1>
      <ul>
        <li v-for="item in items"  v-bind:key="item.id">
            {{ item.message }}
        </li>
      </ul>
  </div>
</template>

<script>
export default {
  name: 'Todos',
  props: {
    msg: String
  },
  data: function () {
    return {
      items: [{ id: 1, message: 'Foo' }, { id: 2, message: 'Bar' }]
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
