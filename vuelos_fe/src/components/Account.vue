<template>
  <section>
    <div v-if="loaded" class="container">
      <div class="left"><img src="..\assets\user2.png" ></div>

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

      axios.get(`user/${userId}`, {
        headers: {Authorization: `Bearer ${token}`}
        })
        .then((result) => {
          this.nombres = result.data.first_name;
          this.apellidos = result.data.last_name;
          this.correo = result.data.email;
          this.id_tarjetas = result.data.tarjeta.id_tarjeta;
          this.nombre_propietario = result.data.tarjeta.nombre_propietario;
          this.tipo = result.data.tarjeta.tipo;
          this.loaded = true;
          this.tipo_text = this.options[this.tipo];
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },

    verifyToken: function () {
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
  margin: 10px auto;
  display:flex;
  justify-content: center;
  align-items:center ;
  background-color: rgba(141, 140, 140, 0);
  border-radius: 20px;
}
.left{
  margin: 10px 0px 10px;
}
.left img{
  height: 300px;
  width: 250px;
}
.right{
  width: 90%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  border-style: double;
  border-width: thick;
  border-color: rgb(74, 135, 248);
  padding: auto;
  margin: auto 10px;
  background-color: #e1e8f1;
  color: rgb(8, 1, 1);
  font-family: serif;
}
.right h1{
  font-size: 35px;
  font-weight: bold;
  color: black;
}
.right h2{
  font-size: 25px;
  color: rgb(13, 13, 41);
}

</style>
