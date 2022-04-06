<template>
  <div id="wrapper">
    <router-view/>
  </div>
</template>

<script>

export default {

}


</script>

<style>
::-webkit-scrollbar {
  width: 16px;
}

::-webkit-scrollbar-track{
  background-color: #EBEBEB;
}

::-webkit-scrollbar-thumb {
  border-radius: 100px;
  border: 5px solid transparent;
  background-clip: padding-box;
  background-color: gray;
}

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

/* Set core body defaults */
body {
  min-height: 100vh;
  text-rendering: optimizeSpeed;
}

/* Make images easier to work with */


/* Inherit fonts for inputs and buttons */
input,
button,
textarea,
select {
  font: inherit;
}
</style>
