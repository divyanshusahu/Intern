import { saveAs } from "file-saver";

export function collect_inputs() {
  var inp_json = {};

  var planform_user_defined = document.getElementsByName(
    "planform_user_define"
  );
  var chord_length_percent = [];
  for (let i = 0; i < planform_user_defined.length; i++) {
    let cur = planform_user_defined[i].value.split(",").map(function(x) {
      return parseFloat(x);
    });
    chord_length_percent.push(cur);
  }

  inp_json["planform_description"] = {
    max_chord_length: parseFloat(
      document.getElementsByName("planform_chord")[0].value
    ),
    spanwise_chord_length_percentc: chord_length_percent,
    shape: document.getElementsByName("planform_plftype")[0].value,
    span_length: parseFloat(
      document.getElementsByName("planform_span")[0].value
    )
  };

  inp_json["number_of_panel"] = parseFloat(
    document.getElementsByName("planform_total_ribs")[0].value
  );

  inp_json["rib_description"] = {
    LE_cut: {
      angle_with_chord_line: parseFloat(
        document.getElementsByName("airfoil_acl")[0].value
      ),
      chord_length_percentc: parseFloat(
        document.getElementsByName("airfoil_clp")[0].value
      )
    },
    lightening_holes: [
      {
        shape: "ELLIPTIC",
        box_index: 0,
        minor_to_major_axes: 0.7,
        size: 5
      },
      {
        shape: "TRIANGULAR",
        box_index: 1,
        minor_to_major_axes: 0.7
      }
    ],
    aerofoil: "/solverMain/test/airfoil.txt",
    tape_V_angle: 20
  };

  inp_json["volute_description"] = {
    shape: "ELLIPTIC",
    semi_span_angle: parseFloat(
      document.getElementsByName("volute_input_ssa")[0].value
    ),
    minor_to_major_axes: parseFloat(
      document.getElementsByName("volute_input_minot_ratio")[0].value
    )
  };

  inp_json["drawing_2d"] = {
    file_name: "/work/ram_2d_drawing.dxf",
    sewing_allowance: {
      panel_rear_percentc: parseFloat(
        document.getElementsByName("flat_panels_sap_rear")[0].value
      ),
      max_value: parseFloat(
        document.getElementsByName("flat_panels_sa_max_value")[0].value
      ),
      min_value: parseFloat(
        document.getElementsByName("flat_panels_sa_min_value")[0].value
      ),
      rib_rear_percentc: parseFloat(
        document.getElementsByName("flat_panels_sar_rear")[0].value
      ),
      rib_front_percentc: parseFloat(
        document.getElementsByName("flat_panels_sar_front")[0].value
      ),
      panel_front_percentc: parseFloat(
        document.getElementsByName("flat_panels_sap_front")[0].value
      ),
      panel_sides_percentc: parseFloat(
        document.getElementsByName("flat_panels_sap_sides")[0].value
      ),
      rib_sides_percentc: parseFloat(
        document.getElementsByName("flat_panels_sar_sides")[0].value
      )
    }
  };

  let al = document.getElementsByName("ribs_connection");
  let al_value;
  for (let i = 0; i < al.length; i++) {
    if (al[i].checked) al_value = al[i].value;
  }

  let udrs = [1, 3, 8, 13];

  if (al_value == "USER_DEFINED") {
    udrs = document
      .getElementsByName("user_defined_ribs")[0]
      .value.split(",")
      .map(function(x) {
        return parseInt(x) - 1;
      });
  }

  inp_json["anchor_description"] = [
    {
      rib_connection: al_value,
      riser_length: parseFloat(
        document.getElementsByName("rla_cl_susplen")[0].value
      ),
      chordwise_locations_percentc: document
        .getElementsByName("rla_cl_location")[0]
        .value.split(",")
        .map(function(x) {
          return parseFloat(x, 10);
        }),
      distance_between_karabinas: parseFloat(
        document.getElementsByName("advip_others_dkl")[0].value
      ),
      user_defined_ribs: udrs,
      riser_end_separation_length: 400.0
    }
  ];

  if (document.getElementsByName("is_rla_l1").checked) {
    let rla_l1 = {};
    rla_l1["L1_length_percentl"] = parseFloat(
      document.getElementsByName("rla_l1_length")[0].value
    );
    let usrl1 = [];
    let inpsl1 = document.getElementsByName("rla_l1_inputs");
    for (let i = 0; i < inpsl1.length; i++) {
      let cur = inpsl1[i].value.split(",").map(function(x) {
        return parseFloat(x);
      });
      usrl1.push(cur);
    }
    rla_l1["L1_combination"] = usrl1;
    Object.assign(inp_json["anchor_description"][0], rla_l1);
  }

  if (document.getElementsByName("is_rla_l2").checked) {
    let rla_l2 = {};
    rla_l2["L2_length_percentl"] = parseFloat(
      document.getElementsByName("rla_l2_length")[0].value
    );
    let usrl2 = [];
    let inpsl2 = document.getElementsByName("rla_l2_inputs");
    for (let i = 0; i < inpsl2.length; i++) {
      let cur = inpsl2[i].value.split(",").map(function(x) {
        return parseFloat(x);
      });
      usrl2.push(cur);
    }
    rla_l2["L2_combination"] = usrl2;
    Object.assign(inp_json["anchor_description"][0], rla_l2);
  }

  let br = document
    .getElementsByName("bl_brake_ribs")[0]
    .value.split(",")
    .map(function(x) {
      return x;
    });
  inp_json["brake_line_description"] = {
    user_defined_ribs: br,
    enable_generation: true
  };

  if (document.getElementsByName("is_bl_l1").checked) {
    let bl_l1 = {};
    bl_l1["L1_length_percentl"] = parseFloat(
      document.getElementsByName("bl_l1_length")[0].value
    );
    let usrl1 = [];
    let inpsl1 = document.getElementsByName("bl_l1_inputs");
    for (let i = 0; i < inpsl1.length; i++) {
      let cur = inpsl1[i].value.split(",").map(function(x) {
        return parseFloat(x);
      });
      usrl1.push(cur);
    }
    bl_l1["L1_combination"] = usrl1;
    Object.assign(inp_json["brake_line_description"], bl_l1);
  }

  if (document.getElementsByName("is_bl_l2").checked) {
    let bl_l2 = {};
    bl_l2["L1_length_percentl"] = parseFloat(
      document.getElementsByName("bl_l2_length")[0].value
    );
    let usrl2 = [];
    let inpsl2 = document.getElementsByName("bl_l2_inputs");
    for (let i = 0; i < inpsl2.length; i++) {
      let cur = inpsl2[i].value.split(",").map(function(x) {
        return parseFloat(x);
      });
      usrl2.push(cur);
    }
    bl_l2["L1_combination"] = usrl2;
    Object.assign(inp_json["brake_line_description"], bl_l2);
  }

  inp_json["side_flap_description"] = {
    rear_edge_length_percentl: parseFloat(
      document.getElementsByName("advip_sfd_rel")[0].value
    ),
    start_line_index: parseFloat(
      document.getElementsByName("advip_sfd_index")[0].value
    ),
    front_edge_length_percentl: parseFloat(
      document.getElementsByName("advip_sfd_fel")[0].value
    ),
    enable_generation: true
  };
  inp_json["wash_out_description"] = {
    user_defined_angle: [-10, -8, -6, -4, -2, -1],
    center_of_rotation_percentc: parseFloat(
      document.getElementsByName("advip_washout_description_cr")[0].value
    ),
    variation: document.getElementsByName(
      "advip_washout_description_variation"
    )[0].value,
    tip_angle: parseFloat(
      document.getElementsByName("advip_washout_description_ta")[0].value
    )
  };
  inp_json["slider"] = {
    percent_area: parseFloat(
      document.getElementsByName("advip_slider_ap")[0].value
    ),
    width_length_ratio: parseFloat(
      document.getElementsByName("advip_slider_wlr")[0].value
    )
  };
  inp_json["transform_geometry"] = {
    rotation: {
      angle: document
        .getElementsByName("advip_tg_ra")[0]
        .value.split(",")
        .map(function(x) {
          return parseFloat(x, 10);
        })
    },
    translation: document
      .getElementsByName("advip_tg_ta")[0]
      .value.split(",")
      .map(function(x) {
        return parseFloat(x, 10);
      })
  };

  return inp_json;
}

export function save_input() {
  var input = collect_inputs();
  input = JSON.stringify(input, null, 4);
  var input_blob = new Blob([input], { type: "text/plain;charset=utf-8" });
  saveAs(input_blob, "input.scf");
}

function merge_inputs(inp_json) {
  document.getElementsByName("planform_total_ribs")[0].value =
    inp_json["number_of_panel"];
  document.getElementsByName("planform_chord")[0].value =
    inp_json["planform_description"]["max_chord_length"];
  document.getElementsByName("planform_span")[0].value =
    inp_json["planform_description"]["span_length"];
  document.getElementsByName("planform_plftype")[0].value =
    inp_json["planform_description"]["shape"];
  if (inp_json["planform_description"]["shape"] == "USER_DEFINED") {
    let cur = inp_json["planform_description"]["spanwise_chord_length_percentc"];
    for (let i=0;i<cur.length;i++) {
      let a = document.getElementsByName("planform_user_define")[i];
      if (a) {
        a.value = cur[i].join();
      }
      else {
        let inp_node = document.createElement("input");
        inp_node.setAttribute("type", "text");
        inp_node.setAttribute("name", "planform_user_define");
        document.getElementById("user_defined_planform").appendChild(inp_node);
        inp_json.setAttribute("value", cur[i].join());
      }
    }
  }

  document.getElementsByName("airfoil_clp")[0].value =
    inp_json["rib_description"]["LE_cut"]["chord_length_percentc"];
  document.getElementsByName("airfoil_acl")[0].value =
    inp_json["rib_description"]["LE_cut"]["angle_with_chord_line"];

  document.getElementsByName("volute_input_minot_ratio")[0].value =
    inp_json["volute_description"]["minor_to_major_axis"];
  document.getElementsByName("volute_input_ssa")[0].value =
    inp_json["volute_description"]["semi_span_angle"];

  document.getElementsByName("flat_panels_sa_max_value")[0].value =
    inp_json["drawing_2d"]["sewing_allowance"]["max_value"];
  document.getElementsByName("flat_panels_sa_min_value")[0].value =
    inp_json["drawing_2d"]["sewing_allowance"]["min_value"];
  document.getElementsByName("flat_panels_sar_sides")[0].value =
    inp_json["drawing_2d"]["sewing_allowance"]["rib_sides_percentc"];
  document.getElementsByName("flat_panels_sar_front")[0].value =
    inp_json["drawing_2d"]["sewing_allowance"]["rib_front_percentc"];
  document.getElementsByName("flat_panels_sar_rear")[0].value =
    inp_json["drawing_2d"]["sewing_allowance"]["rib_rear_percentc"];
  document.getElementsByName("flat_panels_sap_front")[0].value =
    inp_json["drawing_2d"]["sewing_allowance"]["panel_front_percentc"];
  document.getElementsByName("flat_panels_sar_rear")[0].value =
    inp_json["drawing_2d"]["sewing_allowance"]["panels_rear_percentc"];
  document.getElementsByName("flat_panels_sap_sides")[0].value =
    inp_json["drawing_2d"]["sewing_allowance"]["panels_sides_percentc"];

  

}

export function load_input(blob) {
  var project_file = new FileReader();
  project_file.addEventListener("load", function() {
    merge_inputs(JSON.parse(project_file.result));
  });
  project_file.readAsText(blob, "UTF-8");
}
