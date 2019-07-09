import Viewer from 'viewerjs';

export function dxf_image_viewer() {
  const viewer = new Viewer(document.getElementById("dxf_image"), {
    inline: true,
    viewed() {
    viewer.view(1);
    }
  });
}
