<template>
  <!-- Modal -->
  <div
    class="modal fade"
    id="exampleModalTwo"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Iniciar Sesión</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <form v-on:submit.prevent="processLogInUser">
          <div class="modal-body">
            <div class="mb-3">
              <label for="formGroupExampleInput1" class="form-label"
                >Usuario</label
              >
              <input
                type="text"
                v-model="user.username"
                class="form-control"
                id="formGroupExampleInput1"
                placeholder="Ingresa tu nombre de usuario"
              />
            </div>
            <div class="mb-3">
              <label for="formGroupExampleInput2" class="form-label"
                >Contraseña</label
              >
              <input
                type="password"
                v-model="user.password"
                class="form-control"
                id="formGroupExampleInput2"
                placeholder="Ingresa tu contraseña"
              />
            </div>
            <div class="d-grid gap-2 col-6 mx-auto">
              <button class="btn btn-primary" type="submit" data-bs-dismiss="modal">
                Iniciar Sesión
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LogIn",

  data: function () {
    return {
      user: {
        username: "",
        password: ""
      }
    }
  },

  methods: {
    // pendiente
    // completada
    // rechazada

    processLogInUser: function(){
      //axios.post("http://127.0.0.1:8000/login/",
      axios.post("https://mintic-vuelos-be.herokuapp.com/login/",
          this.user,
          // "también se le puede enviar un mensaje"
          { headers: {} } // por aquí se puede enviar la metadata
        )
        .then((result) => {
          let dataLogIn = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          }

          this.$emit("completedLogIn", dataLogIn);
        })
        .catch((error) => {

          if (this.user.username == ""  || this.user.password == ""  )
            alert("Falta un nombre de usuario y/o contraseña")
  
          if (error.response.status == "401")
            alert("ERROR 401: Credenciales Incorrectas.");

          this.user.username = ""
          this.user.password = ""
        });
    }
  }
}
</script>