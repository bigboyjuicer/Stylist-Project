<template>
  <div class="dialog" v-if="show === true" @click.stop="hideDialog">
    <div @click.stop class="dialog_content">
      <slot>
      </slot>
    </div>
  </div>
</template>

<script>

export default {


  name: "my-dialog",
  components: {
  },

  props: {
    show: {
      type: Boolean,
      default: false,
    }
  },
  methods: {
    hideDialog() {
      this.$emit('update:show', false)
    }
  }
}
</script>

<style scoped lang="scss">

.dialog {
  z-index: 1;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);

}

</style>