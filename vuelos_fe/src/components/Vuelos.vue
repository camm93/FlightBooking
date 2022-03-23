
<template>
  
  <div
    class="modal fade "
    id="exampleModalVuelos"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-xl">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Programa tu vuelo</h5>
          <button
            v-on:click="clearFields"
            onclick="document.getElementById('btnReserve').disabled = true;"
            id = "close_button"
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
            data-dismiss = "modal"
          ></button>
        </div>

        <form v-on:submit.prevent="processSearch">
          <div class="modal-body">

            <div id="chooseFilter" >
              <h6 > Selecciona un criterio de búsqueda (filtro) </h6>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="option1" v-on:click="filtro = 'd'"
                onclick="document.getElementById('input1').disabled = false; document.getElementById('input2').disabled = true; 
                document.getElementById('input3').disabled = true;">
                <label class="form-check-label" for="exampleRadios1">
                  Ciudad Destino
                </label>
              </div>
              <div class="form-check form-check-inline ">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="option2" v-on:click="filtro = 'o'"
                onclick="document.getElementById('input2').disabled = false; document.getElementById('input1').disabled = true;
                 document.getElementById('input3').disabled = true; ">
                <label class="form-check-label" for="exampleRadios2">
                  Ciudad Origen
                </label>
              </div>
              <div class="form-check form-check-inline ">
                <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio3" value="option3" v-on:click="filtro = 'i'"
                onclick="document.getElementById('input3').disabled = false; document.getElementById('input1').disabled = true; 
                document.getElementById('input2').disabled = true; ">
                <label class="form-check-label" for="exampleRadios3">
                  Número de vuelo
                </label>
              </div>
            </div>

            <div class="mb-3">
              <label class="form-label">Ciudad de destino</label>
              <div>
                <select class="form-select" v-model="selectedCity1" id="input1" disabled>
                  <option :value="null" disabled>
                    -- Seleccione la ciudad de destino
                  </option>
                  <option v-for="city in cities"
                    :key="city.text" :value="city.value">
                    {{ city.text }}
                  </option>
                </select>
              </div>
            </div>

            <div class="mb-3">
              <label class="form-label">Ciudad de origen</label>
              <div>
                <select class="form-select" v-model="selectedCity2" id="input2" disabled>
                  <option :value="null" disabled>
                    -- Seleccione la ciudad de partida
                  </option>
                  <option v-for="city in cities" 
                    :key="city.text" :value="city.value" >
                    {{ city.text }}
                  </option>
                </select>
              </div>
            </div>

            <div class="mb-3">
              <label for="input3" class="form-label">Número de Vuelo</label>
              <input
                type="text"
                v-model="id_vuelo"
                class="form-control"
                id="input3"
                placeholder="Ingrese el número del vuelo"
                disabled
              />
            </div>

            <div>
              <table class="table table-hover table-bordered table-responsive" >
                <thead>
                  <tr>
                    <th scope="col">Vuelo</th>
                    <th scope="col">Compañía</th>
                    <th scope="col">Destino</th>
                    <th scope="col">Origen</th>
                    <th scope="col">Fecha salida (UTC)</th>
                    <th scope="col">Fecha llegada (UTC)</th>
                    <th scope="col">Precio ($)</th>
                    <th scope="col">Estado</th>
                    <th scope="col">Capacidad</th>
                    <th scope="col">Puestos</th>
                    <th scope="col">Check</th>
                  </tr>
                </thead>
                <tbody id="myList">
                  <tr v-for="(ivuelo, index) in vueloEncontrados" :key="index">           
                    <td v-text="ivuelo.id_vuelo" ></td>
                    <td v-text="ivuelo.company"></td>
                    <td v-text="ivuelo.destino"></td>
                    <td v-text="ivuelo.origen"></td>
                    <td v-text="ivuelo.fecha_salida"></td>
                    <td v-text="ivuelo.fecha_llegada"></td>
                    <td v-text="ivuelo.precio"></td>
                    <td v-text="ivuelo.estado"></td>
                    <td v-text="ivuelo.cupos"></td>
                    <td> <input type="number" id="puestos" v-model="infoReserva.puestos" min="1"></td>
                    <td> <input class="form-check-input" type="radio" name="reservarRadioOptions" v-on:click="infoReserva.vuelo=ivuelo.id_vuelo"
                    onclick="document.getElementById('btnReserve').disabled = false;"></td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div>
              <button id="btnSearch" class="btn btn-primary btn-lg" type="submit" onclick="document.getElementById('btnReserve').disabled = true;">
                Buscar vuelos
              </button>
              <button v-on:click="processReserve" id="btnReserve" class="btn btn-primary btn-md" data-bs-dismiss="modal" disabled>
                Reservar vuelo
              </button> 
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>


<script>

import jwt_decode from "jwt-decode";
import axios from "axios";

export default {
  name: "Vuelos",

  data: function () {
    return {
      selectedCity1: null,
      selectedCity2: null,
      filtro: null,
      cities: [
        {value: 1, text: "Amazonía"},
        {value: 2, text: "Barranquilla"},
        {value: 3, text: "Bogotá"},
        {value: 4, text: "Bucaramanga"},
        {value: 5, text: "Cali"},
        {value: 6, text: "Cartagena"},
        {value: 7, text: "Cúcuta"},
        {value: 8, text: "Ibagué"},
        {value: 9, text: "Medellín"},
        {value: 10, text: "Neiva"},
        {value: 11, text: "Pamplona"},
        {value: 12, text: "Quibdó"},
        {value: 13, text: "Risaralda"},
        {value: 14, text: "San Andrés"},
        {value: 15, text: "Villavicencio"},
      ],
      id_vuelo : "",
      vueloEncontrados : [],
      infoReserva : {
        vuelo : null,
        cliente : 0,
        puestos : 1
      },
      estados: 
        {"A": "Activo",
         "C": "Cancelado",
         "F": "Finalizado",
         "R": "Retrasado"},  
      username: null,   
    };
  },

  methods: {
    
    processSearch: function () {
      let url_filtro = this.filtro || "";
      let pk = this.returnPk()

      axios.get(`vuelos/${url_filtro}/${pk}`, {
        headers: {},
      })
        .then((result) => {
          let input = result.data
          this.vueloEncontrados = input;
          let raw_fields = ["estado", "origen", "destino", "fecha_llegada", "fecha_salida"]
          let proc_fields = this.getValues(input, raw_fields)
          let proc_dates = this.datetimeformat(proc_fields.slice(-2))
          this.setValues(proc_fields.slice(0, -2), proc_dates)
        })
        .catch((error) => {
          console.log(error);
          if(error.response.status == "500"){
            alert("ERROR: La plataforma está presentando problemas. \nIntente de nuevo más tarde.");
          }
        });
    },

    processReserve: async function () {
      if (
        localStorage.getItem("token_access") === null ||
        localStorage.getItem("token_refresh") === null
      ) {
        this.$emit("betterLogIn");
        return;
      }
      await this.verifyToken();

      let token = localStorage.getItem("token_access");
      this.infoReserva.cliente = jwt_decode(token).user_id.toString(); // id_user o user_id

      axios.post("reserva/create/",
        this.infoReserva,
        { headers: { Authorization: `Bearer ${token}` } } // por aquí se puede enviar la metadata
      )
        .then(() => {
          this.$emit("completedReservation");
        }
        )
        .catch(() => {
          this.$emit("logOut");
        })
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
    
    returnPk: function () {
      if (this.filtro == "d"){
        return this.selectedCity1;}
      else if (this.filtro == "o"){
        return this.selectedCity2;}
      else if (this.filtro == "i"){
        return this.id_vuelo;}
      else { alert("El atributo this.filtro está tomando un valor inválido")
        console.log(`Atributo this.filtro tiene valor inválido ${this.filtro}`)
      }
    },
    
    getValues: function (input, fields) {
      let output = []
      for(var i=0; i < fields.length; i++){
        output.push(input.map(a => a[fields[i]]));
      }
      return output
    }, 

    datetimeformat: function (dtArray){
      for(var i=0; i < dtArray.length; i++){
        dtArray[i] = dtArray[i].map((element) => {
          return new Date(element).toUTCString().slice(5, -4)  // to remove " GMT" from dates
        })
      }
      return dtArray
    },
    
    setValues: function (fields, dates) {
      const [estado, origen, destino] = fields
      const [llegada, salida] = dates

      for(var i = 0; i < estado.length; i++){
        this.vueloEncontrados[i]["estado"] = this.estados[estado[i]];
        this.vueloEncontrados[i]["origen"] = this.cities[origen[i]-1]["text"];
        this.vueloEncontrados[i]["destino"] = this.cities[destino[i]-1]["text"];
        this.vueloEncontrados[i]["fecha_llegada"] = llegada[i];
        this.vueloEncontrados[i]["fecha_salida"] = salida[i];
      }
    }, 

    clearFields: function () {
      this.selectedCity1 = null;
      this.selectedCity2 = null;
      this.id_vuelo = "";
      this.vueloEncontrados= [];
      this.infoReserva.vuelo = null;
      this.infoReserva.puestos = 1;
      this.radioBtn = false;
    },
  },
};

</script>

<style scoped>
#chooseFilter{
  margin: auto;
  font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  font-size:  18px;
  display:flex;
  justify-content: center;
  align-items: stretch;
  text-align: stretch;
  width: 80%;
}
h6{
  font-size: 22px;
  width: 100%;  
  justify-content: center;
}
.modal-body {
  overflow : auto;
}
#btnSearch{
  margin: 1% 15%;
  width: 40%;
}
#btnReserve{
  width: 20%;
}
input[type=number] {
  width: 3.5em;
}
</style>

  
  
 