<template>
  <section>
    <div v-if="loaded" class="container">
      <div class="left"><img src="..\assets\atardecer.png" class="d-block w-100" ></div>

      <div class="right">
        <div class="information">
          <h1>Información de su cuenta</h1>
          <h2>
            Nombres: <span>{{ nombres }}</span>
          </h2>
          <h2>
            Apellidos: <span>{{ apellidos }}</span>
          </h2>
          <h2>
            Correo electrónico: <span>{{ correo }}</span>
          </h2>
          <h2>
            Número de tarjeta: <span>{{ id_tarjetas }}</span>
          </h2>
          <h2>
            Nombre de propietario: <span>{{ nombre_propietario }}</span>
          </h2>

          <h2>
            Tipo de tarjeta: <span>{{ tipo_text }}</span>
          </h2>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import jwt_decode from "jwt-decode";
import axios from "axios";

export default {
  name: "Account",
  data: function () {
    return {
      nombres: "",
      apellidos: "",
      correo: "",
      id_tarjetas: "",
      nombre_propietario: "",
      tipo: "",
      loaded: false,
      tipo_text : "",
      options: 
        {"A": "American Express" ,
         "B": "Bank of America" ,
         "D": "Diners Club" ,
         "M": "MasterCard" ,
         "V": "Visa" },
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

      //axios.get(`http://127.0.0.1:8000/user/${userId}`, {
      axios.get(`https://mintic-vuelos-be.herokuapp.com/user/${userId}`, {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then((result) => {
          this.nombres = result.data.nombres;
          this.apellidos = result.data.apellidos;
          this.correo = result.data.correo;
          this.id_tarjetas = result.data.tarjetas.id_tarjeta;
          this.nombre_propietario = result.data.tarjetas.nombre_propietario;
          this.tipo = result.data.tarjetas.tipo;
          this.loaded = true;
          this.tipo_text = this.options[this.tipo];
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },

    verifyToken: function () {
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
*{
  padding:0;
  margin: 0;
  box-sizing: border-box;
}
section{
  
  justify-content: center;
  align-items: center;

}
.container{
  width: 100%;
  margin: 0 auto;
  display:flex;
  justify-content: center;
  align-items:center ;
  background-color: rgba(141, 140, 140, 0.548);
  border-radius: 20px;

}
.left{
  
  margin: 10px 0px 10px;

}
.right{
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  padding: auto;
  margin: auto 10px;
  background-color: #283747;
  color: white;
  font-family: serif;
}
.right h1{
  font-size: 35px;
  font-weight: lighter;
}
.right h2{
  font-size: 25px;

}

</style>
