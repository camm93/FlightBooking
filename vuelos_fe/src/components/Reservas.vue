<template>
  <div class="upper_message">
    <h1>
      ¡Hola&nbsp; <span> {{ username }} </span>! Gracias por preferirnos.
    </h1>
    <div class="upper_img">
      <img
        src="..\assets\landscape.jpg"
        class="d-block w-100"
        style="height: 10em; width: 2em"
      />
    </div>
  </div>

  <section>
      <h1> A continuación encontrarás toda la
      información de tus reservaciones.</h1>
    <div v-if="loaded" class="container2">

      <div>
        <table class="table table-hover table-bordered table-responsive">
          <thead>
            <tr>
              <th scope="col">ID de la reserva</th>
              <th scope="col">Fecha de reserva</th>
              <th scope="col">Última Modificación</th>
              <th scope="col">Número de Vuelo</th>
              <th scope="col">Selección</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(ivuelo, index) in vueloEncontrados" :key="index">
              <td v-text="ivuelo.id_reservas"></td>
              <td v-text="ivuelo.fecha"></td>
              <td v-text="ivuelo.last_updated"></td>
              <td v-text="ivuelo.vuelo"></td>
              <td> <input class="form-check-input" type="radio" name="modificarRadioOptions" v-on:click="infoReserva=ivuelo.id_reservas"
                    onclick="document.getElementById('btnDelete').disabled = false;"></td>
            </tr>
          </tbody>
        </table>
        <div align="right"> 
          <button v-on:click="processDelete" id="btnDelete" class="btn btn-primary btn-md" disabled>        
            Eliminar Reservación </button> 
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import jwt_decode from "jwt-decode";
import axios from "axios";

export default {
  name: "Reservas",
  data: function () {
    return {
      username          : localStorage.getItem("username") || null,
      loaded            : false,
      vueloEncontrados  : [],
      infoReserva       : null,   
    };
  },

  methods: {
    getData: async function () {
      if (
        localStorage.getItem("token_access") === null ||
        localStorage.getItem("token_refresh") === null
      ) {
        this.$emit("logOut");
        return;
      }

      await this.verifyToken();

      let token = localStorage.getItem("token_access");
      let userId = jwt_decode(token).user_id.toString(); // id_user o user_id

      //axios.get(`http://127.0.0.1:8000/reserva/list/${userId}`, {
      axios.get(`https://mintic-vuelos-be.herokuapp.com/reserva/list/${userId}`, {
          headers: { Authorization: `Bearer ${token}` },
        })
        //.then(response --> response.json())
        .then((result) => {
            let input = result.data
            this.vueloEncontrados = input;       
            console.log(this.vueloEncontrados)
            this.loaded = true;
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },
    processDelete: async function(){

      if (
        localStorage.getItem("token_access") === null ||
        localStorage.getItem("token_refresh") === null
      ) {
        this.$emit("logOut");
        return;
      }

      console.log("id_reservas ", this.infoReserva)

      await this.verifyToken();

      let token = localStorage.getItem("token_access");
      let userId = jwt_decode(token).user_id.toString(); // id_user o user_id

      //axios.delete(`http://127.0.0.1:8000/reserva/remove/${userId}/${this.infoReserva}`, {
      axios.delete(`https://mintic-vuelos-be.herokuapp.com/reserva/remove/${userId}/${this.infoReserva}`, {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then(() => {
          alert("La reservación ha sido eliminada")
           this.getData()
        })
        .catch(() => {
          this.$emit("logOut");
        });

    },

    verifyToken: async function () {
      return (
        //axios.post("http://127.0.0.1:8000/refresh/",
        axios.post("https://mintic-vuelos-be.herokuapp.com/refresh/",
            { refresh: localStorage.getItem("token_refresh") },
            { headers: {} }
          )
          .then((result) => {
            localStorage.setItem("token_access", result.data.access);
          })
          .catch(() => {
            this.$emit("logOut");
          })
      );
    },
  },

  created: async function () {
    this.getData();
  },
};
</script>

<style>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
section {
  justify-content: center;
  align-items: center;
}
.container2{
    padding-left: 15px;
    padding-right: 15px;
}

.left {
  margin: 10px 0px 10px;
}
.right {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  padding: auto;
  margin: auto 10px;
  color: white;
  font-family: serif;
}
.table{
    padding: 20px;
    margin: 0 0 0 0;
    width: 100%;
}
h1 {
    padding: 10px;
  font-size: 35px;
  font-weight: lighter;
  display:flex;
  justify-content: center;
}

</style>
