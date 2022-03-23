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
              <th scope="col">Última Modificación (UTC)</th>
              <th scope="col">Número de Vuelo</th>
              <th scope="col">Puestos</th>
              <th scope="col">Eliminar</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(ivuelo, index) in vueloEncontrados" :key="index">
              <td v-text="ivuelo.id_reserva"></td>
              <td v-text="ivuelo.fecha"></td>
              <td v-text="ivuelo.last_updated"></td>
              <td v-text="ivuelo.vuelo"></td>
              <td> <input type="number" id="puestos" v-model="ivuelo.puestos" min="1" max="10" v-on:change="reservaUpdate(index)"> </td>
              <td> <input class="form-check-input" type="radio" name="modificarRadioOptions" v-on:click="deleteReservaId=ivuelo.id_reserva"
                    onclick="document.getElementById('btnDelete').disabled = false;"></td>
            </tr>
          </tbody>
        </table>
        <div align="center"> 
            <button v-on:click="processUpdate" id="btnUpdate" class="btn btn-primary btn-md" disabled>        
            Actualizar Reservación </button>           
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
      username : localStorage.getItem("username") || null,
      loaded : false,
      vueloEncontrados : [],
      deleteReservaId : null,
      infoReserva : null,   
      infoUpdate : {
        vuelo: null,
        cliente: null,
        puestos: null
      }
    };
  },

  methods: {
    getData: async function () {

      const [token, userId] = await this.checkTokens()

      axios.get(`reserva/list/${userId}`, {
        headers: { Authorization: `Bearer ${token}` },
      })
        .then((result) => {
            let input = result.data
            this.vueloEncontrados = input
            this.datetimeformat(input, "last_updated")
            this.loaded = true;
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },
    reservaUpdate: function(index){
      document.getElementById('btnUpdate').disabled = false;
      this.infoReserva = this.vueloEncontrados[index].id_reserva
      this.infoUpdate.vuelo = this.vueloEncontrados[index].vuelo
      this.infoUpdate.puestos = this.vueloEncontrados[index].puestos
    },
    processUpdate: async function(){

      const [token, userId] = await this.checkTokens()
      this.infoUpdate.cliente = userId

      axios.patch(`reserva/update/${userId}/${this.infoReserva}`, 
        this.infoUpdate,
        {headers: { Authorization: `Bearer ${token}` },
      })
        .then(() => {
          alert("La reservación ha sido actualizada.")
           this.getData()
        })
        .catch(() => {
          this.$emit("logOut");
        });

    },
    processDelete: async function(){

      const [token, userId] = await this.checkTokens()

      axios.delete(`reserva/remove/${userId}/${this.deleteReservaId}`, {
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
    checkTokens: async function() {
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

      return [token, userId]
    },
    verifyToken: async function () {
      return (
        axios.post("refresh/",
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

    datetimeformat: function (input, datefield) {
      let output = input.map((element) => {
        let a = element[datefield]
        return new Date(a).toUTCString().slice(0, -4)  // to remove " GMT" from dates
        })

      for (var i=0; i < output.length; i++){
        this.vueloEncontrados[i]["last_updated"] = output[i]
      }
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
    width: 100%;
}
h1 {
    padding: 10px;
  font-size: 35px;
  font-weight: lighter;
  display:flex;
  justify-content: center;
}
#btnUpdate {
  margin: 0 15% 0 0;
}
input[type=number] {
  width: 3.5em;
}
</style>
