Vue.component("cfp-numinput", {
  props: ["name", "label", "help_text", "min", "max"],
  template: `
    <b-field type="is-primary" label-position="on-border"
        label="[[ label ]]"
        message="[[ help_text ]]">
          <b-numberinput controls-position="compact" controls-rounded
            name="[[ name ]]" 
            v-model="[[ name ]]" 
            min="[[ min ]]" 
            max="[[ max ]]">
          </b-numberinput>
    </b-field>
  `,
});

new Vue({
  delimiters: ["[[", "]]"],
  el: "#app",
  data: {
    name: "Anonymous PP-er",
    email: "ppcfp@yopmail.com",
    offset: 0,
    a1: 5000,
    a2: 100,
    a3: 1000,
    a4: 5000,
    a5: 5000,
    b1: 120,
    b2: 48,
    b3: 6,
    c1: 10,
    c2: 1,
    c3: 10,
    c4: 1,
    c5: 20,
    c6: 1,
    c7: 10,
    c8: 1,
    d1: 200,
    d2: 200,
    d3: 200,
    d4: 200,
    d5: 100,
    d6: 100,
    d7: 14,
    d8: 300,
    d9: 75,
    da: 25,
    e1: 0,
    e2: 50,
    e3: 1,
    e4: 6,
    e5: 1,
    e6: 800,
    f1: 5,
    f2: 20,
    f3: 50,
    f4: 1000,
    f5: 4,

    activeStep: 0,
  },

  computed: {
    db: function () {
      if (100 - this.d9 - this.da < 0) {
        this.da = this.da - 25;
      }
      if (100 - this.d9 - this.da < 0) {
        this.da = this.da - 25;
      }
      if (100 - this.d9 - this.da < 0) {
        this.da = this.da - 25;
      }
      if (100 - this.d9 - this.da < 0) {
        this.da = this.da - 25;
      }
      return 100 - this.d9 - this.da;
    },

    isFullySolar: function () {
      return this.e1 === 100;
    },

    isWoodHouse: function () {
      return this.f4 < 1;
    },

    isVegan: function () {
      return (
        this.d2 + this.d1 + this.d3 + this.d4 + this.d5 + this.d6 + this.d7 == 0
      );
    },
  },

  methods: {
    turnVegan: function (event) {
      this.d1 = 0;
      this.d2 = 0;
      this.d3 = 0;
      this.d4 = 0;
      this.d5 = 0;
      this.d6 = 0;
      this.d7 = 0;
    },
  },
});
