<template>
    <div>
        <roundCanopyInput />
        <inputParameterSidebarPlanform />
        <inputParameterSidebarAirfoil />
        <inputParameterSidebarVolute />
        <inputParameterSidebarAl />
    </div>
</template>

<script>
import roundCanopyInput from './roundCanopyInput.vue'
import inputParameterSidebarPlanform from './inputParameterSidebarPlanform.vue'
import inputParameterSidebarAirfoil from './inputParameterSidebarAirfoil.vue'
import inputParameterSidebarVolute from './inputParameterSidebarVolute.vue'
import inputParameterSidebarAl from './inputParameterSidebarAl.vue'

export default {
    components : {
        roundCanopyInput,
        inputParameterSidebarPlanform,
        inputParameterSidebarAirfoil,
        inputParameterSidebarVolute,
        inputParameterSidebarAl
    }
}
</script>
