import bpy

class Blend2Operator(bpy.types.Operator):
    """Blend two objects together"""
    bl_idname = "object.blend2_operator"
    bl_label = "Blend 2 Objects"

    def execute(self, context):
        # Get the selected objects
        objs = bpy.context.selected_objects
        if len(objs) != 2:
            self.report({'ERROR'}, "Please select two objects to blend")
            return {'CANCELLED'}

        # Create a new material for the blended object
        mat = bpy.data.materials.new(name="BlendMaterial")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links

        # Create a Mix Shader node
        mix = nodes.new(type="ShaderNodeMixShader")
        mix.location = (-300, 0)

        # Connect the object materials to the Mix Shader node
        mat1 = objs[0].material_slots[0].material
        mat2 = objs[1].material_slots[0].material
        links.new(mat1.node_tree.nodes["Material Output"].inputs[0], mix.inputs[1])
        links.new(mat2.node_tree.nodes["Material Output"].inputs[0], mix.inputs[2])

        # Create a new object with the blended material
        blend_obj = bpy.data.objects.new(name="BlendedObject", object_data=None)
        blend_obj.location = (0, 0, 0)
        blend_obj.active_material = mat
        bpy.context.scene.collection.objects.link(blend_obj)

        # Set the origin of the blended object to its center
        bpy.ops.object.select_all(action='DESELECT')
        blend_obj.select_set(True)
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')

        return {'FINISHED'}

def register():
    bpy.utils.register_class(Blend2Operator)

def unregister():
    bpy.utils.unregister_class(Blend2Operator)

if _name_ == "_main_":
    register()