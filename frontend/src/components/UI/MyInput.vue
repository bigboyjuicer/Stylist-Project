<template>
  <input class="input" @input="updateInput" :value="modelValue">
</template>

<script>
export default {
  name: "my-input",
  props: {
    modelValue: [String, Number]
  },
  methods: {
    updateInput(event){
      this.$emit('update:modelValue', event.target.value)
    }
  }
}
</script>

<style scoped>
.input {
  display: block;
  height: 50px;
  width: 100%;
  background-color: rgba(255, 255, 255, 0.15);
  border-radius: 5px;
  padding: 0 10px;
  margin-top: 15px;
  font-size: 14px;
  font-weight: 300;
}
</style>