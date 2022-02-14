<template>
  <div class="greetings">
    <h1>
      ¡Bienvenido&nbsp; <span> {{ username }} </span>!
    </h1>
    <h2 v-if= username>
      Ahora puedes dirigirte a la sección <span> Buscar vuelos </span> y realizar tus reservaciones.
    </h2>
    <h2 v-else>
      Regístrate para comenzar a reservar tus vuelos.
    </h2>
  </div>
</template>

<script>
export default {
  name: "Home",
  data: function () {
    return {
      username: localStorage.getItem("username") || null,
    };
  },
};
</script>

<style>
.greetings {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
}
.greetings h1 {
  font-size: 35px;
  color: #283747;
}
.greetings h2 {
  font-size: 25px;
  color: #283747;
  margin: 10px;
}
.greetings span {
  color: rgb(41, 11, 230);
  font-weight: bold;
}
</style>