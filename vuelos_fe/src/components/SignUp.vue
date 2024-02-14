<template>
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
          <h5 class="modal-title" id="exampleModalLabel">Sign Up</h5>
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
                >Name</label
              >
              <input
                type="text"
                v-model="user.first_name"
                class="form-control"
                id="formGroupExampleInput"
                placeholder="Enter your name"
              />
            </div>

            <div class="mb-3">
              <label for="formGroupExampleInput2" class="form-label"
                >Last Name</label
              >
              <input
                type="text"
                v-model="user.last_name"
                class="form-control"
                id="formGroupExampleInput2"
                placeholder="Enter your last name"
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
                placeholder="Enter your username"
              />
            </div>

            <div class="mb-3">
              <label for="formGroupExampleInput4" class="form-label"
                >Password</label
              >
              <input
                type="password"
                v-model="user.password"
                class="form-control"
                id="formGroupExampleInput4"
                placeholder="Enter your password"
              />
            </div>

            <div class="mb-3">
              <label for="formGroupExampleInput5" class="form-label"
                >Email</label>
              <input
                type="email"
                v-model="user.email"
                class="form-control"
                id="formGroupExampleInput5"
                placeholder="Enter your email address"
              />
            </div>

            <div class="mb-3">
              <label for="formGroupExampleInput6" class="form-label"
                >Credit/debit card owner</label
              >
              <input
                type="text"
                v-model="user.tarjeta.nombre_propietario"
                class="form-control"
                id="formGroupExampleInput6"
                placeholder="Enter card owner's full name"
              />
            </div>

            <div class="mb-3">
              <label class="form-label">Card Type</label>
              <div>
                <select class="form-select" v-model="selected" >
                  <option v-for="option in options" :key="option.text" :value="option.value"> {{option.text}} </option>
                  </select>
              </div>
            </div>

            <div class="mb-3">
              <label for="formGroupExampleInput8" class="form-label"
                >Security Code (3 digits)</label
              >
              <input
                type="text" maxlength="3"
                v-model="user.tarjeta.codigo"
                class="form-control"
                id="formGroupExampleInput8"
                placeholder="Enter the security code"
              />
            </div>

            <div class="mb-3">
              <label for="formGroupExampleInput9" class="form-label"
                >Expiration Date</label
              >
              <input
                type="date"
                v-model="user.tarjeta.fecha_vencimiento"
                class="form-control"
                id="formGroupExampleInput9"
                placeholder="Enter the expiration date (YYYY-MM-DD)"
              />
            </div>

            <div class="d-grid gap-2 col-6 mx-auto">
              <button
                class="btn btn-primary"
                type="submit"
                data-bs-dismiss="modal"
              >
                Submit
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
        first_name: "",
        last_name: "",
        password: "",
        username: "",
        email: "",

        tarjeta: {
          nombre_propietario: "",
          tipo: "",
          codigo: "000",
          fecha_vencimiento: (new Date()).toJSON().toString(),
        },
      },
    };
  },

  methods: {
    processSignUp: function () {
      this.user.tarjeta.tipo = this.selected

      axios.post("user/",
        this.user, 
        { headers: {} }
      )
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
