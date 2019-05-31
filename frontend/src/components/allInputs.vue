<template>
    <div>
        <roundCanopyInput />
        <inputParameterSidebarPlanform />
        <inputParameterSidebarAirfoil />
        <inputParameterSidebarVolute />
        <inputParameterSidebarAl />
        <inputParameterSidebarFp />
        <inputParameterSidebarRLA />
        <inputParameterSidebarBL />
        <inputParameterSidebarAi />
    </div>
</template>

<script>
import roundCanopyInput from './roundCanopyInput.vue'
import inputParameterSidebarPlanform from './inputParameterSidebarPlanform.vue'
import inputParameterSidebarAirfoil from './inputParameterSidebarAirfoil.vue'
import inputParameterSidebarVolute from './inputParameterSidebarVolute.vue'
import inputParameterSidebarAl from './inputParameterSidebarAl.vue'
import inputParameterSidebarFp from './inputParameterSidebarFp.vue'
import inputParameterSidebarRLA from './inputParameterSidebarRLA.vue'
import inputParameterSidebarBL from './inputParameterSidebarBL.vue'
import inputParameterSidebarAi from './inputParameterSidebarAi.vue'

export default {
    components : {
        roundCanopyInput,
        inputParameterSidebarPlanform,
        inputParameterSidebarAirfoil,
        inputParameterSidebarVolute,
        inputParameterSidebarAl,
        inputParameterSidebarFp,
        inputParameterSidebarRLA,
        inputParameterSidebarBL,
        inputParameterSidebarAi
    }
}
</script>
