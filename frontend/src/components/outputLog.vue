<template>
  <div id="outputLog" class="card">
    <!--<p>{{ result.input_file }}</p>
    <p>{{ result.input_file_result }}</p>
    <p>{{ result.running_solver }}</p>
    <p>{{ result.running_solver_result}}</p>
    <p>{{ result.running_gmsh }}</p>
    <p>{{ result.running_gmsh_result }}</p>
    <p>{{ result.converting_vtp }}</p>
    <p>{{ result.coverting_vtp_result }}</p>
    <p>{{ result.success }}</p>-->
    <p>{{ logRender }}</p>
  </div>
</template>

<script>
import { EventBus } from '../main.js';
import { display_result } from '../vtkview.js';

export default {
  data : function() {
    return {
      caseID : {},
      result : {},
      logRender : ""
    }
  },
  created() {
    let self=this;
    EventBus.$on("solver_overall_result",(solver_result) =>{
      Object.assign(this.caseID, solver_result);
      self.logRender = "";
      if (this.caseID['case_id'])
      {
        var check_status = setInterval(function() {
          self.axios.post('/api/job_status', self.caseID).then((res) => {
            if (self.logRender != res.data["current_status"]) {
              self.logRender = res.data["current_status"];
              try {
                this.$forceUpdate();
              }
              catch {
                // This can be empty
              }
            }
            if(res.data['current_status'] == 'SUCCEEDED') {
              Object.assign(self.result, res.data);
              display_result(self.result['url']);
              EventBus.$emit("dxf", self.caseID);
              clearInterval(check_status);
            }
          });
        },5000);
      }
    });
  }
}
</script>

