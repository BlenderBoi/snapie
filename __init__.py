import bpy

bl_info = {
    "name": "Snapie",
    "author": "BlenderBoi",
    "version": (1, 0),
    "blender": (3, 00, 0),
    "location": "Shift + Tab",
    "description": "Pie for Snap Presets",
    "warning": "",
    "doc_url": "",
    "category": "Tools",
}


class SNAPIE_Set_Snap(bpy.types.Operator):
    """Set Snap"""
    bl_idname = "snapie.set_snap"
    bl_label = "Set Snap"

    mode: bpy.props.StringProperty()

    def execute(self, context):

        scn = context.scene
        tool_settings = scn.tool_settings

        if self.mode == "VERTEX":
            tool_settings.snap_elements = {"VERTEX"}

        if self.mode == "EDGE":
            tool_settings.snap_elements = {"EDGE", "EDGE_MIDPOINT"}

        if self.mode == "FACE":
            tool_settings.snap_elements = {"FACE"}

        if self.mode == "INCREMENT":
            tool_settings.snap_elements = {"INCREMENT"}

        if self.mode == "VOLUME":
            tool_settings.snap_elements = {"VOLUME"}

        if self.mode == "CENTER":
            tool_settings.snap_target = "CENTER"

        if self.mode == "CLOSEST":
            tool_settings.snap_target = "CLOSEST"

        return {'FINISHED'}

class SNAPIE_MT_Snap_Pie(bpy.types.Menu):

    bl_label = "Snap Preset"

    def draw(self, context):

        layout = self.layout

        pie = layout.menu_pie()
        pie.prop(context.scene.tool_settings, "use_snap", text="Toogle Snap")
        pie.operator("snapie.set_snap", text="Vertex", icon="SNAP_VERTEX").mode = "VERTEX"
        #pie.operator("snapie.set_snap", text="Increment", icon="SNAP_INCREMENT").mode = "INCREMENT"

        #pie.operator("snapie.set_snap", text="Volume", icon="SNAP_VOLUME").mode = "VOLUME"

        #pie.prop(context.scene.tool_settings, "snap_target", expand=True)

        pie.operator("snapie.set_snap", text="Snap Center").mode = "CENTER"
        pie.operator("snapie.set_snap", text="Snap Closest").mode = "CLOSEST"

        if context.scene.tool_settings.snap_elements == {"INCREMENT"}:
            pie.prop(context.scene.tool_settings, "use_snap_grid_absolute", text="Absolute Grid")
        else: 
            pie.prop(context.scene.tool_settings, "use_snap_align_rotation", text="Align Rotation")

        pie.operator("snapie.set_snap", text="Edge", icon="SNAP_EDGE").mode = "EDGE"
        pie.prop(context.scene.tool_settings, "use_mesh_automerge", text="Auto Merge")
        pie.operator("snapie.set_snap", text="Face", icon="SNAP_FACE").mode = "FACE"

classes = [SNAPIE_Set_Snap, SNAPIE_MT_Snap_Pie]

addon_keymaps = []

def register():

    for cls in classes:
        bpy.utils.register_class(cls)



    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:

        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("wm.call_menu_pie", type="TAB", shift=True, value="PRESS")
        kmi.properties.name = "SNAPIE_MT_Snap_Pie"
        addon_keymaps.append([km, kmi])

def unregister():


    for cls in classes:
        bpy.utils.unregister_class(cls)


    addon_keymaps.clear()

if __name__ == "__main__":
    register()
