Name = 'TranslateOriginOfUniformGrid'
Label = 'Translate Origin of Uniform Grid'
FilterCategory = 'CSM Geophysics Filters'
Help = 'This filter will translate the origin of vtkImageData to any specified Corner of the data set assuming it is currently in the South West Bottom Corner (will not work if Corner was moved prior).'

NumberOfInputs = 1
InputDataType = 'vtkImageData'
OutputDataType = 'vtkImageData'
ExtraXml = '''\
<IntVectorProperty
    name="Corner"
    command="SetParameter"
    number_of_elements="1"
    initial_string="test_drop_down_menu"
    default_values="0">
    <EnumerationDomain name="enum">
          <Entry value="1" text="South East Bottom"/>
          <Entry value="2" text="North West Bottom"/>
          <Entry value="3" text="North East Bottom"/>
          <Entry value="4" text="South West Top"/>
          <Entry value="5" text="South East Top"/>
          <Entry value="6" text="North West Top"/>
          <Entry value="7" text="North East Top"/>
    </EnumerationDomain>
    <Documentation>
        This is the new origin corner you'd like the origin to reside.
    </Documentation>
</IntVectorProperty>

'''


Properties = dict(
    Corner=0,
)


def RequestData():
    pdi = self.GetInput() # vtkImageData
    pdo = self.GetOutput() # vtkImageData

    [nx, ny, nz] = pdi.GetDimensions()
    [ox, oy, oz] = pdi.GetOrigin()

    pdo.DeepCopy(pdi)

    xx,yy,zz = 0.0,0.0,0.0

    if Corner == 1:
        # South East Bottom
        xx = ox - nx
        yy = oy
        zz = oz
    elif Corner == 2:
        # North West Bottom
        xx = ox
        yy = oy - ny
        zz = oz
    elif Corner == 3:
        # North East Bottom
        xx = ox - nx
        yy = oy - ny
        zz = oz
    elif Corner == 4:
        # South West Top
        xx = ox
        yy = oy
        zz = oz - nz
    elif Corner == 5:
        # South East Top
        xx = ox - nx
        yy = oy
        zz = oz - nz
    elif Corner == 6:
        # North West Top
        xx = ox
        yy = oy - ny
        zz = oz - nz
    elif Corner == 7:
        # North East Top
        xx = ox - nx
        yy = oy - ny
        zz = oz - nz

    pdo.SetOrigin(xx, yy, zz)
