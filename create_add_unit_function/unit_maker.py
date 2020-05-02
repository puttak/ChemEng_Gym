

class FlowsheetSpecInfo:
	"""Might still need to add more here -
	 - setreams with unknowns still have a number of N\As that refer to compound number so need to make changes there
	 """
	compounds = ["Water", "Benzene", "Toluene"]
	compound_spec = """
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
"""


class UnitMaker(FlowsheetSpecInfo):
	spacing = 10
	box_width = 30
	max_layers = 3

	def __init__(self, inlet_stream_info, column_number, n_stages=20,
				 specification1=("1 Spec Reflux ratio", 2), specification2=("1 Spec Boilup ratio", 1.5),
				 feed_stage='middle', pressure_increase=0,):

		self.feed_temperature = inlet_stream_info["Temperature"]
		self.feed_pressure = inlet_stream_info["Pressure"]
		self.vapour_fraction_feed = inlet_stream_info["vapour_fraction"]
		self.inlet_stream_number = inlet_stream_info['number']
		self.component_flow = inlet_stream_info["component_flow"]  # list of component flows
		self.n_components = len(self.component_flow)
		self.inlet_coordinates = inlet_stream_info["end_coordinates"]
		self.layer_number = int(str(self.inlet_stream_number)[0]) + 1

		y_max = self.inlet_coordinates[1] + self.box_width/2
		y_min = self.inlet_coordinates[1] - self.box_width/2
		x_min = self.inlet_coordinates[0]
		x_max = self.inlet_coordinates[0] + self.box_width
		outlet_spacing = self.spacing*(self.max_layers - self.layer_number) + 2

		self.specification1 = specification1
		self.specification2 = specification2

		self.tops_stream_number = int(str(self.layer_number) + str(column_number) + str(1))
		self.bottoms_stream_number = int(str(self.layer_number) + str(column_number) + str(2))

		self.column_name = "Column_" + str(column_number)
		self.n_stages = n_stages
		self.pressure = self.feed_pressure + pressure_increase
		if feed_stage == 'middle':
			self.feed_stage = n_stages//2
		else:
			self.feed_stage = feed_stage

		flow_string = '\n'.join([str(self.component_flow[i]) + ' Component ' + str(i+1) + ' flow'
								 for i in range(self.n_components)])

		NAs_empty_stream = ("N/A;"*self.n_components)[0:-1]
	
		self.unit_string = fr"""<unitOperation CLSID="ChemSepUO.ChemSep_UnitOperation.1" name="{self.column_name}" type="COM:1.0">
<description>ChemSep Unit Operation</description>
<properties>
<value name="sepFile" type="str">[ChemSep]
Version=8.20
Compiled=2020-4-6 01:55 717b5cb3d168
Name=C:\Users\MEATRO~1\AppData\Local\Temp\CS_3_1~2.sep
Title=ChemSep CO Unit Operation "{self.column_name}" in COFE Flowsheet
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

[Cape-Open-Variables]
3
TACo=TACo=do=kg0 m0 s0 K0 kmol0 rad0 A0 =Total Annual Cost=output=TAC=
QCo=QCo=do=kg1 m2 s-3 K0 kmol0 rad0 A0 =Condenser duty=output=QC=J/s
QRo=QRo=do=kg1 m2 s-3 K0 kmol0 rad0 A0 =Reboiler duty=output=QR=J/s

{self.compound_spec}

[Operation]
2 Operation Column
1 Operation kind Simple Distillation
1 Condenser Total (Liquid product)
1 Reboiler Partial (Liquid product)
{n_stages} Stages
1 Feed stages
0 Sidestream stages
F={self.feed_stage}
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
{self.pressure} Condenser pressure
{self.pressure} Top pressure
* Pressure Drop
* Bottom pressure

[Feeds]
1 Number
*  Feed state *
{self.feed_stage} Stage Feed1{{split}}
{self.feed_temperature} Temperature
{self.feed_pressure} Pressure
{self.vapour_fraction_feed} Vapour fraction
{self.n_components} componentflows
{flow_string}

[Condenser]
{self.specification1[0]}
{self.specification1[1]} Value Qcondenser
* Subcooling
*  Type *
* Initialization guess * *

[Reboiler]
{specification2[0]}
{specification2[1]} Value Qreboiler
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
      <value type="str[]" name="userParameters">
        <el>Total Annual Cost</el>
        <el>Condenser duty</el>
        <el>Reboiler duty</el>
      </value>
      <value type="str[]" name="userParameterTags">
        <el>TACo</el>
        <el>QCo</el>
        <el>QRo</el>
      </value>
      <value type="str[]" name="userParameterUnitsOfMeasure">
        <el></el>
        <el>J/s</el>
        <el>J/s</el>
      </value>
      <value type="str[]" name="userParameterDataType">
        <el>real</el>
        <el>real</el>
        <el>real</el>
      </value>
      <value type="i4[]" name="userParameterStages">-1;-1;-1</value>
      <value type="i4[]" name="userParameterCompoundIndices">-1;-1;-1</value>
      <value type="bool[]" name="userParameterInput">false;false;false</value>
	  <value name="reports" type="empty" />
	  <value name="inletPortNames" type="str[]">
		<el>Feed1_stage{self.feed_stage}</el>
	  </value>
	  <value name="inletPortCSNames" type="str[]">
		<el>Feed1</el>
	  </value>
	  <value name="inletPortStages" type="i4[]">{self.feed_stage}</value>
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
	<connection feed="true" port="Feed1_stage{self.feed_stage}" type="material">{self.inlet_stream_number}</connection>
	<connection feed="false" port="TopProduct" type="material">{self.tops_stream_number}</connection>
	<connection feed="false" port="BottomProduct" type="material">{self.bottoms_stream_number}</connection>
  </unitOperation>
"""

		self.bottom_stream_string = fr"""
			<stream name="{self.bottoms_stream_number}">
			<start x="{x_max}" y="{y_max-2}" />
			<end x="{x_max + 30}" y="{y_max+outlet_spacing}" />
			<labelCenter x="{x_max + 15}" y="{y_max+outlet_spacing}" />
			<boundingBox bottom="{y_max-2}" left="{x_max}" right="{x_max + 30}" top="{y_max+outlet_spacing}" />
			<routePoint x="{x_max}" y="{y_max-2}" />
			<routePoint x="{x_max + 15}" y="{y_max-2}" />\
			<routePoint x="{x_max + 15}" y="{y_max+outlet_spacing}" />
			<routePoint x="{x_max + 30}" y="{y_max+outlet_spacing}" />
			<type>material</type>
			<materialType>default</materialType>
			<phase name="Overall">
			  <moleFraction>{NAs_empty_stream}</moleFraction>
			  <massFraction>{NAs_empty_stream}</massFraction>
			</phase>
			</stream>
			"""

		self.top_stream_string = fr"""
		<stream name="{self.tops_stream_number}">
		<start x="{x_max}" y="{y_min+2}" />
		<end x="{x_max + 30}" y="{y_min-outlet_spacing}" />
		<labelCenter x="{x_max + 15}" y="{y_min+2}" />
		<boundingBox bottom="{y_min-outlet_spacing}" left="{x_max}" right="{x_max + 30}" top="{y_min+2}" />
		<routePoint x="{x_max}" y="{y_min+2}" />
		<routePoint x="{x_max+15}" y="{y_min+2}" />
		<routePoint x="{x_max+15}" y="{y_min-outlet_spacing}" />
		<routePoint x="{x_max + 30}" y="{y_min-outlet_spacing}" />
		<type>material</type>
		<materialType>default</materialType>
		<phase name="Overall">
		  <moleFraction>{NAs_empty_stream}</moleFraction>
		  <massFraction>{NAs_empty_stream}</massFraction>
		</phase>
		</stream>
		"""