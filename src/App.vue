<template>
  <div id="app">
    <h1>{{ header }}</h1>
    Deployed Branch Name:
    <input type="text" v-model="deployedBranch"/>
    <br />
    Candidate Branch Name:
    <input type="text" v-model="diffBranch"/>
    <table>
      <tr>
        <th>
          filename:
        </th>
        <th>
          filepath:
        </th>
      </tr>
      <tr v-for="item in filePaths" :key="item.name">
        <td>
          {{ item.name }}
        </td>
        <td>
          {{ item.path }}
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      header: "diffify",
      filePaths: [
        { name: "doodle", path: "./doodle.py" },
        { name: "wow", path: "../../wow.go" },
        { name: "fun", path: "extremefun.h" }
      ],
      backendUrl: "",
      deployedBranch: "release",
      diffBranch: "dev"
    };
  }
};
</script>
