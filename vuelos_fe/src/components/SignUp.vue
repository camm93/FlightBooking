<template>
  <!-- Modal -->
  <div
    class="modal fade"
    id="exampleModal"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Registrarse</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>

        <form v-on:submit.prevent="processSignUp">
          <div class="modal-body">
            <div class="mb-3">
              <label for="formGroupExampleInput" class="form-label"
                >Nombres</label
              >
              <input
                type="text"
                v-model="user.nombres"
                class="form-control"
                id="formGroupExampleInput"
                placeholder="Ingresa tu nombre"
              />
            </div>

            <div class="mb-3">
              <label for="formGroupExampleInput2" class="form-label"
                >Apellidos</label
              >
              <input
                type="text"
                v-model="user.apellidos"
                class="form-control"
                id="formGroupExampleInput2"
                placeholder="Ingresa tus apellidos"
              />
            </div>

            <div class="mb-3">
              <label for="formGroupExampleInput3" class="form-label"
                >Username</label
              >
              <input
                type="text"
                v-model="user.username"
                class="form-control"
                id="formGroupExampleInput3"
                placeholder="Ingresa tu username"
              />
            </div>

            <div class="mb-3">
              <label for="formGroupExampleInput4" class="form-label"
                >Contraseña</label
              >
              <input
                type="password"
                v-model="user.password"
                class="form-control"
                id="formGroupExampleInput4"
                placeholder="Ingresa tu contraseña"
              />
            </div>

            <div class="mb-3">
              <label for="formGroupExampleInput5" class="form-label"
                >Correo electrónico</label>
              <input
                type="text"
                v-model="user.correo"
                class="form-control"
                id="formGroupExampleInput5"
                placeholder="Ingresa tu correo electrónico"
              />
            </div>

            <div class="mb-3">
              <label for="formGroupExampleInput6" class="form-label"
                >Nombre del propietario de la tarjeta</label
              >
              <input
                type="text"
                v-model="user.tarjetas.nombre_propietario"
                class="form-control"
                id="formGroupExampleInput6"
                placeholder="Ingresa nombre y apellido"
              />
            </div>

            <div class="mb-3">
              <label class="form-label">Tipo de Tarjeta</label>
              <div>
                <select class="form-select" v-model="selected" >
                  <option v-for="option in options" :key="option.text" :value="option.value"> {{option.text}} </option>
                  </select>
              </div>
            </div>

            <div class="mb-3">
              <label for="formGroupExampleInput8" class="form-label"
                >Código</label
              >
              <input
                type="number"
                v-model="user.tarjetas.codigo"
                class="form-control"
                id="formGroupExampleInput8"
                placeholder="Ingresa el código único de tu tarjeta"
              />
            </div>

            <div class="mb-3">
              <label for="formGroupExampleInput9" class="form-label"
                >Fecha Vencimiento</label
              >
              <input
                type="date"
                v-model="user.tarjetas.fecha_vencimiento"
                class="form-control"
                id="formGroupExampleInput9"
                placeholder="Ingresa la fecha en formato YYYY-MM-DD"
              />
            </div>

            <div class="d-grid gap-2 col-6 mx-auto">
              <button
                class="btn btn-primary"
                type="submit"
                data-bs-dismiss="modal"
              >
                Registrarse
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
  name: "SignUp",

  data: function () {
    return {
      selected: "A",
      options: [
        { value: "A", text: "American Express" },
        { value: "B", text: "Bank of America" },
        { value: "D", text: "Diners Club" },
        { value: "M", text: "MasterCard" },
        { value: "V", text: "Visa" },
      ],
      user: {
        nombres: "",
        apellidos: "",
        password: "",
        username: "",
        correo: "",

        tarjetas: {
          nombre_propietario: "",
          tipo: "",
          codigo: 0,
          fecha_vencimiento: (new Date()).toJSON().toString(),
        },
      },
    };
  },

  methods: {
    processSignUp: function () {
      this.user.tarjetas.tipo = this.selected

      //axios.post("http://127.0.0.1:8000/user/", this.user, {
      axios.post("https://mintic-vuelos-be.herokuapp.com/user/", this.user, {

          headers: {},
        })
        .then((result) => {
          let dataSignUp = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };

          this.$emit("completedSignUp", dataSignUp);
        })
        .catch((error) => {
          console.log(error);
          alert("ERROR: Fallo en el registro.");
        });
    },
  },
};
</script>