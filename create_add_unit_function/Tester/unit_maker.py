column_name = 'Column_1'
n_stages = 30
feed_stage = 10
pressure = 101325*2 # assuming no pressure drop currently
feed_pressure = 101325
feed_temperature = 348.15
vapour_fraction_feed = 0.429878
component_flow = [0.333333, 0.333333, 0.333333]
specification_1 = "1 Spec Reflux ratio"
specification_1_value = 2
specification_2 = "1 Spec Boilup ratio"
specification_2_value = 1.5
inlet_stream_number = 1
tops_stream_number = 2
bottoms_stream_number = 3
y_max = 38
x_min = 48
x_max = 62
y_min = 14 
unit_string = fr"""<unitOperation CLSID="ChemSepUO.ChemSep_UnitOperation.1" name="{column_name}" type="COM:1.0">
    <description>ChemSep Unit Operation</description>
    <properties>
      <value name="sepFile" type="str">[ChemSep]
Version=8.20
Compiled=2020-4-6 01:55 717b5cb3d168
Name=C:\Users\MEATRO~1\AppData\Local\Temp\CS_3_1~2.sep
Title=ChemSep CO Unit Operation "{column_name}" in COFE Flowsheet
User=meatrobot
Date=2020-04-22
Time=09:27:25

[Paths]
Device drivers path=c:\program files\chemsepl8v20\bin\
Help and Info path=c:\program files\chemsepl8v20\help\
Component data path=c:\program files\chemsepl8v20\pcd\
Property data path=c:\program files\chemsepl8v20\ipd\
Section data path=c:\program files\chemsepl8v20\ild\
Executables path=C:\Program Files\ChemSepL8v20\bin\
Temporary path=C:\Users\MEATRO~1\AppData\Local\Temp\
Scripts path=c:\program files\chemsepl8v20\bin\

[Units]
Temperature=K
Flow=kmol/s
Mass flow=kg/s
Vapour volumetric flow=m3/s
Liquid volumetric flow=m3/s
Pressure=N/m2
Heat=J/s
Enthalpy=J/kmol
Entropy=J/kmol/K
Fraction=_
Length=m
1/Length=1/m
Area=m2
Volume=m3
Moles=kmol
Mass=kg
Angle=rad
Velocity=m/s
Surface tension=N/m
Density=kg/m3
Molar density=kmol/m3
Viscosity=N/m2.s
Molecular weight=kg/kmol
Heat capacity=J/kmol/K
Thermal conductivity=J/s/m/K
Diffusivity=m2/s
Interaction parameter=J/mol
Time=s

[Components]
3 Number of Components
14 1921 Library Offset, Index DT=2020-04-03,20:56:46 CHK=271822342 CAS=7732-18-5 CID=Water
Name=Water
Lib=c:\program files\chemsepl8v20\pcd\chemsep1.pcd
125 501 Library Offset, Index DT=2020-04-03,20:56:46 CHK=63532870 CAS=71-43-2 CID=Benzene
Name=Benzene
Lib=c:\program files\chemsepl8v20\pcd\chemsep1.pcd
140 502 Library Offset, Index DT=2020-04-03,20:56:46 CHK=403992560 CAS=108-88-3 CID=Toluene
Name=Toluene
Lib=c:\program files\chemsepl8v20\pcd\chemsep1.pcd

[Operation]
2 Operation Column
1 Operation kind Simple Distillation
1 Condenser Total (Liquid product)
1 Reboiler Partial (Liquid product)
{n_stages} Stages
1 Feed stages
0 Sidestream stages
F={feed_stage}
S=
0 Pumparound stages
P=
0 Interconnections
I=
0 Extra condensers
C=
0 Extra reboilers
R=

[Simulation Model]
*  Simulation model *

[Properties]
350 BIP estimation temperature
0 Estimation BIPs

[Thermodynamics]
1 K model Raoult's law
1 * Activity coefficient Ideal solution
*  Wilson model *
*  UNIQUAC model *
1 Equation of State Ideal gas law
*  Cubic EOS *
*  Virial EOS *
1 Vapour pressure Antoine
0 Henry's law
*  Henry's default *

[Enthalpy]
2 Enthalpy Ideal
1 Enthalpy reference state Vapour
298.15 Enthalpy reference temperature
1 Formation enthalpies Excluded
298.15 Exergy surroundings temperature

[Physical property models]
1 1 No Check T range
*  Cubic EOS *
*  Virial EOS *
*  Vapour model *
*  Liquid mixture density *
*  Liquid component density *
*  Vapour mixture viscosity *
*  Vapour mixture viscosity pressure correction *
*  Vapour component viscosity *
*  Liquid mixture viscosity *
*  Liquid component viscosity *
* Vapour mixture Cp
1 Vapour component Cp T correlation
1 Liquid mixture Cp Mole fraction average of pure compound values
* Liquid component Cp
*  Vapour mixture conductivity *
*  Vapour component conductivity *
*  Liquid mixture conductivity *
*  Liquid component conductivity *
*  Mixture surface tension *
*  Component surface tension *
*  Vignes MS D-model *
*  D mixture model *
*  Vapour Diffusion Coefficients *
11 Default Liquid Diffusion Coefficients Modified Wilke-Chang
*  Interfacial tension *

[Reaction data]
0 Number of reactions

[Specifications]
Top
Bottom

[Heaters/Coolers]
0 Number
0 Column duty Qcolumn
2 First stage
{n_stages - 1} Last stage
0 Qcolumn lost to surroundings

[Efficiencies]
1 Default efficiency
0 Number

[Pressures]
1 Column pressure Constant pressure
{pressure} Condenser pressure
{pressure} Top pressure
* Pressure Drop
* Bottom pressure

[Feeds]
1 Number
*  Feed state *
{feed_stage} Stage Feed1{{split}}
{feed_temperature} Temperature
{feed_pressure} Pressure
{vapour_fraction_feed} Vapour fraction
3 componentflows
{component_flow[0]} Component 1 flow
{component_flow[1]} Component 2 flow
{component_flow[2]} Component 3 flow

[Condenser]
{specification_1}
{specification_1_value} Value Qcondenser
* Subcooling
*  Type *
* Initialization guess * *

[Reboiler]
{specification_2}
{specification_2_value} Value Qreboiler
* Superheating
*  Type *
* Initialization guess * *

[Monitored Variables]
*


[Solve options]
1 Initialization Automatic
1 Method Newton's method
0.5 Flow Step limit
10 Temperature Step limit
1 Composition Step limit
1 Flux Step limit
0.000001 Accuracy
30 Maximum iterations
1 Iteration count &amp; function vector
0 T/V/L profiles
0 X/Y profiles
0 Variable and function vectors
0 Jacobian
1 History Screen
History file=
1 Feeds type Stage below
0 Interactive
0 Log thermodynamics
0 Log enthalpy/entropy
0 Log physical properties
0 Log timing
0 CO numeric differencing
* Log from iteration
0 CS K-value
0 CS enthalpy
0 CS entropy
0 CS flash
0 CS activity coefficient
0 CS vapor pressuure
0 CS density
0 CS viscosity
0 CS thermal conductivity
0 CS heat capacity
0 CS surface tension
0 CS diffusivity
0 Trace treshold

[Programs]
Temporary file=SCRATCH.TMP
User program=
1 Compiler Gfortran
1 Show windows Hidden


[End of Input]

</value>
      <value name="parameters" type="str[]">
        <el>GUIArguments</el>
        <el>UseCOSEThermo</el>
        <el>UseCOSEDiffusionCoefficients</el>
        <el>UsePerturbedDerivativesOnly</el>
        <el>UsePerturbed_ddX</el>
        <el>SuppressWarnings</el>
        <el>RelativePerturbationTemperature</el>
        <el>RelativePerturbationPressure</el>
        <el>PerturbationComposition</el>
        <el>OutletFlash</el>
        <el>UseOnlyKValuesAndEnthalpyFromCOSE</el>
        <el>RestartDataAvailable</el>
        <el>OmitStageFromPortName</el>
        <el>WilsonEstimate</el>
        <el>LogPropertyCalls</el>
        <el>EnergyPorts</el>
        <el>Allowed temperature difference</el>
      </value>
      <value name="GUIArguments" type="str">/kpld</value>
      <value name="UseCOSEThermo" type="bool">false</value>
      <value name="UseCOSEDiffusionCoefficients" type="bool">false</value>
      <value name="UsePerturbedDerivativesOnly" type="bool">false</value>
      <value name="UsePerturbed_ddX" type="bool">false</value>
      <value name="SuppressWarnings" type="bool">true</value>
      <value name="RelativePerturbationTemperature" type="r8">0.001</value>
      <value name="RelativePerturbationPressure" type="r8">0.001</value>
      <value name="PerturbationComposition" type="r8">0.001</value>
      <value name="OutletFlash" type="str">Auto</value>
      <value name="UseOnlyKValuesAndEnthalpyFromCOSE" type="bool">false</value>
      <value name="RestartDataAvailable" type="bool">false</value>
      <value name="OmitStageFromPortName" type="bool">false</value>
      <value name="WilsonEstimate" type="bool">false</value>
      <value name="LogPropertyCalls" type="bool">false</value>
      <value name="EnergyPorts" type="bool">false</value>
      <value name="Allowed temperature difference" type="r8">12</value>
      <value name="profileParameters" type="empty" />
      <value name="userParameters" type="empty" />
      <value name="reports" type="empty" />
      <value name="inletPortNames" type="str[]">
        <el>Feed1_stage{feed_stage}</el>
      </value>
      <value name="inletPortCSNames" type="str[]">
        <el>Feed1</el>
      </value>
      <value name="inletPortStages" type="i4[]">{feed_stage}</value>
      <value name="inletPortIDs" type="i4[]">0</value>
      <value name="outletPortNames" type="str[]">
        <el>TopProduct</el>
        <el>BottomProduct</el>
      </value>
      <value name="outletPortCSNames" type="str[]">
        <el>top</el>
        <el>bottom</el>
      </value>
      <value name="outletPortStages" type="i4[]">-1;-1</value>
      <value name="outletPortIDs" type="i4[]">-1;-2</value>
      <value name="outletPortFlashTypes" type="i4[]">4;4</value>
    </properties>
    <id>1</id>
    <location bottom="{y_max}" left="{x_min}" right="{x_max}" top="{y_min}" /> 
    <connection feed="true" port="Feed1_stage{feed_stage}" type="material">{inlet_stream_number}</connection>
    <connection feed="false" port="TopProduct" type="material">{tops_stream_number}</connection>
    <connection feed="false" port="BottomProduct" type="material">{bottoms_stream_number}</connection>
  </unitOperation>
"""


bottom_stream_string = fr"""
	<stream name="{bottoms_stream_number}">
	<start x="{x_max}" y="{y_max-2}" />
	<end x="{x_max + 30}" y="{y_max-2}" />
	<labelCenter x="{x_max + 15}" y="{y_max-2}" />
	<boundingBox bottom="{y_max-2}" left="{x_max}" right="{x_max + 30}" top="{y_max-2}" />
	<routePoint x="{x_max}" y="{y_max-2}" />
	<routePoint x="{x_max + 30}" y="{y_max-2}" />
	<type>material</type>
	<materialType>default</materialType>
	<phase name="Overall">
	  <moleFraction>N/A;N/A;N/A</moleFraction>
	  <massFraction>N/A;N/A;N/A</massFraction>
	</phase>
	</stream>
	"""
	
top_stream_string = fr"""
	<stream name="{tops_stream_number}">
	<start x="{x_max}" y="{y_min+2}" />
	<end x="{x_max + 30}" y="{y_min+2}" />
	<labelCenter x="{x_max + 15}" y="{y_min+2}" />
	<boundingBox bottom="{y_min+2}" left="{x_max}" right="{x_max + 30}" top="{y_min+2}" />
	<routePoint x="{x_max}" y="{y_min+2}" />
	<routePoint x="{x_max + 30}" y="{y_min+2}" />
	<type>material</type>
	<materialType>default</materialType>
	<phase name="Overall">
	  <moleFraction>N/A;N/A;N/A</moleFraction>
	  <massFraction>N/A;N/A;N/A</massFraction>
	</phase>
	</stream>
	"""