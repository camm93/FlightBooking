<template>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>Flights</title>

    <link rel="shortcut icon" href="./assets/avion.png" type="image/x-icon" />
  </head>

  <body>
    <section>
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">
            <img
              src="./assets/avion.png"
              alt=""
              width="30"
              height="24"
              class="d-inline-block align-text-top"
            />
            Book Your Next Flight
          </a>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <button
                  v-on:click="loadVuelos"
                  class="btn btn-outline-primary"
                  data-bs-toggle="modal"
                  data-bs-target="#exampleModalVuelos"
                >
                  Search
                </button>

                <button v-if="is_auth" v-on:click="loadReservas" class="btn btn-outline-primary">
                  My Reservations
                </button>

                <button
                  v-if="is_auth"
                  v-on:click="loadHome"
                  class="btn btn-outline-dark"
                >
                  Home
                </button>
              </li>
            </ul>
            <div class="d-flex">
              <!-- Button trigger modal -->
              <button
                v-if="!is_auth"
                v-on:click="loadSignUp"
                class="btn btn-light"
                data-bs-toggle="modal"
                data-bs-target="#exampleModal"
              >
                Create an Account
              </button>

              <!-- Button trigger modal -->
              <button
                v-if="!is_auth"
                v-on:click="loadLogIn"
                class="btn btn-primary"
                data-bs-toggle="modal"
                data-bs-target="#exampleModalTwo"
              >
                Log In
              </button>

              <button
                v-if="is_auth"
                v-on:click="loadAccount"
                class="btn btn-outline-dark"
              >
                Account
              </button>

              <button
                v-if="is_auth"
                v-on:click="logOut"
                class="btn btn-danger"
              >
                Log Out
              </button>
            </div>
          </div>
        </div>
      </nav>
    </section>

    <!-- router-view permite que los componentes hijos ejecuten métodos del componente padre -->
    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:logOut="logOut"
        v-on:betterLogIn="betterLogIn"
        v-on:completedReservation="completedReservation"
      >
      </router-view>
    </div>

    <section>
      <div
        id="carouselExampleFade"
        class="carousel slide carousel-fade"
        data-bs-ride="carousel"
      >
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="./assets/imagen1.jpg" class="d-block w-100" alt="..." />
          </div>
          <div class="carousel-item">
            <img src="./assets/imagen2.jpg" class="d-block w-100" alt="..." />
          </div>
          <div class="carousel-item">
            <img src="./assets/imagen3.jpg" class="d-block w-100" alt="..." />
          </div>
        </div>
        <button
          class="carousel-control-prev"
          type="button"
          data-bs-target="#carouselExampleFade"
          data-bs-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button
          class="carousel-control-next"
          type="button"
          data-bs-target="#carouselExampleFade"
          data-bs-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </section>
  </body>

  <footer class="bg-light text-center text-lg-start">
    <!-- Grid container -->
    <div class="container p-4">
      <!--Grid row-->
      <div class="row">
        <!--Grid column-->
        <div class="col-lg-6 col-md-12 mb-4 mb-md-0">
          <h5 class="text-uppercase">Disclaimer</h5>

          <p>
            TusVuelos is not responsible for content on external Websites.
            © 2021 TusVuelos, a flight-booking website. All rights reserved. 
            TusVuelos and the Airplane Logo are not registered trademarks. 
            This website is not meant for commercial but academic purposes.
          </p>
        </div>
        <!--Grid column-->

        <div class="col-lg-6 col-md-12 mb-4 mb-md-0">
          <h5 class="text-uppercase">Designed by</h5>

          <p id="author">
            Cristian Murillo
          </p>
        </div>
      </div>
    </div>
    <div class="text-center p-3" id="bootstrap" style="background-color: rgba(0, 0, 0, 0.2)">
      © 2022 Copyright:
      <a class="text-dark" href="https://mdbootstrap.com/">MDBootstrap.com</a>
    </div>
  </footer>
</template>

<script>
export default {
  name: "App",

  data: function () {
    return {
      is_auth: false,
    };
  },

  components: {},

  methods: {
    verifyAuth: function () {
      this.is_auth = localStorage.getItem("isAuth") || false;

      if (this.is_auth == false) this.$router.push({ name: "logIn" });
      else this.$router.push({ name: "home" });
    },
    loadLogIn: function () {
      this.$router.push({ name: "logIn" });
    },
    loadSignUp: function () {
      this.$router.push({ name: "signUp" });
    },
    loadVuelos: function () {
      this.$router.push({ name: "vuelos" });
    },
    loadHome: function () {
      this.$router.push({ name: "home" });
    },
    loadAccount: function () {
      this.$router.push({ name: "account" });
    }, 
    loadReservas: function () {
      this.$router.push({ name: "reservas" });
    },   
    logOut: function () {
      localStorage.clear();
      alert("Closing Session");
      this.verifyAuth();
    },
    completedLogIn: function (data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Authentication Successful");
      this.verifyAuth();
    },
    completedSignUp: function (data) {
      alert("Account Created");
      this.completedLogIn(data);
    },
    completedReservation: function () {
      alert("Reservación Exitosa");
      this.loadReservas();
    },
    betterLogIn: function () {
      alert("Es necesario que primero inicies sesión para reservar un vuelo");
      this.loadLogIn();
    },    

    created: function () {
      this.verifyAuth();
    },
  },
};
</script>

<style scoped>
.carousel-inner img {
  width: 100%;
  max-height: 460px;
  margin-top: 20px;
  margin-bottom: 50px;
}

.modal-title {
  color: #0d6efd;
}

#bootstrap{
  margin: 10px;
}

#author{
  display: flex;
  align-content: center;
  justify-content: center;
  margin: 35px;
  font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 25px;
  font-weight: bold;
}
</style>
