<template>
    <div>
        <roundCanopyInput />
        <inputParameterSidebarPlanform />
        <inputParameterSidebarAirfoil />
        <inputParameterSidebarVolute />
        <inputParameterSidebarAl />
        <inputParameterSidebarFp />
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
import inputParameterSidebarAi from './inputParameterSidebarAi.vue'

export default {
    components : {
        roundCanopyInput,
        inputParameterSidebarPlanform,
        inputParameterSidebarAirfoil,
        inputParameterSidebarVolute,
        inputParameterSidebarAl,
        inputParameterSidebarFp,
        inputParameterSidebarAi
    }
}
</script>
