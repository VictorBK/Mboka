<template>
    <div class="py-10 px-6">
        <h1 class="mb-6 text-2xl">My jobs</h1>
       
        <div class="space-y-4">
            <job :my="true" />

            <job :my="true" />

            <job :my="true" />
        </div>    
    </div>
</template>
