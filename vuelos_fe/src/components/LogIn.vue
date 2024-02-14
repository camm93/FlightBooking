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
          <h5 class="modal-title" id="exampleModalLabel">Log In</h5>
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
                >Username</label
              >
              <input
                type="text"
                v-model="user.username"
                class="form-control"
                id="formGroupExampleInput1"
                placeholder="Enter your username"
              />
            </div>
            <div class="mb-3">
              <label for="formGroupExampleInput2" class="form-label"
                >Password</label
              >
              <input
                type="password"
                v-model="user.password"
                class="form-control"
                id="formGroupExampleInput2"
                placeholder="Enter your password"
              />
            </div>
            <div class="d-grid gap-2 col-6 mx-auto">
              <button class="btn btn-primary" type="submit" data-bs-dismiss="modal">
                Done!
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

    processLogInUser: function(){
      axios.post("login/",
          this.user,
          { headers: {} }
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
            alert("All fields are mandatory.")
  
          if (error.response.status == "401")
            alert("ERROR 401: Wrong Credentials");

          this.user.username = ""
          this.user.password = ""
        });
    }
  }
}
</script>
