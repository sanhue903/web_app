<template>
  <div class="flex">
    <SideBar />
    <div class="flex-1">
      <Header />
      <main class="p-6">
        <!-- Contenido principal aquí -->
      </main>
    </div>
  </div>
</template>

<script lang="ts">
import SideBar from '../components/ui/SideBar.vue';
import Header from '../components/ui/Header.vue';

export default {
  components: {
    SideBar,
    Header
  },
};
</script>