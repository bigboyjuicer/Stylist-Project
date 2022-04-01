<template>
  <div id="wrapper">
    <router-view/> <!--v-slot="{ Component, route }">
      <transition :name="route.meta.transition">
        <component :is="Component"/>
      </transition>
    </router-view>-->
  </div>
</template>

<script>

export default {

}


</script>

<style>
/* Box sizing rules */
*,
*::before,
*::after {
  box-sizing: border-box;
}

/* Remove default margin */
body,
h1,
h2,
h3,
h4,
p,
figure,
blockquote,
dl,
dd {
  margin: 0;
}

/* Remove list styles on ul, ol elements with a list role, which suggests default styling will be removed */
ul[role='list'],
ol[role='list'] {
  list-style: none;
}

/* Set core root defaults */
html:focus-within {
  scroll-behavior: smooth;
}

/* Set core body defaults */
body {
  min-height: 100vh;
  text-rendering: optimizeSpeed;
  line-height: 1.5;
}

/* A elements that don't have a class get default styles */
a:not([class]) {
  text-decoration-skip-ink: auto;
}

/* Make images easier to work with */
img,
picture {
  max-width: 100%;
  display: block;
}

/* Inherit fonts for inputs and buttons */
input,
button,
textarea,
select {
  font: inherit;
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
