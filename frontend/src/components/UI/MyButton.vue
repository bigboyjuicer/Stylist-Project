<template>
  <button>
    <slot>

    </slot>
  </button>
</template>

<script>
export default {
  name: "my-button",
}
</script>

<style scoped>
button {
  margin-top: 15%;
  width: 100%;
  background-color: transparent;
  border: 2px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 40px rgba(8, 7, 16, 0.6);
  color: white;
  padding: 15px 0;
  font-size: 18px;
  font-weight: 600;
  border-radius: 5px;
  cursor: pointer;
}
</style>