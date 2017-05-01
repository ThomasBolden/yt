"""
Enzo-P-specific fields



"""

#-----------------------------------------------------------------------------
# Copyright (c) 2017, yt Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

from yt.fields.field_info_container import \
    FieldInfoContainer

# We need to specify which fields we might have in our dataset. The field info
# container subclass here will define which fields it knows about.  There are
# optionally methods on it that get called which can be subclassed.

v_units = "code_velocity"
acc_units = "code_velocity / code_time"
de_units = "code_mass / code_length**3"
E_units = "code_mass * code_velocity**2"
p_units = "code_mass * code_velocity * code_length**2 / code_time"
b_units = "code_magnetic"

# unsure about the names after the colon
#REMOVE
known_species_names = {
    'HI'      : 'H',
    'HII'     : 'H_p1',
    'HeI'     : 'He',
    'HeII'    : 'He_p1',
    'HeIII'   : 'He_p2',
    'H2I'     : 'H2',
    'H2II'    : 'H2_p1',
    'DI'      : 'D',
    'DII'     : 'D_p1',
    'HDI'     : 'HD',
    'e'       : 'El'
}

class EnzoPFieldInfo(FieldInfoContainer):
    known_other_fields = (
        # Each entry here is of the form
        # ( "name", ("units", ["fields", "to", "alias"], # "display_name")),
        ("density",         (de_units, ["density"],         None)),
        ("pressure",        (p_units,  ["pressure"],        None)),
        ("total_Energy",    (E_units,  ["total_energy"],    None)),
        ("internal_Energy", (E_units,  ["internal_energy"], None)),
        ("temperature",     ("K",      ["temperature"],     None)),

        ("velocity_x", (v_units, ["velocity_x"], None)),
        ("velocity_y", (v_units, ["velocity_y"], None)),
        ("velocity_z", (v_units, ["velocity_z"], None)),

        ("acceleration_x", (acc_units, ["acceleration_x"], None)),
        ("acceleration_y", (acc_units, ["acceleration_y"], None)),
        ("acceleration_z", (acc_units, ["acceleration_z"], None)),

        ("metal_density", (de_units,         ["metal_density"], None)),
        ("e_density",     (de_units,         ["e_density"],     None)),
        ("cooling_time",  ("s",              ["cooling_time"],  None)),
        ("gamma",         ("ev / code_time", ["gamma"],         None)),# ??

        ("HI_density",    (de_units, ["HI_density"],    None)),
        ("HII_density",   (de_units, ["HII_density"],   None)),
        ("HeI_density",   (de_units, ["HeI_density"],   None)),
        ("HeII_density",  (de_units, ["HeII_density"],  None)),
        ("HeIII_density", (de_units, ["HeIII_density"], None)),

        ("HM_density",   (de_units, ["HM_density"],   None)),
        ("H2I_density",  (de_units, ["H2I_density"],  None)),
        ("H2II_density", (de_units, ["H2II_density"], None)),

        ("DI_density",  (de_units, ["DI_density"],  None)),
        ("DII_density", (de_units, ["DII_density"], None)),
        ("HDI_density", (de_units, ["HDI_density"], None)),
    )

    known_particle_fields = (
        # Identical form to above
        # ( "name", ("units", ["fields", "to", "alias"], # "display_name")),
    )

    def __init__(self, ds, field_list):
        super(EnzoPFieldInfo, self).__init__(ds, field_list)
        # If you want, you can check self.field_list

    def setup_fluid_fields(self):
        # Here we do anything that might need info about the dataset.
        # You can use self.alias, self.add_output_field (for on-disk fields)
        # and self.add_field (for derived fields).
        pass

    def setup_particle_fields(self, ptype):
        super(EnzoPFieldInfo, self).setup_particle_fields(ptype)
        # This will get called for every particle type.
