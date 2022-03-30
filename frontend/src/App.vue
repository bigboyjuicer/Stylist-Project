<template>
  <div id="wrapper">
    <router-view v-slot="{ Component, route }">
      <transition :name="route.meta.transition">
        <component :is="Component"/>
      </transition>
    </router-view>
  </div>
</template>

<script>
export default {

}


</script>

<style>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

.slide-left-enter-active,
.slide-left-leave-active {
  transition: all 0.75s ease-in-out;
}


.slide-left-enter-to {
  position: absolute;
  right: 0;
}


.slide-left-enter-from {
  position: absolute;
  right: -100%;
}


.slide-left-leave-to {
  position: absolute;
  left: -30%;
}


.slide-left-leave-from {
  position: absolute;
  left: 0;
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.75s ease-in-out;
}


.slide-enter-to {
  position: absolute;
  left: 0;
}


.slide-enter-from {
  position: absolute;
  left: -100%;
}


.slide-leave-to {
  position: absolute;
  right: -30%;
}


.slide-leave-from {
  position: absolute;
  right: 0;
}
</style>
